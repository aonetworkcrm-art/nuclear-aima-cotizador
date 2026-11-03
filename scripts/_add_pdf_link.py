#!/usr/bin/env python3
import re

path = "adspro-estrategia.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# Replace the actions section to add PDF download link before Imprimir
old = '  <div class="ap-actions">\n    <button class="ap-btn ap-btn-primary" onclick="window.print()">🖨 Imprimir Estrategia</button>'
new = '  <div class="ap-actions">\n    <a href="adspro-estrategia-ejecutivo.pdf" class="ap-btn ap-btn-primary" download>⬇️ Descargar PDF</a>\n    <button class="ap-btn ap-btn-primary" onclick="window.print()">🖨 Imprimir Estrategia</button>'

if old in html:
    html = html.replace(old, new, 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ PDF download link added. File size: {len(html):,} chars")
else:
    print("❌ Could not find the target text in the file.")
