# Review — DynamicNotch hero film

**Creative calls**
- Built storyline A, "Your notch does nothing", on the person's go-ahead. B ("one song, all the way through") and C ("words that open") are in `../STORYLINES.md`.
- The Extensions beat was dropped from the film. In the only footage of it (src 56 s), the notch is a few pixels tall, and enlarging it would be mush. It belongs on the site as its own feature loop.
- The end card is the notch itself: the open shelf notch grows into a full-bleed black panel, then shrinks back into the idle notch, so the 20.9 s loop is seamless.
- One accent (#6AD09D, the icon's waveform mint), on "useful" only. The real icon and the real footage are used throughout; nothing is redrawn.

**Measured vs looked at**
- `hyperframes check` passes (lint, layout, contrast, motion, craft). The review sheets, every cut strip and the phone-width sheet were looked at.
- Fixed in review: "DynamicNotch" landing on the HUDs settings window (P0), "AI usage" landing on the AI Usage window (P0), a Music window corner and a song change at the Now Playing shot's edges (P1), and an end card too small at phone width (P1).
- Not checked: the render itself (not made yet), and the loop seam in a real browser `<video loop>`.

**Weakest shot**
- The shelf: its source is zoomed out, so even at 1.45x the files and AirDrop read small and soft (the source is 1 Mbps). With more time I'd re-record the shelf zoomed in.

**Warnings kept on purpose**
- `film_silent`: the film autoplays muted on the website, so it has no sound by design.
- `nested_media_start_basis_ambiguous` (#open-vid): its `data-start` is meant to be local to the scene.
