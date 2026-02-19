"""
Example 01 — Basic
==================
Minimales Beispiel: 6 Nodes (A1/A2 → B1/B2 → C1/C2), 6 Links, 4 Quartale.

Zeigt das Grundprinzip:
- nodes / links definieren die Topologie einmalig
- time_series.values sind positionsgebunden zur links-Liste
"""

SANKEY_CONFIG = {
    "nodes": [
        {"id": 0, "label": "A1", "color": "#4C78A8"},
        {"id": 1, "label": "A2", "color": "#F58518"},
        {"id": 2, "label": "B1", "color": "#54A24B"},
        {"id": 3, "label": "B2", "color": "#E45756"},
        {"id": 4, "label": "C1", "color": "#72B7B2"},
        {"id": 5, "label": "C2", "color": "#B279A2"},
    ],
    "links": [
        {"source": 0, "target": 2},   # 0: A1 → B1
        {"source": 1, "target": 3},   # 1: A2 → B2
        {"source": 0, "target": 3},   # 2: A1 → B2
        {"source": 2, "target": 4},   # 3: B1 → C1
        {"source": 3, "target": 4},   # 4: B2 → C1
        {"source": 3, "target": 5},   # 5: B2 → C2
    ],
    "time_series": [
        {"label": "Q1 2024", "values": [8, 4, 2, 8, 4, 2]},
        {"label": "Q2 2024", "values": [6, 5, 3, 6, 5, 1]},
        {"label": "Q3 2024", "values": [7, 3, 4, 5, 6, 2]},
        {"label": "Q4 2024", "values": [9, 2, 1, 9, 3, 3]},
    ],
}
