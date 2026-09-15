---
title: "What Technical Due Diligence Finds That the Questionnaire Never Will"
standfirst: "A clean vendor questionnaire and a passed compliance audit tell you what an organisation says about itself. Only hands-on technical inspection tells you what is actually running."
authorName: "Adrian Voss"
authorTitle: "Senior Consultant, CYBERVETTER"
published: "2026-07-20"
lastReviewed: "2026-07-20"
relatedServices:
  - title: "Digital Vetting & Cyber Due Diligence"
    to: "/services/vetting/cyber-due-diligence"
  - title: "Supplier & Third-Party Vetting"
    to: "/services/vetting/supplier-vetting"
---

Over two decades of security consulting, I've sat on both sides of the due diligence table — as the person producing evidence for a buyer's technical team, and as the person tearing apart someone else's environment on a tight deadline before a deal closed. The pattern that keeps repeating is almost boring in its consistency: the paperwork looks fine, and the infrastructure tells a different story.

This matters more than ever. Third-party risk, supplier onboarding, and M&A technical due diligence have all become more formalised in Europe over the past few years, partly pushed by NIS2's supply-chain obligations and DORA's requirements around ICT third-party risk in financial services. Organisations now routinely send out security questionnaires, request ISO 27001 certificates, and ask for SOC 2 reports before signing anything. That's progress. It's also, on its own, close to useless as a risk signal — and I say that as someone who has both written and audited against those frameworks.

## The certificate is not the terrain

A certification scope statement is one of the most under-read documents in the entire due diligence process. I've reviewed ISO 27001 certificates covering a holding company's head office network while the actual product — the thing being acquired or the service being onboarded — ran on infrastructure entirely outside that scope, sometimes managed by a different team, sometimes by a subcontractor nobody mentioned. The certificate is real. The audit was real. It simply wasn't measuring the thing the buyer cared about.

The same applies to penetration test reports, which I've probably reviewed more of than almost any other artifact in this line of work. A clean pen test report tells you that a specific set of testers, working within a specific scope and time box, didn't find critical issues in the specific systems presented to them. It does not tell you what wasn't in scope, what was excluded because it was "legacy and being decommissioned" (a phrase I've heard about systems that were still in production three years later), or what changed in the environment the week after the test concluded. None of this is fraud on the vendor's part, usually — it's just the natural gap between a point-in-time assessment and a living environment. Treating a clean report as a pass/fail gate, rather than one data point among several, is the single most common mistake I see on the buy side.

## What actually shows up when you look

When technical vetting goes beyond documents — external attack surface mapping, architecture walkthroughs with actual engineers rather than account managers, sampling of configuration on representative systems, review of identity and access patterns — a fairly consistent set of findings emerges across very different sectors and company sizes.

Shadow IT is close to universal. Almost every mid-sized organisation I've assessed has some meaningful chunk of infrastructure — a marketing analytics stack, a reporting database, an integration server — that isn't on the official asset inventory because it was stood up by a business unit outside formal IT governance. It's rarely malicious. It's also rarely patched, rarely backed up properly, and often holds more sensitive data than anyone in security realises, because business teams don't think about data classification when they're just trying to hit a deadline.

Identity hygiene is the second recurring theme. Service accounts with domain admin rights that nobody can explain the origin of. Shared credentials for third-party integrations that were set up once, years ago, and never rotated. Departed employees' accounts still active, sometimes still used by automated processes because someone hardcoded a personal account into a script instead of a service identity. None of this shows up in a questionnaire answer of "we enforce role-based access control," which is technically true and practically meaningless without evidence of enforcement.

Then there's the architecture-level red flag I've come to trust more than almost anything else: undocumented or poorly understood third-party dependencies. A core business process quietly depending on an unsupported library, a single external API provider with no contractual continuity clause, or a critical integration built by a contractor who left the company years ago and whose knowledge left with them. In due diligence for an acquisition, this is often more consequential than any individual vulnerability, because it speaks to operational fragility and key-person risk that a security scan simply cannot detect.

End-of-life and unpatched systems remain stubbornly common, and the interesting part isn't finding them — everyone expects some legacy debt — it's understanding why they're there and whether there's a credible remediation plan versus an indefinite "risk accepted" note that's been rolled over annually for five years. That distinction is where technical judgment matters more than tooling.

## Weighing findings against the deal, not a checklist

The mistake I see less experienced teams make, on both the consulting and the buyer side, is trying to convert technical findings into a binary verdict. Real technical risk assessment for a transaction or a supplier relationship has to be weighed against business context: What's the actual exposure if this system is compromised? What's the cost and timeline to remediate versus the value of the deal? Is this a control gap that's expensive to close, or a symptom of a broader pattern — inconsistent patching, poor asset management, weak change control — that will keep generating new gaps regardless of what you fix today?

A single unpatched server is a line item. A dozen unpatched servers, an undocumented network segment, and three different unmanaged admin accounts found in the same engagement is a pattern, and patterns predict future incidents far better than any individual finding does. I've walked into environments with a genuinely clean-looking control set on paper that nonetheless felt fragile the moment you started asking engineers how things actually worked day to day — and I've seen messier-looking environments run by teams who clearly understood their own risk and were managing it deliberately. The technical inspection is what lets you tell those two situations apart, and it's exactly what a questionnaire, by design, cannot do.

If there's one piece of contrarian advice I'd leave a deal team with, it's this: don't ask for evidence that a control exists. Ask to watch it work, on a system you picked, not one that was prepared for you. The gap between those two things is where the real risk lives.
