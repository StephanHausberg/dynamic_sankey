"""
Example 02 — Energiemix
========================
Vereinfachter Energiefluss: Quellen → Umwandlung → Verbrauchssektoren.

Topologie (10 Nodes, 12 Links):

  Quellen       Umwandlung          Sektoren
  ──────────    ──────────────      ──────────────
  Wind    ──┐
  Solar   ──┤
  Gas     ──┼──► Stromerzeugung ──► Industrie
  Kohle   ──┘         │         └──► Haushalte
             └──► Wärme & Heizung──► Industrie
  Gas     ──►         │         └──► Haushalte
  Kohle   ──►─────────┘
                                  ► Verkehr (via Strom, E-Mobilität)

4 Zeitschritte = Quartale 2023.
Zeigt saisonale Variation: Winter → mehr Wind/Gas, Sommer → mehr Solar.
Im Jahresverlauf: leichte Verschiebung hin zu erneuerbaren Quellen.
Einheit: vereinfachte TWh/Quartal (illustrativ, nicht amtlich).
"""

SANKEY_CONFIG = {
    "nodes": [
        # Quellen
        {"id":  0, "label": "Wind",             "color": "#72B7B2"},
        {"id":  1, "label": "Solar",            "color": "#F5A623"},
        {"id":  2, "label": "Gas",              "color": "#4C78A8"},
        {"id":  3, "label": "Kohle",            "color": "#888888"},
        {"id":  4, "label": "Kernkraft",        "color": "#E45756"},
        # Umwandlung
        {"id":  5, "label": "Stromerzeugung",   "color": "#54A24B"},
        {"id":  6, "label": "Wärme & Heizung",  "color": "#B279A2"},
        # Sektoren
        {"id":  7, "label": "Industrie",        "color": "#4C78A8"},
        {"id":  8, "label": "Haushalte",        "color": "#54A24B"},
        {"id":  9, "label": "Verkehr",          "color": "#F58518"},
    ],
    "links": [
        # Quellen → Stromerzeugung
        {"source": 0, "target": 5},   #  0: Wind   → Strom
        {"source": 1, "target": 5},   #  1: Solar  → Strom
        {"source": 2, "target": 5},   #  2: Gas    → Strom
        {"source": 3, "target": 5},   #  3: Kohle  → Strom
        {"source": 4, "target": 5},   #  4: Kernkraft → Strom
        # Quellen → Wärme & Heizung
        {"source": 2, "target": 6},   #  5: Gas    → Wärme
        {"source": 3, "target": 6},   #  6: Kohle  → Wärme
        # Strom → Sektoren
        {"source": 5, "target": 7},   #  7: Strom  → Industrie
        {"source": 5, "target": 8},   #  8: Strom  → Haushalte
        {"source": 5, "target": 9},   #  9: Strom  → Verkehr (E-Mobilität)
        # Wärme → Sektoren
        {"source": 6, "target": 7},   # 10: Wärme  → Industrie
        {"source": 6, "target": 8},   # 11: Wärme  → Haushalte
    ],
    "time_series": [
        {
            # Q1: Winter — viel Wind, wenig Solar; Gas/Kohle noch stark
            "label": "Q1 2023",
            "values": [58, 14, 46, 38, 5,   28, 34,   52, 42, 14,   32, 30],
        },
        {
            # Q2: Frühling — Solar zieht an; erneuerbare Quellen wachsen
            "label": "Q2 2023",
            "values": [44, 36, 30, 24, 5,   20, 24,   42, 36, 10,   24, 20],
        },
        {
            # Q3: Sommer — Solar auf Spitze; Wind und Kohle am niedrigsten
            "label": "Q3 2023",
            "values": [32, 58, 24, 18, 0,   14, 18,   38, 30, 12,   18, 14],
        },
        {
            # Q4: Herbst/Winter — Wind wieder stark; Kernkraft abgeschaltet
            "label": "Q4 2023",
            "values": [62, 18, 38, 32, 0,   22, 28,   46, 38, 14,   26, 24],
        },
    ],
}
