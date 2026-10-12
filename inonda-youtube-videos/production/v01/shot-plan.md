# V01 shot plan: Full Bathroom Renovation in Cyprus, Old to New

**This is a plan only.** Nothing has been generated and no credits have been spent.
Built from `inonda-youtube-videos/scripts/v01.md`, the Video 01 section, Realism standard and
re-tag rules in `inonda-youtube-videos/shot-list.md`, `inonda-youtube-videos/presenter/README.md`
and the `video-ai-generation` skill. The rules in `/CLAUDE.md` still apply: price first, the owner
approves each batch, **one test clip first (V01-01)**, no blind retries, never auto-open results.

Narration: `inonda-youtube-videos/audio/Inonda_Video01_narration_Emma.mp3` (7:10, female voice "Emma").
Every AI clip: 5 s, 16:9, 1080p, most photoreal tier (never fast, draft or turbo), no text in frame.

## Decisions made in this plan (please check them)

1. **No lip-sync in V01.** The narration is Emma's female voice, so the owner can't be shown
   speaking it. The owner appears **working or looking, not talking**, while Emma narrates. If the
   owner wants to speak on camera, that needs his own voice (a real recording or a consented
   voice clone) plus a lip-sync model. That is a separate batch with its own price.
2. **Owner shots take 2 steps.** (a) A still made with gemini-3-pro-image (ElevenLabs) from
   reference photos `presenter/2.jpg`–`5.jpg` (**never 1.jpg**). (b) The approved still is turned
   into video (image-to-video) on Krea or vidIQ. Owner prompts call him "the man from the
   reference photos". He always wears the same outfit: **plain dark-grey work t-shirt and work
   trousers**.
3. **One style-line change for owner shots.** The shared style says "fictional people only".
   That would contradict the owner, so in owner prompts it becomes "the only person is the man
   from the reference photos". Every other word of the style line and the realism guard is
   unchanged.
4. **Shots with two actions are split, and only the first is in the base plan** (Realism
   standard). V01-16 becomes V01-16a (owner, new clip) and V01-16b (a REUSE of V01-04, free). Second actions
   are listed under "Optional additions". They are not priced into the base total.
5. **Continuity (the same rooms in every shot).**
   - *Old bathroom:* small 1990s Cyprus apartment bathroom; beige 20×25 cm ceramic wall tiles
     with a brown border strip; grey terrazzo-look floor tiles; old white acrylic shower tray;
     frosted aluminium window.
   - *New bathroom:* light-grey large-format porcelain tiles (60×120 cm); walk-in glass shower;
     floating wood-effect vanity with white basin; mirror with soft warm backlight.
   - *Hands-only work shots:* forearms in the same dark-grey t-shirt sleeves, so they read as the
     same worker.

## Shared blocks (already copied into every prompt below)

**STYLE (B-roll, verbatim from shot-list.md):** Photorealistic, handheld documentary look,
natural Mediterranean daylight, warm slightly desaturated tones, shallow depth of field, typical
Cyprus home (white render, flat roofs, 1990s ceramic tiles, aluminium windows), fictional people
only, no on-screen text, no logos.

**STYLE (owner shots):** the same text, with "fictional people only" replaced by "the only
person is the man from the reference photos".

**REALISM GUARD (verbatim):** Shot on a real camera, natural imperfect lighting, realistic
physics and textures, real-world scale, subtle handheld movement. Avoid: CGI, 3D render, cartoon,
illustration, oversaturated colours, glowing light, slow-motion, warped hands, extra fingers,
melting objects, garbled text, watermarks.

## Overview

