---
title: "Hardening Is Not a Project: Building Resilience Into Systems That Never Stop Changing"
standfirst: "Secure configuration, identity management, and patching are too often treated as one-off compliance exercises. Genuine resilience comes from treating hardening as a continuous discipline — and from auditors and engineers actually talking to each other."
authorName: "Marieta Musat"
authorTitle: "Cybersecurity Consulting Manager, CYBERVETTER"
published: "2026-08-03"
lastReviewed: "2026-08-03"
relatedServices:
  - title: "Identity, Access & Zero Trust Review"
    to: "/services/technical-assurance/identity-zero-trust"
  - title: "Security Governance & Operating Model Design"
    to: "/services/governance-risk-compliance/security-governance"
---

"We hardened the servers last year" is a sentence I hear often, usually said with genuine confidence, and it usually signals a problem. Hardening is not a state a system reaches and then stays in — it is a moving target, because the system itself keeps changing (new packages, new configuration drift, new users, new integrations), and because the threat landscape it needs to resist keeps changing too. A CIS-benchmarked build that was solid eighteen months ago can be quietly full of holes today, not because anyone did anything wrong, but because nobody kept checking.

This is one of the places where my background straddles two worlds that do not always talk to each other well: audit and governance on one side, hands-on technical hardening on the other. I have sat on both sides of that table — as the person reviewing configuration baselines against a framework, and as the person actually setting group policy, disabling unnecessary services, and reviewing firewall rulesets. The organisations that do this best are the ones where those two functions are in continuous dialogue rather than meeting once a year for an audit.

## Baselines are a starting point, not an outcome

A secure configuration baseline — whether built from CIS Benchmarks, vendor hardening guides, or an internal standard — is only useful if it is actively monitored for drift. I have reviewed environments with beautifully documented baselines sitting in a policy folder that bore almost no resemblance to what was actually deployed, because the baseline was applied once at build time and nothing since then checked whether it held. Configuration compliance monitoring — ideally automated, checking systems against the baseline on a recurring basis and flagging deviations — is what turns a baseline from a document into a control. Where I see this done well, drift detection feeds directly into the same ticketing queue as vulnerability findings, so remediation is prioritised by actual risk rather than by which team happens to own which tool.

A common pitfall worth naming directly: over-hardening to the point that operations quietly routes around security. If a hardening standard makes a legitimate administrative task take five extra approval steps every time, staff will find workarounds, and those workarounds are usually far less secure than the thing the standard was trying to prevent. Good hardening balances restriction with usability, and that balance requires the same iterative attention as the technical controls themselves — it is not something you get right once.

## Identity is the perimeter now

Network perimeters have not disappeared, but for most organisations I work with, identity has become the more consequential control point. Multi-factor authentication is close to table stakes at this point, yet I still routinely find MFA enforced inconsistently — strong on the primary email and VPN, but absent on a legacy admin portal, a third-party SaaS integration, or a service account that "nobody remembers exists." Attackers know this and go looking for exactly those gaps rather than attacking MFA head-on.

Single sign-on brings real security benefits — centralised authentication logging, easier deprovisioning, consistent policy enforcement — but it also concentrates risk. A compromised identity provider is a compromise of everything behind it, which is why conditional access policies, session controls, and privileged access management around the identity provider itself deserve at least as much scrutiny as the applications it protects. I have found, in access reviews, that privileged accounts accumulate quietly over time: a contractor's admin rights that were never revoked, a service account with domain admin because it was easier six years ago. Periodic, genuinely enforced access recertification is unglamorous work, but it closes more real exposure than most headline security projects.

## Zero Trust as a direction, not a product

Zero Trust has become one of the most misused terms in the industry, largely because it gets sold as a product category rather than described honestly as an architectural principle: never trust, always verify, regardless of network location. I encourage clients to treat it as a direction of travel rather than a destination with a certificate at the end. The practical starting points are usually the same regardless of environment — strong identity verification for every access request, micro-segmentation so a compromised device or account cannot move laterally unchecked, and least-privilege access enforced continuously rather than granted once at onboarding and never revisited.

The trade-off worth being honest about is complexity and cost. A full Zero Trust architecture is a multi-year undertaking for most mid-sized organisations, and I have seen programmes stall when leadership expected a single project to "deliver Zero Trust" rather than understanding it as a set of ongoing architectural decisions applied consistently as systems are built or replaced. Sequencing matters here too: get identity and segmentation fundamentals solid before investing heavily in the more advanced tooling that assumes those fundamentals are already in place.

## Vulnerability and patch management: the discipline nobody wants to own

Vulnerability management is frequently treated as a scanning exercise — run the scanner, generate the report, file it — rather than as the remediation discipline it actually needs to be. A vulnerability report nobody acts on is not a control, it is a liability, because it demonstrates the organisation knew about the exposure. The organisations I have seen manage this well treat patch management as a standing operational cadence with clear service-level expectations tied to severity and exploitability (not just a raw CVSS score — actual exploitability in the wild matters more), rather than as an occasional catch-up project after an incident.

The perennial pitfall is prioritisation by severity score alone, ignoring exposure. A critical vulnerability on an internal system with no network path from the internet is a very different risk than a medium-severity one on an internet-facing asset handling personal data under GDPR. Effective programmes triage using both the technical severity and the business and regulatory context of the asset — and they track exceptions formally, with a documented risk acceptance and a review date, rather than letting "we'll patch it next cycle" become a permanent, undocumented state. That documentation habit, more than any single tool, is what makes a hardening programme something you can actually stand behind when someone — an auditor, a regulator, or your own incident responders after the fact — asks what you knew and when.
