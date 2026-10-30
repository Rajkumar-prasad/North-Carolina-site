#!/usr/bin/env python3
"""Static site generator for the garage door referral site.

Usage:  pip install zipcodes   then   python3 build/build.py
Output: public/   (set this as the output folder on Cloudflare Pages / Vercel)

Edit CONFIG below for the domain, name and tracking number.
Edit build/content.py for the text. Add a city to TOP_CITIES in content.py
(with real, specific content) to make its page indexable.
"""
import collections, html, json, math, os, re, shutil, sys
from datetime import date

import zipcodes

sys.path.insert(0, os.path.dirname(__file__))
from content import (SERVICES, PROBLEMS, STEPS, DOOR_TYPES, CHECKLIST, HOME_FAQ,
                     GUIDES, REGIONS, TOP_CITIES)

# ------------------------------------------------------------------ CONFIG
CONFIG = {
    "domain": "https://garagedoorrepairservices.online",
    "site_name": "GarageDoorRepairServices.online",
    "brand_top": "Garage Door",
    "brand_sub": "REPAIR SERVICES",
    "phone_display": "(555) 000-0000",   # <-- replace with your MarketCall tracking number
    "phone_tel": "+15550000000",          # <-- same number in +1XXXXXXXXXX format
    "email": "hello@garagedoorrepairservices.online",
    "state": "NC",
    "state_name": "North Carolina",
    "state_slug": "north-carolina",
}
# -------------------------------------------------------------------------

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILD = os.path.join(ROOT, "build")
OUT = os.path.join(ROOT, "public")
TODAY = date.today().isoformat()
DISPLAY_FIX = {"Winston Salem": "Winston-Salem"}
C = CONFIG
e = html.escape

DISCLAIMER = (
    f"{C['site_name']} is a free service to assist homeowners in connecting with local service providers. "
    f"All contractors/providers are independent and {C['site_name']} does not warrant or guarantee any work performed. "
    "It is the responsibility of the homeowner to verify that the hired contractor furnishes the necessary license and "
    "insurance required for the work being performed. All persons depicted in a photo or video are actors or models and "
    f"not contractors listed on {C['site_name']}."
)


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def disp(city):
    return DISPLAY_FIX.get(city, city.title() if city.isupper() else city)


# ------------------------------------------------------------------ icons
ICONS = {
    "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "check": '<svg viewBox="0 0 24 24" fill="none" stroke="#4c6b14" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10" fill="#d4f34a" stroke="none"/><path d="M7.5 12.5l3 3 6-6.5" stroke="#1a2410"/></svg>',
    "repair": '<svg viewBox="0 0 24 24" fill="none" stroke="#d4f34a" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a4 4 0 0 0-5.4 5.4L3 18l3 3 6.3-6.3a4 4 0 0 0 5.4-5.4l-2.5 2.5-2.4-.6-.6-2.4z"/></svg>',
    "spring": '<svg viewBox="0 0 24 24" fill="none" stroke="#d4f34a" stroke-width="1.8" stroke-linecap="round"><path d="M3 12h2M19 12h2"/><path d="M5 12c0-3 2-3 2 0s2 3 2 0 2-3 2 0 2 3 2 0 2-3 2 0 2 3 2 0"/><path d="M5 12c0 3 2 3 2 0M17 12c0 3 2 3 2 0"/></svg>',
    "opener": '<svg viewBox="0 0 24 24" fill="none" stroke="#d4f34a" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="7" y="3" width="10" height="18" rx="3"/><circle cx="12" cy="9" r="2"/><path d="M10 15h4M10 18h4"/></svg>',
    "track": '<svg viewBox="0 0 24 24" fill="none" stroke="#d4f34a" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M5 21V8a5 5 0 0 1 5-5h9"/><circle cx="5" cy="13" r="2"/><circle cx="12" cy="3" r="0.5"/></svg>',
    "install": '<svg viewBox="0 0 24 24" fill="none" stroke="#d4f34a" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 10l9-6 9 6v11H3z"/><path d="M7 21v-8h10v8M7 16h10"/></svg>',
    "panel": '<svg viewBox="0 0 24 24" fill="none" stroke="#d4f34a" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="16" rx="1.5"/><path d="M3 8h18M3 12h18M3 16h18"/></svg>',
    "door": '<svg viewBox="0 0 24 24" fill="none" stroke="#d4f34a" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 10l9-6 9 6v11H3z"/><path d="M6 21v-9h12v9M6 15h12M6 18h12"/></svg>',
}
LOGO_MARK = '<svg viewBox="0 0 24 24" fill="none" stroke="#d4f34a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 10l9-6 9 6v11H3z"/><path d="M6.5 21v-8.5h11V21M6.5 15.5h11M6.5 18.3h11"/></svg>'


