# polycycle-port

Industrial symbiosis and energy-systems modelling for a circular-economy retrofit of a petrochemical industrial park (4413INTPR – Integrated Project, Industrial Track, MSc Industrial Ecology, TU Delft/Leiden, Feb–Jun 2026).

The case is **PolyCycle Park**, a five-plant cluster at the Port of Antwerp–Bruges (CHP, Olefins, Aromatics, EO/EG, PET) connected through shared steam, electricity, material, and water flows.

> **Note on contributions.** This was a 6-person group project. This repository contains **only my individual contributions** — files and analysis built or led by teammates have been deliberately excluded, even where they appear in the joint final report. Per the project's official contribution record, I participated in Chapters 1–6 and 9, both main presentations, the post-feedback revision pass, and final review.

## My contributions

- **Chapter 3** — the full stakeholder analysis section, including the bridging discussion connecting Chapter 3's stakeholder/conceptual framing to Chapter 5's technical flows
- **Chapter 6.1.2** — the integrated system representation: an interactive Sankey diagram (energy + material flow) covering all five plants and all seven symbiosis interventions (S-01–S-07)
- **Chapter 5** — the technical/energy-analysis methodology (energy balance approach, KPI/performance evaluation, pinch and utility matching) and the complete EO/EG plant analysis with all of its interventions (S-01 HTHP, S-02 CO₂ capture, S-03 waste-heat recovery)
- **Full-park Linny-R energy network model** — the energy/intervention network spanning all five plants and all seven interventions (S-01–S-07)
- **Energy-layer network analysis** — degree centrality, betweenness centrality, density, and strength (weighted degree) for the steam/electricity flow network between the five plants
- **Section 9.3** — the final conclusions

The park-wide material-balance Linny-R network and the Materials layer of the original multilayer network analysis were built by teammates — none of that work or those files are included here. Other sections of the joint report (including the CHP Utility-Hub Retrofit economics in Chapter 6) were led by teammates and are likewise excluded.

## Repository contents

| Component | Description |
|---|---|
| Stakeholder analysis | Park stakeholder mapping, interests, dependencies, and the Ch.3→Ch.5 bridging discussion |
| Sankey diagram | Interactive energy + material flow visualization, all 5 plants + 7 interventions (Chapter 6.1.2) |
| EO/EG energy analysis | Full energy-balance evaluation and intervention design for S-01–S-03 (Chapter 5) |
| Energy/intervention Linny-R model | Full-park network covering all 5 plants and 7 interventions (S-01–S-07) |
| Energy-layer network analysis | Degree, betweenness, density, and strength for the inter-plant steam/electricity network |
| Conclusions | Cross-intervention synthesis and final recommendation (Section 9.3) |

## Key results

- **EO/EG four-intervention package** (S-01–S-03 + centralised WWTP) — diagnosed as the park's highest-emission, highest-waste-heat plant. Not advanced as the project's primary recommendation since equivalent costing depth wasn't developed for it in this project's scope; flagged as the strongest candidate for assessment once the CHP retrofit is underway.
- A unit error in the original CO₂-avoidance accounting (kt vs. t) was identified and corrected during the EO/EG energy analysis, materially changing the comparative ranking between EO/EG and the CHP retrofit.
- **Energy-layer network analysis:** CHP is the clear hub of the steam/electricity network — highest degree (4 direct connections) and the only node with non-zero betweenness centrality (3.0), meaning every other plant's energy supply currently routes through it. Network density across the energy layer is 0.2.

## Repository structure

```
polycycle-port/
├── report/
│   └── PolyCycle_Port_Final_Report.pdf       # full 102-page joint final submission (included for context)
├── linnyr/
│   └── Full-Park-Network-With-Intervention.lnr   # energy/intervention network, S-01–S-07 (mine)
├── analysis/
│   ├── sankey_polycycle.py                    # interactive Plotly Sankey source
│   └── 6_1_2_sankey_polycycle.html             # rendered Sankey output
└── sna/
    └── energy_layer_network_analysis.ipynb    # Energy-layer network analysis
```

## Tools used

Linny-R (network/energy-material flow modelling), Python — Plotly for the interactive Sankey diagram, matplotlib for the EO/EG energy analysis, pandas for data handling — and network analysis (NetworkX/pymnet).
