# polycycle-port

Industrial symbiosis and energy-systems modelling for a circular-economy retrofit of a petrochemical industrial park (4413INTPR – Integrated Project, Industrial Track, MSc Industrial Ecology, TU Delft/Leiden, Feb–Jun 2026).

The case is **PolyCycle Port**, a five-plant cluster at the Port of Antwerp–Bruges (CHP, Olefins, Aromatics, EO/EG, PET) connected through shared steam, electricity, material, and water flows.

> \*\*Note on contributions.\*\* Group project, 5 members (Rasoul Babaei Dargani, Salih Ali, Juting Hsu, Mona Mirzaei,  Andrew Chang Ann Chen), instructors Paola Ibarra González and Gijsbert Korevaar. Per the project's official contribution record, I participated in Chapters 1–6 and 9, the mid-project presentation, the post-feedback revision pass, and final review. The final presentation was delivered by a teammate, not by me.

## Assessment

**Final grade: 9.0/10** — 4413INTPR Integrated Project, Industrial Systems track, TU Delft (2026)

> This is the group's collective grade (same for all group members, per course grading rules) — see \*\*My contributions\*\* below for what was individually mine.

> "The report demonstrates strong systems thinking, extensive quantitative analysis, and clear alignment with industrial symbiosis principles. The depth of the material and energy chapter and systems integration chapter are particularly strong."
> — Grading committee remarks

**Collective chapters (50%)**

|Item|Grade|
|-|-|
|Ch.1 Background and Context|9.0|
|Ch.2 Eco-Industrial Parks \& Problem Statement|9.0|
|Ch.3 Project Scope and Research Approach|9.0|
|Ch.6 System Integration|9.5|
|Ch.7 Economic Assessment|9.0|
|Ch.8 Strategic Planning and Policy Alignment|8.5|
|Ch.9 Discussion, Conclusions and Recommendations|8.5|
|Overall set-up and layout|8.5|
|Overall quality of report|9.0|
|References|9.0|

**Specialization chapters — Energy Analysis (40%)**

|Item|Grade|
|-|-|
|Flows Assessment|9.0|
|Performance Evaluation|9.0|
|Symbiosis Analysis|9.0|
|Interventions|8.5|
|Reporting Quality|9.0|
|References|9.0|

**Presentation (10%)** — delivered by a teammate, not by me

|Item|Grade|
|-|-|
|Oral presentation quality|8.5|
|Presentation material \& content|9.0|

## My contributions

* **Chapter 3** — the full stakeholder analysis section, including the bridging discussion connecting Chapter 3's stakeholder/conceptual framing to Chapter 5's technical flows
* **Chapter 6.1.2** — the integrated system representation: a Sankey diagram (energy + material flow) and a static system-integration diagram, both covering all five plants and all seven symbiosis interventions (S-01–S-07)
* **Chapter 5** — the technical/energy-analysis methodology (energy balance approach, KPI/performance evaluation) and the complete EO/EG plant analysis with all of its interventions (S-01 HTHP, S-02 CO₂ capture, S-03 waste-heat recovery). Pinch and utility matching was a teammate's contribution, not mine.
* **Full-park Linny-R energy network model** — the energy/intervention network spanning all five plants and all seven interventions (S-01–S-07)
* **Network analysis of the Energy layer** of the park's plant cluster (degree, betweenness, strength, participation coefficient). The Materials-layer analysis and the composite multiplex importance ranking combining both layers were built by the group, not individually by me.
* **Section 9.3** — the final conclusions

The CHP Utility-Hub Retrofit (Chapter 6 system representation, TONF structure, trade-off matrix, economics, spider diagram) was led by a teammate, not by me. The park-wide material-balance Linny-R network underlying the Chapter 6.1.2 diagrams was also built by the group rather than individually by me.

## Repository contents

|Component|Description|Mine / Team|
|-|-|-|
|Stakeholder analysis|Park stakeholder mapping, interests, dependencies, and the Ch.3→Ch.5 bridging discussion|Mine|
|Sankey diagram|Interactive energy + material flow visualization, all 5 plants + 7 interventions (Chapter 6.1.2)|Mine|
|EO/EG energy analysis|Full energy-balance evaluation and intervention design for S-01–S-03 (Chapter 5)|Mine|
|Energy/intervention Linny-R model|Full-park network covering all 5 plants and 7 interventions (S-01–S-07)|Mine|
|Energy-layer SNA|Network analysis of the 5-plant cluster's Energy layer — degree, betweenness, strength, participation coefficient|Mine|
|Materials-layer SNA \& multiplex ranking|Materials-layer analysis, interlayer connectivity, and composite multiplex importance ranking|Team|
|Conclusions|Cross-intervention synthesis and final recommendation (Section 9.3)|Mine|



## Key results

* **EO/EG four-intervention package** (S-01–S-03 + centralized WWTP) — diagnosed as the park's highest-emission, highest-waste-heat plant after correcting a kt-vs-t unit error in the original CO₂-avoidance accounting that had affected its ranking against the CHP retrofit. Not advanced as the project's primary recommendation since equivalent costing depth wasn't developed for it in this project's scope; flagged as the strongest candidate for assessment once the CHP retrofit is underway.
* **Multilayer SNA finding** (Energy-layer analysis mine; Materials-layer and combined multiplex ranking by the group): CHP is the park's central *energy* hub, but EO/EG comes out as the most-networked node overall once both the Energy and Materials layers are combined — two different but compatible framings, not a contradiction, reflecting the different scope of "energy hub" vs. "most interconnected across the full symbiosis network."
* **CHP Utility-Hub Retrofit** (teammate's work) — \~651 tCO₂/y avoided, the only intervention in scope with a full investment-grade economic case, and ultimately the project's headline recommendation.

## Repository structure

```
polycycle-port/  
├── report/  
│   └── PolyCycle\\\_Port\\\_Final\\\_Report.pdf       \\# full 102-page final submission  
├── linnyr/  
│   ├── Full-Park-Network-With-Intervention.lnr   \\# energy/intervention network, S-01–S-07 (mine)  
│   └── S01-S07\\\_Intervention\\\_Table.md              \\# supplementary table documenting S-01–S-07 (mine)  
├── analysis/  
│   ├── sankey\\\_polycycle.py                    \\# interactive Plotly Sankey source (mine)  
│   └── 6\\\_1\\\_2\\\_sankey\\\_polycycle.html             \\# rendered Sankey output (mine)  
└── sna/  
    └── multilayer\\\_sna.ipynb                   \\# multilayer network analysis — Energy layer mine, Materials layer \& multiplex ranking team
```

## Tools used

Linny-R (network/energy-material flow modelling), Python — Plotly for the interactive Sankey diagram, matplotlib for the system integration diagram and EO/EG energy analysis, pandas for data handling — and social network analysis (NetworkX/pymnet).

