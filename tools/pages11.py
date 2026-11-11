import re, sys, os, glob
SITE = sys.argv[1]
src = open("/home/claude/build/pages18.py").read()
helpers = src[src.index("BASE = "):src.index("# ---------------- SUBURB PAGES")]
writer = src[src.index("# ---------------- WRITE PAGES"):src.index("# ---------------- LINKING")]
os.chdir(SITE)
import json, html
exec(helpers)

HOME = ("Home", "index.html"); BF = ("Business finance", "business-finance.html"); TAX = ("Tax and accounting", "tax-compliance.html")
def svc2(slug, title, desc, parent, crumb, h1, lede, h2, feats, band_t, band_i, cols, faqs):
    main = hero([HOME, parent, (crumb, slug)], h1, lede) + features(h2, feats) + band(band_t, band_i, cols)
    page(slug, title, desc, [HOME, parent, (crumb, slug)], main, faqs, "service", h1)

ACC = "Ask your accountant how the GST and tax treatment applies to your business."

# ---------- ASSET FINANCE (5) ----------
svc2("truck-finance.html", "Truck Finance | Prime Movers, Rigid Trucks & Trailers | Creditt.",
 "Truck and trailer finance for owner-drivers, fleets and transport businesses. Chattel mortgage, finance lease and low doc options compared across lenders.",
 BF, "Truck finance", "Truck and trailer finance", "Whether it's your first truck as an owner-driver or the next addition to a fleet, we compare lenders that understand transport.",
 "How truck finance works", [
  ("New and used trucks", "Finance for light, medium and heavy rigid trucks, prime movers and tippers, new or used, from dealers or private sellers. Lenders set limits on the age of the truck at the end of the term."),
  ("Trailers and bodies", "Finance can cover trailers, refrigeration units, tippers and custom bodies, either with the truck or separately."),
  ("Chattel mortgage or lease", "A <a href=\"chattel-mortgage.html\">chattel mortgage</a> means you own the truck from day one; a finance lease keeps it off your balance sheet. See <a href=\"chattel-mortgage-vs-finance-lease.html\">chattel mortgage vs finance lease</a>. " + ACC),
  ("Balloon payments", "A balloon (residual) at the end of the term lowers regular repayments, but you'll need to pay or refinance it when the term ends.")],
 "What lenders look at", "Transport lending is specialised, so lender choice matters.", [
  ("Experience", "Time in the industry and holding the right licence, especially for first-time owner-drivers."),
  ("Work lined up", "Contracts or regular work can strengthen an application."),
  ("Business history", "ABN and GST registration time, and financials or BAS. <a href=\"low-doc-asset-finance.html\">Low doc options</a> exist.")],
 [("Can I get truck finance as a new owner-driver?", "Often, yes, especially if you have driving experience and work lined up. Some lenders specialise in first-time owner-drivers."),
  ("Can I finance a used truck from a private seller?", "Many lenders allow private sales, usually with checks on ownership, condition and any money owing on the truck."),
  ("How long can truck finance run?", "Terms are commonly one to seven years, depending on the truck's age and the lender.")])

svc2("earthmoving-equipment-finance.html", "Excavator & Earthmoving Equipment Finance | Creditt.",
 "Finance for excavators, bobcats, loaders, rollers and other earthmoving and construction equipment, new or used, with repayments matched to your cash flow.",
 BF, "Earthmoving equipment finance", "Excavator and earthmoving equipment finance", "From a mini excavator to a full fleet of yellow gear, we find lenders that finance construction and civil equipment on terms that suit how you earn.",
 "What we finance", [
  ("Excavators and mini excavators", "New and used excavators from dealers, auctions or private sellers, plus attachments such as buckets, rippers and tilt hitches."),
  ("Loaders, skid steers and bobcats", "Wheel loaders, compact track loaders and skid steers for landscaping, civil and construction work."),
  ("Rollers, graders and trucks", "Compaction gear, graders, water carts and tipper trucks, financed together or one at a time."),
  ("Auction purchases", "Some lenders can approve finance for auction purchases if arranged before you bid.")],
 "Matching repayments to your work", "Construction income can be lumpy, so structure matters.", [
  ("Seasonal repayments", "Some lenders offer structured repayments around quieter months."),
  ("Balloons", "A balloon lowers regular repayments, with a lump sum due at the end."),
  ("Tax treatment", "Depreciation and GST depend on the structure. " + ACC)],
 [("Can I finance a used excavator?", "Yes. Lenders usually check the machine's age, hours and value, and some limit the age at the end of the loan."),
  ("Can I buy earthmoving equipment at auction with finance?", "Often, yes, if you have approval in place before the auction and the lender accepts the auction house."),
  ("Do I need a deposit?", "Not always. Many established businesses can finance the full price; newer businesses may need a deposit.")])

