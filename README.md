# polycycle-port

Energy-systems and industrial-symbiosis modelling for the EO/EG plant and the wider park network at PolyCycle Port — a five-plant petrochemical cluster (CHP, Olefins, Aromatics, EO/EG, PET) at the Port of Antwerp–Bruges. Built for 4413INTPR (Integrated Project, Industrial Track, MSc Industrial Ecology, TU Delft/Leiden, Feb–Jun 2026).

This was a 6-person group project. **This repo contains only my individual contributions** — not the full group submission. See the note below for what that was.

## My contributions

- **Stakeholder analysis** (Chapter 3) — full stakeholder mapping, interests, and dependencies for the park, plus the bridging discussion connecting it to the technical flows in Chapter 5
- **EO/EG energy analysis** (Chapter 5) — the energy-balance methodology, KPI/performance evaluation, pinch and utility matching, and the complete EO/EG intervention package (S-01 HTHP, S-02 CO₂ capture, S-03 waste-heat recovery)
- **Full-park Linny-R energy network model** — covering all 5 plants and all 7 interventions (S-01–S-07)
- **Multilayer social-network analysis** of stakeholder relationships *(to be added)*
- **Sankey diagram** — park-wide material-flow visualization (Chapter 4) *(to be added)*
- **Conclusions** (Section 9.3) — final synthesis

## Key result

A unit error in the original CO₂-avoidance accounting (kt vs. t) was identified and corrected during the EO/EG energy analysis, materially changing the comparative ranking between the EO/EG package and the rest of the park's interventions. The EO/EG package was diagnosed as the park's highest-emission, highest-waste-heat plant — flagged as the strongest candidate for follow-up investment analysis.

## Repository structure

```
polycycle-port/
├── linnyr/
│   └── Full-Park-Network-With-Intervention.lnr   # energy/intervention network, S-01–S-07
└── report/
    └── PolyCycle_Port_Final_Report.pdf            # full group submission, included for context only
```

Coming soon: Sankey diagram source and the multilayer SNA notebook.

## Note on the full report

The PDF above is the complete group submission (6 authors). My sections are Chapter 3 (stakeholder analysis), Chapter 5 (EO/EG energy analysis), and Section 9.3 (conclusions). The CHP Utility-Hub Retrofit (Chapter 6) and the park-wide material-balance model were led by teammates and aren't reproduced here.

## Tools used

Linny-R (network/energy-material flow modelling), Python (pandas, matplotlib) for the energy analysis, social network analysis (NetworkX/pymnet).
