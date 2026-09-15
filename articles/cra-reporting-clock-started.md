---
title: "The CRA Reporting Clock Started. Most Manufacturers Cannot Yet Meet It."
standfirst: "The Cyber Resilience Act's vulnerability reporting obligations took effect on 11 September 2026. The timelines are measured in hours, and they assume a manufacturer already knows what is inside its own products — which is the part most organisations have not solved."
authorName: "Marieta Musat"
authorTitle: "Cybersecurity Consulting Manager, CYBERVETTER"
published: "2026-09-14"
lastReviewed: "2026-09-14"
relatedServices:
  - title: "Cyber Resilience Act Readiness"
    to: "/compliance/cyber-resilience-act"
  - title: "Supplier & Third-Party Vetting"
    to: "/services/vetting/supplier-vetting"
---

On Friday 11 September 2026, Article 14 of the Cyber Resilience Act became enforceable, and ENISA's Single Reporting Platform opened on the same day. From that date, a manufacturer of a product with digital elements placed on the EU market must submit an early warning within 24 hours of becoming aware of an actively exploited vulnerability or a severe incident affecting the security of that product, a fuller notification within 72 hours, and a final report within 14 days of a corrective measure becoming available — or within a month of the 72-hour notification where the trigger was a severe incident.

The obligation reads as a reporting duty, and organisations have accordingly been treating it as a documentation exercise. It is not one. The 24-hour window runs from the moment of awareness and nothing pauses it, which means the duty can only be discharged by a manufacturer who already knows what it ships, who inside the organisation is permitted to decide that something is being actively exploited, and how a notification physically gets filed at eight o'clock on a Friday evening. All three of those have to exist before the clock starts. None of them can be assembled once it has.

## The scope question most organisations get wrong

The first practical problem is that a large number of organisations in scope do not think of themselves as manufacturers. A product with digital elements covers considerably more than consumer devices: firmware, software embedded in hardware, components such as integrated circuits and sensors, mobile applications, industrial and building IoT. If a company ships something into the EU market that contains software and is placed on the market under its own name, it is likely within scope, whether it describes itself as a manufacturer, a systems integrator, an equipment supplier or a software house.

Two further points are worth stating explicitly, because both are routinely missed. The reporting duty applies to products already on the market, not only to products placed on the market after 11 September. And it reaches manufacturers established outside the EU where their products are made available on the EU market. An organisation that concluded it had until December 2027 to think about the CRA, on the basis that the essential requirements and CE marking obligations under Article 13 apply from then, has misread which parts of the regulation start when.

The first deliverable, therefore, is not a procedure. It is a written scope determination: which of our products fall within the regulation, on what reasoning, reviewed by someone competent to be wrong in public about it. Organisations that cannot produce that document today are not in a position to know whether any of this applies to them, which is a worse place to be than being in scope and knowing it.

## You cannot report on a component you cannot locate

The reporting trigger is a vulnerability under active exploitation. In practice that means a disclosure lands — a widely used library, a common runtime, a component nobody thought about — and the manufacturer has to answer one question quickly: is this in anything we ship, in which versions, and which of those are still supported and in the field. That is not a security question. It is an inventory question, and it is the one that decides whether the 24 hours are comfortable or impossible.

This is where the gap between having an SBOM and having a usable one becomes expensive. A software bill of materials generated once, exported to satisfy a customer questionnaire and filed, answers nothing under time pressure. It describes one build of one product at one moment, and the estate has moved since. What the obligation implicitly requires is an SBOM produced as part of every build, retained per released version, and queryable across the whole product portfolio — so that the question "which of our shipped versions contain this component" is a lookup rather than a project.

The organisations that came out of the last few widely exploited library vulnerabilities well were not the ones with better analysts. They were the ones that could answer the inventory question in hours instead of weeks, and the difference was entirely decided before the disclosure happened. Article 14 has now attached a legal deadline to that difference.

Transitive dependencies are where this most often breaks down. A manufacturer knows what it declared in its manifests and does not know what those dependencies pulled in. For a reporting duty this matters more than for a general hygiene programme, because the component under active exploitation is quite frequently three levels down from anything a developer consciously chose.

## Awareness is a decision, and it needs an owner

