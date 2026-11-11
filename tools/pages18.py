import re, json, glob, os, sys, html
os.chdir(sys.argv[1])
BASE = "https://creditt.com.au/"
TODAY = "2026-11-11"
def esc(s): return html.escape(s, quote=True)
def strip(s): return re.sub(r"\s+", " ", html.unescape(re.sub(r"<.*?>", "", s))).strip()

ASIDE = '<aside class="aside-card"><h3 class="dt">Talk it through</h3><p>A short call is usually enough to see what\'s realistic. No cost and no obligation.</p><a class="btn btn-primary btn-block" href="contact.html">Book a free chat</a><p style="margin-top:22px;margin-bottom:6px;"><a href="tel:+61402993545">0402 993 545</a></p><p style="margin:0;"><a href="mailto:hello@creditt.com.au">hello@creditt.com.au</a></p></aside>'
CTA = '<section class="cta bg-yellow on-yellow"><div class="container cta-grid"><div><h2 class="dt dt-purple">Ready when you are</h2><p class="lede">Tell us what you\'re planning. We\'ll tell you what\'s realistic, with no cost and no obligation.</p><div class="btn-row"><a class="btn btn-dark" href="contact.html">Book a free chat</a><a class="btn btn-line" href="calculators.html">Try the calculators</a></div></div><div class="cta-details"><p>Prefer to talk now?</p><p><a href="tel:+61402993545">0402 993 545</a></p><p><a href="mailto:hello@creditt.com.au">hello@creditt.com.au</a></p><p>Annex Building, 15 Orion Rd, Lane Cove West NSW 2066</p></div></div></section>'
DISC = '<p><small>General information only. It doesn\'t take your personal circumstances into account and isn\'t personal financial or credit advice. Lending criteria, fees and charges apply and vary between lenders.</small></p>'

def faq_html(faqs):
    items = "".join(f'<div class="faq-item"><button class="faq-q" type="button">{esc(q)}</button><div class="faq-a"><div><p>{a}</p></div></div></div>' for q, a in faqs)
    return f'<section class="section"><div class="container"><div class="section-head"><h2 class="dt">Common questions</h2></div><div class="faq">{items}</div></div></section>'

def hero(crumbs, h1, lede):
    c = " / ".join([f'<a href="{u}">{n}</a>' for n, u in crumbs[:-1]] + [crumbs[-1][0]])
    return f'<section class="page-hero"><div class="container"><div class="crumbs">{c}</div><h1 class="dt">{h1}</h1><p class="lede">{lede}</p></div></section>'

def features(h2, feats):
    f = "".join(f'<div class="feature"><h3>{t}</h3><p>{p}</p></div>' for t, p in feats)
    return f'<section class="section"><div class="container layout"><div><h2 class="dt">{h2}</h2>{f}</div>{ASIDE}</div></section>'

def band(h2, intro, cols):
    c = "".join(f'<div><h3>{t}</h3><p>{p}</p></div>' for t, p in cols)
    return f'<section class="section bg-mist"><div class="container"><div class="section-head"><h2 class="dt">{h2}</h2><p>{intro}</p></div><div class="ready">{c}</div></div></section>'

def article(body):
    return f'<section class="section"><article class="container article">{body}{DISC}</article></section>'

PAGES = {}
def page(slug, title, desc, crumbs, main, faqs, kind="service", h1=""):
    PAGES[slug] = dict(title=title, desc=desc, crumbs=crumbs, main=main + (faq_html(faqs) if faqs else "") + CTA, faqs=faqs, kind=kind, h1=h1)

NS = ("North Shore", "mortgage-broker-north-shore.html")
HOME = ("Home", "index.html")
GUIDES = ("Guides", "blog.html")