def door_art(cls="door-art"):
    rows = "".join(
        f'<rect x="58" y="{118 + i*36}" width="284" height="32" rx="3" fill="#{c}"/>'
        f'<rect x="72" y="{126 + i*36}" width="120" height="16" rx="2" fill="none" stroke="#2d4a37" stroke-width="2"/>'
        f'<rect x="208" y="{126 + i*36}" width="120" height="16" rx="2" fill="none" stroke="#2d4a37" stroke-width="2"/>'
        for i, c in enumerate(["e9ede4", "e3e8dd", "dde3d6", "d6ddce", "d0d8c7"]))
    return f'''<svg class="{cls}" viewBox="0 0 400 340" aria-hidden="true">
<path d="M20 112 200 20l180 92" fill="none" stroke="#d4f34a" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/>
<rect x="40" y="100" width="320" height="230" rx="10" fill="#0c140f" stroke="#2d4a37" stroke-width="3"/>
{rows}
<rect x="176" y="292" width="48" height="8" rx="4" fill="#d4f34a"/>
<rect x="30" y="322" width="340" height="10" rx="5" fill="#2d4a37"/>
</svg>'''


def type_art(kind):
    if kind == 0:  # insulated steel - raised panels
        cells = "".join(f'<rect x="{18 + c*44}" y="{20 + r*34}" width="38" height="26" rx="3" fill="none" stroke="#9aa58f" stroke-width="2.5"/>' for r in range(4) for c in range(4))
        return f'<svg viewBox="0 0 200 160"><rect x="8" y="10" width="184" height="146" rx="6" fill="#f7f8f4" stroke="#13241a" stroke-width="3"/>{cells}</svg>'
    if kind == 1:  # wood look - vertical planks
        planks = "".join(f'<rect x="{14 + i*22}" y="16" width="20" height="134" fill="#{c}"/>' for i, c in enumerate(["b07a4a", "a46f42", "b98353", "a87346", "b17b4b", "9f6a3e", "b48050", "a97448"]))
        return f'<svg viewBox="0 0 200 160"><rect x="8" y="10" width="184" height="146" rx="6" fill="#7a4f2c" stroke="#13241a" stroke-width="3"/>{planks}<rect x="14" y="80" width="176" height="4" fill="#5e3c20"/></svg>'
    glass = "".join(f'<rect x="{16 + c*44}" y="{18 + r*34}" width="40" height="30" fill="#bfd3d8" stroke="#2b3a33" stroke-width="3"/>' for r in range(4) for c in range(4))
    return f'<svg viewBox="0 0 200 160"><rect x="8" y="10" width="184" height="146" rx="4" fill="#2b3a33" stroke="#13241a" stroke-width="3"/>{glass}</svg>'


# ------------------------------------------------------------------ data
def load_data():
    raw = [l.strip().zfill(5) for l in open(os.path.join(BUILD, "data", "target-zips.txt")) if l.strip()]
    covered = sorted(set(raw))
    cities = collections.OrderedDict()
    zip_to_city = {}
    for z in covered:
        m = zipcodes.matching(z)
        if not m:
            continue
        m = m[0]
        if m["state"] != C["state"]:
            continue
        key = m["city"]
        if m["zip_code_type"] == "STANDARD":
            c = cities.setdefault(key, {"name": disp(key), "slug": slugify(disp(key)), "zips": [], "counties": collections.Counter(), "pts": []})
            c["zips"].append(z)
            c["counties"][m["county"]] += 1
            c["pts"].append((float(m["lat"]), float(m["long"])))
        zip_to_city[z] = key
    for c in cities.values():
        c["county"] = c["counties"].most_common(1)[0][0]
        c["lat"] = sum(p[0] for p in c["pts"]) / len(c["pts"])
        c["lon"] = sum(p[1] for p in c["pts"]) / len(c["pts"])
        c["indexed"] = c["name"] in TOP_CITIES or (c["name"] == "Winston-Salem" and "Winston Salem" in TOP_CITIES)
    # PO box / unique ZIPs map to their city page if it exists
    nc_map = {z: f"{cities[k]['slug']}|{cities[k]['name']}" for z, k in zip_to_city.items() if k in cities}

    def dist(a, b):
        return math.hypot(a["lat"] - b["lat"], (a["lon"] - b["lon"]) * math.cos(math.radians(a["lat"])))
    vals = list(cities.values())
    for c in vals:
        c["nearby"] = sorted((o for o in vals if o is not c), key=lambda o: dist(c, o))[:8]
    return covered, cities, nc_map


# ------------------------------------------------------------------ layout
def call_btn(cls="btn-lime", label=None):
    label = label or f"Call {C['phone_display']}"
    return f'<a class="btn {cls}" href="tel:{C["phone_tel"]}"><span class="dot">{ICONS["phone"]}</span>{e(label)}</a>'


