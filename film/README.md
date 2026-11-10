# Hero video

The hero on the home page is a steady 2.4:1 loop of the top of a Mac screen, cut from a 4K screen recording made without zoom (the recording itself is too big for git).

To rebuild it:

```bash
python3 film/build-hero.py "<recording>.mp4" <out-dir>
```

Then encode `<out-dir>/hero-loop.mp4` into `public/media/hero/` (`hero.mp4`, `hero.webm`, `hero-960.mp4` and `still.jpg`). The moments it uses, and the crop, are listed at the top of the script. Each moment is chosen so no app window enters the frame.