# ---------------- SUBURB PAGES ----------------
SUBURBS = [
 dict(slug="mortgage-broker-lane-cove.html", area="Lane Cove", covers="Lane Cove, Lane Cove West, Lane Cove North, Riverview, Longueville, Linley Point and Northwood",
  lede="Our office is in Lane Cove West, so this is home turf. We help Lane Cove buyers, upgraders, investors and business owners compare lenders and get from first chat to settlement.",
  local=[("Apartments around the village and Lane Cove West", "Much of the newer stock is apartments, including off-the-plan buildings. Lenders treat these differently: valuations happen at completion, and some lenders cap lending on small units or large high-density complexes. We check the building against lender policy before you commit."),
         ("Family homes that are tightly held", "Houses in Lane Cove don't come up often, so many upgraders find their next home before they've sold. That's where pre-approval that counts your existing equity, or a <a href=\"bridging-loans.html\">bridging loan</a>, can make the difference."),
         ("Waterfront and prestige pockets", "Riverview, Longueville and Northwood include higher-value homes where loan size, lender appetite and valuation risk all matter more. Not every lender treats large loans the same way."),
         ("Local business owners", "The Lane Cove West business park means plenty of self-employed clients. If your income comes through a company or trust, see <a href=\"self-employed-home-loans.html\">self-employed home loans</a>.")],
  near=[("Chatswood", "mortgage-broker-chatswood.html"), ("Ryde, Gladesville and Hunters Hill", "mortgage-broker-ryde-hunters-hill.html"), ("Willoughby and Artarmon", "mortgage-broker-willoughby-artarmon.html")],
  faqs=[("Can I meet you in person in Lane Cove?", "Yes. We're at Annex Building, 15 Orion Rd, Lane Cove West, by appointment. Most clients start with a phone or video call, and we can meet whenever suits you."),
        ("Can you help with an off-the-plan apartment in Lane Cove?", "Yes. We check whether the building and unit meet lender policy, plan for the valuation at completion, and line up finance so you're ready when the building settles."),
        ("What if I need to buy before I sell my Lane Cove home?", "We'll look at whether your existing equity covers the deposit, or whether a bridging loan suits. We work out the numbers for both scenarios before you make an offer.")]),
 dict(slug="mortgage-broker-chatswood.html", area="Chatswood", covers="Chatswood, Chatswood West, Roseville, Castle Cove and Middle Cove",
  lede="Chatswood is one of the busiest lending markets on the North Shore. We help apartment buyers, investors, families and business owners compare lenders and structure loans that suit.",
  local=[("High-rise apartments near the interchange", "Chatswood has a large stock of apartments close to the train and Metro. Lenders look closely at unit size, building density and the developer, so the right lender for one apartment can be the wrong one for the next."),
         ("Investors", "Many Chatswood purchases are investment properties. Structure matters: interest-only periods, splitting loans for deductibility, and keeping your home loan separate. See <a href=\"investment-loans.html\">investment loans</a>."),
         ("Income from overseas or multiple sources", "Some buyers have income, assets or family support from overseas, or income from a mix of salary and business. Lenders vary widely in how they assess this, so comparing policies matters as much as comparing rates."),
         ("Heritage homes in Chatswood West", "Conservation areas and older homes can affect renovation plans and valuations. Talk to us early if you're planning works.")],
  near=[("Lane Cove", "mortgage-broker-lane-cove.html"), ("Willoughby and Artarmon", "mortgage-broker-willoughby-artarmon.html"), ("Lindfield, Killara and Gordon", "mortgage-broker-lindfield-killara-gordon.html")],
  faqs=[("Do you help Chatswood apartment investors?", "Yes. We compare lenders that accept the specific building and unit, and structure the loan around your investment plan and any other properties you hold."),
        ("Can you help if some of my income is from overseas?", "Often, yes. A number of lenders accept foreign income, usually with some shading, and requirements differ. We match you to lenders whose policy fits your situation."),
        ("Is Chatswood too far from your office?", "Not at all. We're about ten minutes away in Lane Cove West, and most of the process happens by phone, video and secure online document upload.")]),
 dict(slug="mortgage-broker-north-sydney-crows-nest.html", area="North Sydney and Crows Nest", covers="North Sydney, Crows Nest, St Leonards, Wollstonecraft, Waverton, Cammeray and Kirribilli",
  lede="From Victoria Cross to Crows Nest and St Leonards, this part of the Lower North Shore is full of professionals, apartment buyers and investors. We help you compare lenders and get the structure right.",
  local=[("Professionals with bonuses and variable pay", "Many clients here are on salaries with bonuses, commissions or RSUs. Lenders treat variable income differently: some use a two-year average, some only the base. Choosing the right lender can change your borrowing power noticeably."),
         ("Apartments near the new Metro stations", "Crows Nest, Victoria Cross and St Leonards have seen lots of new apartment supply. We check building, size and developer against lender policy before you buy, especially for off-the-plan."),
         ("Professional packages and LMI waivers", "Some lenders offer reduced or waived lenders mortgage insurance for eligible professionals, such as doctors, lawyers and accountants, with smaller deposits. Eligibility rules vary."),
         ("Investors and upgraders", "Many buyers here keep their first apartment as an investment when they upgrade. Getting the loan structure right before you move saves headaches later.")],
  near=[("Mosman and Neutral Bay", "mortgage-broker-mosman-neutral-bay.html"), ("Willoughby and Artarmon", "mortgage-broker-willoughby-artarmon.html"), ("Lane Cove", "mortgage-broker-lane-cove.html")],
  faqs=[("Will lenders count my bonus?", "Many will, usually averaged over one or two years with payslips and tax returns as evidence. Policies differ, so we compare how each lender treats your income before you apply."),
        ("Can I buy with less than 20% deposit without paying LMI?", "Possibly. Eligible professionals may qualify for LMI waivers with some lenders, and first home buyers may be eligible for the government 5% Deposit Scheme. See our <a href=\"first-home-buyer-guide-nsw.html\">first home buyer guide</a>."),
        ("Should I keep my apartment as an investment when I upgrade?", "It can work well, but the loan structure matters for tax and flexibility. We'll map out the options, and you should also speak to your accountant.")]),
 dict(slug="mortgage-broker-mosman-neutral-bay.html", area="Mosman and Neutral Bay", covers="Mosman, Neutral Bay, Cremorne, Cremorne Point, Kurraba Point and Clifton Gardens",
  lede="Mosman and Neutral Bay buyers often deal with larger loans, upgrades and more complex finances. We compare lenders and structure finance for prestige and family purchases alike.",
  local=[("Larger loan sizes", "Many purchases here involve loans well above the Sydney average. Lenders set different limits and conditions for large loans, and pricing can be negotiated. Getting several lenders' views matters more at this end of the market."),
         ("Upgrading without selling first", "Families moving from an apartment to a house often need to buy before selling. We work through equity release and <a href=\"bridging-loans.html\">bridging finance</a> so you can bid with confidence."),
         ("Apartments in Neutral Bay and Cremorne", "Older blocks and harbourside apartments sit alongside new developments. Strata, building age and size all affect lender appetite."),
         ("Complex income", "Business owners, partners in firms and people with trust or investment income need lenders who understand their structures. See <a href=\"self-employed-home-loans.html\">self-employed home loans</a>.")],
  near=[("North Sydney and Crows Nest", "mortgage-broker-north-sydney-crows-nest.html"), ("Willoughby and Artarmon", "mortgage-broker-willoughby-artarmon.html"), ("Chatswood", "mortgage-broker-chatswood.html")],
  faqs=[("Do you arrange large home loans?", "Yes. We compare lenders' policies and pricing for larger loans and present the options side by side, including what each lender needs from you."),
        ("Can I use the equity in my apartment to buy a house?", "Often, yes. We work out how much usable equity you have, then structure the deposit and loans so you're not over-committed while you sell."),
        ("Do you only help with prestige purchases?", "No. We help first home buyers, apartment buyers and investors in Mosman and Neutral Bay too.")]),
 dict(slug="mortgage-broker-willoughby-artarmon.html", area="Willoughby and Artarmon", covers="Willoughby, North Willoughby, Artarmon, Naremburn, Northbridge, Castlecrag and Cammeray",
  lede="Family homes, renovations and local business owners define Willoughby and Artarmon. We help you compare lenders for buying, renovating, rebuilding and refinancing.",
  local=[("Renovations and extensions", "Many Willoughby and Naremburn families renovate rather than move. Options include drawing on equity, a construction loan for larger works, or refinancing to fund the project. The right choice depends on the size of the job and how it's being paid."),
         ("Knock-down rebuilds", "Larger blocks in Castlecrag and Northbridge suit rebuilds. These need a <a href=\"construction-loans.html\">construction loan</a> with progress payments, and somewhere to live in the meantime."),
         ("Artarmon business owners", "Artarmon's industrial and commercial areas mean many local clients run their own business. We also arrange <a href=\"business-finance.html\">business, equipment and commercial property finance</a>."),
         ("Apartments near Artarmon station", "Unit buyers and investors near the station need lenders comfortable with the building and size.")],
  near=[("Chatswood", "mortgage-broker-chatswood.html"), ("North Sydney and Crows Nest", "mortgage-broker-north-sydney-crows-nest.html"), ("Lane Cove", "mortgage-broker-lane-cove.html")],
  faqs=[("How do I finance a renovation?", "Smaller works are often funded from equity or a loan top-up. Larger structural work usually needs a construction loan that pays builders in stages. We'll compare both."),
        ("Can you help with business finance as well as my home loan?", "Yes. We arrange business loans, equipment and vehicle finance, and commercial property loans alongside home loans."),
        ("Do you work with Artarmon apartment buyers?", "Yes. We check the building against lender policy and compare lenders that suit your deposit and income.")]),
 dict(slug="mortgage-broker-ryde-hunters-hill.html", area="Ryde, Gladesville and Hunters Hill", covers="Ryde, West Ryde, North Ryde, Macquarie Park, Gladesville, Putney, Hunters Hill and Woolwich",
  lede="From Macquarie Park apartments to Hunters Hill heritage homes, this area has a wide mix of buyers. We help first home buyers, families and investors compare lenders.",
  local=[("First home buyers", "Ryde, West Ryde and Macquarie Park include apartments and townhouses that can fall within first home buyer price thresholds. That can mean stamp duty savings and a smaller deposit. See our <a href=\"first-home-buyer-guide-nsw.html\">first home buyer guide</a>."),
         ("Macquarie Park professionals", "The business park employs thousands of professionals, many on salary plus bonus or share packages. How lenders count that income varies."),
         ("Heritage homes in Hunters Hill", "Older homes and heritage controls can affect valuations and renovation plans. Talk to us before committing to major works."),
         ("Investors", "Units near transport and the university attract investors. Structure and lender choice matter for rental income assessment.")],
  near=[("Lane Cove", "mortgage-broker-lane-cove.html"), ("Chatswood", "mortgage-broker-chatswood.html"), ("Lindfield, Killara and Gordon", "mortgage-broker-lindfield-killara-gordon.html")],
  faqs=[("Can I buy with a 5% deposit in Ryde?", "Possibly. Eligible first home buyers may use the government 5% Deposit Scheme within the price cap, and may also pay reduced or no stamp duty. We'll check your eligibility."),
        ("How do lenders treat rental income?", "Most lenders count a portion of expected rent, not the full amount, to allow for vacancies and costs. The percentage varies by lender."),
        ("Do you help Hunters Hill buyers?", "Yes, including heritage and higher-value homes where lender choice and valuation matter.")]),
 dict(slug="mortgage-broker-lindfield-killara-gordon.html", area="Lindfield, Killara and Gordon", covers="Roseville, Lindfield, East Lindfield, Killara, East Killara and Gordon",
  lede="The Upper North Shore is family territory. We help upgraders, families and downsizers in Lindfield, Killara and Gordon compare lenders and plan their next move.",
  local=[("Family upgraders", "Many buyers move here for schools and space, often selling an apartment or smaller home on the Lower North Shore. Timing the sale and purchase is usually the biggest finance question."),
         ("Planning changes around stations", "NSW planning reforms are changing what can be built near some Upper North Shore stations. If you're buying near a station, consider how this might affect the property and future plans."),
         ("Renovating established homes", "Older family homes on large blocks often need work. We compare equity release, construction loans and refinancing options."),
         ("Downsizers", "Some long-term owners are buying smaller homes or units nearby. Bridging and short-term finance can help you buy first and sell without pressure.")],
  near=[("Pymble, Turramurra and Wahroonga", "mortgage-broker-pymble-turramurra-wahroonga.html"), ("Chatswood", "mortgage-broker-chatswood.html"), ("Ryde and Hunters Hill", "mortgage-broker-ryde-hunters-hill.html")],
  faqs=[("Should I sell first or buy first?", "It depends on your equity, the market and your risk appetite. We'll model both: buying first with bridging finance, and selling first with a longer settlement."),
        ("Can you help with a renovation loan?", "Yes. Depending on the size of the job, we compare equity release, a loan top-up or a construction loan."),
        ("Do you only work locally?", "We're based in Lane Cove West and work across the North Shore, and with clients Australia-wide by phone and video.")]),
 dict(slug="mortgage-broker-pymble-turramurra-wahroonga.html", area="Pymble, Turramurra and Wahroonga", covers="Pymble, West Pymble, St Ives, Turramurra, Warrawee, Wahroonga and Hornsby",
  lede="Large blocks, family homes and long-term owners make the upper Upper North Shore its own market. We help with upgrades, rebuilds, downsizing and refinancing.",
  local=[("Knock-down rebuilds on large blocks", "Big blocks suit rebuilds and duplex projects. These need a <a href=\"construction-loans.html\">construction loan</a> with progress payments, and lenders want fixed-price building contracts and approved plans."),
         ("Long-term owners with significant equity", "Many owners have built up substantial equity. That can fund renovations, help children into the market, or buy an investment property, if structured carefully."),
         ("Downsizing and bridging", "Buying a smaller home before selling the family home is common. <a href=\"bridging-loans.html\">Bridging loans</a> can cover the gap."),
         ("Family guarantee", "Parents here often help adult children buy, either with a gift or by guaranteeing part of the loan. We explain the risks and options clearly.")],
  near=[("Lindfield, Killara and Gordon", "mortgage-broker-lindfield-killara-gordon.html"), ("Chatswood", "mortgage-broker-chatswood.html"), ("Lane Cove", "mortgage-broker-lane-cove.html")],
  faqs=[("How does a construction loan work for a knock-down rebuild?", "The lender pays the builder in stages as work is completed, and you usually pay interest only on the amount drawn. You'll need a fixed-price contract and approved plans."),
        ("Can I help my children buy their first home?", "Yes, through a gift, a family guarantee or co-ownership. Each has different risks, and we explain them before you decide. Get legal advice too."),
        ("Can I buy my next home before selling?", "Often, yes, with a bridging loan or by using existing equity. We'll work out the peak debt and the end debt so you know where you stand.")]),
]
for s in SUBURBS:
    feats = s["local"]
    services = [("<a href=\"home-loans.html\">Home loans</a>", "Fixed, variable, split and offset loans compared across our lender panel."),
                ("<a href=\"refinancing.html\">Refinancing</a>", "We check whether switching really saves once break and setup costs are counted."),
                ("<a href=\"investment-loans.html\">Investment loans</a>", "Structures for buying and holding investment property."),
                ("<a href=\"business-finance.html\">Business finance</a>", "Business loans, equipment, vehicle and commercial property finance.")]
    near = "".join(f'<li><a href="{u}">{n}</a></li>' for n, u in s["near"])
    main = (hero([HOME, NS, (s["area"], s["slug"])], f'Mortgage broker in {s["area"]}', s["lede"])
            + features(f'What we see in {s["area"]}', feats)
            + band("How we can help", f'We work with clients across {s["covers"]}.', [(t, p) for t, p in services[:3]])
            + f'<section class="section"><div class="container"><div class="section-head"><h2 class="dt">Nearby areas</h2><p>We also help buyers in nearby suburbs. See all <a href="mortgage-broker-north-shore.html">North Shore areas we cover</a>.</p></div><ul>{near}</ul></div></section>')
    page(s["slug"], f'Mortgage Broker {s["area"]} | Creditt.'[:70],
         f'Mortgage broker for {s["area"]}. Creditt compares lenders for home loans, refinancing and investment loans across {s["covers"].split(",")[0]} and nearby suburbs. Book a free chat.'[:158],
         [HOME, NS, (s["area"], s["slug"])], main, s["faqs"], "suburb", f'Mortgage broker in {s["area"]}')

