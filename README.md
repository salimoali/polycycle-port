# polycycle-port

Industrial symbiosis and energy-systems modelling for a circular-economy retrofit of a petrochemical industrial park (4413INTPR – Integrated Project, Industrial Track, MSc Industrial Ecology, TU [...]

The case is **PolyCycle Port**, a five-plant cluster at the Port of Antwerp–Bruges (CHP, Olefins, Aromatics, EO/EG, PET) connected through shared steam, electricity, material, and water flows.

> **Note on contributions.** Group project, 6 members (Rasoul Babaei Dargani, Andrew, Salih Ali, Juting Hsu, Mona Mirzaei, Chang Ann Chen), instructors Paola Ibarra González and Gijsbert Korevaar.[...]

## My contributions

- **Chapter 3** — the full stakeholder analysis section, including the bridging discussion connecting Chapter 3's stakeholder/conceptual framing to Chapter 5's technical flows

- **Chapter 6.1.2** — the integrated system representation: a Sankey diagram (energy + material flow) and a static system-integration diagram, both covering all five plants and all seven symbios[...]

- **Chapter 5** — the technical/energy-analysis methodology (energy balance approach, KPI/performance evaluation, pinch and utility matching) and the complete EO/EG plant analysis with all of it[...]

- **Full-park Linny-R energy network model** — the energy/intervention network spanning all five plants and all seven interventions (S-01–S-07)

- **Multilayer network analysis** of the park's plant cluster across Energy and Materials layers (degree, betweenness, strength, participation coefficient, composite multiplex importance ranking)

- **Section 9.3** — the final conclusions

- The CHP Utility-Hub Retrofit (Chapter 6 system representation, TONF structure, trade-off matrix, economics, spider diagram) was led by a teammate, not by me. The park-wide material-balance Linny-R[...]

## Repository contents

| Component | Description | Mine / Team |
| - | - | - |
| Stakeholder analysis | Park stakeholder mapping, interests, dependencies, and the Ch.3→Ch.5 bridging discussion | Mine |
| Sankey diagram | Interactive energy + material flow visualization, all 5 plants + 7 interventions (Chapter 6.1.2) | Mine |
| EO/EG energy analysis | Full energy-balance evaluation and intervention design for S-01–S-03 (Chapter 5) | Mine |
| Energy/intervention Linny-R model | Full-park network covering all 5 plants and 7 interventions (S-01–S-07) | Mine |
| Multilayer SNA | Multiplex network analysis of the 5-plant cluster across Energy and Materials layers — degree, betweenness, strength, participation coefficient, interlayer connectivity, and a[...] | Mine |
| Conclusions | Cross-intervention synthesis and final recommendation (Section 9.3) | Mine |


## Key results

- **EO/EG four-intervention package** (S-01–S-03 + centralised WWTP) — diagnosed as the park's highest-emission, highest-waste-heat plant after correcting a kt-vs-t unit error in the original [...]

- **Multilayer SNA finding:** CHP is the park's central *energy* hub, but EO/EG comes out as the most-networked node overall once both the Energy and Materials layers are combined — two differen[...]

- **CHP Utility-Hub Retrofit** (teammate's work) — ~651 tCO₂/y avoided, the only intervention in scope with a full investment-grade economic case, and ultimately the project's headline recomme[...]

## Repository structure

```
polycycle-port/  
├── report/  
│   └── PolyCycle\_Port\_Final\_Report.pdf       \# full 102-page final submission  
├── linnyr/  
│   ├── Full-Park-Network-With-Intervention.lnr   \# energy/intervention network, S-01–S-07 (mine)  
│   └── S01-S07\_Intervention\_Table.md              \# supplementary table documenting S-01–S-07 (mine)  
├── analysis/  
│   ├── sankey\_polycycle.py                    \# interactive Plotly Sankey source (mine)  
│   └── 6\_1\_2\_sankey\_polycycle.html             \# rendered Sankey output (mine)  
└── sna/  
    └── multilayer\_sna.ipynb                   \# multilayer stakeholder/process network analysis (mine)
```

## Tools used

Linny-R (network/energy-material flow modelling), Python — Plotly for the interactive Sankey diagram, matplotlib for the system integration diagram and EO/EG energy analysis, pandas for data han[...]


## Reproducing the Analysis

### Clone the repository

```bash
git clone https://github.com/salimoali/polycycle-port.git
cd polycycle-port
```

### Create a virtual environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Generate the Sankey Diagram

```bash
python analysis/sankey_polycycle.py
```

### Open the generated visualization

```
analysis/6_1_2_sankey_polycycle.html
```

### Open the Social Network Analysis

```
sna/multilayer_sna.ipynb
```

---

# Title

PolyCycle Port — Industrial Symbiosis & Energy Systems Modelling

# Project description

This repository contains the deliverables for the PolyCycle Port project: a multi-plant industrial symbiosis and energy-systems modelling study focused on a petrochemical park in the Port of Antwerp–Bruges. It includes interactive visualisations (Sankey), multilayer social/network analysis, Linny-R models and the final project report.

# Screenshot of Sankey

![Sankey screenshot](analysis/assets/sankey_screenshot.png)

# Screenshot of Network Analysis

![Network analysis screenshot](analysis/assets/network_analysis_screenshot.png)

# System Diagram

![System diagram](analysis/assets/system_diagram.png)

# Repository Structure

The repository structure is documented above. Use the "Reproducing the Analysis" section for steps to run notebooks and generate visualisations.
