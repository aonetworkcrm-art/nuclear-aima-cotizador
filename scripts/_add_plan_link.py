#!/usr/bin/env python3
path = "adspro-estrategia.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# Add link to Plan Semanal Grupos before the back-to-proyecto link
old = '<a href="campanas-pagas.html" class="ap-btn ap-btn-back">📢 Campañas Pagas</a>\n    <a href="ramon-orlando-proyecto.html"'
new = '<a href="campanas-pagas.html" class="ap-btn ap-btn-back">📢 Campañas Pagas</a>\n    <a href="plan-semanal-grupos.html" class="ap-btn ap-btn-back">📅 Plan Semanal</a>\n    <a href="ramon-orlando-proyecto.html"'

if old in html:
    html = html.replace(old, new, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ Plan Semanal link added. File size: {len(html):,} chars")
else:
    print("❌ Could not find the target text.")