# ---------------- SERVICE PAGES ----------------
LOANS = ("Loan options", "home-loans.html")
def svc(slug, title, desc, crumb, h1, lede, h2, feats, band_t, band_i, cols, faqs):
    main = hero([HOME, LOANS, (crumb, slug)], h1, lede) + features(h2, feats) + band(band_t, band_i, cols)
    page(slug, title, desc, [HOME, LOANS, (crumb, slug)], main, faqs, "service", h1)

svc("self-employed-home-loans.html", "Self-Employed Home Loans | Mortgage Broker Sydney | Creditt.",
    "Home loans for sole traders, company directors and trust beneficiaries. We match self-employed borrowers to lenders whose income policy suits. Book a free chat.",
    "Self-employed home loans", "Self-employed home loans", "Being self-employed shouldn't make borrowing harder than it needs to be. The trick is matching how you earn to a lender whose policy suits it.",
    "How lenders assess self-employed income", [
     ("Two years of returns (sometimes one)", "Most lenders want your last two years of personal and business tax returns plus ATO notices of assessment. Some will consider one year if you've been trading longer or your income is stable."),
     ("Add-backs", "Some lenders add back items such as depreciation, one-off expenses or interest on debts being refinanced. The same tax return can support quite different loan amounts depending on the lender."),
     ("Company and trust income", "If you earn through a company or trust, lenders look at the entity's returns as well as your own. Policies on retained profits and distributions vary widely."),
     ("Recent growth", "If this year is much better than last, some lenders will use the latest year rather than an average.")],
    "What to have ready", "Rough numbers are fine for a first chat.", [
     ("Tax returns", "Last two years of personal and business returns and notices of assessment, if lodged."),
     ("Business details", "ABN, how long you've been trading, and whether you use a company or trust."),
     ("ATO position", "Whether BAS and returns are up to date, and any ATO debt or payment plan.")],
    [("Can I get a home loan if I've only been self-employed for a year?", "Sometimes. Some lenders accept one year of returns, especially if you were in the same industry before. Others may consider a <a href=\"low-doc-home-loans.html\">low doc loan</a>."),
     ("Does claiming more deductions reduce my borrowing power?", "It can, because lenders start from taxable income. Read <a href=\"blog-tax-return-borrowing-power.html\">how your tax return affects your borrowing power</a>."),
     ("What if I have an ATO debt?", "Many lenders will still consider you if the debt is on a formal payment plan that you're keeping up with.")])