svc2("electric-vehicle-business-finance.html", "Electric Vehicle Finance for Business | EV Car & Van Loans | Creditt.",
 "Finance electric cars, vans and utes through your business. Chattel mortgage, lease and novated lease options, plus charging equipment, compared across lenders.",
 BF, "Electric vehicle finance", "Electric vehicle finance for business", "Switching your business vehicles to electric? We compare lenders for EV cars, vans and utes, including some green loan options with sharper pricing.",
 "Your EV finance options", [
  ("Chattel mortgage", "Your business owns the EV from day one and makes fixed repayments. Common for sole traders and companies."),
  ("Finance or operating lease", "The lender owns the vehicle and you make lease payments, with options at the end of the term."),
  ("Novated lease for employees", "A three-way agreement between employer, employee and financier. Eligible electric cars may be exempt from fringe benefits tax under current rules. " + ACC),
  ("Green and low-emission loans", "Some lenders offer discounted rates for low or zero-emission vehicles. Eligibility and pricing vary.")],
 "Before you buy", "A few EV-specific points.", [
  ("Charging", "Home or workplace chargers can sometimes be included in the finance."),
  ("Residual values", "Lenders set balloon limits based on expected resale value, which is still settling for EVs."),
  ("Range and use", "Make sure the vehicle suits your daily distances and loads.")],
 [("Can I finance an EV through my business?", "Yes, through a chattel mortgage, lease or, for employees, a novated lease. The best option depends on your structure and how the vehicle is used."),
  ("Are there cheaper loans for electric vehicles?", "Some lenders offer green loan discounts for eligible low-emission vehicles. We'll compare whether it beats a standard option."),
  ("Can the charger be financed too?", "Some lenders allow charging equipment to be included. We'll check when we compare options.")])

svc2("low-doc-asset-finance.html", "Low Doc Asset Finance | No Financials Equipment Loans | Creditt.",
 "Low doc asset finance for ABN holders without up-to-date financials. Finance vehicles and equipment using BAS, bank statements or a declaration.",
 BF, "Low doc asset finance", "Low doc asset finance", "Need a vehicle or equipment but your financials aren't up to date? Low doc asset finance can approve on simpler evidence.",
 "How low doc asset finance works", [
  ("Less paperwork", "Instead of full financials, lenders may accept an ABN history check, recent BAS, business bank statements or a signed declaration of affordability."),
  ("Loan size limits", "Low doc approvals usually have caps, which vary by lender and depend on your ABN age, credit history and whether you own property."),
  ("Property owners", "Owning property, even with a mortgage, often widens your options and limits."),
  ("Pricing", "Rates can be a little higher than full doc, though for established ABNs the gap is often small.")],
 "Who it suits", "Common situations we see.", [
  ("Established ABNs", "Usually two years or more of ABN and GST registration."),
  ("Financials pending", "Returns not yet lodged, or recent growth not yet showing."),
  ("Fast purchases", "Quicker approvals when the right truck or machine comes up.")],
 [("What is the minimum ABN age for low doc asset finance?", "Many lenders look for around two years, though some consider one year, especially for property owners."),
  ("What can I finance with low doc?", "Most business assets, including cars, utes, vans, trucks, machinery and equipment, within each lender's limits."),
  ("Will low doc cost more?", "Sometimes slightly more than full doc. We'll compare both so you can decide.")])

