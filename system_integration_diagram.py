import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np

fig, ax = plt.subplots(figsize=(24, 15))
ax.set_xlim(0, 24)
ax.set_ylim(0, 15)
ax.axis('off')
fig.patch.set_facecolor('#F8F9FA')
ax.set_facecolor('#F8F9FA')

C = {
    'CHP':       '#1A3E6E',
    'Olefins':   '#2E7D32',
    'Aromatics': '#E65100',
    'EO_EG':     '#6A1B9A',
    'PET':       '#00838F',
    'external':  '#757575',
    'energy':    '#C62828',
    'material':  '#1565C0',
    'water':     '#0277BD',
    'int':       '#E65C00',
    'text':      '#1A1A2E',
}

# node positions (x, y, w, h)
nodes = {
    'CHP':       (1.2,  8.8, 3.2, 1.6),
    'Olefins':   (7.0,  10.2, 3.2, 1.6),
    'Aromatics': (13.5, 10.2, 3.2, 1.6),
    'EO/EG':     (7.0,  6.0,  3.2, 1.6),
    'PET':       (13.5, 6.0,  3.2, 1.6),
}
external = {
    'Greenhouse': (0.2, 3.8, 2.8, 1.0),
    'Urea Plant': (0.2, 2.2, 2.8, 1.0),
    'WWTP':       (0.2, 0.6, 2.8, 1.0),
    'Grid':       (1.2,12.8, 2.8, 1.0),
}

def nc(d, name):
    x,y,w,h = d[name]
    return x+w/2, y+h/2

def box(ax, pos, label, color, ext=False):
    x,y,w,h = pos
    p = FancyBboxPatch((x,y), w, h, boxstyle="round,pad=0.12",
                        facecolor=color, edgecolor='white',
                        linewidth=2, zorder=3, alpha=0.85 if ext else 1.0)
    ax.add_patch(p)
    ax.text(x+w/2, y+h/2, label, ha='center', va='center',
            fontsize=11 if not ext else 9.5,
            fontweight='bold', color='white', zorder=4)

def arr(ax, x1,y1,x2,y2, color, lw=2.0, ls='-', rad=0.0):
    ax.annotate('', xy=(x2,y2), xytext=(x1,y1),
                arrowprops=dict(arrowstyle='->', color=color, lw=lw,
                                linestyle=ls,
                                connectionstyle=f'arc3,rad={rad}'), zorder=2)

def lbl(ax, x, y, text, color, fs=7.5, bold=False, ha='center', va='bottom', bg=None):
    kw = dict(fontsize=fs, color=color, ha=ha, va=va, zorder=5,
              fontweight='bold' if bold else 'normal',
              style='normal' if bold else 'italic')
    if bg:
        kw['bbox'] = dict(boxstyle='round,pad=0.15', facecolor=bg,
                          edgecolor='none', alpha=0.7)
    ax.text(x, y, text, **kw)

# draw nodes
for name, pos in nodes.items():
    col = C['EO_EG'] if name == 'EO/EG' else C[name]
    box(ax, pos, name, col)
for name, pos in external.items():
    box(ax, pos, name, C['external'], ext=True)

chp  = nc(nodes,'CHP');   olef = nc(nodes,'Olefins')
arom = nc(nodes,'Aromatics'); eoeg = nc(nodes,'EO/EG'); pet = nc(nodes,'PET')
gh   = nc(external,'Greenhouse'); urea = nc(external,'Urea Plant')
wwtp = nc(external,'WWTP');  grid = nc(external,'Grid')

# ── ENERGY FLOWS ─────────────────────────────────────────────────
# Grid → CHP
arr(ax, grid[0], grid[1]-0.5, chp[0]+0.3, chp[1]+0.8, '#546E7A', lw=1.5)
lbl(ax, 2.8, 12.5, 'Natural gas', '#546E7A', fs=7.5)

# CHP → Olefins
arr(ax, chp[0]+1.6, chp[1]+0.5, olef[0]-1.6, olef[1]-0.3, C['energy'], lw=2.2)
lbl(ax, 5.5, 10.4, 'Elec+steam\n1,449.9 MJ/h', C['energy'], fs=7.5, bg='#F8F9FA')