svc("low-doc-home-loans.html", "Low Doc Home Loans Sydney | Self-Employed | Creditt.",
    "Low doc home loans for self-employed borrowers without up-to-date tax returns. We compare lenders that accept BAS, bank statements or an accountant's declaration.",
    "Low doc home loans", "Low doc home loans", "If your tax returns aren't up to date or don't reflect what you earn now, a low doc loan may let you verify income another way.",
    "How low doc loans work", [
     ("Alternative income evidence", "Instead of full tax returns, lenders may accept recent BAS statements, business bank statements or a declaration from your accountant."),
     ("Larger deposit, higher cost", "Low doc loans usually need a bigger deposit and can carry higher rates or fees than standard loans, because the lender takes on more risk."),
     ("ABN history", "Most lenders want your ABN and GST registration to have been active for a minimum period, often one to two years."),
     ("A stepping stone", "Many borrowers use a low doc loan for a few years, then refinance to a standard loan once returns are up to date. See <a href=\"refinancing.html\">refinancing</a>.")],
    "Is a low doc loan right for you?", "It suits some situations better than others.", [
     ("Good fit", "Established business, strong recent turnover, returns not yet lodged."),
     ("Consider first", "Whether lodging overdue returns would open up standard loans with better pricing."),
     ("Next step", "A free chat to compare low doc and full doc options side by side.")],
    [("What documents do I need for a low doc loan?", "Usually your ABN details, recent BAS statements or business bank statements, and sometimes an accountant's declaration. Requirements vary by lender."),
     ("Are low doc loans more expensive?", "Generally, yes. Rates and fees are often higher and a larger deposit is usually needed. We compare options so you can see the trade-off."),
     ("Can I switch to a normal loan later?", "Often, yes. Once your returns are lodged, refinancing to a standard loan may reduce your costs.")])

