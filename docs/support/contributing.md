# Contributing

This documentation lives in [Source-Robotics/STEPFOC-docs](https://github.com/Source-Robotics/STEPFOC-docs). A
small fix can be made from the browser: the *Edit it on GitHub* link at the end of every page opens the page's
source, and GitHub turns your change into a pull request. For anything larger, open an issue first.

## How the site is built

- The pages are Markdown, built with MkDocs and the Material theme; the repository's `README.md` says how to
  preview it locally.
- The site describes one firmware release, named in `versions.yml`. The command IDs, frame lengths, the UART
  command list and the defaults in the Reference are read from the firmware's source at that release's tag by
  `tools/sync_firmware.py`; do not edit those facts in the pages. The descriptions of the commands are in
  `docs/includes/can_commands.yml` and `uart_commands.yml`.
- Every push runs a strict build (a broken link fails it) and the tool tests. A push to `main` publishes the
  site under its firmware version with [mike](https://github.com/jimporter/mike).

## House rules

- Facts come from the firmware. When a page and the firmware disagree, the firmware is right; fix the page, or
  report the firmware.
- Spell commands exactly as the firmware does, even where the spelling looks wrong.
- Write for someone who has the driver in front of them and wants to do one thing: say what to do, in order, then
  why.
- Three kinds of boxes: a note, a notice (damage) and a danger (injury). Use them for those, not for emphasis.
- Images: under 2400 px on the long side, with a caption that says what the reader should see.

## Licence

The licence that covers this documentation is stated in the repository.
