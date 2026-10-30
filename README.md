# Nuria landing page

Marketing site for [Nuria](https://github.com/SebasB76/nuria), the El Niño assistant for
Guayaquil. Static HTML, CSS and JavaScript, with no build step.

Live: https://nuria-landing.vinci-espol-bot.workers.dev

## Run it

1. Run `python3 -m http.server 8765 --directory site`.
2. Open `http://localhost:8765`.

## Deploy it

The site runs on Cloudflare Workers as static assets, which the Free plan serves at no cost.

1. Run `npx wrangler login` once, if wrangler has no session.
2. Run `npx wrangler deploy` from this folder.

`wrangler.jsonc` uploads only `site/`, so `reference/`, `tools/` and the docs never go online.

## Files

- `site/index.html`, `site/styles.css`, `site/main.js`: the whole page.
- `site/assets/img/`: paintings (public domain), the Cerro Santa Ana illustration and the share
  image.
- `site/assets/fonts/`: Instrument Serif and Instrument Sans, self-hosted.
- `site/_headers`: long cache for the fonts.
- `tools/cerro_santa_ana.py`: draws the Cerro Santa Ana illustration. Run
  `python3 tools/cerro_santa_ana.py > site/assets/img/cerro-santa-ana.svg` after you change it.
- `CREDITS.md`: the source and license of every image and font.

## Before the pitch

The "Probar la app" and "Ver la demo" buttons show "pronto" until their links exist. Put the
Expo Go link and the demo video link in `LINKS` at the top of `site/main.js`.

`reference/` holds third-party design screenshots and is not committed.