def head(title, desc, path, indexed=True, schema=None):
    url = C["domain"] + path
    robots = "index,follow" if indexed else "noindex,follow"
    sch = "".join(f'<script type="application/ld+json">{json.dumps(s)}</script>' for s in (schema or []))
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta name="theme-color" content="#0c140f">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
{sch}
</head>
<body data-phone="{e(C['phone_display'])}" data-tel="{C['phone_tel']}">
'''


def header(active=""):
    def a(href, label, key):
        return f'<a href="{href}"{" class=\"active\"" if active == key else ""}>{label}</a>'
    return f'''<div class="topbar"><div class="wrap"><span>Connecting {C['state_name']} homeowners with local garage door pros</span><span class="hide-sm">Call <a href="tel:{C['phone_tel']}">{C['phone_display']}</a></span></div></div>
<header class="site"><div class="wrap">
<a class="logo" href="/"><span class="logo-mark">{LOGO_MARK}</span><span>{C['brand_top']}<small>{C['brand_sub']}</small></span></a>
<nav class="main" aria-label="Main">
{a('/', 'Home', 'home')}
{a('/' + C['state_slug'] + '/', 'Locations', 'loc')}
{a('/guides/', 'Guides', 'guides')}
{a('/about/', 'How It Works', 'about')}
</nav>
<div class="header-cta">
<a class="phone-pill" href="tel:{C['phone_tel']}">{ICONS['phone']}{C['phone_display']}</a>
{call_btn('btn-lime', 'Call Now')}
<button class="menu-btn" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
</div>
</div></header>
<main>
'''


def footer(top_cities):
    cities = "".join(f'<li><a href="/{C["state_slug"]}/{c["slug"]}/">{e(c["name"])}</a></li>' for c in top_cities[:6])
    guides = "".join(f'<li><a href="/guides/{g["slug"]}/">{e(g["short"])}</a></li>' for g in GUIDES)
    return f'''</main>
<footer class="site"><div class="wrap">
<div class="foot-grid">
<div><a class="logo" href="/" style="color:#fff"><span class="logo-mark">{LOGO_MARK}</span><span>{C['brand_top']}<small style="color:#98a59b">{C['brand_sub']}</small></span></a>
<p style="margin-top:16px;max-width:320px">A free referral service that connects {C['state_name']} homeowners with independent local garage door providers for repair, replacement and installation.</p>
<p><a href="tel:{C['phone_tel']}" style="color:var(--lime);font-weight:700;font-size:18px">{C['phone_display']}</a></p></div>
<div><h4>Guides</h4><ul>{guides}</ul></div>
<div><h4>Popular Locations</h4><ul>{cities}<li><a href="/{C['state_slug']}/">All {C['state_name']} cities</a></li></ul></div>
<div><h4>Company</h4><ul><li><a href="/about/">How It Works</a></li><li><a href="/privacy-policy/">Privacy Policy</a></li><li><a href="/terms/">Terms of Use</a></li><li><a href="/sitemap.xml">Sitemap</a></li></ul></div>
</div>
<div class="foot-big" aria-hidden="true">Garage Door Help</div>
<div class="disclaimer"><p><b>Disclaimer:</b> {e(DISCLAIMER)}</p>
<p>Calls may be recorded by our call-routing partner for quality and verification purposes.</p></div>
<div class="foot-bottom"><span>&copy; {date.today().year} {e(C['site_name'])}. All rights reserved.</span><span><a href="/privacy-policy/">Privacy</a> &middot; <a href="/terms/">Terms</a></span></div>
</div></footer>
<a class="callbar" href="tel:{C['phone_tel']}">{ICONS['phone']} Call {C['phone_display']}</a>
<script src="/assets/zips.js" defer></script>
<script src="/assets/main.js" defer></script>
</body></html>
'''


def zipbox(label="Check if we cover your area"):
    return f'''<div class="zipbox"><label for="zip-{id(label)}">{e(label)}</label>
<form data-zipcheck><input id="zip-{id(label)}" inputmode="numeric" maxlength="5" placeholder="Enter your ZIP code" aria-label="ZIP code"><button class="btn btn-dark" type="submit">Check ZIP</button></form>
<div class="zip-result" role="status" aria-live="polite"></div></div>'''


def faq_html(items):
    return '<div class="faq">' + "".join(
        f'<details{" open" if i == 0 else ""}><summary>{e(q)}</summary><div class="a">{e(a)}</div></details>'
        for i, (q, a) in enumerate(items)) + "</div>"


def faq_schema(items):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}


def crumbs_schema(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": C["domain"] + p} for i, (n, p) in enumerate(items)]}


def crumbs_html(items):
    parts = [f'<a href="{p}">{e(n)}</a>' for n, p in items[:-1]] + [e(items[-1][0])]
    return '<div class="crumbs">' + " / ".join(parts) + "</div>"


# ------------------------------------------------------------------ sections
def services_section(city=None):
    where = f" in {e(city)}" if city else ""
    cards = "".join(
        f'<a class="svc{" solid" if i == 0 else ""}" href="{link}"><span class="tag">Service {i+1:02d}</span><span class="ico">{ICONS[k]}</span>'
        f'<h3>{e(t)}</h3><p>{e(d)}</p><span class="more">Learn more &rarr;</span></a>'
        for i, (k, t, d, link) in enumerate(SERVICES))
    return f'''<section class="section mist"><div class="wrap">
