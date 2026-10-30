# Nuria landing page

Marketing site for [Nuria](https://github.com/SebasB76/nuria), the El Niño assistant for
Guayaquil. Static HTML, CSS and JavaScript, with no build step.

## Run it

1. Run `python3 -m http.server 8765` in this folder.
2. Open `http://localhost:8765`.

## Files

- `index.html`, `styles.css`, `main.js`: the whole page.
- `assets/img/`: paintings (public domain), the Cerro Santa Ana illustration and the share image.
- `assets/fonts/`: Instrument Serif and Instrument Sans, self-hosted.
- `tools/cerro_santa_ana.py`: draws `assets/img/cerro-santa-ana.svg`. Run
  `python3 tools/cerro_santa_ana.py > assets/img/cerro-santa-ana.svg` after you change it.
- `CREDITS.md`: the source and license of every image and font.

## Before the pitch

The "Probar la app" and "Ver la demo" buttons show "pronto" until their links exist. Put the
Expo Go link and the demo video link in `LINKS` at the top of `main.js`.

`reference/` holds third-party design screenshots and is not committed.