# CHP → EO/EG
arr(ax, chp[0]+1.4, chp[1]-0.5, eoeg[0]-1.6, eoeg[1]+0.5, C['energy'], lw=2.2, rad=0.18)
lbl(ax, 4.0, 7.8, 'Steam\n6,407 MJ/h', C['energy'], fs=7.5, bg='#F8F9FA')

# CHP → Aromatics
arr(ax, chp[0]+3.2, chp[1]+0.6, arom[0]-1.6, arom[1]+0.5, C['energy'], lw=2.2, rad=-0.15)
lbl(ax, 9.0, 12.4, 'Steam 25,129 MJ/h', C['energy'], fs=7.5, bg='#F8F9FA')

# Olefins → Aromatics VHP existing (energy, dashed)
arr(ax, olef[0]+3.2, olef[1]+0.3, arom[0]-1.6, arom[1]+0.3, C['energy'], lw=1.6, ls='--')
lbl(ax, 11.2, 12.0, 'VHP 1,962 MJ/h', C['energy'], fs=7.5)

# ── MATERIAL FLOWS ───────────────────────────────────────────────
# Olefins → EO/EG
arr(ax, olef[0]+0.5, olef[1]-0.8, eoeg[0]+0.5, eoeg[1]+0.8, C['material'], lw=2.2)
lbl(ax, 9.0, 8.7, 'Ethylene 269 kt/y', C['material'], fs=7.5)

# Aromatics → PET
arr(ax, arom[0]+0.8, arom[1]-0.8, pet[0]+0.8, pet[1]+0.8, C['material'], lw=2.2)
lbl(ax, 15.8, 8.7, 'p-Xylene→PTA\n754 kt/y', C['material'], fs=7.5)

# EO/EG → PET
arr(ax, eoeg[0]+3.2, eoeg[1], pet[0]-1.6, pet[1], C['material'], lw=2.2)
lbl(ax, 11.2, 6.9, 'MEG 135 kt/y', C['material'], fs=7.5)

# ── WATER ────────────────────────────────────────────────────────
arr(ax, eoeg[0]+0.5, eoeg[1]-0.8, wwtp[0]+1.4, wwtp[1]+0.8, C['water'], lw=1.4, ls='--', rad=0.05)
lbl(ax, 3.8, 1.8, 'Wastewater', C['water'], fs=7.5)

# ── INTERVENTIONS ────────────────────────────────────────────────
IC = C['int']

# S-01: EO/EG → Greenhouse (target centre of box)
arr(ax, eoeg[0]-0.6, eoeg[1]-0.8, gh[0]+1.4, gh[1], IC, lw=1.8, ls='--', rad=0.1)
lbl(ax, 3.8, 4.8, 'S-01: HTHP\n108–180 MJ/h', IC, fs=8, bold=True)

# S-02: EO/EG → Urea (target centre of box)
arr(ax, eoeg[0]-1.0, eoeg[1]-0.8, urea[0]+1.4, urea[1]+0.5, IC, lw=1.8, ls='--', rad=0.18)
lbl(ax, 3.5, 3.3, 'S-02: CO₂\n58.5 kt/y', IC, fs=8, bold=True)

# S-03: EO/EG incinerator → steam (arrow up toward CHP)
arr(ax, eoeg[0]-0.1, eoeg[1]+0.8, chp[0]+2.5, chp[1]-0.3, IC, lw=1.6, ls='--', rad=-0.18)
lbl(ax, 5.0, 8.3, 'S-03: WHR steam\n19 MJ/h', IC, fs=8, bold=True, bg='#F8F9FA')

# S-04: CHP internal flue gas preheat (self arrow on CHP right side)
ax.annotate("", xy=(chp[0]+3.6, chp[1]+0.3),
            xytext=(chp[0]+3.6, chp[1]-0.6),
            arrowprops=dict(arrowstyle="->", color=IC, lw=2.2,
                            linestyle='--',
                            connectionstyle="arc3,rad=0.9"), zorder=2)
lbl(ax, 1.6, 8.0, "S-04: CHP preheat\n80 MJ/h", IC, fs=8, bold=True)

