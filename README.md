# CYBERVETTER Insights

Source content for [cybervetter.com/insights](https://cybervetter.com/insights) — published here as Markdown for transparency and reference. This repository is the **source of truth** for article content; `website-cybervetter` fetches it at build time and renders it in the site's own design.

## Format

Each article is one file in `articles/`, named `<slug>.md`, matching its URL at `/insights/<slug>`.

```markdown
---
title: "Article title"
standfirst: "One or two sentences stating what the reader will know by the end."
kicker: "Optional topic label, e.g. NIS2"
authorName: "Full name"
authorTitle: "Title, CYBERVETTER"
published: "2026-08-17"
lastReviewed: "2026-08-17"
relatedServices:
  - title: "Service name"
    to: "/services/practice/service-slug"
---

Opening paragraph, no heading.

Second paragraph of the opening passage.

## A section heading

A paragraph in this section.
```

**Body content is plain prose paragraphs, grouped under `##` headings.** No inline formatting (bold, links, lists) is rendered — write plain sentences, matching this publication's existing style. Body text and every frontmatter field are treated as plain text, not raw HTML, when rendered on the site.

## Repositories here

Public repositories in this organisation are published for transparency and reference. They are maintained by CYBERVETTER only — external issues, pull requests and comments are not accepted. See `CONTRIBUTING.md`.
