# dynamic-sankey

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-alpha-orange.svg)](https://github.com/StephanHausberg/dynamic_sankey)

Generate animated, standalone-HTML Sankey diagrams with **true SVG morphing**.

No server. No Plotly. No extra dependencies.
The Python side serialises your config to JSON — D3.js does the rest in the browser.

---

## Why this is different from Plotly Sankey

Plotly's Sankey animation redraw the entire SVG on every frame → nodes "pop in".
`dynamic-sankey` uses D3's `attrTween` to interpolate node positions and link paths numerically at ~60 fps — the diagram **morphs** continuously between states.

```text
Plotly:  step change → full SVG redraw  → visible pop-in
D3:      step change → per-frame lerp   → smooth morph ✓
```

---

## Installation

```bash
pip install dynamic-sankey          # once published on PyPI
# or directly from source:
pip install -e .
```

> No runtime dependencies beyond Python's stdlib (`json`).
> D3.js is loaded from CDN in the generated HTML.

---

## Quick start

```python
from dynamic_sankey import generate_html

config = {
    "nodes": [
        {"id": 0, "label": "A", "color": "#4C78A8"},
        {"id": 1, "label": "B", "color": "#F58518"},
        {"id": 2, "label": "C", "color": "#54A24B"},
    ],
    "links": [
        {"source": 0, "target": 2},
        {"source": 1, "target": 2},
    ],
    "time_series": [
        {"label": "Q1", "values": [10, 5]},
        {"label": "Q2", "values": [6,  9]},
        {"label": "Q3", "values": [12, 3]},
    ],
}

html = generate_html(config, title="My Flows")
with open("output.html", "w") as f:
    f.write(html)
```

Open `output.html` in any browser — no internet required for layout, CDN only for D3.

---

## Config format

```python
{
    # Fixed topology — same across all time steps
    "nodes": [
        {"id": <int|str>, "label": <str>, "color": <hex>},
        ...
    ],
    "links": [
        {"source": <node id>, "target": <node id>},
        ...
    ],

    # Temporal data — values are positionally bound to the links list
    "time_series": [
        {"label": <str>, "values": [<float>, ...]},   # len == len(links)
        ...
    ],
}
```

Key design principle: **topology and values are separated**.
`links` defines the graph structure once; `time_series[i].values[j]` is the flow
of `links[j]` at time step `i`. This makes it trivial to map a CSV column onto
the values list.

---

## API

### `generate_html(config, title="Dynamic Sankey") → str`

Validates the config and returns a complete HTML string.

```python
html = generate_html(config, title="Energy Flow 2023")
with open("chart.html", "w", encoding="utf-8") as f:
    f.write(html)
```

### `validate_config(config) → None`

Raises `ValueError` if:

- a link references a node ID that doesn't exist
- any `time_series` entry has a different number of values than `len(links)`

---

## Examples

Pre-built demos are in [`docs/`](docs/) and viewable directly in the browser via
[htmlpreview.github.io](https://htmlpreview.github.io):

| Example | Live demo | Source | Nodes | Links | Steps |
| ------- | --------- | ------ | ----- | ----- | ----- |
| 01 Basic | [▶ Open](https://htmlpreview.github.io/?https://github.com/StephanHausberg/dynamic_sankey/blob/main/docs/01_basic.html) | [config](examples/01_basic/config.py) | 6 | 6 | 4 |
| 02 Energiemix | [▶ Open](https://htmlpreview.github.io/?https://github.com/StephanHausberg/dynamic_sankey/blob/main/docs/02_energiemix.html) | [config](examples/02_energiemix/config.py) | 10 | 12 | 4 |
| 03 Customer Journey | [▶ Open](https://htmlpreview.github.io/?https://github.com/StephanHausberg/dynamic_sankey/blob/main/docs/03_customer_journey.html) | [config](examples/03_customer_journey/config.py) | 11 | 12 | 4 |

### Run locally

```bash
python examples/02_energiemix/generate.py
# → generates output.html and opens it in the browser
```

### Example 02 — Energiemix

Seasonal energy flow in 4 quarters:

```text
Quellen          Umwandlung        Sektoren
──────────       ──────────────    ────────────
Wind    ──┐
Solar   ──┤──► Stromerzeugung ──► Industrie
Gas     ──┤         └──────────► Haushalte
Kohle   ──┘──► Wärme & Heizung──► Industrie
Kernkraft              └────────► Haushalte
                                ► Verkehr
```

Shows how the mix shifts from coal/gas (Q1 winter) to solar (Q3 summer) while
Kernkraft drops to zero after the 2023 shutdown.

### Example 03 — Customer Journey

Website funnel across 4 quarters:

```text
Traffic-Quellen    Landing Pages    Conversion-Ziele
────────────────   ─────────────    ────────────────
Organic Search ──► Homepage    ──► Kauf
Paid Ads       ──► Produktseite──► Lead / Kontakt
Social Media   ──► Blog        ──► Newsletter
Direct/E-Mail  ──►             └──► Absprung
```

Q4 shows the holiday spike: Paid Ads up, conversions spike, bounce rate drops.

---

## How the morphing works (technical)

When you switch time steps, the library:

1. **Snapshots** the current D3-sankey layout positions (`y0`, `y1`, `width` per link).
2. **Recomputes** the layout with new values.
3. Uses `attrTween` to interpolate the underlying numbers on every animation frame:

```javascript
.attrTween("d", (d, i) => {
    const s = snapLinks[i];          // old positions
    return t => linkPathGen({
        source: d.source,            // x-coords fixed (topology unchanged)
        target: d.target,
        y0:     s.y0    + (d.y0    - s.y0)    * t,
        y1:     s.y1    + (d.y1    - s.y1)    * t,
        width:  s.width + (d.width - s.width) * t,
    });
})
```

`d3.sankeyLinkHorizontal()` recalculates the bezier path on every frame from
the interpolated numbers → continuous morph at ~60 fps via `requestAnimationFrame`.

---

## Contributing

Issues and PRs are welcome.

```bash
git clone https://github.com/StephanHausberg/dynamic_sankey.git
cd dynamic_sankey
pip install -e .
python examples/01_basic/generate.py   # smoke test
```

---

## License

[MIT](LICENSE)