| ID | Tag | Under narration line (from v01.md) | Dur. | Lip-sync | Suggested model | On-screen label |
|---|---|---|---|---|---|---|
| **V01-01 (TEST CLIP)** | AI | "This bathroom in Cyprus had cracked tiles," | 5 s | No | Kling 3.0 Pro (Krea), alt. Veo 3.1 | "Illustration" |
| V01-02 | AI | "a damp ceiling," | 5 s | No | Kling 3.0 Pro | "Illustration" |
| V01-03 | AI | "and a shower that never drained properly. Sound familiar?" | 5 s | No | Veo 3.1 (water physics) | "Illustration" |
| V01-04 | AI | "In the next few minutes, we will show you how we take a bathroom from old to new, step by step." | 5 s | No | Kling 3.0 Pro, alt. Veo 3.1 | "Illustration – example" |
| V01-06 | AI (STOCK first) | "We are Inonda Ltd. We repair, renovate and maintain homes and apartments across Cyprus," | 5 s | No | Stock if found; else Veo 3.1 | none (generic street) |
| V01-05 | AI owner | "Inonda is a new company, but the technician in charge of every job has up to 22 years of hands-on repair experience," | 5 s | No | Still: gemini-3-pro-image (ElevenLabs) → video: Kling 3.0 Pro or Seedance 2.5 | "AI-generated" |
| V01-07 | AI | "We check the walls for damp." | 5 s | No | Kling 3.0 Pro | "Illustration" |
| V01-08 | AI | "In Cyprus, many older bathrooms have old galvanised or poorly joined pipework." | 5 s | No | Kling 3.0 Pro | "Illustration" |
| V01-09 | AI | "Doors are covered, floors are protected, and waste is removed daily." | 5 s | No | Kling 3.0 Pro | "Illustration" |
| V01-17 | GFX over REUSE V01-12 | "Quick pause. If this is useful, please subscribe." | ~20 s hold | No | Editor / Remotion | – |
| V01-10 | AI | "Then we test the pipes under pressure before closing anything up." | 5 s | No | Veo 3.1 (steady needle) | "Illustration" |
| V01-11 | AI | "we apply a waterproof membrane to the shower area and the floor," | 5 s | No | Veo 3.1 (liquid on roller) | "Illustration" |
| V01-12 | AI | "Flat surfaces, the correct adhesive for the tile type, even spacing," | 5 s | No | Kling 3.0 Pro | "Illustration" |
| V01-13 | AI | "In the corners, and wherever two surfaces meet, we use a flexible sealant, not grout." | 5 s | No | Veo 3.1 (sealant flow) | "Illustration" |
| V01-14 | AI (STOCK first) | "We check every tap," | 5 s | No | Veo 3.1 (water physics) | "Illustration" |
| V01-15 | AI owner | "Then we do a walkthrough with you and make a snag list," | 5 s | No | Still: gemini-3-pro-image → video: Kling 3.0 Pro or Seedance 2.5 | "AI-generated" |
| V01-16a | AI owner | "The only honest way to know is to have someone look at the room in person." | 5 s | No | Still: gemini-3-pro-image → video: Kling 3.0 Pro or Seedance 2.5 | "AI-generated" |
| V01-16b | REUSE V01-04 (+ V01-14) | "That is a bathroom from old to new." | 5 s | No | – (no new clip) | "Illustration – example" |
| V01-18 | GFX | "In the next video, we will turn an old Cyprus apartment into a modern rental" | ~20 s | No | Editor / Remotion | – |

Base batch: **16 new AI video clips (80 s)** + **3 owner stills**. If a free stock clip is found
for V01-06 (and V01-14), that drops to 15 (or 14) clips.

---

## Shot details and final prompts

### V01-01 – PROPOSED TEST CLIP
- **Tag:** AI · **Section:** Hook (0:00) · **Duration:** 5 s · **Lip-sync:** No
- **Line:** "This bathroom in Cyprus had cracked tiles,"
- **Model:** Kling 3.0 Pro (quality tier), text-to-video, on Krea. Alternative: Veo 3.1 on Krea or vidIQ.
- **Why this is the test:** no people, one slow move, a real material. It tests the look and
  realism cheaply before any owner shots are made.
- **Prompt:**
  > Close-up, 50mm lens, slow handheld push-in toward a cracked, chipped beige 20×25 cm ceramic
  > wall tile beside an old shower in a small 1990s Cyprus apartment bathroom; a diagonal crack
  > runs across the tile, one corner chipped to the grey adhesive, the grout lines around it
  > stained dark grey-brown, a dried soap streak and a little limescale at the tile edge, a brown
  > border strip tile just in frame; soft daylight from a frosted aluminium window to the left.
  > Photorealistic, handheld documentary look, natural Mediterranean daylight, warm slightly
  > desaturated tones, shallow depth of field, typical Cyprus home (white render, flat roofs, 1990s
  > ceramic tiles, aluminium windows), fictional people only, no on-screen text, no logos. Shot on
  > a real camera, natural imperfect lighting, realistic physics and textures, real-world scale,
  > subtle handheld movement. Avoid: CGI, 3D render, cartoon, illustration, oversaturated colours,
  > glowing light, slow-motion, warped hands, extra fingers, melting objects, garbled text,
  > watermarks.
- **Reject if:** the crack moves or spreads, the tiles warp or bend, the grout looks painted
  on, the surface looks plastic or glossy.

### V01-02
- **Tag:** AI · **Hook** · 5 s · **Lip-sync:** No · **Model:** Kling 3.0 Pro (camera tilt)
- **Line:** "a damp ceiling,"
- **Prompt:**
  > Medium shot, 35mm lens, slow handheld tilt up from the top row of beige wall tiles to the
  > ceiling corner of a small old Cyprus bathroom; a brown tide-marked damp stain spreads from
  > the corner, white paint peeling in curled flakes, clusters of small black mould spots along
  > the edge, a dusty extractor grille at the frame edge; dim overcast daylight from a frosted
  > aluminium window. Photorealistic, handheld documentary look, natural Mediterranean daylight,
  > warm slightly desaturated tones, shallow depth of field, typical Cyprus home (white render,
  > flat roofs, 1990s ceramic tiles, aluminium windows), fictional people only, no on-screen text,
  > no logos. Shot on a real camera, natural imperfect lighting, realistic physics and textures,
  > real-world scale, subtle handheld movement. Avoid: CGI, 3D render, cartoon, illustration,
  > oversaturated colours, glowing light, slow-motion, warped hands, extra fingers, melting
  > objects, garbled text, watermarks.