The 24 hours run from becoming aware. That phrasing puts a great deal of weight on a judgement that somebody has to make, usually with incomplete information, frequently outside working hours. Whether a vulnerability is being actively exploited is not always a clean determination — a researcher's claim, a customer report describing behaviour consistent with exploitation, a pattern in your own telemetry, an entry in a public exploited-vulnerability catalogue. Some of these are unambiguous and some require a call.

The organisational answer has to be specific rather than procedural. A named person who is authorised to make the determination. A named deputy, because the first person will be on a flight. A route by which any of the plausible inputs — support desk, security mailbox, threat intelligence feed, engineering team — reaches that person rather than sitting in a queue until Monday. And, critically, a pre-agreed position on what the early warning may contain without full legal and communications sign-off.

That last point is where most of the 24 hours actually disappear. The technical facts are usually established quickly. What consumes the window is the internal negotiation over whether to file, how much to say, and who approves the wording. An early warning is by design a preliminary notification containing what is known at the time, and treating it as a public statement requiring the same clearance as a press release is the most common way an organisation with good engineering misses a deadline it could easily have met.

## Routing, and the mistake that restarts nothing

A manufacturer files once, through the Single Reporting Platform, and the notification is routed to ENISA and to the CSIRT designated as coordinator. The single filing is a genuine simplification. The complication is identifying the correct coordinating CSIRT, which follows the jurisdictional rules in the regulation, and ENISA has warned that selecting the wrong one can invalidate the notification — leaving the manufacturer to resubmit to the correct recipient while the original clock continues to run.

This is a half-day of work that has to be done before it is needed. Determine the coordinating CSIRT for each product line, write it down alongside the scope determination, and register on the platform now rather than discovering the onboarding requirements during an incident. There is a separate duty to inform impacted users, in a timely manner, with the available mitigations, in a structured machine-readable format — which is a second distribution channel most manufacturers have not built and cannot improvise.

## One event, several regimes

CRA reporting is additional to existing obligations rather than a substitute for them. The same event can simultaneously engage notification duties under NIS2, under DORA for financial entities and their ICT providers, and under the GDPR where personal data is affected — each with its own threshold, its own recipient and its own clock. An organisation that builds a standalone CRA procedure will end up running several parallel processes that share facts and contradict each other on timing.

The more durable arrangement is a single incident intake that classifies an event once against every regime the organisation is subject to, and then generates the notifications each one requires. This is more work initially and much less work permanently, and it is the only version that survives an event which triggers three duties at once at two in the morning.

## A minimum credible position

For an organisation that has not yet started, the following is achievable in weeks rather than quarters and closes most of the practical exposure: a written scope determination covering the whole product portfolio, including products already on the market; the coordinating CSIRT identified per product line, recorded, and registration on the Single Reporting Platform completed; SBOM generation tied to the build, retained per released version, with a documented way to query the whole estate for a given component; a named decision-maker for active exploitation, with a deputy and an out-of-hours contact path that support and engineering both know about; pre-approved wording and a pre-agreed approval threshold for the 24-hour early warning; a user notification channel capable of producing structured, machine-readable advisories; and one rehearsal, end to end, against a realistic scenario.

The rehearsal is the item most likely to be dropped and the one that returns the most. A drill exposes the things a written procedure cannot: that the security mailbox forwards to someone who left, that nobody knows the platform credentials, that the person authorised to approve the filing is also the person who has to write it. One exercise is worth considerably more than a manual nobody has opened.

Article 64 sets penalties for breaches of the Article 14 obligations at up to 15 million euro or 2.5 per cent of total worldwide annual turnover, whichever is higher. I am not persuaded that enforcement risk is the argument that should move a board here, and I would rather not make it the centre of the case. The stronger argument is that the capability the regulation demands — knowing what you ship, being able to locate a component across your estate, and having a rehearsed path from discovery to disclosure — is the same capability that determines how badly an exploited vulnerability damages your customers and your reputation, entirely independently of whether a regulator ever takes an interest.

December 2027 brings the larger programme: essential requirements, technical documentation, conformity assessment, CE marking. That is the substantial piece of work, and it should be planned as one. But the part with operational teeth is already running, it started last Friday, and it is the part where the gap between the organisations that prepared and the organisations that meant to is going to become visible very quickly.