svc("bridging-loans.html", "Bridging Loans Sydney | Buy Before You Sell | Creditt.",
    "Bridging loans let you buy your next home before selling your current one. We explain peak debt, end debt and the costs, and compare lenders.",
    "Bridging loans", "Bridging loans: buy before you sell", "Found the right home before you've sold? A bridging loan can cover the gap so you don't miss out or rush your sale.",
    "How bridging finance works", [
     ("Peak debt", "For a period you owe on both properties. The lender assesses this combined 'peak debt' against the value of both homes."),
     ("End debt", "Once your current home sells, the proceeds pay down the loan, leaving the 'end debt' on your new home. You need to be able to afford the end debt."),
     ("Interest during the bridge", "Many bridging loans let interest accumulate during the bridging period rather than requiring repayments, but that adds to the debt."),
     ("Time limit", "Bridging periods are usually short, often six to twelve months, so a realistic sale plan matters.")],
    "Questions to answer first", "We'll work these out together before you make an offer.", [
     ("What's my likely sale price?", "Be conservative. A lower-than-expected sale increases your end debt."),
     ("How long might it take to sell?", "The longer the bridge, the more interest builds up."),
     ("Is there a simpler option?", "Sometimes existing equity, or a longer settlement, works better than bridging.")],
    [("How much does a bridging loan cost?", "You pay interest on the combined debt during the bridging period, plus normal loan fees. We'll estimate the total cost for your situation."),
     ("What happens if my home doesn't sell in time?", "Lenders set a maximum bridging term. If it runs out, you may need to reduce the price or arrange other finance, so plan conservatively."),
     ("Can I avoid bridging finance?", "Possibly, by using existing equity for the deposit, negotiating a longer settlement, or selling first. We'll compare the options.")])

svc("construction-loans.html", "Construction Loans & Knock-Down Rebuild Finance | Creditt.",
    "Construction loans for new builds, knock-down rebuilds and major renovations. Progress payments, interest only during the build, compared across lenders.",
    "Construction loans", "Construction and knock-down rebuild loans", "Building, rebuilding or renovating in a big way? Construction loans pay your builder in stages and keep you in control of the cost.",
    "How construction loans work", [
     ("Progress payments", "The lender pays your builder in stages, such as slab, frame, lock-up, fixing and completion, after each stage is checked."),
     ("Interest only on what's drawn", "During the build you usually pay interest only on the amount drawn so far, not the full loan."),
     ("Valuation 'as if complete'", "The lender values the finished home based on your plans and contract, which determines how much you can borrow."),
     ("Fixed-price contract", "Most lenders want a fixed-price building contract with a licensed builder, approved plans and builder's insurance.")],
    "Plan ahead for", "These are the common surprises.", [
     ("Somewhere to live", "For a knock-down rebuild, budget for rent during the build."),
     ("Variations", "Changes during the build may need extra funds approved before work proceeds."),
     ("Timeline", "Lenders may set a maximum build period, so check your builder's schedule.")],
    [("Can I get a construction loan for a knock-down rebuild?", "Yes. The loan typically covers demolition and the build, secured against the land and the finished home."),
     ("Do I make repayments during construction?", "Usually interest only on the amount drawn. Full repayments generally start after completion."),
     ("Can I use an owner-builder?", "Some lenders consider owner-builder projects, but options are limited and requirements are stricter.")])

svc("debt-consolidation-home-loan.html", "Debt Consolidation Home Loan | Refinance Debts | Creditt.",
    "Consolidating car loans, personal loans and credit cards into your home loan can lower repayments. Understand the trade-offs before you refinance.",
    "Debt consolidation", "Debt consolidation home loans", "Rolling car loans, personal loans and credit cards into your home loan can cut monthly repayments. Done carelessly, it can also cost more over time.",
    "How it works and the trade-offs", [
     ("One lower repayment", "Home loan rates are usually lower than credit card and personal loan rates, so combining debts often reduces your monthly outgoings."),
     ("Longer loan term", "Spreading a short-term debt over a long mortgage term can mean paying more interest overall, unless you keep making higher repayments."),
     ("Equity required", "You need enough equity in your home to absorb the extra debt, usually within a lender's limits."),
     ("Close what you clear", "Consolidation works best when you close cleared cards and accounts so the debt doesn't return.")],
    "Before you consolidate", "A few checks make the difference.", [
     ("List every debt", "Balances, rates, repayments and any break costs."),
     ("Compare total cost", "Not just the monthly repayment, but the total interest over time."),
     ("Get support if you need it", "If repayments are hard to manage, talk to your lender early. Free financial counselling is available on 1800 007 007 (National Debt Helpline).")],
    [("Will debt consolidation hurt my credit score?", "Applying for credit creates an enquiry on your file, and closing accounts can change your credit profile. Paying debts down on time generally helps over time."),
     ("Can I consolidate debts into my mortgage if I have bad credit?", "Some lenders may consider it depending on the history. We'll look at which lenders suit your situation."),
     ("How much can I save?", "It depends on your debts and how you repay. We'll compare your current position with a consolidated loan, including total interest.")])

# Business finance hub
bf_main = (hero([HOME, LOANS, ("Business finance", "business-finance.html")], "Business finance for Sydney businesses",
                "Equipment, vehicles, commercial property and working capital, compared across lenders and structured around how your business trades.")
           + features("What we finance", [
               ("<a href=\"business-loans.html\">Business loans and lines of credit</a>", "Term loans for growth, and revolving lines of credit for cash flow."),
               ("<a href=\"asset-finance.html\">Asset finance</a>", "Finance for the equipment and vehicles your business runs on."),
               ("<a href=\"equipment-finance.html\">Equipment finance</a>", "Machinery, technology, fit-outs and tools, with repayments matched to cash flow."),
               ("<a href=\"vehicle-finance-business.html\">Business vehicle finance</a>", "From a single ute to a fleet."),
               ("<a href=\"medical-equipment-finance.html\">Medical and dental equipment finance</a>", "For practices setting up or upgrading."),
               ("<a href=\"chattel-mortgage.html\">Chattel mortgage</a>", "Own the asset from day one. Compare with a finance lease in our <a href=\"chattel-mortgage-vs-finance-lease.html\">guide</a>."),
               ("<a href=\"commercial-property-loans.html\">Commercial property loans</a>", "Buy your premises or a commercial investment, or <a href=\"refinance-commercial-property.html\">refinance an existing one</a>.")])
           + band("Why use a finance broker for business lending", "Business lending varies more between lenders than home lending does.", [
               ("Policy fit", "Lenders differ on industries, trading history and security."),
               ("Structure", "The right structure depends on cash flow, tax and how long you'll keep the asset. Ask your accountant about tax treatment."),
               ("Speed", "We know which lenders move quickly for the deal you have.")]))