### V01-03
- **Tag:** AI · **Hook** · 5 s · **Lip-sync:** No · **Model:** Veo 3.1 (water physics)
- **Line:** "and a shower that never drained properly. Sound familiar?"
- **Prompt:**
  > Overhead shot, 35mm lens, slight handheld drift, looking down into an old white acrylic
  > shower tray, yellowed and scratched, with a shallow puddle of slightly murky soapy water
  > draining very slowly around a corroded round chrome drain grate with rust at its rim; a few
  > hairs and limescale rings on the tray, a dark mouldy silicone line where the tray meets
  > beige wall tiles; flat daylight from a small window. Photorealistic, handheld documentary
  > look, natural Mediterranean daylight, warm slightly desaturated tones, shallow depth of field,
  > typical Cyprus home (white render, flat roofs, 1990s ceramic tiles, aluminium windows),
  > fictional people only, no on-screen text, no logos. Shot on a real camera, natural imperfect
  > lighting, realistic physics and textures, real-world scale, subtle handheld movement. Avoid:
  > CGI, 3D render, cartoon, illustration, oversaturated colours, glowing light, slow-motion,
  > warped hands, extra fingers, melting objects, garbled text, watermarks.
- **Reject if:** the water flows uphill or sideways, or moves like gel.

### V01-04
- **Tag:** AI (example result) · **Hook** · 5 s · **Lip-sync:** No · **Model:** Kling 3.0 Pro, alt. Veo 3.1
- **Line:** "In the next few minutes, we will show you how we take a bathroom from old to new, step by step."
- **Label:** "Illustration – example". It must **not** be presented as the real result of the
  bathroom in V01-01 to V01-03 (see open question 1).
- **Prompt:**
  > Wide shot, 24mm lens, slow handheld push-in through the doorway into a small, freshly
  > renovated Cyprus apartment bathroom: light-grey large-format 60×120 cm porcelain tiles on the
  > walls and floor with thin even grout lines, a walk-in shower with a single clear glass panel
  > and a matt black floor drain channel, a floating wood-effect vanity with a white basin and a
  > chrome tap, a mirror with soft warm backlight, a folded white towel and a slightly
  > crumpled bath mat; daylight from a frosted aluminium window, a faint water spot on the glass.
  > Photorealistic, handheld documentary look, natural Mediterranean daylight, warm slightly
  > desaturated tones, shallow depth of field, typical Cyprus home (white render, flat roofs, 1990s
  > ceramic tiles, aluminium windows), fictional people only, no on-screen text, no logos. Shot on
  > a real camera, natural imperfect lighting, realistic physics and textures, real-world scale,
  > subtle handheld movement. Avoid: CGI, 3D render, cartoon, illustration, oversaturated colours,
  > glowing light, slow-motion, warped hands, extra fingers, melting objects, garbled text,
  > watermarks.
- **Reject if:** it looks like a showroom or a 3D render, the mirror light glows, or the tiles bend.

### V01-06
- **Tag:** STOCK first, AI fallback · **Intro** (0:25) · 5 s · **Lip-sync:** No · **Model:** Veo 3.1 if no stock
- **Line:** "We are Inonda Ltd. We repair, renovate and maintain homes and apartments across Cyprus,"
- **Stock:** a generic Cyprus or Mediterranean apartment street in morning sun very likely
  exists for free on Pexels or Pixabay. Researcher check pending; stock hosts are currently
  blocked in this environment's network settings (see the open items in `memory/requests.md`).
- **Prompt (only if no stock clip is found):**
  > Wide establishing shot, 35mm lens, slow handheld pan right along a quiet residential street
  > of three- and four-storey white-rendered Cyprus apartment blocks in low morning sun;
  > balconies with aluminium railings and rolled shutters, solar water heaters and tanks on the
  > flat roofs, a few parked small cars, a palm tree, faded paint and rust streaks under a
  > balcony, long soft shadows. Photorealistic, handheld documentary look, natural Mediterranean
  > daylight, warm slightly desaturated tones, shallow depth of field, typical Cyprus home (white
  > render, flat roofs, 1990s ceramic tiles, aluminium windows), fictional people only, no
  > on-screen text, no logos. Shot on a real camera, natural imperfect lighting, realistic physics
  > and textures, real-world scale, subtle handheld movement. Avoid: CGI, 3D render, cartoon,
  > illustration, oversaturated colours, glowing light, slow-motion, warped hands, extra fingers,
  > melting objects, garbled text, watermarks.
- **Reject if:** shop signs or number plates are legible or garbled.

### V01-05 – OWNER
- **Tag:** AI likeness of the owner (consent 2026-10-12) · **Intro** · 5 s · **Lip-sync:** No
- **Line:** "Inonda is a new company, but the technician in charge of every job has up to 22 years of hands-on repair experience,"
- **Model:** Step A still: gemini-3-pro-image via ElevenLabs with `presenter/2.jpg`–`5.jpg` as
  references. Step B: image-to-video with Kling 3.0 Pro or Seedance 2.5 (reference input) on Krea or vidIQ.
