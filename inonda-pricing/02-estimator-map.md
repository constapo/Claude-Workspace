# Step 2: Estimator map and error log (inonda.homes)

Date: 2026-11-18. Repo `constapo/inonda-service-estimator`, `main` at commit `a57c75a` (16 Nov).
**Method:** I read the code, ran all the existing tests, ran the site locally in a headless
browser in all 6 languages at phone width, and checked the live site.
**Gortex:** not used. Its installer (get.gortex.dev) is blocked by this environment's network
policy, so the map was made by reading the code directly.
**Existing tests:** all pass (46 JavaScript and 21 Python). None of the errors below is caught by them.

## 1. Where everything lives

| What | File | Notes |
|---|---|---|
| Prices: rate per unit and minimum job price | `dist/estimator.mjs` → `JOBS` | 15 jobs, 50 types of work. One entry looks like `tiles:[45,350]`, meaning €45 per m² and a €350 minimum, VAT included. Metalwork items also carry their own unit and default quantity. |
| Gypsum board extra | `BOARDS` | €0, €8 or €12 per m² |
| Job complexity | `COMPLEXITY` | standard ×1, many cuts ×1.2, complex ×1.4 (never shown to visitors) |
| Commercial factor | `COMMERCIAL_UPLIFT` | ×1.2 (never shown to visitors) |
| Skip & site preparation | `SKIP` | €250 per skip + 5% of the jobs (at least €100). Added automatically. |
| Range width | `SPREAD` | ±15%, rounded to the nearest €5. **To be removed: single figures from now on.** |
| Travel | `TRAVEL`, `PLACES` (72 places) | Free up to 20 km from Nicosia, then €10 per 10 km. Hidden inside the skip line. |
| Formula | `calculate()` | job = max(quantity × (rate + board extra), minimum) × complexity × commercial factor; total = sum of all lines |
| VAT | `VAT_RATE=19` | Rates already include VAT. The total is never increased; the VAT part (net, VAT) is only worked out for display. |
| Labels for jobs and types of work | `estimator.mjs` → `COPY`, `GYP`, `WELD`, `DESC`, `HOW`, `WHERE` | 6 languages |
| Page wording | `dist/i18n.mjs` | 6 languages; Hebrew right-to-left |
| Screen, WhatsApp text, Save as PDF | `dist/app.js` | |
| Carpentry (no automatic price) | `dist/carpentry.mjs`, `carpentry-ui.mjs` | Shown as "Price on request" |
| On-page guide and chat | `dist/assistant.mjs`, `dist/inonda-chat.js` (copy of `tools/inonda_chat.js`) | Shared by all three sites |
| Language pages /en/, /ru/ … | `tools/build_language_pages.py` | Built when the site is published |
| Python host | `server.py` = `host/server.py` | Serves an allow-list of files |

## 2. Errors found

### A. Errors visitors see
1. **Error messages are in English in every language.** For example, a Greek, Russian or
   Hebrew visitor who enters quantity 0 sees "Quantity must be between 1 and 5000." All 9
   messages in `calculate()` are English-only, and `app.js` shows them untranslated.
2. **Fractional quantities are accepted for whole items.** 1.5 interior doors or 2.5 sockets
   are priced without complaint. Points, pieces, rooms, gates and skips should be whole numbers.
   The quantity box also accepts "1e3", which it reads as 1,000.
3. **Place names are only in Greek and English.** The town list and the WhatsApp message show
   "Larnaca" to Russian, Ukrainian, Hebrew and Romanian visitors.
4. **The skip line reads badly:** "1 skip(s)" (EN), "1 контейнер(ы)" (RU), "1 containere"
   (RO, should be "1 container"), "1 מכולות" (HE, plural with 1).
5. **On phones the chat greeting pops up over the budget.** After about 5 seconds it covers
   the price lines (seen at 360 px wide).
6. **Search engines get mixed signals about the language pages.** The sitemap and page
   addresses use `/en/`, `/ru/` …, but the `hreflang` tags in `index.html` point to `/?lang=en`.

