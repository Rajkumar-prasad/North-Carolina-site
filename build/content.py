# All written content for the site. Edit text here, then run build.py.
# Style rule: use regular hyphens, never em dashes.

SERVICES = [
    ("repair", "Garage Door Repair", "Doors that are stuck, noisy, slow, uneven or damaged - diagnosed and fixed by a local technician.", "/guides/garage-door-wont-close/"),
    ("spring", "Spring Repair & Replacement", "Broken torsion or extension springs replaced safely, with the door balanced afterwards.", "/guides/broken-garage-door-spring/"),
    ("opener", "Opener Repair & Installation", "Openers that hum, click or ignore the remote - repaired, or replaced with a new unit.", "/guides/garage-door-opener-not-working/"),
    ("track", "Off-Track & Cable Repair", "Rollers out of the track, crooked doors and snapped lift cables put back in working order.", "/guides/garage-door-off-track/"),
    ("install", "New Door Installation", "New garage doors measured, supplied and installed - steel, insulated, wood-look and more.", "/guides/repair-or-replace-garage-door/"),
    ("panel", "Panels, Seals & Tune-Ups", "Dented panels, worn weather seals and noisy hardware sorted out before they become bigger problems.", "/guides/noisy-garage-door/"),
]

PROBLEMS = [
    ("Door won't close", "Reverses, stops halfway or won't move.", "/guides/garage-door-wont-close/"),
    ("Opener issue", "Remote or wall button does nothing.", "/guides/garage-door-opener-not-working/"),
    ("Broken spring", "Loud bang, door suddenly very heavy.", "/guides/broken-garage-door-spring/"),
    ("Door off track", "Crooked door, rollers out of the rail.", "/guides/garage-door-off-track/"),
]

STEPS = [
    ("Tell us what's wrong", "Call and describe the problem - what the door is doing, what you heard, and your ZIP code."),
    ("Get connected locally", "Your call is routed to an independent garage door provider who serves your area."),
    ("Book the visit", "Agree a time with the provider. A technician inspects the door and explains options before any work."),
]

DOOR_TYPES = [
    ("Popular", "Insulated Steel", "Durable, low-maintenance and better at keeping heat and cold out of attached garages."),
    ("Classic", "Wood & Wood-Look", "Real wood looks warm but needs regular finishing; steel wood-look gives a similar style with less upkeep."),
    ("Modern", "Glass & Aluminum", "Full-view panels bring light into the garage and suit contemporary homes."),
]

CHECKLIST = [
    ("Proof of insurance", "Ask for liability insurance before anyone works on springs or installs a door."),
    ("Any license required locally", "Check what license, if any, your town or county requires for the job."),
    ("A written, itemized price", "Get the price for parts and labor in writing before work begins."),
    ("Warranty details", "Ask what is covered on parts and on labor, and for how long."),
    ("Clear explanation", "A good technician explains what failed and why, and shows you the worn part."),
]

HOME_FAQ = [
    ("How does this service work?", "We are a free referral service. When you call, you are connected with an independent garage door provider who serves your area. You then talk to them directly about your door and book a visit."),
    ("Is it safe to fix a broken spring myself?", "We strongly advise against it. Garage door springs hold a lot of tension and can cause serious injury when released. Leave the door closed, don't use the opener, and have a trained technician replace the spring."),
    ("Should I repair or replace my garage door?", "If the problem is a spring, cable, roller or opener, a repair is usually the sensible choice. Replacement makes more sense when panels are badly damaged, the door is very old, or repairs keep adding up. Our repair-or-replace guide covers this in more detail."),
    ("Can I get a new garage door installed through you?", "Yes. Providers in our network handle new door installation and full replacements, including insulated and wood-look steel doors."),
    ("What should I do if my garage door won't open and my car is inside?", "First check the basics: the opener has power, the remote battery works, and the door isn't locked. If the door still won't move, use the emergency release only if the springs are intact - never with a broken spring - and call for help."),
]