- **Label:** "AI-generated" (the owner's AI likeness).
- **Step A, still prompt:**
  > Medium-wide shot, 35mm lens, eye level: the man from the reference photos, same face, hair
  > and build as in the references, wearing a plain dark-grey work t-shirt and work trousers,
  > stands in the doorway of a small old Cyprus apartment bathroom, one hand resting on the door
  > frame, looking calmly into the room with a natural relaxed expression; behind him beige
  > 1990s wall tiles with a brown border strip, an old white shower tray, a damp stain in the
  > ceiling corner; soft daylight from a frosted aluminium window, a little dust on the t-shirt.
  > Photorealistic, handheld documentary look, natural Mediterranean daylight, warm slightly
  > desaturated tones, shallow depth of field, typical Cyprus home (white render, flat roofs, 1990s
  > ceramic tiles, aluminium windows), the only person is the man from the reference photos, no
  > on-screen text, no logos. Shot on a real camera, natural imperfect lighting, realistic physics
  > and textures, real-world scale, subtle handheld movement. Avoid: CGI, 3D render, cartoon,
  > illustration, oversaturated colours, glowing light, slow-motion, warped hands, extra fingers,
  > melting objects, garbled text, watermarks.
- **Step B, motion prompt (image-to-video):**
  > Slow handheld push-in toward the man from the reference photos as he stands in the bathroom
  > doorway and turns his head slightly to look at the damp ceiling corner, then back into the
  > room; he does not speak; his face, plain dark-grey work t-shirt and work trousers stay
  > exactly as in the image; the tiles and door frame do not move. [STYLE (owner shots) + REALISM GUARD, as in Step A]
- **Reject if:** the face drifts from the owner's, the skin looks waxy or doll-like, the eyes
  look dead, the mouth moves as if talking, or the fingers on the door frame are warped.

### V01-07
- **Tag:** AI · **Survey** (1:05) · 5 s · **Lip-sync:** No · **Model:** Kling 3.0 Pro
- **Line:** "We check the walls for damp."
- **Prompt:**
  > Close-up, 50mm lens, slow handheld push-in: a worker's hand, forearm in a plain dark-grey
  > t-shirt sleeve, presses a small grey handheld pin-type moisture meter against the lower part
  > of a painted bathroom wall just above beige tiles, where the paint is stained and slightly
  > bubbled; the meter's small display glows dimly, its digits out of focus; an old radiator
  > pipe and a scuffed skirting at the frame edge; window daylight from the right.
  > Photorealistic, handheld documentary look, natural Mediterranean daylight, warm slightly
  > desaturated tones, shallow depth of field, typical Cyprus home (white render, flat roofs, 1990s
  > ceramic tiles, aluminium windows), fictional people only, no on-screen text, no logos. Shot on
  > a real camera, natural imperfect lighting, realistic physics and textures, real-world scale,
  > subtle handheld movement. Avoid: CGI, 3D render, cartoon, illustration, oversaturated colours,
  > glowing light, slow-motion, warped hands, extra fingers, melting objects, garbled text,
  > watermarks.
- **Note:** the shot list says "display reading high". The digits are kept out of focus on
  purpose, because models garble numbers. Add the "high reading" in the edit as GFX if needed.

### V01-08
- **Tag:** AI · **Survey** · 5 s · **Lip-sync:** No · **Model:** Kling 3.0 Pro
- **Line:** "In Cyprus, many older bathrooms have old galvanised or poorly joined pipework."
- **Change from shot-list.md:** the survey happens "before any demolition", so the pipe is shown
  under the old basin instead of in an opened wall.
- **Prompt:**
  > Close-up, 35mm lens, slow handheld move along a torch beam in a dim space under an old white
  > pedestal basin in a Cyprus bathroom, tracing old grey galvanised steel water pipes coming out
  > of the beige-tiled wall; a rusty threaded joint wrapped in old hemp and paint, an orange rust
  > stain dripping down the tile below it, a dusty chrome isolation valve; the only light is the
  > torch beam and faint daylight from behind. Photorealistic, handheld documentary look,
  > natural Mediterranean daylight, warm slightly desaturated tones, shallow depth of field,
  > typical Cyprus home (white render, flat roofs, 1990s ceramic tiles, aluminium windows),
  > fictional people only, no on-screen text, no logos. Shot on a real camera, natural imperfect
  > lighting, realistic physics and textures, real-world scale, subtle handheld movement. Avoid:
  > CGI, 3D render, cartoon, illustration, oversaturated colours, glowing light, slow-motion,
  > warped hands, extra fingers, melting objects, garbled text, watermarks.

### V01-09
- **Tag:** AI · **Strip-out** (2:00) · 5 s · **Lip-sync:** No · **Model:** Kling 3.0 Pro
- **Line:** "Doors are covered, floors are protected, and waste is removed daily."
- **Note:** this is only the first action of the shot-list entry (laying floor sheeting). The
  chisel lifting tiles becomes optional V01-09b, which is recommended.
- **Prompt:**
  > Low medium shot, 35mm lens, slow handheld pull-back along an apartment hallway with a
  > speckled marble-look floor: two hands, forearms in plain dark-grey t-shirt sleeves, unroll
  > a grey-white protective floor sheet toward the open bathroom door, pressing it flat; a roll
  > of tape, a bucket of tools and a dust sheet over a doorway at the frame edge, a faint film
  > of tile dust in the window light. Photorealistic, handheld documentary look, natural
  > Mediterranean daylight, warm slightly desaturated tones, shallow depth of field, typical Cyprus
  > home (white render, flat roofs, 1990s ceramic tiles, aluminium windows), fictional people
  > only, no on-screen text, no logos. Shot on a real camera, natural imperfect lighting,
  > realistic physics and textures, real-world scale, subtle handheld movement. Avoid: CGI, 3D
  > render, cartoon, illustration, oversaturated colours, glowing light, slow-motion, warped
  > hands, extra fingers, melting objects, garbled text, watermarks.
- **Reject if:** printing appears on the sheet or tape, or the sheet melts into the floor.

### V01-17
- **Tag:** GFX over REUSE V01-12 · **Mid CTA** (2:45–3:05) · ~20 s · **Lip-sync:** No · **Model:** editor or Remotion (free)
- **Line:** "Quick pause. If this is useful, please subscribe. In two weeks we are covering how to turn an old Cyprus apartment into a modern rental."
- **Note:** a subscribe lower third with "Next up: old apartment to modern rental", over V01-12
  slowed to a hold or looped. No new clip.

### V01-10
- **Tag:** AI · **Plumbing** (3:05) · 5 s · **Lip-sync:** No · **Model:** Veo 3.1
- **Line:** "Then we test the pipes under pressure before closing anything up."
- **Prompt:**
  > Close-up, 50mm lens, slow handheld push-in on an unbranded round analogue pressure-test gauge
  > screwed onto a brass fitting at the end of new white multilayer PEX supply pipes, clipped to
  > a bare grey rendered bathroom wall with an open chase cut into it; the gauge needle holds
  > perfectly steady, its dial markings soft and out of focus; plaster dust on the pipe clips,
  > a cut offcut of pipe on the floor at the frame edge, work-light and window daylight mixed.
  > Photorealistic, handheld documentary look, natural Mediterranean daylight, warm slightly
  > desaturated tones, shallow depth of field, typical Cyprus home (white render, flat roofs, 1990s
  > ceramic tiles, aluminium windows), fictional people only, no on-screen text, no logos. Shot on
  > a real camera, natural imperfect lighting, realistic physics and textures, real-world scale,
  > subtle handheld movement. Avoid: CGI, 3D render, cartoon, illustration, oversaturated colours,
  > glowing light, slow-motion, warped hands, extra fingers, melting objects, garbled text,
  > watermarks.
- **Note:** the shot list allowed copper or PEX. Only PEX is shown, so the clip has one
  material.
- **Reject if:** the needle swings or the numbers are garbled and readable.

### V01-11
- **Tag:** AI · **Waterproofing** (3:45) · 5 s · **Lip-sync:** No · **Model:** Veo 3.1
- **Line:** "we apply a waterproof membrane to the shower area and the floor,"
- **Note:** this is the first action only. The corner tape becomes optional V01-11b, which is
  recommended because the narration says it.
- **Prompt:**
  > Medium close-up, 35mm lens, slow handheld push-in: a worker's hand, forearm in a plain
  > dark-grey t-shirt sleeve, pushes a short-pile paint roller across a levelled cement screed
  > shower floor, laying an even coat of grey liquid waterproof membrane that leaves a slightly
  > wet sheen; part of the floor is still bare light-grey screed; the walls are bare rendered
  > plaster with no tiles yet, an open tub of membrane and a stained roller tray in the corner;
  > window daylight. Photorealistic, handheld documentary look, natural Mediterranean daylight,
  > warm slightly desaturated tones, shallow depth of field, typical Cyprus home (white render, flat
  > roofs, 1990s ceramic tiles, aluminium windows), fictional people only, no on-screen text, no
  > logos. Shot on a real camera, natural imperfect lighting, realistic physics and textures,
  > real-world scale, subtle handheld movement. Avoid: CGI, 3D render, cartoon, illustration,
  > oversaturated colours, glowing light, slow-motion, warped hands, extra fingers, melting
  > objects, garbled text, watermarks.
- **Reject if:** the membrane flows like gel or has a glossy CGI shine, or there are labels on
  the tub.

### V01-12
- **Tag:** AI · **Tiling** (4:35) · 5 s · **Lip-sync:** No · **Model:** Kling 3.0 Pro
- **Line:** "Flat surfaces, the correct adhesive for the tile type, even spacing,"
- **Note:** this is the first action only (combing adhesive). Pressing the tile and the spirit
  level are in optional V01-12b, which shows the owner tiling. This clip is also the background
  for V01-17.
- **Prompt:**
  > Close-up, 50mm lens, slow handheld push-in: a worker's hand, forearm in a plain dark-grey
  > t-shirt sleeve, drags a steel notched trowel at a steady angle through grey cement tile
  > adhesive on a flat bare bathroom wall, leaving clean parallel ridges; at the frame edge a
  > stack of light-grey large-format porcelain tiles, a bucket with adhesive on its rim and a
  > few plastic tile spacers; adhesive smears on the knuckles, window daylight raking across the
  > ridges. Photorealistic, handheld documentary look, natural Mediterranean daylight, warm
  > slightly desaturated tones, shallow depth of field, typical Cyprus home (white render, flat
  > roofs, 1990s ceramic tiles, aluminium windows), fictional people only, no on-screen text, no
  > logos. Shot on a real camera, natural imperfect lighting, realistic physics and textures,
  > real-world scale, subtle handheld movement. Avoid: CGI, 3D render, cartoon, illustration,
  > oversaturated colours, glowing light, slow-motion, warped hands, extra fingers, melting
  > objects, garbled text, watermarks.
- **Reject if:** the trowel merges into the hand, or the ridges don't follow the trowel.

### V01-13
- **Tag:** AI · **Tiling** · 5 s · **Lip-sync:** No · **Model:** Veo 3.1
- **Line:** "In the corners, and wherever two surfaces meet, we use a flexible sealant, not grout."
- **Prompt:**
  > Extreme close-up, 50mm lens, slow handheld follow along a vertical inside corner where two
  > walls of new light-grey large-format porcelain tiles meet in a shower; the nozzle of a
  > sealant gun lays a smooth, even bead of white flexible silicone into the corner joint, the
  > bead slightly glossy, the grey grout lines on either side already set; blue masking tape
  > along both edges, a tiny smear on the tape; soft window daylight. Photorealistic, handheld
  > documentary look, natural Mediterranean daylight, warm slightly desaturated tones, shallow
  > depth of field, typical Cyprus home (white render, flat roofs, 1990s ceramic tiles, aluminium
  > windows), fictional people only, no on-screen text, no logos. Shot on a real camera, natural
  > imperfect lighting, realistic physics and textures, real-world scale, subtle handheld
  > movement. Avoid: CGI, 3D render, cartoon, illustration, oversaturated colours, glowing light,
  > slow-motion, warped hands, extra fingers, melting objects, garbled text, watermarks.
- **Reject if:** the sealant flows by itself, comes out ahead of the nozzle, or the corner warps.

### V01-14
- **Tag:** AI (STOCK first) · **Fixtures** (5:15) · 5 s · **Lip-sync:** No · **Model:** Veo 3.1
- **Line:** "We check every tap,"
- **Note:** this is the first action only. "Shower running onto clean tiles" is optional
  V01-14b. Stock tap clips are common, but this one has to match the new bathroom (white basin,
  wood-effect vanity), so AI is likely needed. Researcher check pending.
- **Prompt:**
  > Close-up, 50mm lens, slow handheld push-in: a hand, forearm in a plain dark-grey t-shirt
  > sleeve, lifts the lever of a new chrome single-lever basin tap and clear water starts to
  > run into a white ceramic basin on a floating wood-effect vanity; light-grey large-format
  > porcelain tiles behind, a few water droplets on the chrome, a fingerprint on the tap body;
  > soft daylight and a warm mirror light from above. Photorealistic, handheld documentary look,
  > natural Mediterranean daylight, warm slightly desaturated tones, shallow depth of field,
  > typical Cyprus home (white render, flat roofs, 1990s ceramic tiles, aluminium windows),
  > fictional people only, no on-screen text, no logos. Shot on a real camera, natural imperfect
  > lighting, realistic physics and textures, real-world scale, subtle handheld movement. Avoid:
  > CGI, 3D render, cartoon, illustration, oversaturated colours, glowing light, slow-motion,
  > warped hands, extra fingers, melting objects, garbled text, watermarks.
- **Reject if:** the water bends or looks like glass, the water slows into slow-motion, or the
  fingers fuse with the lever.

### V01-15 – OWNER
- **Tag:** AI likeness of the owner · **Fixtures** · 5 s · **Lip-sync:** No
- **Line:** "Then we do a walkthrough with you and make a snag list,"
- **Model:** Step A still: gemini-3-pro-image (ElevenLabs, refs 2–5). Step B: Kling 3.0 Pro or Seedance 2.5 image-to-video.
- **Label:** "AI-generated". The client stays off-frame, so there is no second AI person and the
  shot only implies "with you".
- **Step A, still prompt:**
  > Medium shot, 35mm lens, eye level: the man from the reference photos, same face, hair and
  > build as in the references, wearing a plain dark-grey work t-shirt and work trousers, stands
  > inside a freshly renovated small Cyprus bathroom holding a clipboard low at his side, the
  > paper turned away from camera, looking closely along the edge of a clear glass shower panel
  > with a focused, natural expression; light-grey large-format porcelain tiles, a floating
  > wood-effect vanity with white basin and chrome tap, a mirror with soft warm backlight;
  > daylight from a frosted aluminium window, a dust sheet folded in the doorway.
  > Photorealistic, handheld documentary look, natural Mediterranean daylight, warm slightly
  > desaturated tones, shallow depth of field, typical Cyprus home (white render, flat roofs, 1990s
  > ceramic tiles, aluminium windows), the only person is the man from the reference photos, no
  > on-screen text, no logos. Shot on a real camera, natural imperfect lighting, realistic physics
  > and textures, real-world scale, subtle handheld movement. Avoid: CGI, 3D render, cartoon,
  > illustration, oversaturated colours, glowing light, slow-motion, warped hands, extra fingers,
  > melting objects, garbled text, watermarks.
- **Step B, motion prompt:**
  > Slow handheld pan following the man from the reference photos as he walks one slow step
  > along the glass shower panel, eyes tracing its silicone edge, the clipboard held at his
  > side; he does not speak; his face, plain dark-grey work t-shirt and work trousers stay
  > exactly as in the image; the tiles, glass and vanity do not move. [STYLE (owner shots) + REALISM GUARD]
- **Reject if:** text is legible on the clipboard, his reflection in the glass or mirror is
  wrong or doubled, or there is any likeness drift.

### V01-16a – OWNER
- **Tag:** AI likeness of the owner · **Cost and time** (5:50) · 5 s · **Lip-sync:** No
- **Line:** "The only honest way to know is to have someone look at the room in person."
- **Change from shot-list.md:** the shot list has "presenter to camera". Without lip-sync, a silent
  look to camera would feel odd, so the owner is shown doing exactly what the line says:
  looking at the room in person. It uses the old bathroom for continuity.
- **Model:** Step A still: gemini-3-pro-image (ElevenLabs, refs 2–5). Step B: Kling 3.0 Pro or Seedance 2.5.
- **Label:** "AI-generated".
- **Step A, still prompt:**
  > Medium shot, 35mm lens, eye level: the man from the reference photos, same face, hair and
  > build as in the references, wearing a plain dark-grey work t-shirt and work trousers, holds
  > a yellow tape measure stretched across the width of a beige-tiled wall in a small old
  > Cyprus apartment bathroom, looking at the tape with a calm, attentive expression; the old
  > white shower tray, the brown border strip tiles and the damp stain in the ceiling corner
  > visible; soft daylight from a frosted aluminium window. Photorealistic, handheld documentary
  > look, natural Mediterranean daylight, warm slightly desaturated tones, shallow depth of field,
  > typical Cyprus home (white render, flat roofs, 1990s ceramic tiles, aluminium windows), the
  > only person is the man from the reference photos, no on-screen text, no logos. Shot on a real
  > camera, natural imperfect lighting, realistic physics and textures, real-world scale, subtle
  > handheld movement. Avoid: CGI, 3D render, cartoon, illustration, oversaturated colours,
  > glowing light, slow-motion, warped hands, extra fingers, melting objects, garbled text,
  > watermarks.
- **Step B, motion prompt:**
  > Static-feeling handheld shot with a slight drift: the man from the reference photos lets the
  > tape measure retract slowly into its case and glances up at the ceiling corner; he does not
  > speak; his face, plain dark-grey work t-shirt and work trousers stay exactly as in the
  > image; the wall and tiles do not move. [STYLE (owner shots) + REALISM GUARD]
- **Reject if:** the tape bends or melts, the tape has readable or garbled numbers, or there
  is any likeness drift.

### V01-16b
- **Tag:** REUSE V01-04 (plus V01-14 for the "several angles" montage) · **Cost and End** (6:15 and 6:35) · 5 s · **Lip-sync:** No
- **Line:** "That is a bathroom from old to new."
- **Label:** "Illustration – example". No new clip, so no cost.

### V01-18
- **Tag:** GFX · **End** (6:35–7:10) · ~20 s · **Lip-sync:** No · **Model:** editor or Remotion
- **Line:** "In the next video, we will turn an old Cyprus apartment into a modern rental, with a full walkthrough."
- **Note:** end screen with the next-video card ("Old apartment to modern rental") and the
  WhatsApp card. The `[ADD PHONE/WHATSAPP]` placeholder must be filled first.

---

## Optional additions (NOT in the base price, each needs approval)

V01 has 7:10 of narration but only about 80 s of new AI footage, so the editor will rely on long
holds, reuse and GFX text cards. These additions match lines that currently have no picture.
The first three are recommended.

| ID | Line | Shot | Model |
|---|---|---|---|
| **V01-09b** (rec.) | "Out come the old tiles, the sanitaryware, and any rotten flooring." | Close-up: the worker's hand (dark-grey sleeve) drives a wide steel bolster chisel behind an old beige wall tile, which pops off with a puff of dust in the window light. | Kling 3.0 Pro |
| **V01-11b** (rec.) | "and seal the corners and joints with tape." | Close-up: a brush presses grey reinforcing tape into the wet membrane in the wall-to-floor corner of a shower. | Veo 3.1 |
| **V01-12b** (rec., owner working) | "Large format tiles look modern, but they need a very flat surface." | Owner (still + I2V): the man from the reference photos, in a plain dark-grey work t-shirt and work trousers, kneels and lays a spirit level on a freshly set light-grey large-format tile and checks the bubble. | gemini-3-pro-image → Kling 3.0 Pro / Seedance 2.5 |
| V01-08b | "A good contractor tells you straight away and shows you photos," | Hand holds a phone up to photograph a damp, rotten patch behind removed tiles (screen not visible). | Kling 3.0 Pro |
| V01-09c | "and waste is removed daily." | Tied rubble bags lined up on floor sheeting by the apartment door. | Kling 3.0 Pro |
| V01-10b | "Sockets, lights and extractor fans must be suitable for wet areas," | Hands fit a white extractor fan into a round hole in a bare bathroom wall. | Kling 3.0 Pro |
| V01-11c | "Then we let it cure fully," | Close-up push-in on a cured, matt grey membrane on a shower floor and its corners. | Kling 3.0 Pro |
| V01-14b | "and run the shower for a while to confirm there are no drips and the drain keeps up." | Rain shower running onto light-grey tiles, water flowing into a linear floor drain. | Veo 3.1 |
| V01-08c | "Then we agree the layout with you." | GFX: a simple layout sketch (free) instead of an AI clip. | Editor |

Full prompts for these are written on request. They use the same formula, style line and
guard as above.

---

## Cost table

**Free estimate available only for ElevenLabs stills.** Krea and vidIQ give no estimate before
generating, so their totals are formulas, not quotes.

### Base batch

| Item | Count | Unit | Rate | Rate source | Total |
|---|---|---|---|---|---|
| Owner stills, gemini-3-pro-image via ElevenLabs (V01-05, V01-15, V01-16a) | 3 images | per image | ≈ $0.12 (1,218 credits) | ElevenLabs free estimate | **≈ $0.36 (3,654 credits)** |
| AI video clips, ElevenLabs | – | – | – | **Not available.** Video needs a paid ElevenLabs plan on the owner's account | – |
| AI video clips (13 B-roll incl. V01-06 + 3 owner I2V) on **Krea** (Kling 3.0 Pro / Veo 3.1 / Seedance 2.5) | 16 clips × 5 s = 80 s | per second, model-dependent | unknown | No free estimate; check the Krea UI or price page before approval | **unknown** |
| Same 16 clips on **vidIQ** | 80 s | seconds × model rate × 20 credits | model rate unpublished | Owner's account notes, no free estimate | **80 × rate × 20 = 1,600 × rate credits**. Balance 80 (refills to 150 on 2026-11-06), which does not cover the batch. One 5 s clip = 100 × rate credits, so it fits the balance only if the rate is 0.8 or less |
| Lip-sync | 0 | – | – | – | $0 (none planned, narration is Emma) |
| GFX (V01-17, V01-18) and REUSE (V01-16b) | 3 | – | free | Editor / Remotion | $0 |
| Stock (V01-06, maybe V01-14) | 0–2 | – | free (Pexels / Pixabay) | Free licence; host access is currently blocked | $0, would remove 1–2 AI clips |

**Caution on the still price.** The ElevenLabs connector generates several variations per call by
default. Confirm on the free estimate whether 1,218 credits is per image or per call at the
default variation count before approving. If it is per image, a call that returns 4
variations costs about $0.48.

### Test clip first (recommended)

```
Batch: V01 test clip
Clips: 1 × 5 s, 16:9, 1080p, V01-01 (cracked tile push-in), text-to-video,
       Kling 3.0 Pro on Krea (alternative: Veo 3.1)
Rate:  unknown (no free estimate on Krea; on vidIQ = 5 × model rate × 20 credits,
       rate unpublished, balance 80)
Total: unknown until the Krea / vidIQ price is shown in the service. Nothing is spent until
       the owner approves this one clip.
```

Suggested order (each step needs the owner's yes):
1. V01-01 test clip, checked against the reject list.
2. One owner still (V01-05, ≈ $0.12) to check the likeness. The reference photos are low-res
   (959×512) and backlit, so likeness is the biggest risk.
3. The rest of the B-roll.
4. The owner image-to-video clips.

## Open questions for the owner

1. **The hook says "This bathroom in Cyprus had…"** and V01-04 shows "the same bathroom
   renovated". With AI footage that would be an invented real before/after (not allowed).
   Options: (a) reword to "A bathroom like this…" and label both as "Illustration – example",
   or (b) use real photos of a real Inonda job.
2. **Presenter voice.** Is the owner OK appearing silent while Emma narrates? If not, speaking
   shots need his own voice and a lip-sync model, priced separately.
3. **Which video service:** Krea (price unknown), vidIQ (80 credits, likely too little), or an
   ElevenLabs paid plan?
4. Should the recommended optional shots V01-09b, V01-11b and V01-12b be added to the batch?
5. Placeholders still in the script: `[ADD REAL PRICE]`, `[ADD REAL DURATION]` and
   `[ADD PHONE/WHATSAPP]` (on-screen text in the Cost section and on V01-18).
