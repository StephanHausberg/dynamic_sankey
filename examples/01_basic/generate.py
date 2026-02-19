"""
Example 01 — Basic
==================
Erzeugt output.html im gleichen Verzeichnis.

Aufruf:
    python examples/01_basic/generate.py
"""

import os
import sys

# Damit das Beispiel auch ohne installiertes Paket läuft
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))

from dynamic_sankey import generate_html
from config import SANKEY_CONFIG

html = generate_html(SANKEY_CONFIG, title="Basic Sankey — Q1–Q4 2024")

out = os.path.join(os.path.dirname(__file__), "output.html")
with open(out, "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅  {out}")

import webbrowser
webbrowser.open(f"file://{os.path.abspath(out)}")
