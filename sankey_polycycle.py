import plotly.graph_objects as go
import json
# ── NODES ────────────────────────────────────────────────────────
# Order matters — index used in links below
labels = [
    # 0  Sources
    "Natural Gas",
    # 1-5  Plants
    "CHP",
    "Olefins",
    "Aromatics",
    "EO/EG",
    "PET",
    # 6-8  Steam headers
    "HP Steam",
    "MP Steam",
    "LP Steam",
    # 9  VHP
    "VHP Steam",
    # 10-11  Electricity
    "Electricity",
    # 11  Products / sinks
    "MEG → PET",        # 11
    "Ethylene → EO/EG", # 12
    "p-Xylene → PTA",   # 13
    "PET Product",      # 14
    # 15-17  Interventions / external sinks
    "Greenhouse (S-01)", # 15
    "Urea Plant (S-02)", # 16
    "WHR Steam (S-03)",  # 17
    "FW Preheat (S-04)", # 18
    "Aromatics WHR (S-05)", # 19
    "VHP Cascade (S-06)",   # 20
    "PET LP Steam (S-07)",  # 21
    # 22  Waste heat
    "Cooling Water Rejection", # 22
]

# colours per node
node_colors = [
    "#546E7A",   # Natural Gas
    "#1A3E6E",   # CHP
    "#2E7D32",   # Olefins
    "#E65100",   # Aromatics
    "#6A1B9A",   # EO/EG
    "#00838F",   # PET
    "#B71C1C",   # HP Steam
    "#C62828",   # MP Steam
    "#E53935",   # LP Steam
    "#FF6F00",   # VHP Steam
    "#F9A825",   # Electricity
    "#00838F",   # MEG
    "#2E7D32",   # Ethylene
    "#E65100",   # p-Xylene
    "#00838F",   # PET Product
    "#43A047",   # Greenhouse
    "#78909C",   # Urea
    "#B71C1C",   # WHR Steam
    "#1A3E6E",   # FW Preheat
    "#E65100",   # Aromatics WHR
    "#FF6F00",   # VHP Cascade
    "#2E7D32",   # PET LP
    "#78909C",   # CW Rejection
]