page("business-finance.html", "Business Finance Broker Sydney | Creditt.",
     "Business loans, equipment and vehicle finance, chattel mortgages and commercial property loans for Sydney businesses, compared across lenders.",
     [HOME, LOANS, ("Business finance", "business-finance.html")], bf_main, [
      ("What do I need to apply for business finance?", "Usually your ABN, time in business, recent financials or BAS, and details of the asset or purpose. Some lenders offer low doc options for smaller amounts."),
      ("Can a new business get finance?", "Some lenders consider newer businesses, especially with industry experience or security. Options widen after one to two years of trading."),
      ("Is a chattel mortgage or lease better?", "It depends on cash flow, GST and how long you'll keep the asset. See our <a href=\"chattel-mortgage-vs-finance-lease.html\">comparison guide</a> and ask your accountant.")], "service", "Business finance for Sydney businesses")

# ---------------- GUIDES ----------------
def guide(slug, title, desc, h1, read, body, faqs):
    main = hero([GUIDES, (h1, slug)], h1, "").replace('<p class="lede"></p>', "") + article(body)
    page(slug, title, desc, [GUIDES, (h1, slug)], main, faqs, "guide", h1)
    PAGES[slug]["read"] = read

guide("first-home-buyer-guide-nsw.html", "First Home Buyer Guide NSW 2026 | Creditt.",
      "NSW first home buyer guide for 2026: stamp duty exemptions up to $800,000, the 5% Deposit Scheme with a $1.5m Sydney cap, the First Home Owner Grant and more.",
      "First home buyer guide for NSW (2026)", "7 min read", """
<p>Buying your first home in Sydney is expensive, but government help can make a real difference to how much you need upfront. Here's what's available in NSW in 2026, and how to make it work.</p>
<h2>1. Stamp duty: the First Home Buyers Assistance Scheme</h2>
<p>Eligible first home buyers in NSW pay no transfer (stamp) duty on new or existing homes up to $800,000, and a reduced amount on homes between $800,000 and $1,000,000. For vacant land you intend to build on, the full exemption applies up to $350,000, with a concession up to $450,000. Above those caps, full duty applies. Eligibility rules, including living in the home, apply, so check the details with Revenue NSW.</p>
<h2>2. The 5% Deposit Scheme</h2>
<p>The Australian Government 5% Deposit Scheme (formerly the Home Guarantee Scheme) lets eligible first home buyers buy with a 5% deposit without paying lenders mortgage insurance. The government guarantees up to 15% of the property value to the lender. Since October 2025 there are no income caps and no limit on places, and the price cap for Sydney is $1.5 million. You apply through a participating lender, which a broker can arrange.</p>
<h2>3. The First Home Owner Grant (new homes)</h2>
<p>A $10,000 grant may be available for eligible buyers of a new home, including off-the-plan, valued up to $600,000, or for building a new home within the relevant cap. It doesn't apply to existing homes.</p>
<h2>4. Your deposit and the real upfront costs</h2>
<ul><li>Deposit: from 5% with the scheme, 20% to avoid LMI without it, or somewhere in between with LMI.</li><li>Stamp duty: possibly nil or reduced, as above.</li><li>Conveyancing, building and pest inspections, and loan fees.</li><li>A buffer for moving costs and the first few months.</li></ul>
<h2>5. How much can you borrow?</h2>
<p>Lenders look at your income, expenses, existing debts and deposit, and test repayments at a rate higher than the actual rate. See <a href="how-much-can-i-borrow.html">how much can I borrow</a> and try our <a href="calculators.html#borrowing-power">borrowing power calculator</a>.</p>
<h2>6. Get pre-approval before you bid</h2>
<p>Pre-approval tells you your real limit, so you can bid at auction or make offers with confidence. We'll also check which schemes you qualify for and line up a participating lender.</p>
<p>Ready to start? <a href="contact.html">Book a free chat</a>, or read about <a href="first-home-buyers.html">first home buyer loans</a>.</p>
<p><small>Figures current as at November 2026 and subject to change. Check current rules with <a href="https://www.revenue.nsw.gov.au/grants-schemes/assistance-scheme">Revenue NSW</a> and Housing Australia.</small></p>""",
      [("How much stamp duty do first home buyers pay in NSW?", "Eligible first home buyers pay no stamp duty on homes up to $800,000 and a reduced amount between $800,000 and $1,000,000 (as at November 2026)."),
       ("What is the 5% Deposit Scheme price cap in Sydney?", "$1.5 million (as at November 2026). There are no income caps, and you apply through a participating lender."),
       ("Can I use the 5% Deposit Scheme and the stamp duty exemption together?", "Yes, if you meet the eligibility rules for both. We'll check your eligibility before you apply.")])