svc2("hospitality-equipment-finance.html", "Restaurant & Café Equipment Finance | Hospitality Fit-Out | Creditt.",
 "Finance commercial kitchens, coffee machines, refrigeration, POS and fit-outs for restaurants, cafés and bars. Compare lenders that understand hospitality.",
 BF, "Hospitality equipment finance", "Restaurant and café equipment finance", "Opening, upgrading or expanding a venue? We finance the kitchen, the coffee machine and the fit-out, with repayments that work around your trading.",
 "What we finance", [
  ("Commercial kitchen equipment", "Combi ovens, ranges, fryers, dishwashers, exhaust canopies and refrigeration."),
  ("Coffee machines and grinders", "Commercial espresso machines and grinders, new or used."),
  ("Fit-outs", "Shopfitting, furniture and joinery. Fit-out lending is more specialised because the assets are harder to resell."),
  ("POS and technology", "Point-of-sale systems, screens and ordering technology.")],
 "Hospitality lending tips", "Lenders see hospitality as higher risk, so preparation helps.", [
  ("Trading history", "Established venues have more options; new venues may need a deposit or extra security."),
  ("Lease terms", "Lenders look at how long your premises lease runs."),
  ("Mix of finance", "Equipment finance plus a <a href=\"business-loans.html\">business loan</a> or <a href=\"unsecured-business-loans.html\">unsecured loan</a> for working capital can work well.")],
 [("Can a new café get equipment finance?", "Sometimes, especially with industry experience, a deposit or property as security. Options widen after trading for a year or two."),
  ("Can I finance a fit-out?", "Yes, though fewer lenders do it because fit-outs have little resale value. We know which lenders will consider it."),
  ("Can I finance second-hand kitchen equipment?", "Many lenders will, subject to the equipment's age and value.")])

# ---------- BUSINESS FINANCE (3) ----------
svc2("unsecured-business-loans.html", "Unsecured Business Loans Sydney | Fast Working Capital | Creditt.",
 "Unsecured business loans for working capital, stock, wages and growth, without property security. Compare lenders, terms and costs with a broker.",
 BF, "Unsecured business loans", "Unsecured business loans", "Need working capital quickly without putting your home up as security? Unsecured business loans can fund stock, wages, marketing or a short-term gap.",
 "How unsecured business loans work", [
  ("No property security", "The loan isn't secured against property, although most lenders ask for a personal guarantee from directors."),
  ("Fast decisions", "Many lenders assess using bank statement data, with decisions in days rather than weeks."),
  ("Shorter terms, higher cost", "Terms are usually short, often up to a few years, and costs are higher than secured lending. Compare the total cost, not just the repayment."),
  ("Flexible use", "Stock, wages, equipment deposits, marketing, tax debts or bridging a slow period.")],
 "Before you borrow", "Unsecured lending is easy to get and easy to overuse.", [
  ("Total cost", "Ask for the total repayable and any fees, including early repayment costs."),
  ("Repayment frequency", "Some lenders take daily or weekly repayments, which affects cash flow."),
  ("Alternatives", "A secured <a href=\"business-loans.html\">business loan</a>, <a href=\"invoice-finance.html\">invoice finance</a> or a line of credit may be cheaper.")],
 [("Do I need a personal guarantee?", "Most unsecured business lenders ask directors for a personal guarantee, even though no property is used as security."),
  ("How fast can I get an unsecured business loan?", "Some lenders decide within a day or two of receiving bank statements and documents."),
  ("How much can I borrow unsecured?", "It depends on your turnover, trading history and the lender. Limits are generally lower than secured lending.")])