# S-05: Aromatics WHR → steam network (arrow from Aromatics down-left to CHP area)
arr(ax, arom[0]-0.3, arom[1]-0.8, chp[0]+3.0, chp[1]+0.7, IC, lw=1.8, ls='--', rad=0.22)
lbl(ax, 10.5, 10.0, 'S-05: Aromatics WHR\n600 MJ/h', IC, fs=8, bold=True, bg='#F8F9FA')

# S-06: Olefins VHP → HP/MP pool (separate arrow below existing VHP line)
arr(ax, olef[0]+3.2, olef[1]-0.1, arom[0]-1.6, arom[1]-0.1, IC, lw=2.0, ls='--')
lbl(ax, 11.2, 11.1, 'S-06: VHP cascade\n1,962 MJ/h', IC, fs=8, bold=True, bg='#F8F9FA')

# S-07: Olefins LP → PET
arr(ax, olef[0]+3.0, olef[1]-0.5, pet[0]-0.2, pet[1]+0.8, IC, lw=1.6, ls='--', rad=-0.18)
lbl(ax, 12.5, 9.5, 'S-07: LP steam\n9.09 MJ/h', IC, fs=8, bold=True, bg='#F8F9FA')

# ── TITLE ────────────────────────────────────────────────────────
ax.text(12, 14.7, 'PolyCycle Park Antwerp — Integrated System Representation',
        ha='center', va='top', fontsize=15, fontweight='bold', color=C['text'])
ax.text(12, 14.15, 'Chapter 6.1.2  |  Energy, Material & Water Flows + Symbiosis Interventions S-01 to S-07',
        ha='center', va='top', fontsize=10, color='#555555', style='italic')

# ── LEGEND (far right, well spaced) ─────────────────────────────
lx = 19.5

# Flow types
ax.text(lx, 14.0, 'Flow types', fontsize=10, fontweight='bold', color=C['text'], va='top')
flows = [
    ('-',  C['energy'],   'Energy / steam'),
    ('-',  C['material'], 'Material'),
    ('-',  C['water'],    'Water'),
    ('--', C['int'],      'Symbiosis intervention'),
]
for i,(ls,col,lab) in enumerate(flows):
    y = 13.4 - i*0.65
    ax.plot([lx, lx+0.8], [y,y], color=col, lw=2.2, linestyle=ls)
    ax.text(lx+1.0, y, lab, fontsize=9, va='center', color=C['text'])

# Plants
ax.text(lx, 10.8, 'Plants', fontsize=10, fontweight='bold', color=C['text'], va='top')
plants = [
    (C['CHP'],       'CHP'),
    (C['Olefins'],   'Olefins'),
    (C['Aromatics'], 'Aromatics'),
    (C['EO_EG'],     'EO/EG'),
    (C['PET'],       'PET'),
    (C['external'],  'External node'),
]
for i,(col,lab) in enumerate(plants):
    y = 10.2 - i*0.58
    p = mpatches.FancyBboxPatch((lx, y-0.17), 0.65, 0.35,
                                 boxstyle="round,pad=0.04",
                                 facecolor=col, edgecolor='white', lw=1, zorder=3)
    ax.add_patch(p)
    ax.text(lx+0.85, y, lab, fontsize=9, va='center', color=C['text'])

# Interventions index
ax.text(lx, 6.6, 'Interventions', fontsize=10, fontweight='bold', color=C['text'], va='top')
intervs = [
    'S-01  HTHP heat → Greenhouse',
    'S-02  CO₂ capture → Urea plant',
    'S-03  EO/EG WHR → steam (19 MJ/h)',
    'S-04  CHP flue gas preheat (80 MJ/h)',
    'S-05  Aromatics WHR → steam (600 MJ/h)',
    'S-06  Olefins VHP cascade (1,962 MJ/h)',
    'S-07  Olefins LP steam → PET',
]
for i,txt in enumerate(intervs):
    ax.text(lx, 6.0 - i*0.52, txt, fontsize=8.5,
            color=IC, va='top')

plt.tight_layout(pad=0.3)
plt.savefig('6_1_2_system_integration_diagram.png',
            dpi=180, bbox_inches='tight', facecolor=fig.get_facecolor())
print("Saved.")