guide("how-much-can-i-borrow.html", "How Much Can I Borrow? What Lenders Look At | Creditt.",
      "How lenders work out your borrowing power: income, expenses, debts, the serviceability buffer and credit card limits, plus ways to borrow more responsibly.",
      "How much can I borrow? What lenders actually look at", "6 min read", """
<p>Your borrowing power isn't a fixed multiple of your salary. Each lender runs its own calculation, which is why the same person can get quite different answers from different banks. Here's what goes into it.</p>
<h2>1. Your income</h2>
<p>Base salary is counted in full. Overtime, bonuses, commissions and allowances are often counted only in part, or averaged over one or two years. Self-employed income is assessed from tax returns. See <a href="self-employed-home-loans.html">self-employed home loans</a>. Rental income is usually counted at a reduced percentage.</p>
<h2>2. Your living expenses</h2>
<p>Lenders use the higher of your declared expenses and a benchmark for your household size and income. Bank statements are checked, so be realistic.</p>
<h2>3. Existing debts and credit limits</h2>
<p>Car loans, personal loans, HECS-HELP and buy now pay later all reduce borrowing power. Credit cards count at their limit, not their balance, so cancelling unused cards or lowering limits can help.</p>
<h2>4. The serviceability buffer</h2>
<p>Lenders test whether you could afford repayments at a rate a few percentage points above the actual rate, under guidance from the banking regulator APRA. Banks also limit how much of their lending goes to borrowers with very high debt compared with income.</p>
<h2>5. Dependants and household</h2>
<p>Children and other dependants increase the expense benchmark and reduce borrowing power.</p>
<h2>Ways to improve your borrowing power</h2>
<ul><li>Pay down or close high-interest debts and reduce credit card limits.</li><li>Choose a lender whose income policy suits you, for example one that counts more of your bonus or rental income.</li><li>Consider a longer loan term or a co-borrower, understanding the trade-offs.</li></ul>
<p>For a quick estimate, use our <a href="calculators.html#borrowing-power">borrowing power calculator</a>. For a real number across lenders, <a href="contact.html">book a free chat</a>.</p>""",
      [("How many times my salary can I borrow?", "There's no fixed multiple. It depends on your expenses, debts, dependants, deposit and each lender's policy, so results vary between lenders."),
       ("Do credit cards affect borrowing power?", "Yes. Lenders count the full credit limit, even if you pay it off each month."),
       ("Why do different banks give different answers?", "Each lender uses its own expense benchmarks, income rules and calculations. Comparing several is how you find the best fit.")])

guide("refinancing-checklist.html", "Refinancing Checklist: Steps & Documents to Refinance | Creditt.",
      "A step-by-step refinancing checklist: what to check before you switch, the documents you'll need, and how long refinancing takes.",
      "Refinancing checklist: steps and documents", "5 min read", """
<p>Thinking of refinancing? Work through this checklist first so you know whether it's worth it and what to have ready.</p>
<h2>Step 1: Know your current loan</h2>
<ul><li>Current balance, rate and repayment.</li><li>Whether any part is fixed, and the break cost if so.</li><li>Discharge fees and features you use, such as an offset or redraw.</li></ul>
<h2>Step 2: Ask your current lender first</h2>
<p>A quick call asking for a rate review sometimes gets a better rate without switching. Use it as a benchmark.</p>
<h2>Step 3: Compare the total cost</h2>
<p>Add up exit costs and new loan costs, then work out how long it takes for the lower repayment to pay them back. Our guide <a href="blog-refinancing-worth-it.html">five questions to ask before you refinance</a> walks through it.</p>
<h2>Step 4: Gather your documents</h2>
<ul><li>Photo ID.</li><li>Recent payslips, or tax returns if self-employed.</li><li>Recent statements for your home loan and any other debts.</li><li>Council rates notice and home insurance details.</li></ul>
<h2>Step 5: Apply, value and settle</h2>
<p>The new lender values your property, approves the loan and arranges settlement with your current lender. It typically takes two to six weeks.</p>
<h2>Step 6: After you switch</h2>
<p>Set up repayments, move your offset savings, and keep your repayments at the old amount if you can afford it, to pay the loan down faster.</p>
<p>Want us to run the numbers? See <a href="refinancing.html">refinancing</a> or <a href="contact.html">book a free chat</a>.</p>""",
      [("How long does refinancing take?", "Usually two to six weeks from application to settlement, depending on the lender and how quickly documents come together."),
       ("Does refinancing cost money?", "There can be discharge, application and valuation fees, plus break costs on fixed loans. Some lenders waive or rebate costs. We'll compare the total."),
       ("Can I refinance if my property value has dropped?", "Possibly, but a lower value can affect your loan-to-value ratio and whether LMI applies. We'll check before you apply.")])

guide("is-a-mortgage-broker-free.html", "Is a Mortgage Broker Free? How Brokers Are Paid | Creditt.",
      "How mortgage brokers in Australia are paid, why it's usually free for borrowers, the best interests duty, and what to ask your broker.",
      "Is a mortgage broker free? How brokers are paid", "4 min read", """
<p>For most home loans, using a mortgage broker costs you nothing directly. Here's how it works and what protects you.</p>
<h2>How brokers are paid</h2>
<p>When your loan settles, the lender usually pays the broker an upfront commission, and often a smaller ongoing 'trail' commission while the loan is active. These payments come from the lender, not from your loan amount.</p>
<h2>When a fee might apply</h2>
<p>Some brokers charge a fee for complex or commercial lending, or if a loan is repaid very early. Any fee should be explained to you in writing before you proceed.</p>
<h2>The best interests duty</h2>
<p>Mortgage brokers in Australia must act in your best interests when giving credit assistance, and put your interests ahead of their own. That includes how they choose lenders to recommend.</p>
<h2>What your broker must tell you</h2>
<p>Your broker gives you a credit guide explaining who they are, how they're paid, and the lenders on their panel. At Creditt, we can only recommend products from lenders we have access to, and we explain why each option is on your shortlist.</p>
<h2>Questions worth asking any broker</h2>
<ul><li>How many lenders do you compare?</li><li>Will you charge me any fee?</li><li>Why are you recommending this lender over others?</li></ul>
<p>Have more questions? <a href="contact.html">Book a free chat</a>.</p>""",
      [("Do I pay a mortgage broker?", "Usually not. For most home loans the lender pays the broker's commission. Any fee must be disclosed upfront."),
       ("Do brokers get paid more by some lenders?", "Commission rates are broadly similar across lenders, and brokers must act in your best interests regardless."),
       ("Is it better to go to my bank directly?", "Your bank can only offer its own products. A broker compares options across a panel of lenders.")])

