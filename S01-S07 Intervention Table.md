# PolyCycle Port — Full-Park Symbiosis Opportunities (S-01–S-07)

**Source:** `linnyr/Full-Park-Network-With-Intervention.lnr` (Linny-R model, author: Salih Ali)
**Context:** Chapter 6.1.8 ("Wider System Context") and Chapter 7 of the PolyCycle Port final
report reference this S-01–S-07 opportunity set and use several of its values directly in
calculations. This file documents the full set behind those references, straight from the
underlying Linny-R model — supplementary material alongside the submitted report, which is
otherwise unchanged.

## The seven interventions

| Label | Intervention | Value | Status in the Linny-R model |
|---|---|---|---|
| S-01 | High-Temperature Heat Pump (HTHP) | 108–180 MJ/h | **Modelled & connected** — fed by `CW Heat → HTHP` |
| S-02 | Urea / crop CO₂ (external CO₂ off-take) | 58.5 kt CO₂/y | **Modelled & connected** — fed by `E1-T2 EO desorber → S-02` |
| S-03 | WHR Steam Recovery | 19 MJ/h | **Modelled & connected** — fed by `E1-FU1B Incinerator → S-03` |
| S-04 | Boiler Feedwater Preheat | 80 MJ/h | Defined node, **not yet connected** — future opportunity |
| S-05 | Aromatics Heat Recovery | 600 MJ/h | Defined node, **not yet connected** — future opportunity |
| S-06 | VHP Pressure Cascade | 1,962 MJ/h | Defined node, **not yet connected** — future opportunity |
| S-07 | Olefins–PET LP Symbiosis | 9.09 (unit not specified in model or report; likely MJ/h, consistent with S-04/S-05/S-06, but unconfirmed) | Defined node, **not yet connected** — future opportunity |

**Cross-check against the report text:** Chapter 6.1.8 states that external steam demand is
reduced by 2,642 MJ/h when S-04, S-05, and S-06 are considered together, with S-06 contributing
1,962 MJ/h (~74% of the total). Both figures match exactly:

- 80 (S-04) + 600 (S-05) + 1,962 (S-06) = **2,642 MJ/h** ✓
- 1,962 / 2,642 = **74.3%** ✓

Every number the report cites from this set is traceable directly to this model file.

## Note on a labelling collision with Chapter 5

Chapter 5 of the report defines a *separate*, EO/EG-plant-specific intervention set that reuses
the same S-01–S-04 labels for different things:

| Label | Chapter 5 (EO/EG-specific) | This file (full-park) |
|---|---|---|
| S-01 | HTHP | HTHP *(consistent)* |
| S-02 | CO₂ Capture from the K₂CO₃ Scrubber | Urea/crop CO₂ off-take *(consistent — same flow, different framing)* |
| S-03 | Waste Heat Recovery from E1-FU1B | WHR Steam Recovery *(consistent)* |
| S-04 | Centralized Wastewater Treatment (WWTP) | Boiler Feedwater Preheat *(conflict — same label, different intervention)* |

S-01–S-03 line up cleanly across both. **S-04 does not** — it means two different things
depending on which chapter you're reading. Worth keeping in mind if this model or report ever
gets revisited or extended.

## Why S-04–S-07 are unconnected in the model

This matches the report's own framing of the set: Chapter 6 calls these "additional future
symbiosis opportunities," and Chapter 7 explicitly excludes "External S-01 to S-07 opportunities"
from the cost-screening boundary. The Linny-R model reflects that exactly — S-01–S-03 are wired
into the active network with real upstream/downstream flows, while S-04–S-07 exist only as
placeholder nodes with capacity bounds, not yet linked to any process. They're identified and
quantified, but deliberately left as future work rather than part of the selected package.
