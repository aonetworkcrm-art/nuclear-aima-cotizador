import re

# Read catalog CSV (strip BOM)
with open('data/catalogo-completo-ramon-orlando.csv', 'r', encoding='utf-8-sig') as f:
    cat_csv = f.read()

# Escape backticks for JS template literal safety
cat_csv_safe = cat_csv.replace('\\', '\\\\').replace('`', '\\`')

# Check for ${ that would break template literals
if '${' in cat_csv_safe:
    print('WARNING: ${ found in catalog CSV, need to escape')
    cat_csv_safe = cat_csv_safe.replace('${', '\\${')

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find the exact fetch block we need to replace
old_block = '''<script>
// ── Load CSV and render top yield table ──
fetch('data/catalogo-completo-ramon-orlando.csv')
  .then(r => r.text())
  .then(csv => {
    const lines = csv.split('\\n').filter(l => l.trim());
    if (lines.length < 2) return;
    const header = lines[0].split(',');
    const data = lines.slice(1).map(line => {
      const vals = [];
      let current = '', inQuotes = false;
      for (const ch of line) {
        if (ch === '"') { inQuotes = !inQuotes; continue; }
        if (ch === ',' && !inQuotes) { vals.push(current.trim()); current = ''; }
        else current += ch;
      }
      vals.push(current.trim());
      return vals;
    }).filter(d => d.length >= 7);

    // Sort by yield descending
    data.sort((a, b) => {
      const yieldA = parseInt(a[5]?.replace(/[^0-9]/g,'') || '0');
      const yieldB = parseInt(b[5]?.replace(/[^0-9]/g,'') || '0');
      return yieldB - yieldA;
    });

    const tbody = document.getElementById('yieldBody');
    tbody.innerHTML = data.slice(0, 30).map((row, i) => {
      const yieldVal = parseInt(row[5]?.replace(/[^0-9]/g,'') || '0');
      const yieldClass = yieldVal > 1000 ? 'yield-high' : yieldVal > 500 ? 'yield-mid' : 'yield-low';
      return `<tr>
        <td>${i + 1}</td>
        <td>${row[0] || ''}</td>
        <td>${row[1] || ''}</td>
        <td>${row[3] || ''}</td>
        <td>${parseInt(row[4]?.replace(/[^0-9]/g,'') || '0').toLocaleString()}</td>
        <td class="${yieldClass}">$${yieldVal.toLocaleString()}</td>
        <td>${(row[6] || '').trim() === 'Sí' ? '✅' : '⏳'}</td>
      </tr>`;
    }).join('');
  })
  .catch(() => {
    document.getElementById('yieldBody').innerHTML = '<tr><td colspan="7" style="text-align:center;color:var(--muted)">Esperando datos del oráculo...</td></tr>';
  });

</script>'''

new_block = '''<script>
// ── EMBEDDED CATALOG DATA (works with file:// protocol, no fetch needed) ──
const EMBEDDED_CATALOG_CSV = `''' + cat_csv_safe + '''`;

// ── Load CSV and render top yield table ──
function renderYieldTable(csvText) {
  if (csvText.charCodeAt(0) === 0xFEFF) csvText = csvText.slice(1);
  const lines = csvText.split('\\n').filter(l => l.trim());
  if (lines.length < 2) return;
  const data = lines.slice(1).map(line => {
    const vals = [];
    let current = '', inQuotes = false;
    for (const ch of line) {
      if (ch === '"') { inQuotes = !inQuotes; continue; }
      if (ch === ',' && !inQuotes) { vals.push(current.trim()); current = ''; }
      else current += ch;
    }
    vals.push(current.trim());
    return vals;
  }).filter(d => d.length >= 7);

  // Sort by yield descending
  data.sort((a, b) => {
    const yieldA = parseInt(a[5]?.replace(/[^0-9]/g,'') || '0');
    const yieldB = parseInt(b[5]?.replace(/[^0-9]/g,'') || '0');
    return yieldB - yieldA;
  });

  const tbody = document.getElementById('yieldBody');
  tbody.innerHTML = data.slice(0, 30).map((row, i) => {
    const yieldVal = parseInt(row[5]?.replace(/[^0-9]/g,'') || '0');
    const yieldClass = yieldVal > 1000 ? 'yield-high' : yieldVal > 500 ? 'yield-mid' : 'yield-low';
    return `<tr>
      <td>${i + 1}</td>
      <td>${row[0] || ''}</td>
      <td>${row[1] || ''}</td>
      <td>${row[3] || ''}</td>
      <td>${parseInt(row[4]?.replace(/[^0-9]/g,'') || '0').toLocaleString()}</td>
      <td class="${yieldClass}">$${yieldVal.toLocaleString()}</td>
      <td>${(row[6] || '').trim() === 'Sí' ? '✅' : '⏳'}</td>
    </tr>`;
  }).join('');
}

// Try fetch first, fall back to embedded data
fetch('data/catalogo-completo-ramon-orlando.csv?t=' + Date.now())
  .then(r => r.text())
  .then(csv => renderYieldTable(csv))
  .catch(() => renderYieldTable(EMBEDDED_CATALOG_CSV));

</script>'''

if old_block in html:
    html = html.replace(old_block, new_block, 1)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('index.html updated successfully')
    print('New file size:', len(html), 'bytes')
    print('Catalog CSV embedded:', len(cat_csv_safe), 'chars')
else:
    print('ERROR: Could not find the fetch block in index.html')
    # Debug
    idx = html.find('Load CSV')
    if idx >= 0:
        print('Found "Load CSV" at position', idx)
        print(repr(html[idx:idx+300]))
    else:
        print('Could not find "Load CSV" in the HTML')
