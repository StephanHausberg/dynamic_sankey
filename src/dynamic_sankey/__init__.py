"""
dynamic-sankey
==============
Generate animated, standalone-HTML Sankey diagrams with true SVG morphing.

No server. No Plotly. Pure D3.js under the hood — the Python side only
serialises your config to JSON and injects it into the HTML template.

Quick start:
    from dynamic_sankey import generate_html
    html = generate_html(MY_CONFIG, title="My Flows")
    with open("output.html", "w") as f:
        f.write(html)
"""

from .generator import generate_html, validate_config

__version__ = "0.2.0"
__all__ = ["generate_html", "validate_config"]
