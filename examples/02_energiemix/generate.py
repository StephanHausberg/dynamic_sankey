"""
Example 02 — Energiemix
========================
Erzeugt output.html im gleichen Verzeichnis.

Aufruf:
    python examples/02_energiemix/generate.py
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "src"))

from dynamic_sankey import generate_html
from config import SANKEY_CONFIG

html = generate_html(SANKEY_CONFIG, title="Energiemix Deutschland — Quartale 2023")

out = os.path.join(os.path.dirname(__file__), "output.html")
with open(out, "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅  {out}")

import webbrowser
webbrowser.open(f"file://{os.path.abspath(out)}")
