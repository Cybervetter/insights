# CYBERVETTER Insights

Source content for [cybervetter.com/insights](https://cybervetter.com/insights) — published here as Markdown for transparency and reference. This repository is the **source of truth** for article content; `website-cybervetter` fetches it at build time and renders it in the site's own design.

## Articles

Newest first — regenerated automatically by `.github/workflows/publish.yml` on every push that changes `articles/`, so this list never drifts from what's actually published.

<!-- ARTICLES:START -->
- **[The CRA Reporting Clock Started. Most Manufacturers Cannot Yet Meet It.](articles/cra-reporting-clock-started.md)** — 14 September 2026
  The Cyber Resilience Act's vulnerability reporting obligations took effect on 11 September 2026. The timelines are measured in hours, and they assume a manufacturer already knows what is inside its own products — which is the part most organisations have not solved.
- **[The Certificate Is Issued to a System, Not to a Week](articles/the-certificate-is-issued-to-a-system.md)** — 31 August 2026
  An audit samples a fortnight of evidence and infers a year of behaviour. That inference only holds where the management system runs on habit rather than on preparation — which is a question about people, not about documentation.
- **[Security Left, Security in the Cloud, and the New Question of Securing AI Itself](articles/security-left-cloud-and-securing-ai.md)** — 17 August 2026
  DevSecOps and cloud security are now well-established disciplines — but AI is reshaping both how software gets built and what security teams need to defend. A practical look at where the real risk sits, beyond the hype.
- **[AI Coding Assistants Didn't Create Supply-Chain Risk — They Accelerated It](articles/ai-coding-assistants-and-supply-chain-risk.md)** — 10 August 2026
  AI-assisted development is now mainstream in most engineering teams, and it genuinely speeds delivery. It has also opened new paths into the software supply chain that traditional review processes weren't built to catch.
- **[Hardening Is Not a Project: Building Resilience Into Systems That Never Stop Changing](articles/hardening-is-not-a-project.md)** — 3 August 2026
  Secure configuration, identity management, and patching are too often treated as one-off compliance exercises. Genuine resilience comes from treating hardening as a continuous discipline — and from auditors and engineers actually talking to each other.
- **[What Technical Due Diligence Finds That the Questionnaire Never Will](articles/what-technical-due-diligence-finds.md)** — 20 July 2026
  A clean vendor questionnaire and a passed compliance audit tell you what an organisation says about itself. Only hands-on technical inspection tells you what is actually running.
- **[Inside the SOC: Why Detection and Response Is a Discipline, Not a Dashboard](articles/inside-the-soc-detection-and-response.md)** — 6 July 2026
  Behind every well-run Security Operations Centre is less about the tools on screen and more about triage discipline, documentation habits, and honest post-incident learning. Here is what actually separates fast, defensible incident response from slow, chaotic response.
<!-- ARTICLES:END -->

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