svc2("invoice-finance.html", "Invoice Finance & Debtor Finance | Unlock Cash Flow | Creditt.",
 "Invoice finance turns unpaid customer invoices into cash. Compare invoice discounting, factoring and selective invoice finance for B2B businesses.",
 BF, "Invoice finance", "Invoice finance (debtor finance)", "Waiting 30, 60 or 90 days for customers to pay? Invoice finance releases cash tied up in unpaid invoices so you can pay staff and suppliers on time.",
 "Types of invoice finance", [
  ("Invoice discounting", "You borrow against your whole debtor book and keep collecting from customers yourself. Usually confidential."),
  ("Factoring", "The financier manages collections from your customers. Simpler for some businesses, but customers know about it."),
  ("Selective (single) invoice finance", "Finance individual invoices when you need to, instead of your whole ledger."),
  ("Advance rates", "Lenders typically advance a percentage of each eligible invoice, with the balance, less fees, paid when your customer pays.")],
 "Who it suits", "It works best for businesses that sell to other businesses.", [
  ("B2B invoicing", "Recruitment, wholesale, manufacturing, transport and professional services."),
  ("Growing fast", "When growth ties up cash in receivables."),
  ("Quality customers", "Lenders look at your customers' creditworthiness as much as yours.")],
 [("How quickly can I get paid with invoice finance?", "Once the facility is set up, funds against new invoices are often available within a day or two."),
  ("Will my customers know?", "With confidential invoice discounting, usually not. With factoring, the financier deals with your customers directly."),
  ("Does invoice finance need property security?", "Usually not. The invoices themselves are the main security, though directors may need to give guarantees.")])

svc2("business-acquisition-loans.html", "Business Acquisition Loans | Finance to Buy a Business | Creditt.",
 "Finance to buy a business or franchise: deposits, security, goodwill and what lenders need to see. Compare lenders with a business finance broker.",
 BF, "Business acquisition loans", "Business acquisition loans: finance to buy a business", "Buying an existing business or franchise? We help you understand what lenders need and structure the purchase so it's financeable.",
 "How business purchase finance works", [
  ("Security", "Most lenders want security, often residential or commercial property, because goodwill alone is hard to lend against."),
  ("Deposit or equity", "Expect to contribute a meaningful share of the price yourself. The amount depends on the business, your experience and the security."),
  ("Due diligence", "Lenders look at the business's financial statements, cash flow, lease and the reason for sale. Your accountant and lawyer play key roles."),
  ("Franchises", "Some lenders have accredited franchise programs that make approval easier for established brands.")],
 "What lenders want to see", "A strong application tells a clear story.", [
  ("Your experience", "Industry or management experience relevant to the business."),
  ("The numbers", "At least two to three years of financials and a realistic forecast."),
  ("The structure", "Purchase entity, premises lease and how working capital will be funded.")],
 [("Can I buy a business with no deposit?", "It's uncommon. Most lenders want you to contribute equity or provide property security, especially when much of the price is goodwill."),
  ("Can I use my home as security to buy a business?", "Yes, many buyers do. It can improve approval chances and pricing, but it puts your home at risk, so get advice."),
  ("Do you help with franchise finance?", "Yes. Some lenders have franchise programs for accredited brands, which we can compare.")])

# ---------- BOOKKEEPING (3) ----------
svc2("bookkeeper-north-shore.html", "Bookkeeper North Shore Sydney | Small Business Bookkeeping | Creditt.",
 "Bookkeeping for small businesses on Sydney's North Shore: reconciliations, BAS, payroll and Xero, by registered agents based in Lane Cove West.",
 TAX, "Bookkeeping", "Bookkeeper on Sydney's North Shore", "Tidy books, on-time BAS and payroll that just works, from a Lane Cove West team of registered agents and Xero Platinum Partners.",
 "Bookkeeping services", [
  ("Weekly or monthly bookkeeping", "Bank reconciliations, coding transactions, supplier bills and customer invoices, so your numbers are always current."),
  ("BAS and IAS", "Prepared from your reconciled books and lodged by registered agents. See <a href=\"tax-compliance.html\">tax compliance</a>."),
  ("Payroll and super", "Pay runs, Single Touch Payroll and super on each payday. See <a href=\"payroll-bookkeeping.html\">payroll bookkeeping</a>."),
  ("Catch-up and clean-up", "Behind on your books? We bring them up to date and fix past errors.")],
 "Why use a local bookkeeper", "Clean books do more than keep the ATO happy.", [
  ("Better decisions", "Up-to-date numbers show cash flow and profit as they happen."),
  ("Finance-ready", "Lenders want accurate financials. Being a finance broker too, we know what they look for."),
  ("Local and online", "Based in Lane Cove West, working with businesses across the North Shore and Australia.")],
 [("How much does a bookkeeper cost?", "It depends on transaction volume, payroll and how often you need work done. We'll quote a fixed monthly fee after a quick chat."),
  ("Do you only work with Xero?", "We specialise in Xero as a Platinum Partner, and can help you move from other software."),
  ("Can you catch up on overdue BAS?", "Yes. We reconcile the backlog, prepare the outstanding BAS and lodge them through our registered agents.")])