GUIDES = [
    {
        "slug": "broken-garage-door-spring",
        "title": "Broken Garage Door Spring: Signs, Safety & What to Do",
        "short": "Broken Spring",
        "desc": "How to tell if a garage door spring is broken, why you should not fix it yourself, and what happens during a spring replacement.",
        "icon": "spring",
        "body": """
<p>Springs do the heavy lifting on a garage door. A typical double door can weigh well over 100 pounds, and the springs counterbalance that weight so the opener - or your arms - only has to guide it. When a spring breaks, the door suddenly becomes very heavy and usually won't open.</p>
<h2>Signs your spring is broken</h2>
<ul>
<li>A loud bang from the garage, like a firework, often when nobody was using the door.</li>
<li>A visible gap in the coiled spring above the door (torsion spring) or a stretched, snapped spring along the side tracks (extension springs).</li>
<li>The opener strains, hums or lifts the door only a few inches before stopping.</li>
<li>The door feels extremely heavy when you try to lift it by hand, or slams down quickly.</li>
<li>Loose or dangling cables beside the door.</li>
</ul>
<div class="warn"><b>Safety first:</b> Do not try to wind, unwind or replace a garage door spring yourself. Springs store a large amount of energy and can cause serious injury. Keep the door closed, keep children and pets away, and don't keep pressing the opener button - it can damage the opener.</div>
<h2>Why springs break</h2>
<p>Most standard springs are rated for a set number of open-and-close cycles - commonly around 10,000. A household that uses the door four or five times a day can reach that in roughly six or seven years. Rust, lack of lubrication and big temperature swings also shorten spring life.</p>
<h2>What a technician will do</h2>
<ol>
<li>Secure the door so it can't move while the spring is changed.</li>
<li>Measure the old spring (wire size, length, inside diameter) so the replacement is matched to your door's weight.</li>
<li>Replace the spring - many technicians recommend replacing both springs on a two-spring door, since the second one is usually close to failing too.</li>
<li>Check cables, drums, rollers and bearings for wear.</li>
<li>Balance the door and test the opener's safety reverse.</li>
</ol>
<h2>Can I open the door with a broken spring?</h2>
<p>It is best not to. Without the spring, the full weight of the door is on you or the opener. If a car is trapped inside and you have no other option, have at least two adults lift slowly and evenly, and prop the door securely - but calling a technician is the safer choice.</p>
<h2>Get a broken spring fixed</h2>
<p>Call us and we'll connect you with a local garage door provider who can come out, replace the spring and get the door balanced and working again.</p>
""",
    },
    {
        "slug": "garage-door-off-track",
        "title": "Garage Door Off Track: Causes & Safe Next Steps",
        "short": "Door Off Track",
        "desc": "What it means when a garage door comes off its track, what usually causes it, and why it needs a professional repair.",
        "icon": "track",
        "body": """
<p>A garage door rides up and down on rollers that sit inside two metal tracks. When one or more rollers pop out of the track, the door can hang crooked, jam partway, or tilt dangerously. An off-track door is unstable, so it needs attention quickly.</p>
<h2>Signs the door is off track</h2>
<ul>
<li>The door hangs at an angle or one side is higher than the other.</li>
<li>Rollers are visibly outside the track or the track is bent.</li>
<li>The door jams, scrapes or makes grinding noises.</li>
<li>A gap appears between the door and the track on one side.</li>
</ul>
<div class="warn"><b>Safety first:</b> Stop using the door and the opener. Unplug the opener so nobody presses the button. An off-track door can fall, and the springs and cables are still under tension.</div>
<h2>Common causes</h2>
<ul>
<li><b>Bumping the door with a car</b> - a common cause, especially when backing out before the door is fully open.</li>
<li><b>A broken lift cable or spring</b> - when one side loses support, the door twists and the rollers jump out.</li>
<li><b>Worn or broken rollers</b> - old plastic or steel rollers can crack and slip out of the track.</li>
<li><b>Loose or bent tracks</b> - brackets loosen over time and tracks drift out of alignment.</li>
</ul>
<h2>What a technician will do</h2>
<p>The technician will secure the door, release tension where needed, straighten or replace damaged track sections, reset the rollers, and replace any broken cables or rollers. They should finish by checking the door's balance and the opener's safety settings.</p>
<h2>Can I push it back myself?</h2>
<p>Small adjustments to a slightly loose track bracket can be done by a careful homeowner, but a door that is tilted, jammed or has slack cables should be left to a professional. Cables and springs work together, and forcing the door can make the damage worse.</p>
<h2>Get an off-track door repaired</h2>
<p>Call us to be connected with a local garage door provider who can safely reset the door and repair any damaged parts.</p>
""",
    },
    {
        "slug": "garage-door-wont-close",
        "title": "Garage Door Won't Close? 7 Common Causes",
        "short": "Won't Close",
        "desc": "Why a garage door reverses, stops halfway or won't close at all - the quick checks you can do and when to call a technician.",
        "icon": "door",
        "body": """
<p>A garage door that won't close leaves your home and belongings exposed, so it's worth finding the cause quickly. Some causes are simple checks you can do yourself; others need a technician.</p>
<h2>Quick checks you can do safely</h2>
<ol>
<li><b>Safety sensors (photo eyes).</b> The two small sensors near the bottom of the tracks must face each other with a clear line between them. If something blocks the beam, or a sensor is knocked out of line, the door reverses. Look for a steady light on both sensors.</li>
<li><b>Dirty sensor lenses.</b> Dust, cobwebs and spring pollen on the lenses can confuse the sensors. Wipe them gently with a soft dry cloth.</li>
<li><b>Something in the way.</b> Check the floor and tracks for objects, debris or ice.</li>
<li><b>Lock mode or vacation lock.</b> Many wall controls have a lock button that disables remotes. Check the wall panel.</li>
<li><b>Remote batteries.</b> If the wall button works but the remote doesn't, start with a fresh battery.</li>
</ol>
<h2>Causes that need a technician</h2>
<ol start="6">
<li><b>Broken spring or cable.</b> The door may stop, sag or refuse to move. Do not try to force it.</li>
<li><b>Opener limit or force settings, or a failing opener.</b> If the door reverses as soon as it touches the floor, or stops for no reason, the opener may need adjustment or repair.</li>
</ol>
<p>Bent tracks and damaged rollers can also make the door bind and reverse, which a technician can straighten or replace.</p>
<div class="warn"><b>Don't disable the safety sensors.</b> They stop the door from closing on people, pets and cars. If they keep tripping, get them checked rather than bypassed.</div>
<h2>Get help with a door that won't close</h2>
<p>If the quick checks don't solve it, call us and we'll connect you with a local garage door provider who can diagnose the problem and fix it.</p>
""",
    },
    {
        "slug": "garage-door-opener-not-working",
        "title": "Garage Door Opener Not Working: Troubleshooting Guide",
        "short": "Opener Issue",
        "desc": "Simple checks for a garage door opener that won't respond, hums or clicks, plus signs it is time for repair or a new opener.",
        "icon": "opener",
        "body": """
<p>When the opener stops working, the cause is often simple - but sometimes the opener is worn out or the problem is actually the door itself. Here is how to narrow it down.</p>
<h2>Step-by-step checks</h2>
<ol>
<li><b>Power.</b> Make sure the opener is plugged in and the outlet works. Check for a tripped breaker or GFCI outlet in the garage.</li>
<li><b>Remote vs wall button.</b> If the wall button works but the remote doesn't, replace the remote battery or re-pair the remote using the opener's learn button.</li>
<li><b>Lock mode.</b> Check whether the wall control is set to lock or vacation mode.</li>
<li><b>Safety sensors.</b> Misaligned or dirty sensors will stop the door from closing. Look for steady lights on both sensors.</li>
<li><b>Disconnected trolley.</b> If someone pulled the red emergency release cord, the motor will run but the door won't move until the trolley is reconnected.</li>
</ol>
<h2>What the sounds can tell you</h2>
<ul>
<li><b>Humming but the door doesn't move:</b> could be a stripped gear, a disconnected trolley, or a door that is too heavy because of a broken spring.</li>
<li><b>Clicking only:</b> often an electrical or logic board issue.</li>
<li><b>Grinding:</b> worn gears or a chain or belt problem.</li>
</ul>
<div class="warn"><b>Check the springs first.</b> If the door is very heavy or a spring looks broken, don't keep running the opener - it is not designed to lift the full weight of the door and you may burn out the motor.</div>
<h2>Repair or replace the opener?</h2>
<p>Older openers without modern safety sensors, units that need repeated repairs, or openers that are very loud are good candidates for replacement. Newer models can be quieter and may offer smartphone control and battery backup.</p>
<h2>Get your opener fixed or replaced</h2>
<p>Call us to be connected with a local provider who can repair your opener or install a new one.</p>
""",
    },
    {
        "slug": "noisy-garage-door",
        "title": "Noisy Garage Door: What the Sounds Mean",
        "short": "Noisy Door",
        "desc": "Squeaking, grinding, rattling or banging - what each garage door noise usually points to and which ones need a technician.",
        "icon": "panel",
        "body": """
<p>Garage doors make some noise, but new or louder sounds usually mean a part is wearing out. Catching it early can prevent a bigger repair later.</p>
<h2>Common noises and their causes</h2>
<ul>
<li><b>Squeaking or squealing:</b> dry rollers, hinges or bearings. A garage-door-specific lubricant on hinges and roller bearings often helps. Don't grease the inside of the tracks - it attracts dirt.</li>
<li><b>Grinding:</b> worn rollers, bent tracks, or worn opener gears.</li>
<li><b>Rattling:</b> loose nuts, bolts and brackets, or a loose opener chain.</li>
<li><b>Popping or banging:</b> springs under strain, or panels flexing. A single very loud bang often means a spring has broken.</li>
<li><b>Scraping:</b> the door rubbing on the track or frame because something is out of alignment.</li>
</ul>
<h2>What you can do</h2>
<ul>
<li>Lubricate hinges, roller bearings and springs with a product made for garage doors.</li>
<li>Tighten loose bolts on the door hinges and track brackets - but never loosen anything attached to the springs or the bottom cable brackets.</li>
<li>Clean the tracks with a cloth.</li>
</ul>
<div class="warn"><b>Leave springs and cables alone.</b> If the noise comes from the springs, cables or bottom brackets, call a technician. These parts are under high tension.</div>
<h2>When a tune-up makes sense</h2>
<p>If the door is still noisy after basic care, a professional tune-up usually covers replacing worn rollers, adjusting the springs and balance, checking cables and tightening hardware.</p>
<h2>Get a noisy door checked</h2>
<p>Call us to be connected with a local provider for a tune-up or repair.</p>
""",
    },
    {
        "slug": "repair-or-replace-garage-door",
        "title": "Repair or Replace Your Garage Door? How to Decide",
        "short": "Repair or Replace",
        "desc": "When a garage door repair makes sense, when a full replacement is the better value, and what to consider when choosing a new door.",
        "icon": "install",
        "body": """
<p>Most garage door problems can be repaired. But when a door is old, damaged or costing more each year, replacing it can be the better long-term choice.</p>
<h2>When repair usually makes sense</h2>
<ul>
<li>A broken spring, cable or roller.</li>
<li>An opener problem.</li>
<li>One damaged panel on an otherwise solid door, if a matching panel is still available.</li>
<li>Worn weather seals or noisy hardware.</li>
</ul>
<h2>When replacement is worth considering</h2>
<ul>
<li>Several panels are dented, cracked, rotted or rusted through.</li>
<li>The door is very old and replacement parts are hard to find.</li>
<li>You are repairing the door repeatedly.</li>
<li>The garage is attached and the door has no insulation, making the garage and nearby rooms hot in summer and cold in winter.</li>
<li>You are planning to sell and want to improve curb appeal.</li>
</ul>
<h2>Choosing a new door</h2>
<ul>
<li><b>Material:</b> steel is the most common for durability and low upkeep; wood looks classic but needs regular finishing; aluminum and glass suit modern homes.</li>
<li><b>Insulation:</b> insulated doors are quieter and help with temperature in attached garages.</li>
<li><b>Local requirements:</b> in coastal and high-wind areas, ask whether your door needs a wind-load rating to meet local building code.</li>
<li><b>Opener:</b> if your opener is old, it can make sense to replace it at the same time.</li>
</ul>
<h2>Talk it through with a local pro</h2>
<p>A technician can look at the door in person and tell you honestly whether a repair or a replacement is the better option. Call us to be connected with a provider in your area.</p>
""",
    },
]