# ---------------- WRITE PAGES ----------------
tpl = open("home-loans.html").read()
for slug, p in PAGES.items():
    s = tpl
    s = re.sub(r"<title>.*?</title>", f"<title>{esc(p['title'])}</title>", s)
    s = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{esc(p["desc"])}">', s)
    s = re.sub(r'<link rel="canonical" href=".*?">', f'<link rel="canonical" href="{BASE}{slug}">', s)
    s = re.sub(r'og:title" content=".*?"', f'og:title" content="{esc(p["title"])}"', s)
    s = re.sub(r'og:description" content=".*?"', f'og:description" content="{esc(p["desc"])}"', s)
    s = re.sub(r'og:url" content=".*?"', f'og:url" content="{BASE}{slug}"', s)
    if p["kind"] == "guide": s = s.replace('og:type" content="website"', 'og:type" content="article"')
    s = re.sub(r'<script type="application/ld\+json">.*?</script>', "", s, flags=re.S)
    lds = []
    if p["faqs"]:
        lds.append({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip(a)}} for q, a in p["faqs"]]})
    lds.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": strip(n), "item": BASE if u == "index.html" else BASE + u} for i, (n, u) in enumerate(p["crumbs"])]})
    if p["kind"] == "guide":
        lds.append({"@context": "https://schema.org", "@type": "Article", "headline": p["h1"], "datePublished": TODAY, "dateModified": TODAY,
                    "image": BASE + "images/og-share.jpg", "author": {"@type": "Person", "name": "Sidharth Singhal"}, "publisher": {"@id": BASE + "#business"}, "mainEntityOfPage": BASE + slug})
    if p["kind"] in ("suburb", "service"):
        lds.append({"@context": "https://schema.org", "@type": "Service", "name": p["h1"], "provider": {"@id": BASE + "#business"}, "areaServed": "Sydney NSW", "url": BASE + slug})
    s = s.replace("</head>", "".join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>' for j in lds) + "</head>", 1)
    s = s.replace(' aria-current="page"', "")
    s = re.sub(r'<main id="main">.*?</main>', lambda m: '<main id="main">' + p["main"] + "</main>", s, flags=re.S)
    open(slug, "w").write(s)

# ---------------- LINKING ----------------
def edit(fn, fnc):
    s = open(fn).read(); n = fnc(s)
    if n != s: open(fn, "w").write(n)

# North Shore hub: suburb links
sub_links = "".join(f'<li><a href="{x["slug"]}">Mortgage broker {x["area"]}</a></li>' for x in SUBURBS)
edit("mortgage-broker-north-shore.html", lambda s: s if "mortgage-broker-lane-cove.html" in s else s.replace(
    '<section class="section"><div class="container"><div class="section-head"><h2 class="dt">Common questions',
    f'<section class="section"><div class="container"><div class="section-head"><h2 class="dt">Local area pages</h2><p>What we see in each part of the North Shore.</p></div><ul>{sub_links}</ul></div></section><section class="section"><div class="container"><div class="section-head"><h2 class="dt">Common questions', 1))

NEW_NAV = [("Business Finance", "business-finance.html"), ("Self-Employed Loans", "self-employed-home-loans.html"), ("Low Doc Loans", "low-doc-home-loans.html"), ("Bridging Loans", "bridging-loans.html"), ("Construction Loans", "construction-loans.html")]
for fn in glob.glob("*.html"):
    def f(s):
        if 'href="bridging-loans.html">Bridging Loans' not in s:
            add = "".join(f'<li><a href="{u}">{n}</a></li>' for n, u in NEW_NAV)
            s = s.replace('<li><a href="commercial-lending.html">Commercial Lending</a></li></ul></li>', '<li><a href="commercial-lending.html">Commercial Lending</a></li>' + add + '</ul></li>', 1)
            addm = "".join(f'<a class="sub" href="{u}">{n}</a>' for n, u in NEW_NAV)
            s = s.replace('<a class="sub" href="commercial-lending.html">Commercial Lending</a>', '<a class="sub" href="commercial-lending.html">Commercial Lending</a>' + addm, 1)
        if 'first-home-buyer-guide-nsw.html">First home buyer guide' not in s:
            s = s.replace('<li><a href="blog.html">Guides</a></li>', '<li><a href="blog.html">Guides</a></li><li><a href="first-home-buyer-guide-nsw.html">First home buyer guide NSW</a></li><li><a href="how-much-can-i-borrow.html">How much can I borrow?</a></li>', 1)
        return s
    edit(fn, f)

# Blog cards
cards = "".join(f'<a class="post" href="{slug}"><h2>{p["h1"]}</h2><p>{esc(p["desc"])}</p><span class="meta">{p["read"]}</span></a>' for slug, p in PAGES.items() if p["kind"] == "guide")
edit("blog.html", lambda s: s if "first-home-buyer-guide-nsw.html\"><h2>" in s else s.replace('<div class="post-grid">', '<div class="post-grid">' + cards, 1))
# Cross links from existing pages
edit("first-home-buyers.html", lambda s: s if "first-home-buyer-guide-nsw.html\">Read" in s else s.replace('</aside>', '<p style="margin-top:16px;"><a href="first-home-buyer-guide-nsw.html">Read the NSW first home buyer guide</a></p></aside>', 1))
edit("asset-finance.html", lambda s: s if 'business-finance.html">All business' in s else s.replace('</aside>', '<p style="margin-top:16px;"><a href="business-finance.html">All business finance options</a></p></aside>', 1))
edit("refinancing.html", lambda s: s if 'refinancing-checklist.html">' in s else s.replace('</aside>', '<p style="margin-top:16px;"><a href="refinancing-checklist.html">Refinancing checklist</a></p></aside>', 1))

# ---------------- SITEMAP ----------------
urls = []
for fn in sorted(glob.glob("*.html")):
    if fn == "404.html": continue
    pr = "1.0" if fn == "index.html" else ("0.3" if fn in ("privacy.html", "terms.html") else ("0.7" if fn.startswith("blog") or PAGES.get(fn, {}).get("kind") == "guide" else "0.8"))
    urls.append(f"  <url><loc>{BASE if fn == 'index.html' else BASE + fn}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>")
open("sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n")
print("new pages", len(PAGES), "sitemap", len(urls))