svc2("xero-bookkeeping.html", "Xero Bookkeeping & Setup | Xero Platinum Partner Sydney | Creditt.",
 "Xero setup, migration, training, clean-ups and ongoing bookkeeping from a Xero Platinum Partner in Lane Cove West, Sydney.",
 TAX, "Xero bookkeeping", "Xero bookkeeping, setup and support", "Get the most out of Xero, from a clean setup and bank feeds to automated rules, payroll and reporting, with a Xero Platinum Partner.",
 "How we help with Xero", [
  ("Setup and migration", "New Xero files, or moving from MYOB, QuickBooks or spreadsheets, with your chart of accounts, opening balances and bank feeds set up properly."),
  ("Clean-ups", "Unreconciled transactions, duplicate entries and miscoded accounts fixed so your reports can be trusted."),
  ("Automation", "Bank rules, receipt capture, recurring invoices and connected apps to cut manual work."),
  ("Training", "Practical training for you or your team on the tasks you do every week.")],
 "Ongoing Xero support", "Choose the level of help you need.", [
  ("Do it yourself", "We set up and review, you do the day-to-day."),
  ("Done with you", "Monthly review and reconciliation alongside your team."),
  ("Done for you", "Full <a href=\"bookkeeper-north-shore.html\">bookkeeping</a>, BAS and payroll.")],
 [("Can you move my business from MYOB to Xero?", "Yes. We plan the conversion, bring across balances and history as needed, and set up bank feeds and payroll."),
  ("What does a Xero clean-up involve?", "We review unreconciled items, fix miscoding and duplicates, reconcile balances, and set up rules to keep it clean."),
  ("Do you offer Xero training?", "Yes, one-on-one or for your team, focused on the tasks you actually do.")])

svc2("payroll-bookkeeping.html", "Payroll Services & Payday Super | STP Bookkeeping | Creditt.",
 "Outsourced payroll for small businesses: pay runs, Single Touch Payroll, Payday Super, leave and award rates, handled in Xero by registered agents.",
 TAX, "Payroll bookkeeping", "Payroll services, STP and Payday Super", "Payroll got harder from 1 July 2026 with Payday Super. We run your pays, report through Single Touch Payroll and get super paid on time.",
 "What's changed: Payday Super", [
  ("Super on every payday", "Since 1 July 2026, employers must pay super guarantee with each pay run, rather than quarterly, and it must reach the employee's fund within 7 business days of payday."),
  ("12% of qualifying earnings", "The super guarantee rate is 12%, now calculated on 'qualifying earnings'."),
  ("STP reporting", "Each pay event reported through Single Touch Payroll now includes qualifying earnings and super liability."),
  ("Clearing house closed", "The ATO's Small Business Superannuation Clearing House has closed, so many businesses need a new way to pay super.")],
 "Our payroll service", "We take payroll off your plate.", [
  ("Pay runs", "Weekly, fortnightly or monthly pays in Xero, with payslips sent to staff."),
  ("Compliance", "STP reporting, super with each pay, leave balances and end-of-year finalisation."),
  ("Setup", "New employees, award and pay rate setup, and moving payroll into Xero.")],
 [("What is Payday Super?", "From 1 July 2026, employers pay super guarantee at the same time as wages, and contributions must reach the fund within 7 business days of payday."),
  ("What is the super guarantee rate?", "12% of qualifying earnings for 2026-27."),
  ("Can you run payroll in Xero for me?", "Yes. We run pays, lodge STP, pay super on time and keep leave balances accurate.")])