<div class="head-row"><div><div class="eyebrow">Services</div><h2>Garage door help{where} for every problem</h2></div>
<p class="lead">Repairs for the problem you have today, or a full replacement when it's time for a new door.</p></div>
<div class="grid g3">{cards}</div></div></section>'''


def steps_section():
    cards = "".join(f'<div class="step"><span class="n">{i+1:02d}</span><h3>{e(t)}</h3><p>{e(d)}</p></div>' for i, (t, d) in enumerate(STEPS))
    return f'''<section class="section dark"><div class="wrap">
<div class="head-row"><div><div class="eyebrow">How it works</div><h2>From garage door problem to working door</h2></div>
<p class="lead">Three simple steps. One call connects you with a local provider.</p></div>
<div class="grid g3 steps">{cards}</div></div></section>'''


def checklist_section():
    items = "".join(f'<li>{ICONS["check"]}<div><b>{e(t)}</b><span>{e(d)}</span></div></li>' for t, d in CHECKLIST)
    return f'''<section class="section"><div class="wrap split">
<div><div class="eyebrow">Hire with confidence</div><h2>What to ask before work begins</h2>
<p class="lead">Every provider in our network is an independent business. These questions help you choose with confidence.</p>
<ul class="checklist">{items}</ul></div>
<div class="note-card"><h3>Never DIY a spring</h3><p>Garage door springs hold enough tension to cause serious injury. If a spring is broken, keep the door closed, unplug the opener, and let a trained technician handle it.</p>
<p>The same goes for lift cables and the bottom brackets they attach to.</p>{call_btn('btn-lime', 'Talk to a local pro')}</div>
</div></section>'''


def cta_band(city=None):
    title = f"Garage door stuck in {e(city)}?" if city else "Garage door stuck or refusing to open?"
    return f'''<section class="section" style="padding-top:0"><div class="wrap"><div class="cta-band">
<h2>{title}</h2><p>Call now to be connected with an independent local garage door provider and book a technician visit.</p>
<div class="hero-actions">{call_btn('btn-lime')}<a class="btn btn-ghost" href="/guides/">Read our guides</a></div>
</div></div></section>'''


def guides_section(limit=4):
    cards = "".join(
        f'<a class="guide-card" href="/guides/{g["slug"]}/"><div class="thumb">{ICONS[g["icon"]]}</div><div>'
        f'<h3>{e(g["title"])}</h3><p>{e(g["desc"])}</p><span class="more" style="font-size:13px;font-weight:600;color:#4c6b14">Read guide &rarr;</span></div></a>'
        for g in GUIDES[:limit])
    return f'''<section class="section"><div class="wrap">
<div class="head-row"><div><div class="eyebrow">Guides</div><h2>Helpful advice for a safer garage door</h2></div>
<a class="btn btn-dark" href="/guides/">All guides <span class="dot">{ICONS['arrow']}</span></a></div>
<div class="grid g2">{cards}</div></div></section>'''


# ------------------------------------------------------------------ pages
def write(path, content):
    full = os.path.join(OUT, path.strip("/"), "index.html") if not path.endswith(".html") else os.path.join(OUT, path.strip("/"))
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w") as f:
        f.write(content)


def build_home(cities, covered, top):
    n_cities = len(cities)
    n_zips = sum(len(c["zips"]) for c in cities.values())
    n_counties = len({c["county"] for c in cities.values()})
    problems = PROBLEMS
    pcard = lambda i, p: (f'<a class="card" href="{p[2]}"><span class="num">{i+1:02d}</span><h3>{e(p[0])}</h3><p>{e(p[1])}</p>'
                          f'<span class="more">Find the fix &rarr;</span></a>')
    door_cards = "".join(
        f'<div class="doortype"><div class="art">{type_art(i)}</div><div class="body"><span class="tag">{e(t)}</span><h3>{e(n)}</h3><p>{e(d)}</p></div></div>'
        for i, (t, n, d) in enumerate(DOOR_TYPES))
    city_links = "".join(f'<a href="/{C["state_slug"]}/{c["slug"]}/">{e(c["name"])}</a>' for c in top)
    mini = [("Clear guidance", "Plain-English guides help you understand the problem before you call."),
            ("Local providers", "Calls are routed to independent providers who serve your ZIP code."),
            ("Repair or replace", "Spring, opener, cable and track repairs, plus full door installation."),
            ("Free to use", "There is no charge to use this service to find a provider.")]
    minis = "".join(f'<div class="mini"><h3>{e(t)}</h3><p>{e(d)}</p></div>' for t, d in mini)
    schema = [{"@context": "https://schema.org", "@type": "WebSite", "name": C["site_name"], "url": C["domain"] + "/"}, faq_schema(HOME_FAQ)]
    body = f'''<section class="hero"><div class="wrap"><div class="hero-card"><div class="hero-grid"><div>
