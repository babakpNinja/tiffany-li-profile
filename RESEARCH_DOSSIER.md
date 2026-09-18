# Tiffany Li (The Information) — Verified Research Dossier

Prepared for the profile-page build. Everything below was pulled live on 2026-09-18
from theinformation.com or Tavily; nothing is inferred about her personally except
where labelled. See "Source discipline" at the end.

## 1. Identity — the right Tiffany Li

Tavily returns two people with this name. They are NOT the same person:
- **Tiffany C. Li** — law professor (Southwestern Law School / Yale ISP), privacy
  and AI law scholar. Different person.
- **Tiffany Li** — reporter at The Information, San Francisco. THIS is the person
  Babak is meeting. All bio facts below come from her own theinformation.com
  profile JSON-LD (author id 2805337), which is authoritative.

## 2. Bio — verbatim from her The Information profile

> Tiffany Li is a reporter at The Information's San Francisco office. She is the
> recipient of a Tarbell Fellowship, funded by the Tarbell Center for AI
> Journalism, which provides training in AI and journalism. She previously covered
> politics and campaigns for ABC News and WisPolitics. She also served as the
> editor-in-chief of the Chicago Maroon, the University of Chicago's student
> newspaper.

- Title on profile: **Editorial Fellow**
- Email: tiffany.li@theinformation.com
- Signal: @tiffanyli.99
- Profile: https://www.theinformation.com/u/tiffanyli25y4pe
- Photo (real, from profile): https://tii.imgix.net/production/avatars/2805337/Screenshot_2026-06-18_at_2.43.45_PM.png?w=1200&auto=compress,format
  (downloaded to research/tiffany.jpg, 1200x1200 JPEG)

## 3. Career timeline (from verifiable sources)

- University of Chicago, Class of 2026. Transferred from Middlebury College.
  Studies **political science and economics**. (Chicago Maroon staff page)
- **Chicago Maroon**: reporter and editor across News, and also on the Arts,
  Copy-editing and Data teams; elected **Editor-in-Chief for the 2025-26 term**
  (with Elena Eisenstadt deputy EIC, Evgenia Anastasakos). Source: chicagomaroon.com.
- **WisPolitics of State Affairs**, News Intern, Aug-Sep 2024 (Madison, WI).
  Published a deep dive on the rollout of a $525M Wisconsin housing package;
  covered the governor's 2025-27 biennial budget, the DNC, and used Excel for
  analysis. Source: LinkedIn / Maroon.
- **ABC News**: covered politics and campaigns. Source: her TI profile bio.
- **The Information**: Editorial Fellow, currently reporting AI safety.

## 4. Articles in 2026 (the beat: AI safety)

Five pieces visible on her profile, all AI-safety themed, Sept 2026:
- 2026-09-18 — "AI Safety Push Sparks Demand for Watchdog Groups. Critics Doubt
  Their Independence." (feature article) /articles/ai-safety-push-sparks-demand-watchdog-groups-critics-doubt-independence
- 2026-09-16 — "OpenAI Discloses More Safety Incidents and Adopts New Reporting Framework" (briefing)
- 2026-09-16 — "Two Google DeepMind AI Researchers Resign Over Safety" (briefing)
- 2026-09-16 — "Elon Musk Says AI Companies Should Test Each Other's Models for Safety" (briefing)
- 2026-09-12 — "OpenAI AI Swarm Hacked Software Service Months Before Hugging Face Incident" (briefing)

Bodies are paywalled (JSON-LD headline/date present, articleBody empty). Only
headlines and dates are verified; do NOT fabricate quotes or summaries.

## 5. What her beat tells us about what excites her (analysis, labelled)

Her five pieces cluster tightly on: independent AI safety oversight and whether
watchdogs are truly independent; safety-incident disclosure and reporting
frameworks; researcher departures over safety; cross-lab model testing; and
agentic systems going off the rails (the "AI swarm hacked a service" story).
Implication for article pitches: she rewards **accountability and governance
angles with named actors and concrete incidents**, not vendor marketing.

## 6. Voice and tone (observed from headlines; full text is paywalled)

Observable from the headlines alone:
- Concrete, noun-led headlines. Names actors (OpenAI, Google DeepMind, Elon
  Musk) rather than abstractions.
- Contrarian framing welded to the fact: "Critics Doubt Their Independence."
- Uses a plain colon-and-clause structure; no hype adjectives; no em dashes.
- Institutions named precisely (Google DeepMind, Hugging Face).

## 7. The Information design system (for visual alignment)

Verified by fetching theinformation.com and its CSS bundle:
- **Fonts** (real, from their @font-face): Suisse Int'l (body/UI), Suisse Works
  (serif, editorial), Suisse Neue, Suisse Screen, Suisse Int'l Mono, Noto Serif.
  Loadable at https://ti-assets.theinformation.com/assets/<file>.otf (HTTP 200).
