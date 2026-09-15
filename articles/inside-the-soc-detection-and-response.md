---
title: "Inside the SOC: Why Detection and Response Is a Discipline, Not a Dashboard"
standfirst: "Behind every well-run Security Operations Centre is less about the tools on screen and more about triage discipline, documentation habits, and honest post-incident learning. Here is what actually separates fast, defensible incident response from slow, chaotic response."
authorName: "Marieta Musat"
authorTitle: "Cybersecurity Consulting Manager, CYBERVETTER"
published: "2026-07-06"
lastReviewed: "2026-07-06"
relatedServices:
  - title: "Incident Response Retainer"
    to: "/services/incident-response/incident-response-retainer"
  - title: "Vulnerability Management as a Service"
    to: "/services/technical-assurance/vulnerability-management"
---

When people picture a Security Operations Centre, they usually picture the wall of monitors: dashboards, red and amber alerts, maybe a map with blinking dots. In my experience, that image is almost entirely beside the point. The dashboards are a symptom of a SOC's maturity, not the cause of it. What actually determines whether an organisation detects an intrusion in minutes or in months is a set of much less glamorous things: how alerts are triaged, how incidents are documented, how escalation works when something is genuinely serious, and whether the team learns anything durable once the fire is out.

I find it useful to anchor SOC practice in the language of the NIST Cybersecurity Framework — govern, identify, protect, detect, respond, recover. Not because any one organisation implements it letter-for-letter, but because it forces a useful discipline: detection and response do not exist in isolation. A SOC that detects brilliantly but sits inside an organisation with no asset inventory (identify) and no patching cadence (protect) will spend most of its energy responding to incidents that better hygiene would have prevented. Recovery, too, is chronically under-resourced relative to detection — teams love building detection use cases and are far less enthusiastic about rehearsing restoration from backup under time pressure.

## Triage is where MTTD and MTTR are actually won or lost

Mean-time-to-detect and mean-time-to-respond are the two metrics every SOC reports upward, and they are also the two metrics most easily gamed by sloppy triage. An alert that sits in a queue for forty minutes before an analyst even opens it is not a detection problem, it is a triage capacity and prioritisation problem, and no amount of new tooling fixes that on its own.

A pattern I have seen repeatedly in engagements I have supported is a SIEM or EDR platform generating a genuinely useful signal, only for that signal to be buried under hundreds of low-fidelity alerts with identical severity labels. Analysts develop alert fatigue and start triaging by habit rather than by risk. The fix is rarely more tooling; it is a disciplined severity and classification taxonomy applied consistently, tied to business impact rather than purely to technical signal strength — a failed login on a developer laptop and a failed login on a domain controller should never carry the same weight in the queue.

Structured incident documentation matters more than most junior analysts realise, and it is where I spend a disproportionate amount of coaching time. A ticket that says "suspicious PowerShell activity, investigated, closed" is worthless six months later when a pattern re-emerges and nobody can reconstruct what was actually checked. Good documentation captures the initial indicator, the hypothesis, the evidence gathered (with timestamps and source systems named), the MITRE ATT&CK techniques observed where relevant, and the actual justification for the closure decision. This is not bureaucracy for its own sake — it is what makes an incident defensible to an auditor, a regulator, or a board afterwards, and it is what makes detection engineering possible at all, because you cannot tune what you cannot review.

## Escalation and working with outside partners

Most incidents a SOC handles are mundane and resolved within the team. The ones that matter — ransomware deployment, data exfiltration, a suspected nation-state or organised actor — require escalation paths that are decided in advance, not improvised at 2 a.m. I have seen incident response degrade badly not because the technical response was wrong, but because nobody had pre-agreed who has authority to declare a major incident, who briefs leadership, and at what threshold external response partners or a national or sector CERT get looped in. Under NIS2 and similar regimes, many EU organisations now also carry formal notification-timeline obligations, which makes pre-agreed escalation criteria a compliance necessity as well as an operational one.

Working with external responders during a live incident has its own etiquette that is worth codifying: a single point of contact on each side, a shared and time-stamped evidence chain, and — something often forgotten — a clear line on what the internal SOC keeps doing itself (containment, business communication) versus what gets handed to specialists (forensic imaging, malware reverse engineering). Coordination breaks down fastest when both sides assume the other is doing the same task.

## Detection engineering: closing the gap between "logged" and "detected"

There is a persistent and dangerous assumption that if a log source is being ingested, the organisation is "covered." Ingestion is not detection. I routinely find, when reviewing detection coverage, that an organisation has excellent visibility into network traffic but almost nothing meaningful on endpoint process execution, or has EDR everywhere but no correlation rules tuned to how their actual environment behaves versus a generic vendor ruleset.

Mapping existing detection use cases against MITRE ATT&CK is one of the more honest exercises a SOC can do, precisely because it is uncomfortable — it usually reveals that an organisation has dense coverage of a handful of techniques (commonly around initial access and malware execution) and almost nothing on lateral movement, privilege escalation, or exfiltration via legitimate channels. Detection engineering, done properly, is a continuous cycle: identify the gap, write or tune a rule, validate it against realistic test data (not just vendor sample data), deploy it, and — critically — measure its false-positive rate in production before declaring victory. A rule nobody trusts gets silently ignored within a month.

## Continuous improvement is a discipline, not an aspiration

The single biggest maturity differentiator I see between SOCs is whether post-incident reviews actually change anything. Too many "lessons learned" sessions produce a document that is filed and never revisited. A mature SOC treats every non-trivial incident as an input to three things: playbook updates (was the response process itself adequate?), detection engineering backlog (should this have been caught earlier, and by what?), and automation candidates (which of the manual steps analysts performed under pressure could be automated safely next time?).

Automation deserves a caveat here, because it is oversold. Automating containment actions — isolating a host, disabling an account — is valuable, but only once the underlying detection logic is trusted enough that false positives will not automatically lock out a finance director during month-end close. I have seen automation introduced too early do more reputational damage to a security programme than the incidents it was meant to prevent. Sequencing matters: get the detection quality and triage discipline right first, document consistently, and only then automate the well-understood, low-ambiguity parts of the response. That order, more than any single tool, is what turns a SOC from a monitoring function into a genuine resilience capability.