<span class="badge"><i></i>Serving {n_cities} cities across {C['state_name']}</span>
<h1>Garage door stuck? <span class="outline">Get it moving again.</span></h1>
<p class="lead">Broken springs, doors off track, openers that won't respond, or a brand-new door - one call connects you with an independent local garage door provider.</p>
<div class="hero-actions">{call_btn('btn-lime')}<a class="btn btn-ghost" href="/{C['state_slug']}/">Find your city <span class="dot">{ICONS['arrow']}</span></a></div>
{zipbox()}
</div><div>{door_art()}</div></div>
<div class="hero-stats">
<div class="stat"><b>{n_cities}</b><span>NC cities covered</span></div>
<div class="stat"><b>{n_zips}</b><span>ZIP codes served</span></div>
<div class="stat"><b>{n_counties}</b><span>Counties</span></div>
<div class="stat"><b>{len(SERVICES)}</b><span>Service types</span></div>
</div></div></div></section>

<section class="section"><div class="wrap">
<div class="head-row"><div><div class="eyebrow">Common problems</div><h2>What's happening with your garage door?</h2></div>
<p class="lead">Choose the problem that sounds closest to yours to see what usually causes it and what to do next.</p></div>
<div class="problem-grid"><div class="stack">{pcard(0, problems[0])}{pcard(1, problems[1])}</div>
<div class="feature-art">{door_art('')}</div>
<div class="stack">{pcard(2, problems[2])}{pcard(3, problems[3])}</div></div>
</div></section>

{services_section()}

<section class="section"><div class="wrap split">
<div><div class="eyebrow">Why use us</div><h2>Clear answers before the work begins</h2>
<p class="lead">A garage door problem can stop your whole day. We help you understand what's wrong and get connected with someone local who can fix it.</p>
<div class="grid g2" style="margin:24px 0">{minis}</div>
{call_btn('btn-dark', 'Call to get connected')}</div>
<div class="feature-art" style="min-height:420px">{door_art('')}</div>
</div></section>

{steps_section()}

<section class="section"><div class="wrap">
<div class="head-row"><div><div class="eyebrow">Thinking of replacing?</div><h2>Popular garage door styles</h2></div>
<p class="lead">A new door can change how your whole home looks. These are the most common options providers install.</p></div>
<div class="grid g3">{door_cards}</div></div></section>

{checklist_section()}

<section class="section mist"><div class="wrap split" style="align-items:start">
<div><div class="eyebrow">FAQ</div><h2>Before you make the call</h2><p class="lead">Quick answers to the questions homeowners ask most.</p>{call_btn('btn-dark')}</div>
{faq_html(HOME_FAQ)}</div></section>

<section class="section"><div class="wrap">
<div class="head-row"><div><div class="eyebrow">Locations</div><h2>Popular {C['state_name']} cities</h2></div>
<a class="btn btn-outline" href="/{C['state_slug']}/">All {n_cities} cities</a></div>
<div class="city-links">{city_links}</div></div></section>

{cta_band()}
{guides_section()}
'''
    title = f"Garage Door Repair & Installation in {C['state_name']} | {C['site_name']}"
    desc = f"Garage door stuck, spring broken or opener not working? Call to be connected with an independent local garage door provider in {C['state_name']}."
    write("/", head(title, desc, "/", True, schema) + header("home") + body + footer(top))


def build_hub(cities, top):
    by_county = collections.defaultdict(list)
    for c in cities.values():
        by_county[c["county"]].append(c)
    blocks = "".join(
        f'<div class="county-block" data-county="{e(county.lower())}"><h3>{e(county)}</h3><ul>' +
        "".join(f'<li><a href="/{C["state_slug"]}/{c["slug"]}/">{e(c["name"])}</a></li>' for c in sorted(cs, key=lambda x: x["name"])) +
        "</ul></div>"
        for county, cs in sorted(by_county.items()))
    city_links = "".join(f'<a href="/{C["state_slug"]}/{c["slug"]}/">{e(c["name"])}</a>' for c in top)
    path = f"/{C['state_slug']}/"
    cr = [("Home", "/"), (C["state_name"], path)]
    body = f'''<section class="page-hero"><div class="wrap">{crumbs_html(cr)}
