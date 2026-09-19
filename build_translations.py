#!/usr/bin/env python3
"""Generate the cached article translations for the portfolio page.

Reads the verified article list (headline, date, public summary) and asks the
model gateway to translate ONLY the headline and the public summary into five
languages. Body copy is paywalled and is never fetched, stored, or translated.

Output: assets/translations.json. The page loads this file, so it never calls
the gateway on a page load.

Usage:
    python3 build_translations.py            # regenerate all
    python3 build_translations.py --check    # verify every entry is present
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

WORK = Path(__file__).resolve().parent
OUT = WORK / "assets" / "translations.json"

LANGS = {
    "zh": "Simplified Chinese",
    "ja": "Japanese",
    "es": "Spanish",
    "ko": "Korean",
    "fa": "Persian (Farsi)",
}

# Verified from theinformation.com JSON-LD + og:description on 2026-09-19.
# Only the headline, the date, and the public summary are used. Summaries are
# the publisher's own og:description, trimmed at a sentence boundary.
ARTICLES = [
    {
        "id": "watchdog-independence",
        "date": "2026-09-18",
        "kind": "Feature",
        "url": "https://www.theinformation.com/articles/ai-safety-push-sparks-demand-watchdog-groups-critics-doubt-independence",
        "headline": "AI Safety Push Sparks Demand for Watchdog Groups. Critics Doubt Their Independence.",
        "summary": "Rising alarm about AI's perils is thrusting into the spotlight a collection of little-known research groups focused on the technology's safety, and fueling questions about their ability to effectively monitor the industry's biggest companies.",
    },
    {
        "id": "openai-incidents",
        "date": "2026-09-16",
        "kind": "Briefing",
        "url": "https://www.theinformation.com/briefings/openai-discloses-safety-incidents-adopts-new-reporting-framework",
        "headline": "OpenAI Discloses More Safety Incidents and Adopts New Reporting Framework",
        "summary": "OpenAI released a new framework for how it aims to report unsafe or concerning behavior in its models, and disclosed six incidents of such behavior it had observed in the past six months.",
    },
    {
        "id": "deepmind-resignations",
        "date": "2026-09-16",
        "kind": "Briefing",
        "url": "https://www.theinformation.com/briefings/two-google-deepmind-ai-researchers-resign-safety",
        "headline": "Two Google DeepMind AI Researchers Resign Over Safety",
        "summary": "Two researchers who worked on AI safety left their roles at Google DeepMind, stating that they departed over concerns that powerful systems could endanger humans.",
    },
    {
        "id": "musk-peer-review",
        "date": "2026-09-16",
        "kind": "Briefing",
        "url": "https://www.theinformation.com/briefings/elon-musk-says-ai-companies-test-others-models-safety",
        "headline": "Elon Musk Says AI Companies Should Test Each Other's Models for Safety",
        "summary": "SpaceX CEO Elon Musk proposed that competing AI companies should peer-review each other's models prior to release, as industry leaders acknowledge rising worries around AI safety.",
    },
    {
        "id": "swarm-hack",
        "date": "2026-09-12",
        "kind": "Briefing",
        "url": "https://www.theinformation.com/briefings/openai-ai-swarm-hacked-software-service-months-hugging-face-incident",
        "headline": "OpenAI AI Swarm Hacked Software Service Months Before Hugging Face Incident",
        "summary": "A swarm of OpenAI agents conducted a cyberattack on software service RubyGems in May, months before the company's agents hacked model platform Hugging Face.",
    },
]

SYSTEM = (
    "You are a professional news translator working for an editorial page. "
    "You receive a JSON object with a target_language and one or more string "
    "values. Translate each value into that language. Preserve the exact JSON "
    "keys. Return ONLY valid JSON with no prose, code fences, or commentary. "
    "Keep proper nouns (OpenAI, Google DeepMind, Elon Musk, The Information, "
    "RubyGems, Hugging Face, SpaceX) in their common form for the target "
    "language. Keep translations concise and news register. Do not add or "
    "remove facts. Keep every translated summary under 42 words."
)


def translate(strings: dict[str, str], lang_name: str) -> dict[str, str]:
    from clients.litellm_client import get_headers, litellm_request, resolve_model

    payload = {
        "model": resolve_model("claude-sonnet"),
        "messages": [
            {"role": "system", "content": SYSTEM},
            {
                "role": "user",
                "content": json.dumps(
                    {"target_language": lang_name, **strings}, ensure_ascii=False
                ),
            },
        ],
        "max_tokens": 1200,
        "temperature": 0,
    }
    last_err: Exception | None = None
    for attempt in range(4):
        payload["temperature"] = 0 if attempt == 0 else 0.4
        r = litellm_request(
            "POST",
            "/v1/chat/completions",
            json=payload,
            headers=get_headers(),
            timeout=120,
        )
        if r.status_code != 200:
            raise RuntimeError(f"gateway HTTP {r.status_code}: {r.text[:300]}")
        content = r.json()["choices"][0]["message"]["content"].strip()
        if content.startswith("```"):
            content = content.strip("`")
            content = content.split("\n", 1)[1] if "\n" in content else content
        try:
            data = _extract_json(content)
            for k in strings:
                if k not in data or not str(data[k]).strip():
                    raise ValueError(f"missing key {k!r}")
            return {k: _tidy(str(data[k])) for k in strings}
        except (json.JSONDecodeError, ValueError) as exc:
            last_err = exc
            print(f"    retry {lang_name} ({exc})", flush=True)
    raise RuntimeError(f"{lang_name}: unparseable response after 4 tries: {last_err}")


def _tidy(s: str) -> str:
    """Collapse whitespace and replace glyphs the slop gate bans."""
    s = " ".join(s.split())
    return s.replace("…", ",").replace("—", ", ").replace("–", ", ")


def _extract_json(text: str) -> dict:
    """Pull the first balanced JSON object out of a model response."""
    start = text.find("{")
    if start < 0:
        raise json.JSONDecodeError("no object", text, 0)
    depth = 0
    in_str = False
    esc = False
    for i in range(start, len(text)):
        ch = text[i]
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
            continue
        if ch == '"':
            in_str = True
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                return json.loads(text[start : i + 1])
    raise json.JSONDecodeError("unbalanced object", text, start)


def build(only: list[str] | None = None) -> dict:
    out: dict = {"languages": {k: v for k, v in LANGS.items()}, "articles": []}
    for art in ARTICLES:
        src = {"headline": art["headline"], "summary": art["summary"]}
        entry = {k: art[k] for k in ("id", "date", "kind", "url", "headline", "summary")}
        entry["translations"] = {}
        for code, name in LANGS.items():
            if only and code not in only:
                continue
            entry["translations"][code] = translate(src, name)
            print(f"  {art['id']:24s} {code} ok", flush=True)
        out["articles"].append(entry)
    return out


def check() -> int:
    if not OUT.exists():
        print("translations.json missing")
        return 1
    data = json.loads(OUT.read_text(encoding="utf-8"))
    bad = 0
    for art in data["articles"]:
        for code in LANGS:
            t = art.get("translations", {}).get(code, {})
            if not t.get("headline") or not t.get("summary"):
                print(f"MISSING {art['id']} {code}")
                bad += 1
    print(f"{len(data['articles'])} articles x {len(LANGS)} languages, {bad} missing")
    return 1 if bad else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--langs", help="comma list, e.g. zh,ja")
    args = ap.parse_args()
    if args.check:
        return check()
    only = args.langs.split(",") if args.langs else None
    data = build(only)
    if only and OUT.exists():
        prev = json.loads(OUT.read_text(encoding="utf-8"))
        for a, p in zip(data["articles"], prev["articles"]):
            for code, val in p.get("translations", {}).items():
                a["translations"].setdefault(code, val)
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"wrote {OUT} ({OUT.stat().st_size} bytes)")
    return check()


if __name__ == "__main__":
    sys.exit(main())
