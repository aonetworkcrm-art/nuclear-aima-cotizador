import re

# Read CSVs (strip BOM)
with open('data/no_hay_nadie_mas_-_ramon_orlando_20260509_1909.csv', 'r', encoding='utf-8-sig') as f:
    live_csv = f.read()

with open('data/catalogo-completo-ramon-orlando.csv', 'r', encoding='utf-8-sig') as f:
    cat_csv = f.read()

# Escape backticks and ${} for JS template literal safety
# Note: we don't need to escape ${} in Python, but the shell does
# For JS template literals, only ` and ${ need escaping
live_csv_safe = live_csv.replace('\\', '\\\\').replace('`', '\\`')
cat_csv_safe = cat_csv.replace('\\', '\\\\').replace('`', '\\`')

# Also escape ${ for shell safety by escaping $ before {
# Actually for JS, we need to escape ${ only if it appears literally in the content
# Let's just check if any ${ exist
if '${' in live_csv_safe:
    print('WARNING: ${ found in live CSV, need to escape')
    live_csv_safe = live_csv_safe.replace('${', '\\${')
if '${' in cat_csv_safe:
    print('WARNING: ${ found in catalog CSV, need to escape')
    cat_csv_safe = cat_csv_safe.replace('${', '\\${')

# Read live-search.html
with open('live-search.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the empty template literals with actual data
old_live = 'const EMBEDDED_LIVE_CSV = `canal,titulo,url,fecha,vistas,vph,usd\n`;'
new_live = 'const EMBEDDED_LIVE_CSV = `' + live_csv_safe + '`;'

if old_live in html:
    html = html.replace(old_live, new_live, 1)
    print('LIVE CSV injected successfully (' + str(len(live_csv_safe)) + ' chars)')
else:
    print('ERROR: Could not find EMBEDDED_LIVE_CSV placeholder')
    idx = html.find('EMBEDDED_LIVE_CSV')
    if idx >= 0:
        print('Found at position', idx)
        print('Context:')
        print(repr(html[idx:idx+250]))

# EMBEDDED_CATALOG_CSV
old_cat = 'const EMBEDDED_CATALOG_CSV = `Canción,Catálogo,Período,Nodos,Vistas,Yield/mes,Auditada\n`;'
new_cat = 'const EMBEDDED_CATALOG_CSV = `' + cat_csv_safe + '`;'

if old_cat in html:
    html = html.replace(old_cat, new_cat, 1)
    print('CATALOG CSV injected successfully (' + str(len(cat_csv_safe)) + ' chars)')
else:
    print('ERROR: Could not find EMBEDDED_CATALOG_CSV placeholder')
    idx = html.find('EMBEDDED_CATALOG_CSV')
    if idx >= 0:
        print('Found at position', idx)
        print('Context:')
        print(repr(html[idx:idx+250]))

# Write updated file
with open('live-search.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('live-search.html updated successfully')
print('New file size:', len(html), 'bytes')