<h1>Garage door repair across {C['state_name']}</h1>
<p class="lead">Find your city below - {len(cities)} cities in {len(by_county)} counties. Every page shows the ZIP codes covered and how to reach a local provider.</p>
<div class="hero-actions">{call_btn('btn-lime')}</div>{zipbox('Or check your ZIP code')}
</div></section>
<section class="section"><div class="wrap">
<div class="eyebrow">Most searched</div><h2>Popular cities</h2><div class="city-links" style="margin-bottom:56px">{city_links}</div>
<div class="eyebrow">All locations</div><h2>Cities by county</h2>
<input class="filter" data-cityfilter placeholder="Filter by city or county" aria-label="Filter cities">
<div class="county-cols">{blocks}</div></div></section>
{services_section()}
{cta_band()}
'''
    title = f"Garage Door Repair in {C['state_name']} - All Cities | {C['site_name']}"
    desc = f"Garage door repair and installation in {len(cities)} {C['state_name']} cities. Find your city or check your ZIP code, then call to be connected with a local provider."
    write(path, head(title, desc, path, True, [crumbs_schema(cr)]) + header("loc") + body + footer(top))


def build_city(c, top):
    name = c["name"]
    path = f"/{C['state_slug']}/{c['slug']}/"
    key = "Winston Salem" if name == "Winston-Salem" else name
    top_info = TOP_CITIES.get(key)
    chips = "".join(f"<span>{z}</span>" for z in c["zips"])
    nearby = "".join(f'<a href="/{C["state_slug"]}/{n["slug"]}/">{e(n["name"])}</a>' for n in c["nearby"])
    cr = [("Home", "/"), (C["state_name"], f"/{C['state_slug']}/"), (name, path)]
    zip_txt = ", ".join(c["zips"])
    faqs = [
        (f"Which ZIP codes in {name} do you cover?", f"We connect homeowners in these {name} ZIP codes: {zip_txt}."),
        (f"Can I get a new garage door installed in {name}?", f"Yes. Providers serving {name} handle new door installation and full replacements as well as repairs."),
        ("Is there a charge to use this service?", "No. Using this service to be connected with a provider is free. You agree any price for the work directly with the provider."),
        ("What should I do if my garage door spring breaks?", "Keep the door closed, unplug the opener and don't try to replace the spring yourself. Call to be connected with a local technician."),
    ]
    local = ""
    if top_info:
        region = REGIONS[top_info[0]]
        paras = "".join(f"<p>{e(p)}</p>" for p in region["paras"])
        tips = "".join(f"<li>{e(t)}</li>" for t in region["tips"])
        local = f'''<section class="section"><div class="wrap article">
<div class="prose"><div class="eyebrow">Local know-how</div><h2>Garage door care in {e(name)}</h2>
<p>{e(top_info[1])} Homeowners here call about the same problems as anywhere else in the {e(region['name'])} area - broken springs, openers that stop responding, doors that won't close, and worn-out doors ready for replacement.</p>
{paras}<h3>Seasonal tips for {e(name)} homeowners</h3><ul>{tips}</ul>
<p>Not sure what's wrong? Start with our guides to <a href="/guides/garage-door-wont-close/">doors that won't close</a>, <a href="/guides/broken-garage-door-spring/">broken springs</a> and <a href="/guides/garage-door-opener-not-working/">opener problems</a>.</p></div>
<aside class="aside"><div class="facts"><h3>{e(name)} at a glance</h3><dl>
<dt>County</dt><dd>{e(c['county'])}</dd>
<dt>ZIP codes covered</dt><dd>{len(c['zips'])} - {e(zip_txt)}</dd>
<dt>Nearby areas</dt><dd>{e(', '.join(n['name'] for n in c['nearby'][:4]))}</dd>
</dl></div>{call_btn('btn-dark')}</aside></div></section>'''
    pcards = "".join(f'<a class="card" href="{p[2]}"><span class="num">{i+1:02d}</span><h3>{e(p[0])}</h3><p>{e(p[1])}</p><span class="more">Find the fix &rarr;</span></a>' for i, p in enumerate(PROBLEMS))
    body = f'''<section class="page-hero"><div class="wrap">{crumbs_html(cr)}
<h1>Garage door repair &amp; installation in {e(name)}, {C['state']}</h1>
<p class="lead">Broken spring, door off track, opener not working, or ready for a new door? Call to be connected with an independent garage door provider serving {e(name)} and {e(c['county'])}.</p>
<div class="hero-actions">{call_btn('btn-lime')}<a class="btn btn-ghost" href="#services">See services</a></div>
<div class="zip-chips" aria-label="ZIP codes covered">{chips}</div>
</div></section>
<section class="section"><div class="wrap">
<div class="head-row"><div><div class="eyebrow">Common problems</div><h2>What's happening with your door?</h2></div>
<p class="lead">Pick the closest match to see what usually causes it and what to do next.</p></div>
<div class="grid g4">{pcards}</div></div></section>
{local}
<div id="services"></div>{services_section(name)}
{steps_section()}
{checklist_section()}
<section class="section mist"><div class="wrap split" style="align-items:start">
<div><div class="eyebrow">FAQ</div><h2>Garage door questions in {e(name)}</h2>{call_btn('btn-dark')}</div>{faq_html(faqs)}</div></section>
<section class="section"><div class="wrap"><div class="eyebrow">Nearby</div><h2>Nearby cities we cover</h2>
<div class="city-links">{nearby}<a href="/{C['state_slug']}/">All {C['state_name']} cities</a></div></div></section>
{cta_band(name)}
'''
    title = f"Garage Door Repair in {name}, {C['state']} | {C['site_name']}"
    desc = f"Garage door repair, spring and opener service, and new door installation in {name}, {C['state']}. Call to be connected with a local provider."
    schema = [crumbs_schema(cr)] + ([faq_schema(faqs)] if c["indexed"] else [])
    write(path, head(title, desc, path, c["indexed"], schema) + header("loc") + body + footer(top))


def build_guides(top):
    cards = "".join(
        f'<a class="guide-card" href="/guides/{g["slug"]}/"><div class="thumb">{ICONS[g["icon"]]}</div><div>'
        f'<h3>{e(g["title"])}</h3><p>{e(g["desc"])}</p></div></a>' for g in GUIDES)
    cr = [("Home", "/"), ("Guides", "/guides/")]
    body = f'''<section class="page-hero"><div class="wrap">{crumbs_html(cr)}<h1>Garage door guides</h1>
