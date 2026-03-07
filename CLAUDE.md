# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a GitHub Pages site hosting supplemental rules clarifications for the card game **Compile**. The site is published as "COMPILE Supplemental Clarifications" — a community reference for edge cases and rulings not fully covered by the official rulebook.

## Site Structure

- `index.md` — The entire site content. This single Markdown file contains all rules clarifications, organized by section (General Rules, Timing/Resolution, Committed Cards, Card Clarifications, Miscellaneous).
- `_config.yml` — Minimal Jekyll config (just sets the page title).
- `claude-context/` — Reference materials for deriving clarifications (not served by the site):
  - `master-rules-reference.md` — Comprehensive synthesized rules document. This is the primary reference for understanding game mechanics, timing, targeting, keywords, and card-specific rulings.
  - `main1-card-database.md` — Complete card text database for all 72 Main 1 cards (12 protocols × 6 cards each), with top/middle/bottom commands transcribed from card images.
  - `COMPILE Cards/` — Card image files (JPGs) for all Main 1 protocols.
  - `MN01_Rulesheet.pdf`, `MN02_Rulesheet.pdf` — Official printed rulesheets.
  - `The_Compile_Codex-1.pdf` — The Compile Codex PDF (official errata/clarifications document).
  - Discord export HTML — Raw export from the `#rules-questions` channel, the primary source for new rulings.

## Development

This is a static Jekyll site hosted on GitHub Pages. No build step or dependencies are needed locally — push to `main` and GitHub Pages builds automatically.

To preview locally: `bundle exec jekyll serve` (requires Ruby + Jekyll).

## Content Guidelines

- Clarifications in `index.md` are derived from official rulings, primarily from the game's Discord `rules-questions` channel and official PDFs in `claude-context/`.
- When researching a ruling, consult `master-rules-reference.md` first (it synthesizes all sources), then check `main1-card-database.md` for exact card text, and the Discord export for specific designer statements.
- Each clarification should cite the specific card(s) involved and explain the ruling clearly.
- The document uses Markdown with YAML front matter (`title: COMPILE Supplemental Clarifications`).
- Sections are separated by horizontal rules (`---`).
- Authoritative sources for rulings: Michael Yang (game designer), the Codex errata, and community members "makario" and "impalsi" in Discord.
