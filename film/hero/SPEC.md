# DynamicNotch hero film — spec (storyline A)

GOAL:    a MacBook owner sees their idle notch come alive, recognises five real features, and clicks Download.
OUTPUT:  HyperFrames, 1920 x 1080, 30 fps, silent, loops seamlessly (last frame == frame 0).
TIME:    20.9 s x 30 = 627 frames.

LOOK:    ground = the recording itself: the real black/silver swirl wallpaper and menu bar, never an added void.
         ink #FFFFFF; quiet ink rgba(255,255,255,0.62); accent #6AD09D (the icon's waveform mint), ONLY on the word
         "useful" in the claim. Display: Geist 600, tracking -0.03em; titles 96 px (8.9% of height), feature words
         150 px, quiet lines 32 px. Left-aligned on x = 192 (10%), baseline band y 760-900 (empty wallpaper under the notch).
         Medium: real product UI on its own desktop, scaled 1.15-1.45x around the notch. Legibility shadow on type only:
         0 2px 18px rgba(0,0,0,0.55). No grain, no vignette, no added blur except motion and transition blur.
OBJECTS: the notch (black, rounded bottom corners) is the carrier through every shot; the cursor is the real one in
         the footage; the app icon is the real DynamicNotch icon (assets/icon.png).
MOTION:  enter expo.out / power4.out; camera power2.inOut; exits power3.in, 40-50% shorter than entrances.
         Word stagger 0.067 s, letter stagger 0.035 s. Spring (icon) back.out(1.15). Motion blur on the root.

SHOTS:
  0.00-1.90   IDLE (still of src 22.30): closed notch, cursor resting on it. "Your notch does nothing" per-word blur-in from 0.25, dead still, blur-out 2.10-2.30.
  1.90-3.45   OPEN (src 22.30-23.85): same framing as the still; notch opens to Now Playing at ~2.40; ends before the settings window slides in. -> blur swap.
  3.30-6.95   MUSIC (src 9.10-12.75): big Now Playing, ends before the song changes. "DynamicNotch" per-letter 3.55-5.05, then "Music" 5.25. -> vertical whip.
  6.80-9.80   AI USAGE (src 30.60-33.60): tab switches to 31% Claude at ~7.4; "AI usage" per word grey -> white at 7.45; ends before the settings window. -> dip cut.
  9.80-13.15  HUD (src 40.70-43.85): Volume -> muted -> Brightness. "Volume" rolls to "Brightness" at 11.40 (src 42.30). -> iris from the notch.
  13.00-17.35 SHELF (src 61.00-63.76, then held last frame): shelf with AirDrop and files. "Shelf" at 13.95; camera pulls back 1.45x -> 1.2x 14.80-15.90;
              claim "Make your notch actually useful" per-word 15.05, hold to 17.0. -> object becomes the world.
  17.00-20.90 END: the notch grows into a full-bleed black panel (0.65 s), icon (190 px) springs in, wordmark (128 px) wipes in, "Download for macOS" button + "macOS 15 Sequoia or later" (40 px);
              hold to 20.10; contents leave 0.15 s; panel shrinks back into the idle notch over the idle still by 20.90 = frame 0.

BANNED:  titles over a moving app window (review 1: "DynamicNotch" on the HUDs window; review 2: "AI usage" on the AI Usage window); a song change or app window at a shot edge; added dark void behind small UI; glow, particles, gradients; titles that drift after landing; everything centred
         (titles are left-aligned; only the notch and end card centre); same entrance twice in a row; three cards in a row;
         logo docked in a corner; any redrawn UI.
QA:      0.0 (== 20.89), 1.2 title1, 2.6 notch open, 4.2 wordmark, 5.8 Music, 8.4 AI usage 31%, 10.7 Volume, 12.0 Brightness,
         14.4 Shelf, 16.4 claim with mint "useful", 18.9 end card, 20.7 shrink-back.