<p class="lead">Plain-English help for the most common garage door problems - what causes them, what you can safely check, and when to call a technician.</p></div></section>
<section class="section"><div class="wrap"><div class="grid g2">{cards}</div></div></section>{cta_band()}'''
    write("/guides/", head(f"Garage Door Guides | {C['site_name']}", "Guides to broken springs, doors off track, openers, noisy doors and choosing between repair and replacement.", "/guides/", True, [crumbs_schema(cr)]) + header("guides") + body + footer(top))
    for g in GUIDES:
        path = f"/guides/{g['slug']}/"
        cr = [("Home", "/"), ("Guides", "/guides/"), (g["short"], path)]
        others = "".join(f'<li><a href="/guides/{o["slug"]}/">{e(o["title"])}</a></li>' for o in GUIDES if o is not g)
        body = f'''<section class="page-hero"><div class="wrap">{crumbs_html(cr)}<h1>{e(g['title'])}</h1><p class="lead">{e(g['desc'])}</p>
<div class="hero-actions">{call_btn('btn-lime')}</div></div></section>
<section class="section"><div class="wrap article"><article class="prose">{g['body']}</article>
<aside class="aside"><div class="facts"><h3>Need a technician?</h3><p style="font-size:14px;color:var(--muted)">Call to be connected with an independent garage door provider near you.</p>{call_btn('btn-dark')}</div>
<div class="facts"><h3>More guides</h3><ul style="padding-left:18px;font-size:14px;margin:0">{others}</ul></div></aside></div></section>
{cta_band()}'''
        schema = [crumbs_schema(cr), {"@context": "https://schema.org", "@type": "Article", "headline": g["title"], "description": g["desc"],
                                      "dateModified": TODAY, "publisher": {"@type": "Organization", "name": C["site_name"]}}]
        write(path, head(f"{g['title']} | {C['site_name']}", g["desc"], path, True, schema) + header("guides") + body + footer(top))


def simple_page(path, title, h1, lead, html_body, top, active=""):
    cr = [("Home", "/"), (h1, path)]
    body = f'''<section class="page-hero"><div class="wrap">{crumbs_html(cr)}<h1>{e(h1)}</h1><p class="lead">{e(lead)}</p></div></section>
<section class="section"><div class="wrap"><div class="prose" style="max-width:780px">{html_body}</div></div></section>'''
    write(path, head(f"{title} | {C['site_name']}", lead, path, True, [crumbs_schema(cr)]) + header(active) + body + footer(top))


def build_static_pages(top):
    sn = e(C["site_name"])
    simple_page("/about/", "How It Works", "How it works", "A free service that connects homeowners with independent local garage door providers.", f'''
<p>{sn} is a referral service. We do not repair or install garage doors ourselves. When you call the number on this site, your call is routed to an independent garage door provider that serves your area.</p>
<h2>What happens when you call</h2>
<ol><li>You call and describe your garage door problem and your location.</li>
<li>You are connected with an independent provider who serves your ZIP code.</li>
<li>You arrange a visit and agree any price directly with that provider.</li></ol>
<h2>What we do and don't do</h2>
<ul><li>Using this service is free for homeowners.</li>
<li>Providers are independent businesses. We do not employ them and do not warrant or guarantee their work.</li>
<li>Availability depends on provider participation and location.</li>
<li>Before work begins, ask the provider for proof of insurance, any license required for the job, and a written price.</li></ul>
<h2>Our guides</h2><p>We publish plain-English <a href="/guides/">garage door guides</a> so you can understand the problem before you call - including which jobs are safe to check yourself and which should always be left to a technician.</p>
<h2>Contact</h2><p>For questions about this website, email <a href="mailto:{C['email']}">{C['email']}</a>.</p>''', top, "about")
    simple_page("/privacy-policy/", "Privacy Policy", "Privacy policy", "How this website handles information about visitors and callers.", f'''