### B. Conflicts with the business rules
7. **Ranges instead of single figures.** The `SPREAD` setting and `range()` produce every
   price on screen, in WhatsApp and in the PDF as a range, which you've now replaced with
   single figures. `README.md` and `AGENTS.md` also say "show only price ranges".
8. **The skip line is automatic and costly on small jobs.** One €150 socket becomes a €500
   estimate, because €350 of skip and site preparation is added. It's not a rule breach, but
   it makes small one-off jobs look expensive. Decision needed (section 3).
9. **The slogan "Quality above all" is missing from the estimator.** I found no "years in
   business" claims anywhere (good).
10. **The quotation-fee rule.** You asked to keep the €50 / 10 km / city-surcharge rules for
    one-off jobs, but they were already removed from all three sites on 11 Nov 2026. The
    commits are "Remove quotation visit fees" in each repo. The estimator now only says
    "Quotations under a maintenance contract are completely free". Bringing them back means
    adding text again, and the old wording described "small repairs up to €1,000", which are
    now contract-only. See section 3.
11. **Durations, costs and margins: no leaks found.** No unit rates, material share, 60/40
    split, complexity percentages, commercial factor, travel amount or job durations appear
    on the page, in WhatsApp or in the PDF, in any language. The only time wording is the rule
    "we take on only jobs of more than one day of work", which is a policy, not a job duration.
12. **Contact details are correct in all 6 languages:** HE490415, +357 94 091 616 and
    +357 94 091 613 with WhatsApp and Viber, plus inonda.org, inonda.site and inonda.homes.
    The registration number is written "HE490415"; the rule spells it "HE 490415".

### C. Code and documentation inconsistencies (nothing a visitor sees)
13. **`server.py` doesn't match how the live site is hosted.** It doesn't serve `/en/`,
    `/ru/`, `/uk/`, `/he/`, `/ro/` (404 locally), yet the live site serves them (HTTP 200).
    Production therefore uses the static build, not this Python host. The README still
    describes the Python host as the live server. Before merging I need to know which host
    actually publishes `main`.
14. **The docs disagree on travel.** `AGENTS.md` says the commercial factor also applies to
    travel; the code and `README.md` say it does not. Today a commercial job in Paphos gets
    €110 travel with no factor.
15. **Leftovers from the old monthly-plan feature.** `calculate()` still returns a `monthly`
    total of 0, and the README still describes "monthly versus one-off totals". The feature
    was removed (contract work is not in the estimator).
16. **Carpentry is priced from a frozen copy.** inonda.org keeps a copy of the estimator's
    carpentry list (`carpentry_catalog.json`). It must be refreshed if the list changes.

## 3. Decisions needed from you
- **Skip & site preparation — DECIDED 2026-11-18: big jobs only** (renovations, kitchens, bathrooms, flooring). Original question: keep it switched on by default, switch it off by default, or
  only add it to bigger jobs such as renovations, kitchens, bathrooms and flooring.
  (Recommended: only bigger jobs.)
- **Quotation fees for one-off jobs:** the old rules no longer exist on any site. Either
  (a) leave them out, so the sites stay as they are now, or (b) send me the exact rule to show
  (amount, distance, which towns).
- **Hosting:** which host publishes `main` to inonda.homes (Wasmer, the Python host or a
  static host)? I'll check that the change goes live the way you expect.

## 4. Owner decisions (2026-11-18)
- Single price per job, plus a total when several jobs are chosen.
- Skip & site preparation: only on big jobs (renovations, kitchens, bathrooms, flooring).
- Quotation fee: restore the rule removed on 11 Nov 2026, word for word, in all 6 languages on all
  three sites: free within 10 km of the Strovolos office; jobs up to €1,000 cost €50 beyond 10 km and
  are charged in Limassol, Larnaca, Agia Napa and Paphos; over €1,000 the quote is included in the
  work; free under a maintenance contract.
- **Small one-off jobs of a few hours are now allowed.** The estimator will price them with a minimum
  charge, and the quote fee applies. This reverses the "no short jobs outside contracts" rule, so the
  "more than one day of work" sentence on all three sites has to change too.
