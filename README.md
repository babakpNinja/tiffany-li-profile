# Tiffany Li — portfolio page

A public portfolio for Tiffany Li, Editorial Fellow at The Information (San
Francisco), covering AI safety. The page opens with the one-minute claymation
trailer, then her background and career, then her recent reporting with links
to The Information.

## What is here

- `index.html` — the page. No build step.
- `assets/trailer.mp4` + `assets/poster.png` — the trailer (16.95 MB, 60.08s).
- `assets/translations.json` — cached translations of every article headline
  and public summary in Chinese, Japanese, Spanish, Korean and Persian.
- `build_translations.py` — regenerates that file through the model gateway.
  Run `python3 build_translations.py` after editing the article list.
- `serve.py` — static host with HTTP range support. The mp4 needs it: a plain
  `python -m http.server` returns 200 with the whole file, and Safari and iOS
  refuse to stream that.
- `research/` — the dossier and the publisher's own public summaries.

## Content rules

- Only headlines, dates and public summaries appear. Article bodies are
  paywalled at The Information and are never fetched or translated.
- No pricing or contract figures.
- All copy passes `tools/slop_enforce.gate_text`.

## Run locally

    PORT=8080 python3 serve.py