<p><i>Last updated: {TODAY}</i></p>
<h2>Information we collect</h2>
<p>This website does not require you to create an account or submit personal details. Like most websites, our hosting provider may log basic technical information such as IP address, browser type and pages visited, for security and performance.</p>
<h2>Phone calls</h2>
<p>When you call a number on this website, the call is handled by a call-tracking and routing partner, which connects you with an independent local service provider. Your phone number, call time, call duration and general location may be recorded, and calls may be recorded for quality and verification purposes. The provider you are connected with will have your phone number and any details you share on the call.</p>
<h2>How information is used</h2>
<ul><li>To connect you with a local service provider.</li><li>To verify and measure calls.</li><li>To keep the website secure and working properly.</li></ul>
<h2>Cookies and analytics</h2>
<p>If we add analytics or similar tools, they may use cookies to measure how the site is used. You can control cookies through your browser settings.</p>
<h2>Third parties</h2>
<p>Independent service providers have their own privacy practices, which are not covered by this policy.</p>
<h2>Contact</h2><p>Questions about this policy: <a href="mailto:{C['email']}">{C['email']}</a>.</p>''', top)
    simple_page("/terms/", "Terms of Use", "Terms of use", "The terms that apply when you use this website.", f'''
<p><i>Last updated: {TODAY}</i></p>
<h2>Referral service</h2><p>{e(DISCLAIMER)}</p>
<h2>No professional advice</h2><p>Our guides are general information only. Garage door springs, cables and related parts are under high tension and can cause serious injury. Do not attempt repairs you are not trained to do safely.</p>
<h2>Agreements with providers</h2><p>Any agreement for work, including price, schedule and warranty, is solely between you and the provider. We are not a party to that agreement.</p>
<h2>Availability</h2><p>Service availability depends on provider participation, location and demand, and is not guaranteed.</p>
<h2>Limitation of liability</h2><p>To the fullest extent permitted by law, {sn} is not liable for any loss or damage arising from work performed by any provider or from use of this website.</p>
<h2>Contact</h2><p><a href="mailto:{C['email']}">{C['email']}</a></p>''', top)
    body = f'''<section class="page-hero"><div class="wrap"><h1>Page not found</h1><p class="lead">The page you're looking for doesn't exist. Try the city list or call us.</p>
<div class="hero-actions">{call_btn('btn-lime')}<a class="btn btn-ghost" href="/{C['state_slug']}/">All cities</a></div></div></section>'''
    write("404.html", head(f"Page not found | {C['site_name']}", "Page not found.", "/404.html", False) + header() + body + footer(top))


def build_assets(covered, nc_map):
    os.makedirs(os.path.join(OUT, "assets"), exist_ok=True)
    shutil.copy(os.path.join(BUILD, "style.css"), os.path.join(OUT, "assets", "style.css"))
    shutil.copy(os.path.join(BUILD, "main.js"), os.path.join(OUT, "assets", "main.js"))
    with open(os.path.join(OUT, "assets", "zips.js"), "w") as f:
        f.write("window.NC_ZIPS=" + json.dumps(nc_map, separators=(",", ":")) + ";\n")
        f.write('window.COVERED_ZIPS=",' + ",".join(covered) + ',";\n')
    with open(os.path.join(OUT, "assets", "favicon.svg"), "w") as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="8" fill="#0c140f"/>'
                '<g transform="translate(4 4)" fill="none" stroke="#d4f34a" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'
                '<path d="M3 10l9-6 9 6v11H3z"/><path d="M6.5 21v-8.5h11V21M6.5 15.5h11M6.5 18.3h11"/></g></svg>')


def build_sitemap(cities):
    paths = ["/", f"/{C['state_slug']}/", "/guides/", "/about/", "/privacy-policy/", "/terms/"]
    paths += [f"/guides/{g['slug']}/" for g in GUIDES]
    paths += [f"/{C['state_slug']}/{c['slug']}/" for c in cities.values() if c["indexed"]]
    urls = "".join(f"<url><loc>{C['domain']}{p}</loc><lastmod>{TODAY}</lastmod></url>" for p in paths)
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\n\nSitemap: {C['domain']}/sitemap.xml\n")
    return len(paths)


def main():
    covered, cities, nc_map = load_data()
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    top_names = [("Winston-Salem" if n == "Winston Salem" else n) for n in TOP_CITIES]
    top = [c for n in top_names for c in cities.values() if c["name"] == n]
    build_assets(covered, nc_map)
    build_home(cities, covered, top)
    build_hub(cities, top)
    for c in cities.values():
        build_city(c, top)
    build_guides(top)
    build_static_pages(top)
    n_sitemap = build_sitemap(cities)
    print(f"cities={len(cities)} indexed_cities={sum(c['indexed'] for c in cities.values())} top={len(top)} sitemap_urls={n_sitemap}")


if __name__ == "__main__":
    main()
