"""
Example 04 — Smart Building Energy Monitor
===========================================
Monatliche Energieflüsse eines mittelgroßen Büro-/Produktionsgebäudes,
simuliert auf Basis typischer Sensordaten.

Topologie (8 Nodes, 10 Links):

  Quellen          Subsysteme         Verbrauchsbereiche
  ─────────────    ─────────────      ─────────────────────
  Netzstrom   ──► HLK-Anlage    ──► Büro & Verwaltung
              ──► Beleuchtung   ──► Außen- & Allgem.-flächen
              ──► Produktion         (direkte Einspeisung)
  PV-Anlage   ──► HLK-Anlage   ──► Wärmeverluste
              ──► Beleuchtung

12 Zeitschritte = Monate Jan–Dez 2024.

Saisonales Muster:
  - Jan/Feb/Nov/Dec: hohe Heizlast (HLK), minimale PV-Einspeisung
  - Jun/Jul/Aug:     hohe Kühllast (HLK), maximale PV-Einspeisung
  - Mrz/Apr/Sep/Okt: Übergangsmonate, niedrige HVAC-Last, mittlere PV

Einheit: kWh/Monat (vereinfacht, illustrativ)

Farbgebung: bewusst schlicht gehalten — gedeckte Grau- und Blautöne.
"""

SANKEY_CONFIG = {
    "nodes": [
        # Quellen
        {"id": 0, "label": "Netzstrom",          "color": "#5A6472"},
        {"id": 1, "label": "PV-Anlage",           "color": "#C8943A"},
        # Subsysteme
        {"id": 2, "label": "HLK-Anlage",          "color": "#4A7FA0"},
        {"id": 3, "label": "Beleuchtung",         "color": "#9A9070"},
        # Verbrauchsbereiche
        {"id": 4, "label": "Produktion",          "color": "#6A7868"},
        {"id": 5, "label": "Büro & Verwaltung",   "color": "#7A8C9A"},
        {"id": 6, "label": "Außen- & Allg.-fl.",  "color": "#8A9A82"},
        {"id": 7, "label": "Wärmeverluste",       "color": "#B09898"},
    ],
    "links": [
        # Quellen → Subsysteme
        {"source": 0, "target": 2},   #  0: Netz      → HLK
        {"source": 0, "target": 3},   #  1: Netz      → Beleuchtung
        {"source": 0, "target": 4},   #  2: Netz      → Produktion (direkt)
        {"source": 1, "target": 2},   #  3: PV        → HLK
        {"source": 1, "target": 3},   #  4: PV        → Beleuchtung
        # Subsysteme → Verbrauchsbereiche
        {"source": 2, "target": 5},   #  5: HLK       → Büro
        {"source": 2, "target": 6},   #  6: HLK       → Außenflächen
        {"source": 2, "target": 7},   #  7: HLK       → Wärmeverluste
        {"source": 3, "target": 5},   #  8: Bel.      → Büro
        {"source": 3, "target": 6},   #  9: Bel.      → Außenflächen
    ],
    "time_series": [
        # fmt: [Netz→HLK, Netz→Bel, Netz→Prod, PV→HLK, PV→Bel,
        #        HLK→Büro, HLK→Außen, HLK→Verlust, Bel→Büro, Bel→Außen]
        {
            "label": "Jan 2024",
            "values": [850, 175, 320, 40,  10,  545, 175, 170, 148, 37],
        },
        {
            "label": "Feb 2024",
            "values": [795, 168, 312, 75,  18,  530, 168, 172, 143, 43],
        },
        {
            "label": "Mrz 2024",
            "values": [495, 148, 330, 135, 38,  390, 150,  90, 140, 46],
        },
        {
            "label": "Apr 2024",
            "values": [195, 128, 342, 185, 58,  240,  95,  45, 128, 58],
        },
        {
            "label": "Mai 2024",
            "values": [248, 108, 352, 225, 72,  300, 112,  61, 118, 62],
        },
        {
            "label": "Jun 2024",
            "values": [548,  98, 362, 285, 82,  520, 200, 113, 112, 68],
        },
        {
            "label": "Jul 2024",
            "values": [682,  93, 358, 265, 78,  600, 232, 115, 108, 63],
        },
        {
            "label": "Aug 2024",
            "values": [618,  98, 348, 258, 73,  558, 214, 104, 112, 59],
        },
        {
            "label": "Sep 2024",
            "values": [278, 118, 338, 205, 62,  318, 122,  43, 128, 52],
        },
        {
            "label": "Okt 2024",
            "values": [448, 142, 328, 122, 32,  368, 138,  64, 138, 36],
        },
        {
            "label": "Nov 2024",
            "values": [718, 168, 318,  58, 15,  488, 182, 106, 143, 40],
        },
        {
            "label": "Dez 2024",
            "values": [868, 182, 308,  38, 10,  562, 192, 152, 152, 40],
        },
    ],
    "animation": {
        "transition_ms":    800,   # längere Überblendung für smooth morph
        "play_interval_ms": 1200,  # etwas mehr Pause zwischen Monaten
        "easing":           "easeSinInOut",  # sanfter als cubic
    },
}