tpl_name = "home-loans.html"
exec(writer.replace('open("home-loans.html")', 'open(tpl_name)'))

# ---------- LINKING ----------
def edit(fn, f):
    s = open(fn).read(); n = f(s)
    if n != s: open(fn, "w").write(n)
asset_links = "".join(f'<li><a href="{u}">{n}</a></li>' for n, u in [("Truck finance", "truck-finance.html"), ("Excavator and earthmoving finance", "earthmoving-equipment-finance.html"), ("Electric vehicle finance", "electric-vehicle-business-finance.html"), ("Low doc asset finance", "low-doc-asset-finance.html"), ("Restaurant and café equipment finance", "hospitality-equipment-finance.html"), ("Unsecured business loans", "unsecured-business-loans.html"), ("Invoice finance", "invoice-finance.html"), ("Business acquisition loans", "business-acquisition-loans.html")])
edit("business-finance.html", lambda s: s if "truck-finance.html" in s else s.replace('<section class="section"><div class="container"><div class="section-head"><h2 class="dt">Common questions',
    f'<section class="section"><div class="container"><div class="section-head"><h2 class="dt">More finance options</h2></div><ul>{asset_links}</ul></div></section><section class="section"><div class="container"><div class="section-head"><h2 class="dt">Common questions', 1))
book_links = '<p style="margin-top:16px;"><a href="bookkeeper-north-shore.html">Bookkeeping</a> · <a href="xero-bookkeeping.html">Xero support</a> · <a href="payroll-bookkeeping.html">Payroll and Payday Super</a></p>'
for fn in ("accounting.html", "tax-compliance.html", "tax-agent-north-shore.html"):
    edit(fn, lambda s: s if "payroll-bookkeeping.html" in s else s.replace("</aside>", book_links + "</aside>", 1) if "</aside>" in s else s.replace("</main>", f'<section class="section"><div class="container">{book_links}</div></section></main>', 1))
for fn in ("asset-finance.html", "equipment-finance.html", "vehicle-finance-business.html"):
    edit(fn, lambda s: s if "truck-finance.html\">" in s else s.replace("</aside>", '<p style="margin-top:16px;"><a href="truck-finance.html">Truck finance</a> · <a href="earthmoving-equipment-finance.html">Earthmoving</a> · <a href="electric-vehicle-business-finance.html">EV finance</a> · <a href="low-doc-asset-finance.html">Low doc</a></p></aside>', 1))
# Tax menu: add Bookkeeping
for fn in glob.glob("*.html"):
    edit(fn, lambda s: s if 'href="bookkeeper-north-shore.html">Bookkeeping</a></li>' in s else s.replace('<li><a href="accounting.html">Accounting</a></li>', '<li><a href="accounting.html">Accounting</a></li><li><a href="bookkeeper-north-shore.html">Bookkeeping</a></li>', 1).replace('<a class="sub" href="accounting.html">Accounting</a>', '<a class="sub" href="accounting.html">Accounting</a><a class="sub" href="bookkeeper-north-shore.html">Bookkeeping</a>', 1))

# ---------- SITEMAP ----------
urls = []
for fn in sorted(glob.glob("*.html")):
    if fn == "404.html": continue
    pr = "1.0" if fn == "index.html" else ("0.3" if fn in ("privacy.html", "terms.html") else "0.8")
    urls.append(f"  <url><loc>{BASE if fn == 'index.html' else BASE + fn}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>")
open("sitemap.xml", "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n")
print("new", len(PAGES), "sitemap", len(urls))