# ── LINKS  (source, target, value MJ/h or kt/y where noted) ─────
# Energy flows in MJ/h; material flows scaled to be visible (kt/y × 5)
links = [
    # Natural gas → CHP
    dict(s=0,  t=1,  v=2500,  label="NG input ~2,500 MJ/h equiv"),

    # CHP → steam headers
    dict(s=1,  t=6,  v=6497,  label="HP Steam 6,497 MJ/h"),
    dict(s=1,  t=7,  v=4111,  label="MP Steam 4,111 MJ/h"),
    dict(s=1,  t=8,  v=722,   label="LP Steam 722 MJ/h"),
    dict(s=1,  t=10, v=1450,  label="Electricity 1,450 MJ/h"),

    # Olefins → VHP / steam exports
    dict(s=2,  t=9,  v=1962,  label="VHP Steam 1,962 MJ/h"),
    dict(s=2,  t=6,  v=187,   label="HP Steam surplus 187 MJ/h"),

    # Steam headers → plants (demand)
    dict(s=6,  t=3,  v=4500,  label="HP → Aromatics"),
    dict(s=6,  t=4,  v=1810,  label="HP → EO/EG"),
    dict(s=7,  t=3,  v=14760, label="MP → Aromatics 14,760 MJ/h"),
    dict(s=7,  t=4,  v=3507,  label="MP → EO/EG 3,507 MJ/h"),
    dict(s=7,  t=2,  v=200,   label="MP → Olefins"),
    dict(s=8,  t=3,  v=5869,  label="LP → Aromatics 5,869 MJ/h"),
    dict(s=8,  t=4,  v=1090,  label="LP → EO/EG 1,090 MJ/h"),
    dict(s=8,  t=5,  v=9,     label="LP → PET 9.09 MJ/h"),

    # Electricity → plants
    dict(s=10, t=2,  v=400,   label="Elec → Olefins"),
    dict(s=10, t=3,  v=300,   label="Elec → Aromatics"),
    dict(s=10, t=4,  v=249,   label="Elec → EO/EG 249 MJ/h"),
    dict(s=10, t=5,  v=100,   label="Elec → PET"),

    # Material flows (kt/y × 8 for visibility)
    dict(s=2,  t=12, v=269*8, label="Ethylene 269 kt/y"),
    dict(s=12, t=4,  v=269*8, label="Ethylene → EO/EG"),
    dict(s=4,  t=11, v=135*8, label="MEG 135 kt/y"),
    dict(s=11, t=5,  v=135*8, label="MEG → PET"),
    dict(s=3,  t=13, v=754*8, label="p-Xylene 754 kt/y"),
    dict(s=13, t=5,  v=754*8, label="p-Xylene → PET"),
    dict(s=5,  t=14, v=110*8, label="PET product"),

    # Cooling water rejection
    dict(s=4,  t=22, v=12298, label="CW rejection EO/EG 12,298 MJ/h"),
    dict(s=3,  t=22, v=15000, label="CW rejection Aromatics"),

    # ── INTERVENTIONS (orange) ──────────────────────────────────
    dict(s=4,  t=15, v=144,   label="S-01 HTHP → Greenhouse 108–180 MJ/h"),
    dict(s=4,  t=16, v=300,   label="S-02 CO₂ → Urea 58.5 kt/y"),
    dict(s=4,  t=17, v=19,    label="S-03 WHR steam 19 MJ/h"),
    dict(s=1,  t=18, v=80,    label="S-04 CHP flue gas preheat 80 MJ/h"),
    dict(s=3,  t=19, v=600,   label="S-05 Aromatics WHR 600 MJ/h"),
    dict(s=9,  t=20, v=1962,  label="S-06 VHP cascade 1,962 MJ/h"),
    dict(s=2,  t=21, v=9,     label="S-07 Olefins LP → PET 9.09 MJ/h"),
]

sources = [l['s'] for l in links]
targets = [l['t'] for l in links]
values  = [l['v'] for l in links]
link_labels = [l['label'] for l in links]

# intervention link indices (for colour)
interv_idx = {28, 29, 30, 31, 32, 33, 34}
link_colors = []
for i in range(len(links)):
    if i in interv_idx:
        link_colors.append("rgba(245, 127, 23, 0.55)")   # orange
    elif links[i]['s'] in {11, 12, 13} or links[i]['t'] in {11, 12, 13, 14}:
        link_colors.append("rgba(21, 101, 192, 0.45)")   # blue material
    elif links[i]['s'] in {6, 7, 8, 9} or links[i]['t'] in {6, 7, 8, 9}:
        link_colors.append("rgba(211, 47, 47, 0.40)")    # red steam
    else:
        link_colors.append("rgba(100, 100, 120, 0.35)")  # grey default

fig = go.Figure(go.Sankey(
    arrangement="snap",
    node=dict(
        pad=18,
        thickness=22,
        line=dict(color="white", width=0.8),
        label=labels,
        color=node_colors,
        hovertemplate='<b>%{label}</b><extra></extra>',
    ),
    link=dict(
        source=sources,
        target=targets,
        value=values,
        label=link_labels,
        color=link_colors,
        hovertemplate='%{label}<extra></extra>',
    )
))

fig.update_layout(
    title=dict(
        text="<b>PolyCycle Park Antwerp — Integrated Energy & Material Flow (Sankey)</b><br>"
             "<sup>Chapter 6.1.2 | Energy in MJ/h · Material flows scaled (kt/y × 8) · "
             "Orange = symbiosis interventions S-01–S-07</sup>",
        font=dict(size=15, color="#1A1A2E"),
        x=0.02,
    ),
    font=dict(size=11, family="Arial"),
    paper_bgcolor="#F8F9FA",
    height=500,
    margin=dict(l=20, r=20, t=90, b=20),
)

fig.write_html('6_1_2_sankey_polycycle.html')
print("Saved.")