- **Brand red**: #F32A52 (her TI icon mark fill). Near-black ink ~#0a0d1c.
- **Logo assets** (already extracted for the bouncy-ball app): the TI "I" icon
  SVG and the full "The Information" wordmark SVG. Wordmark viewBox 0 0 1270 132.
  Copies live in /workspace/ninja/tmp-build/ti-bouncy/*.svg.

## 8. NinjaTech enterprise positioning (from the supplied onepager V10 + enterprise page)

Use these facts, include NO pricing on the public profile page.

- An AI workforce you deploy and own, not a chat window you rent. 24/7 autonomous
  AI employees that take a goal and carry out the whole job, including agent-to-
  agent collaboration, on models you choose. Deployed into your own cloud account
  so output stays inside your boundary.
- Runs in Azure, AWS, Google Cloud, Oracle Cloud; behind your own firewall;
  on-prem and air-gapped options.
- Unmetered on open-weight models: no per-token billing, no rate limits, no
  overage. Frontier models and Internet Search draw on a set credit balance.
- 10x blended cost saving vs the frontier APIs it replaces, same work. Per-model
  multiples in the source: Opus 5 (~7.4x), Fable 5.1 (~8.6x), GPT-6 Astra (~14.8x).
- Every AI employee gets an isolated VM, writes and runs code, drives a real
  browser, works 24/7 unattended, and improves from every run.
- "The best model in every modality": Anthropic and OpenAI for frontier text and
  images, Seedance for video, ElevenLabs for audio and voice, Tavily for search.
- Forward deployed engineers from Infosys are included and run on the already-
  bought unmetered capacity, so their output spends no tokens.
- Deployed in your tenant on dedicated, single-tenant US GPUs. Your prompts never
  enter a shared pool. Scale to a serverless shared endpoint vs dedicated endpoint
  comparison, and a SaaS platform vs deployed-in-tenant comparison.
- Enterprise page: SOC 2 Type II in progress; HIPAA-eligible deployments inside a
  BAA-covered environment. Tokens encrypted at rest (Fernet); OIDC SSO; RBAC;
  full audit trails; in-stack git server (Gitea); LiteLLM control plane; Caddy
  single entry point.
- Announcing: 24/7 enterprise AI employee platform, turn-key, fully unmetered,
  on **Sep 28**.
- BANNED from public copy per the playbook and the onepager: "model-agnostic",
  "works with any model". Mandated phrasing: "the best frontier models,
  proprietary or open-source."

## 9. Dos and don'ts for working with Tiffany (analysis for Babak)

DO:
- Lead with the accountability angle. Her whole current beat is who watches the
  AI and whether the watchers are independent. A vendor that submits to external
  oversight is a story; a vendor that claims to be safe is not.
- Bring named, checkable specifics: incident counts, named labs, dates, named
  people, mechanisms. Her headlines are built from exactly these.
- Offer the "watchdog independence" question honestly: what a third party could
  actually verify about a platform deployed in a customer's own cloud.
- Put the enterprise facts in her hands ahead of the meeting (unmetered, in-tenant,
  dedicated US GPUs, air-gapped option, no egress with open-weight).
- Respect her employer: The Information is a paid, independent newsroom. Anything
  embargoed must stay embargoed, and the Sep 28 announcement is a fact to give,
  not a favour to ask.

DON'T:
- Do not pitch "AI replaces people." The enterprise page itself frames it as
  capacity, not replacement. Her beat would treat a replacement claim as a
  safety-and-labour story, not a product story.
- Do not put pricing, contract figures or internal economics in front of a
  reporter, and do not put any on the public profile page. The onepager has
  internal figures; they do not travel.
- Do not use banned language ("model-agnostic", "any model", em dashes,
  "seamless" and the rest). A reporter notices, and our own style gate blocks it.
- Do not conflate her with Tiffany C. Li the law professor. Different person.
- Do not fabricate quotes, article summaries, or a personal connection. Her
  article bodies are paywalled; only headlines and dates are verified.

## 10. Source discipline

- Her bio, title, email, photo URL, article headlines and dates: theinformation.com
  profile JSON-LD (author 2805337), fetched 2026-09-18.
- Career details (UChicago, Maroon EIC, WisPolitics internship): Chicago Maroon
  staff/leadership pages and LinkedIn summaries via Tavily.
- Design system (fonts, colors, logo): theinformation.com HTML + its CSS bundle.
- Enterprise facts: the supplied ninja_unmetered_onepager - V10.pdf and
  ninjatech.ai/solutions/enterprise.
- Section 5, 6 and 9 are explicitly analysis, not verified fact.
