# Step 1: Service inventory, inonda.org vs inonda.homes

Date: 2026-11-18. Sources: `constapo/inonda-cy-website` (inonda.org) and
`constapo/inonda-service-estimator` (inonda.homes), read from `main`. I checked the live
inonda.org services page against the repo and it matches: the same 17 services and the same
estimator links.

Full lists in all 6 languages (EN, EL, RU, UK, HE, RO):
- `inonda-org-services-6-languages.csv`: 17 services, 68 groups, 270 sub-services and 10 carpentry categories.
- `inonda-homes-estimator-jobs-6-languages.csv`: 15 jobs and 50 types of work.

**Languages.** Both sites have the same structure in all 6 languages: every service, group
and sub-service exists everywhere, and no estimator label falls back to English. The only
difference is on inonda.org: UK and HE have no "areas" or "guides" pages. That is by design
(local content only exists for EL, EN, RU and RO).

## A. How the services match up

| inonda.org service | Group | In estimator? | What the estimator prices |
|---|---|---|---|
| Maintenance plans | maintenance | No (contract only) ✔ | none |
| Air conditioning | maintenance | **No** | none, see B1 |
| Roof waterproofing & damp | maintenance | Yes: roofing | Liquid membrane, torch-on membrane, roof tile repair |
| Plumbing | repairs | Yes: plumbing | New water/drain point, water heater replacement |
| Electrical works | repairs | Yes: electrical | New socket/light point, distribution board |
| Property repairs & handyman | repairs | No (contract only) ✔ | none |
| Urgent damage & repairs | repairs | No (contract only) ✔ | none |
| Kitchen renovation | transformation | Yes: kitchen | Standard units, premium units, worktop |
| Bathroom renovation | transformation | Yes: bathroom | Refresh, full renovation, bath to walk-in |
| Complete home renovation | transformation | Yes: renovation | Cosmetic, partial, full |
| Painting, plaster & gypsum | transformation | Yes: painting + gypsum | Interior, exterior; 6 gypsum types + plastering |
| Flooring & tiling | transformation | Yes: flooring | Floor tiles, laminate/vinyl, tile removal |
| Doors, windows & carpentry | transformation | Yes: doors + carpentry | Interior door, wardrobe; carpentry is price on request |
| Outdoor works | transformation | Yes: outdoor + welding | Paving, decking, fencing; 7 metalwork types |
| Aluminium works | transformation | Yes: aluminium | Windows, sliding, shutters, enclosure, pergola |
| HPL cladding | transformation | Yes: hpl | Interior, ventilated facade, compact |
| Decorative panels | transformation | Yes: decor | PVC marble, WPC/fluted, acoustic |
| Carpentry (10 categories) | — | Yes, unpriced | "Price on request" list, no automatic price |

## B. Gaps between the two sites

**B1. On inonda.org but not priceable in the estimator** (one-off jobs, so the rules allow them):
- **Air conditioning: the whole service is missing.** Supply and install a split, multi-split,
  ducted or cassette unit; remove or relocate a unit; upgrade to a heat pump. (Servicing and
  repair are short jobs, so contract only.)
- Roof: thermal insulation boards, external wall insulation (ETICS), rising-damp and mould
  treatment, balcony re-tiling with waterproofing, shower floor waterproofing, cool-roof coating.
- Plumbing: supplying and fitting sanitaryware (WC, basin, shower, bath), solar water heater
  replacement, pressure pump or booster set, water softener or filter, full re-pipe for a renovation.
- Electrical: full or partial rewiring, EV charger, three-phase upgrade, dedicated AC/oven line,
  outdoor or security lighting, LED/strip lighting.
- Flooring: wall tiles, engineered wood, microcement, screed or self-levelling, skirting, stair cladding.
- Painting: metal railings, gates and shutters; decorative and microcement finishes.
- Doors & windows: security or entrance doors, sliding pocket doors, TV walls and storage units.
  (Most of these could also come under the unpriced carpentry list.)
- Outdoor: wooden or steel pergolas, awnings and shade sails, car ports, automatic gate motors,
  driveways, garden walls and steps, drip irrigation, outdoor kitchen or BBQ.
- Aluminium: glass and aluminium balustrades, frameless glass curtains, fly screens, louvred
  shutters, motorised shutters.
- HPL: removing old cladding; compact window sills and worktops.

**B2. In the estimator but not offered on inonda.org:**
- **Terrace decking**: priced in the estimator but not mentioned on the outdoor-works page.
- **Roof tile repair**: priced, but the roof page only covers flat roofs and terraces.
- **Welding & metalwork**: window security grilles and steel canopies/frames are priced but not
  on inonda.org. (Railings, fences, gates and steel pergolas are on the outdoor-works page.)
- **Skip & site preparation**: an automatic extra line on every estimate. It isn't a service and
  needs no change.

## C. Conflicts with the business rules found during the inventory (inonda.org)

These are texts on inonda.org, in all 6 languages. They are logged now and their fixes will
go into the step 5 changes.
1. **The urgent-repairs page is open to everyone**, not just contract clients ("Out-of-hours
   and urgent call-outs may carry a call-out fee"). The rule is no urgent repairs outside a
   maintenance contract.
2. **"Client supplies materials" wording:** the handyman FAQ says "Specific items … can be
   supplied by us or by you", and the AC FAQ says "or install one you've already bought".
   The rule is that Inonda always supplies the materials.
3. **Short jobs offered on one-off service pages:** AC servicing, cleaning and repairs;
   plumbing "From a dripping tap…", leaking taps and blocked sinks; electrical faults such as
   tripping breakers and dead sockets; window and shutter repairs. The rule allows short jobs
   only under a maintenance contract.

## D. Decisions needed before pricing (step 3)
- **Add AC installation to the estimator as a new job?** I recommend yes: it's a big one-off
  job that's missing.
- **For the B1 gaps:** add the most-requested ones as new types of work (my suggestion:
  sanitaryware, rewiring, EV charger, solar heater, wall tiles, engineered wood, insulation,
  glass balustrades, gate motor), or leave them as "price on request".
- **For B2:** add decking, roof tiles, grilles and canopies to the inonda.org pages, or remove
  them from the estimator.
- **For C3:** reword those items as contract-only, or remove them from the one-off pages.
