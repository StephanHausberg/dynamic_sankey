"""
Example 03 — Customer Journey
==============================
Website-Traffic-Fluss: Quellen → Landing Pages → Conversion-Ziele.

Topologie (11 Nodes, 12 Links):

  Traffic-Quellen   Landing Pages     Conversion-Ziele
  ───────────────   ─────────────     ────────────────
  Organic Search ──► Homepage    ──► Kauf
  Paid Ads       ──► Produktseite──► Lead / Kontakt
  Social Media   ──► Blog        ──► Newsletter
  Direct / E-Mail──►             └──► Absprung

4 Zeitschritte = Quartale 2024.
Zeigt typisches Jahresmuster: Q4 mit Holiday-Spike bei Käufen,
Q1 mit etwas mehr Blog-Traffic durch Content-Kampagne.
Einheit: Besucher (illustrativ).
"""

SANKEY_CONFIG = {
    "nodes": [
        # Traffic-Quellen
        {"id":  0, "label": "Organic Search",  "color": "#4C78A8"},
        {"id":  1, "label": "Paid Ads",        "color": "#F58518"},
        {"id":  2, "label": "Social Media",    "color": "#E45756"},
        {"id":  3, "label": "Direct / E-Mail", "color": "#72B7B2"},
        # Landing Pages
        {"id":  4, "label": "Homepage",        "color": "#888888"},
        {"id":  5, "label": "Produktseite",    "color": "#B279A2"},
        {"id":  6, "label": "Blog / Content",  "color": "#FF9DA7"},
        # Conversion-Ziele
        {"id":  7, "label": "Kauf",            "color": "#54A24B"},
        {"id":  8, "label": "Lead / Kontakt",  "color": "#4C78A8"},
        {"id":  9, "label": "Newsletter",      "color": "#F5A623"},
        {"id": 10, "label": "Absprung",        "color": "#E45756"},
    ],
    "links": [
        # Traffic-Quellen → Landing Pages
        {"source": 0, "target": 4},   #  0: Organic  → Homepage
        {"source": 0, "target": 6},   #  1: Organic  → Blog
        {"source": 1, "target": 5},   #  2: Paid     → Produktseite
        {"source": 1, "target": 4},   #  3: Paid     → Homepage
        {"source": 2, "target": 6},   #  4: Social   → Blog
        {"source": 2, "target": 4},   #  5: Social   → Homepage
        {"source": 3, "target": 5},   #  6: Direct   → Produktseite (E-Mail-Kampagne)
        # Landing Pages → Conversion-Ziele
        {"source": 4, "target": 5},   #  7: Homepage → Produktseite
        {"source": 4, "target": 10},  #  8: Homepage → Absprung
        {"source": 5, "target": 7},   #  9: Produkt  → Kauf
        {"source": 5, "target": 8},   # 10: Produkt  → Lead / Kontakt
        {"source": 6, "target": 9},   # 11: Blog     → Newsletter
    ],
    "time_series": [
        {
            # Q1: nach Weihnachten ruhiger; Blog-Traffic durch New-Year-Content hoch
            "label": "Q1 2024",
            "values": [420, 95,  120, 60,  160, 55,  65,  195, 300,  175, 110, 190],
        },
        {
            # Q2: Frühlings-Kampagne; Paid Ads hochgefahren
            "label": "Q2 2024",
            "values": [480, 110, 155, 95,  145, 65,  85,  230, 315,  205, 125, 200],
        },
        {
            # Q3: Sommer-Delle; Social Media aktiver durch Influencer-Kooperationen
            "label": "Q3 2024",
            "values": [450, 100, 140, 85,  190, 60,  75,  210, 295,  190, 140, 190],
        },
        {
            # Q4: Holiday-Spike; Paid Ads auf Maximum; Käufe steigen stark
            "label": "Q4 2024",
            "values": [510, 105, 210, 130, 150, 75,  120, 275, 330,  280, 155, 205],
        },
    ],
}
