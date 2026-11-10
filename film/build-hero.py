"""Builds the steady hero loop from the Cap recording (fixed frame, cross-fades, no text).

Usage: python3 film/build-hero.py <recording.mp4> <out_dir>
"""
import subprocess, sys

src, out = sys.argv[1], sys.argv[2]
CROP = 'crop=2304:960:768:80'          # the top of the screen, centred on the notch (4K source)
SIZE = 'scale=1920:800:flags=lanczos'  # 2.4:1 letterbox
FADE = 0.5
# (start, end) in the recording: each one is clear of windows inside the crop
SEGMENTS = [
    (0.0, 6.3),    # idle notch, cursor arrives, opens to Now Playing
    (18.4, 22.0),  # Now Playing, skip to the next track and back
    (28.6, 31.6),  # Shelf with AirDrop and files
    (35.6, 39.6),  # Stats: CPU, RAM, swap
    (60.0, 65.2),  # opens to Now Playing, switches to AI usage, closes
]

def run(cmd):
    subprocess.run(cmd, check=True)

inputs, chains = [], []
for i, (a, b) in enumerate(SEGMENTS):
    inputs += ['-ss', str(a), '-to', str(b), '-i', src]
    chains.append(f'[{i}:v]fps=30,{CROP},{SIZE},setsar=1,format=yuv420p,settb=AVTB,setpts=PTS-STARTPTS[v{i}]')

graph, last, offset = chains, 'v0', 0.0
for i in range(1, len(SEGMENTS)):
    a, b = SEGMENTS[i - 1]
    offset += (b - a) - FADE
    graph.append(f'[{last}][v{i}]xfade=transition=fade:duration={FADE}:offset={offset:.3f}[x{i}]')
    last = f'x{i}'

master = f'{out}/hero-master.mp4'
run(['ffmpeg', '-v', 'error', '-y', *inputs, '-filter_complex', ';'.join(graph), '-map', f'[{last}]',
     '-an', '-c:v', 'libx264', '-crf', '12', '-preset', 'slow', '-pix_fmt', 'yuv420p', master])

# Seamless loop: the tail cross-fades into the opening frames.
dur = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', master]))
loop = f'{out}/hero-loop.mp4'
fc = (f'[0]split[x][y];[x]trim=start={FADE},setpts=PTS-STARTPTS[body];[y]trim=0:{FADE},setpts=PTS-STARTPTS[head];'
      f'[body][head]xfade=transition=fade:duration={FADE}:offset={dur - 2 * FADE:.3f},format=yuv420p[v]')
run(['ffmpeg', '-v', 'error', '-y', '-i', master, '-filter_complex', fc, '-map', '[v]',
     '-c:v', 'libx264', '-crf', '12', '-preset', 'slow', '-pix_fmt', 'yuv420p', loop])
print('loop', subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', loop]).decode().strip(), 's')