# Region content for indexed city pages. Each city in TOP_CITIES maps to a region.
REGIONS = {
    "charlotte": {
        "name": "Charlotte metro",
        "paras": [
            "The Charlotte area has grown fast, and many suburban neighborhoods were built from the 1990s onward. That means a lot of homes still run their original springs, rollers and openers - and those parts reach the end of their rated life at roughly the same time across whole subdivisions.",
            "Long, humid summers are hard on weather seals and bottom rubber, which can dry out, crack and let in water, insects and heat. Spring pollen is another local nuisance: the yellow dust coats the safety sensor lenses and is a common reason doors suddenly start reversing.",
        ],
        "tips": [
            "Wipe the safety sensor lenses during pollen season.",
            "Check the bottom seal each spring for cracks and gaps.",
            "If your springs are original on an older home, plan for replacement before one breaks.",
            "Lubricate hinges and rollers twice a year.",
        ],
    },
    "triangle": {
        "name": "Triangle (Raleigh-Durham)",
        "paras": [
            "The Triangle has added thousands of new homes, from Raleigh and Durham out to fast-growing towns in Wake County. Newer doors are often insulated steel with modern openers, while older neighborhoods still have uninsulated doors and openers that lack current safety features.",
            "Hot, humid summers and pollen-heavy springs are the main seasonal stresses. Heat dries out weatherstripping, humidity can swell real wood doors, and pollen on the safety sensors is a frequent cause of doors that refuse to close.",
        ],
        "tips": [
            "Clean the photo-eye sensors when pollen season starts.",
            "Seal or refinish real wood doors regularly to resist humidity.",
            "Consider an insulated door if your garage is attached to living space.",
            "Test the opener's auto-reverse with a roll of paper towels once a month.",
        ],
    },
    "triad": {
        "name": "Piedmont Triad",
        "paras": [
            "The Triad mixes older established neighborhoods with newer suburban growth. Older homes often have wood or early steel doors and openers that are decades old, while newer subdivisions have insulated steel doors with springs that will need replacement as they age together.",
            "Hot, humid summers and cold snaps in winter both work on a garage door. Temperature swings make metal parts expand and contract, and cold weather is a common time for worn springs to finally break.",
        ],
        "tips": [
            "Listen for new noises before winter - worn springs often fail in the cold.",
            "Replace cracked bottom seals to keep out water and pests.",
            "If your opener lacks safety sensors, consider replacing it.",
            "Keep tracks clean and free of debris.",
        ],
    },
    "coast": {
        "name": "Coastal North Carolina",
        "paras": [
            "Near the coast, salt air speeds up corrosion on springs, cables, hinges and rollers. Parts that might last many years inland can rust and fail sooner here, so regular inspection matters more.",
            "Hurricane season also puts garage doors under real pressure. The garage door is often the largest opening in a home, and coastal areas commonly have wind-load requirements for new doors. If you are replacing a door, ask the installer which rating your location requires under local building code.",
        ],
        "tips": [
            "Rinse and inspect hardware for rust a few times a year.",
            "Ask about a wind-load rated door when replacing.",
            "Have springs and cables checked before hurricane season.",
            "Use a corrosion-resistant lubricant made for garage doors.",
        ],
    },
    "sandhills": {
        "name": "Eastern North Carolina",
        "paras": [
            "Eastern North Carolina gets long, hot, humid summers and is exposed to storms during hurricane season. Heat and humidity wear out weather seals and can make wood doors swell, while storms can bend tracks and dent panels.",
            "Sandy soil and wind-blown grit find their way into tracks and rollers, which adds wear and noise. Keeping the tracks clean and the moving parts lubricated helps the door run smoothly for longer.",
        ],
        "tips": [
            "Wipe sand and grit out of the tracks regularly.",
            "Check panels and tracks after major storms.",
            "Replace worn bottom seals to keep out water and insects.",
            "Lubricate rollers and hinges twice a year.",
        ],
    },
    "mountains": {
        "name": "Western North Carolina mountains",
        "paras": [
            "Mountain winters are colder than the rest of the state, and cold is hard on garage doors. Metal springs become more brittle in low temperatures, and many worn springs break on the first cold mornings of the year. Grease and lubricant can also thicken, making the door and opener work harder.",
            "Snow, ice and steep driveways add more stress. The bottom seal can freeze to the ground, and forcing the door open can damage the opener or pull the door off balance.",
        ],
        "tips": [
            "Have springs checked before winter.",
            "If the door is frozen to the ground, free it gently rather than forcing the opener.",
            "Use a lubricant that stays effective in cold weather.",
            "Replace worn bottom seals to keep out snowmelt.",
        ],
    },
    "foothills": {
        "name": "Foothills",
        "paras": [
            "The foothills see bigger temperature swings than the coast or the Piedmont, with hot summers and colder winter nights. Those swings make metal parts expand and contract, which loosens hardware and wears springs over time.",
            "Many homes here have doors and openers that have been in service for a long time. Older openers may not have modern safety sensors, and older springs are more likely to fail in cold weather.",
        ],
        "tips": [
            "Tighten loose hinge and track bolts once a year.",
            "Have older springs checked before winter.",
            "Consider replacing openers without safety sensors.",
            "Keep the bottom seal in good condition.",
        ],
    },
}

# Top cities: indexed, with a city-specific intro line and region.
TOP_CITIES = {
    "Concord": ("charlotte", "Concord is the county seat of Cabarrus County, northeast of Charlotte."),
    "Huntersville": ("charlotte", "Huntersville sits just north of Charlotte, near the eastern shore of Lake Norman."),
    "Mooresville": ("charlotte", "Mooresville lies on the shores of Lake Norman in Iredell County."),
    "Gastonia": ("charlotte", "Gastonia is the county seat of Gaston County, west of Charlotte."),
    "Matthews": ("charlotte", "Matthews is a suburban town southeast of Charlotte."),
    "Cary": ("triangle", "Cary is one of the largest towns in Wake County, between Raleigh and Research Triangle Park."),
    "Apex": ("triangle", "Apex is a fast-growing town in western Wake County."),
    "Wake Forest": ("triangle", "Wake Forest is a growing town north of Raleigh."),
    "Holly Springs": ("triangle", "Holly Springs is a fast-growing town in southern Wake County."),
    "Garner": ("triangle", "Garner is a town just south of Raleigh in Wake County."),
    "Durham": ("triangle", "Durham is home to Duke University and one of the anchor cities of the Triangle."),
    "Raleigh": ("triangle", "Raleigh is North Carolina's capital and the largest city in the Triangle."),
    "Greensboro": ("triad", "Greensboro is the largest city in the Piedmont Triad and the seat of Guilford County."),
    "Winston Salem": ("triad", "Winston-Salem is the seat of Forsyth County in the Piedmont Triad."),
    "High Point": ("triad", "High Point is known nationally for its home furnishings market."),
    "Wilmington": ("coast", "Wilmington sits on the Cape Fear River near the coast and is the seat of New Hanover County."),
    "Fayetteville": ("sandhills", "Fayetteville is the seat of Cumberland County and home to a large military community."),
    "Greenville": ("sandhills", "Greenville is the seat of Pitt County and home to East Carolina University."),
    "Asheville": ("mountains", "Asheville sits in the Blue Ridge Mountains of western North Carolina."),
    "Hickory": ("foothills", "Hickory is in Catawba County in the foothills of western North Carolina."),
}
