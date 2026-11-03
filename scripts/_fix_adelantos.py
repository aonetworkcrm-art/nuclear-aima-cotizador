#!/usr/bin/env python3
"""Apply standalone treatment to adelantos.html."""
import re

PATH = "adelantos.html"

with open(PATH, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Fix the broken comment and SGACEDOM + ASCAP + BMI section
# Current broken structure:
#   <!-- ════════════ 
#     <!-- SGACEDOM --> ... content ...
# TAB 3: CALCULADORA ════════════ -->
# Need to extract the SGACEDOM/ASCAP/BMI content and fix the tab structure

old_broken = '''  <!-- ════════════ \r\n    <!-- SGACEDOM -->'''
# More robust: find the specific pattern
broken_pattern = r'<!-- ════════════ \r?\n    <!-- SGACEDOM -->.*?TAB 3: CALCULADORA ════════════ -->'
match = re.search(broken_pattern, html, re.DOTALL)
if match:
    broken_section = match.group(0)
    # Extract the SGACEDOM, Content ID, ASCAP, BMI cards from within the broken comment
    # They are already valid HTML inside the comment
    # We need to move them to inside the tab-calculator div
    
    # Extract the cards from the broken section
    sgacedom_match = re.search(r'<!-- SGACEDOM -->.*?(?=<!-- |\Z)', broken_section, re.DOTALL)
    contentid_match = re.search(r'<!-- YouTube Content ID -->.*?(?=<!-- |\Z)', broken_section, re.DOTALL)
    ascap_match = re.search(r'<!-- ASCAP -->.*?(?=<!-- |\Z)', broken_section, re.DOTALL)
    bmi_match = re.search(r'<!-- BMI -->.*?(?=<!-- |\Z)', broken_section, re.DOTALL)
    
    # Actually let me look at what cards are in the comment more carefully
    # The comment starts at the line after TAB 2 ends and before TAB 3 starts
    # SGACEDOM card is inside the comment, then ASCAP, then BMI
    # But Content ID and YouTube Content ID might also be there
    
    # Simpler approach: Replace the broken comment with a proper tab separator
    replacement = '  <!-- ════════════ TAB 3: CALCULADORA ════════════ -->'
    # But we also need to keep the platform cards that were inside the comment
    # Extract all content between the broken open and close
    
    # Let me just find what's between the broken open and the closing -->
    start = html.find('<!-- ════════════ \n    <!-- SGACEDOM -->')
    if start == -1:
        start = html.find('<!-- \n    <!-- SGACEDOM -->')
    if start == -1:
        start = html.find('<!-- ════════════ \r\n    <!-- SGACEDOM -->')
    
    if start >= 0:
        end = html.find('TAB 3: CALCULADORA ════════════ -->', start)
        if end >= 0:
            end += len('TAB 3: CALCULADORA ════════════ -->')
            
            # Extract the platform cards
            cards_content = html[start:end]
            # Remove the outer comment markers to get clean HTML
            cards_clean = cards_content.replace('<!-- ════════════ ', '')
            cards_clean = cards_clean.replace('\n    <!-- SGACEDOM -->', '\n    <!-- SGACEDOM -->')
            
            # Actually let me just strip the outermost comment
            cards_clean = re.sub(r'^<!-- .*? -->\n?\r?', '', cards_content)
            cards_clean = re.sub(r'TAB 3: CALCULADORA ════════════ -->$', '', cards_clean)
            
            # Replace the broken section with just the cards (uncommented) + proper tab marker
            new_section = cards_clean + '\n  <!-- ════════════ TAB 3: CALCULADORA ════════════ -->'
            html = html[:start] + new_section + html[end:]
            
            print(f"Fixed broken section: {len(cards_content)} bytes replaced")
else:
    print("WARNING: Could not find broken comment pattern. Trying alternative...")
    # Try alternative pattern
    if '<!-- ════════════ ' in html and '    <!-- SGACEDOM -->' in html:
        idx = html.find('    <!-- SGACEDOM -->')
        # Find the opening comment before it
        prev = html.rfind('<!--', 0, idx)
        if prev >= 0:
            # Find the closing of the big comment
            end = html.find('TAB 3: CALCULADORA ════════════ -->', idx)
            if end >= 0:
                end += len('TAB 3: CALCULADORA ════════════ -->')
                # Extract the cards
                cards = html[idx:end]
                cards = cards.replace('TAB 3: CALCULADORA ════════════ -->', '')
                # Remove leading/trailing whitespace
                cards = cards.strip()
                # Now uncomment the SGACEDOM start
                # The comment structure is: <!-- ════════════ \n    <!-- SGACEDOM --> ... ASCAP ... BMI ... TAB 3: ...
                # So we need to go back further
                pass
    
    print("Could not automatically fix. Manual inspection needed.")

# 2. Add OG/meta tags after the <title>
old_title = '''<title>💰 Adelantos · Financiamiento · Nuclear AIMA</title>'''
new_title = '''<title>💰 Adelantos · Plataformas de Financiamiento · Nuclear AIMA</title>
<meta name="description" content="Guía completa de financiamiento para catálogos musicales: SoundExchange, beatBread, Believe, The Orchard, Content ID, ASCAP, BMI, SGACEDOM. Calcula tu adelanto estimado.">
<meta name="keywords" content="adelanto, financiamiento, SoundExchange, beatBread, Believe, The Orchard, Content ID, ASCAP, BMI, SGACEDOM, regalías, música, Nuclear AIMA">
<meta name="author" content="Nuclear AIMA">
<meta name="robots" content="index, follow">
<!-- Open Graph -->
<meta property="og:type" content="website">
<meta property="og:title" content="Adelantos · Plataformas de Financiamiento para Catálogos Musicales">
<meta property="og:description" content="Guía completa: SoundExchange, beatBread, Believe, The Orchard, Content ID, ASCAP, BMI, SGACEDOM. Calcula tu adelanto estimado.">
<meta property="og:site_name" content="Nuclear AIMA">
<meta property="og:locale" content="es_DO">
<meta property="og:image" content="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1200 630'%3E%3Crect width='1200' height='630' fill='%230a0a0c'/%3E%3Crect x='40' y='40' width='1120' height='550' rx='16' fill='none' stroke='%234cad7c' stroke-width='2'/%3E%3Ctext x='600' y='220' text-anchor='middle' font-family='Inter,system-ui,sans-serif' font-size='52' font-weight='700' fill='%23f0ede8'%3EAdelantos%3C/text%3E%3Ctext x='600' y='290' text-anchor='middle' font-family='Inter,system-ui,sans-serif' font-size='26' fill='%234cad7c'%3EFinanciamiento para Catalogos Musicales%3C/text%3E%3Ctext x='600' y='370' text-anchor='middle' font-family='monospace' font-size='20' fill='%236b6966'%3ESoundExchange · beatBread · Believe · The Orchard%3C/text%3E%3Ctext x='600' y='420' text-anchor='middle' font-family='monospace' font-size='18' fill='%23c9a96e'%3EContent ID · ASCAP · BMI · SGACEDOM%3C/text%3E%3Ctext x='600' y='490' text-anchor='middle' font-family='monospace' font-size='16' fill='%236b6966'%3Enuclearaima.com%3C/text%3E%3C/svg%3E">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:type" content="image/svg+xml">
<meta property="og:url" content="https://nuclearaima.com/adelantos.html">
<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Adelantos · Plataformas de Financiamiento para Catálogos Musicales">
<meta name="twitter:description" content="Guía completa: SoundExchange, beatBread, Believe, The Orchard, Content ID, ASCAP, BMI, SGACEDOM. Calcula tu adelanto estimado.">
<meta name="twitter:image" content="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1200 630'%3E%3Crect width='1200' height='630' fill='%230a0a0c'/%3E%3Crect x='40' y='40' width='1120' height='550' rx='16' fill='none' stroke='%234cad7c' stroke-width='2'/%3E%3Ctext x='600' y='220' text-anchor='middle' font-family='Inter,system-ui,sans-serif' font-size='52' font-weight='700' fill='%23f0ede8'%3EAdelantos%3C/text%3E%3Ctext x='600' y='290' text-anchor='middle' font-family='Inter,system-ui,sans-serif' font-size='26' fill='%234cad7c'%3EFinanciamiento para Catalogos Musicales%3C/text%3E%3Ctext x='600' y='370' text-anchor='middle' font-family='monospace' font-size='20' fill='%236b6966'%3ESoundExchange · beatBread · Believe · The Orchard%3C/text%3E%3Ctext x='600' y='420' text-anchor='middle' font-family='monospace' font-size='18' fill='%23c9a96e'%3EContent ID · ASCAP · BMI · SGACEDOM%3C/text%3E%3Ctext x='600' y='490' text-anchor='middle' font-family='monospace' font-size='16' fill='%236b6966'%3Enuclearaima.com%3C/text%3E%3C/svg%3E">
'''
if old_title in html:
    html = html.replace(old_title, new_title, 1)
    print("OG/meta tags added")
else:
    print("WARNING: Could not find <title> to add OG tags")

# 3. Add premium badges and action buttons after the header paragraph
old_header_end = '''    <p>Guía completa para conseguir adelantos sobre el catálogo de Ramón Orlando — Desde SoundExchange hasta Believe/The Orchard</p>\n  </div>'''
new_header = '''    <p>Guía completa para conseguir adelantos sobre el catálogo de Ramón Orlando — Desde SoundExchange hasta Believe/The Orchard</p>
  </div>

  <!-- ═══ STATS ROW ═══ -->
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:16px 0" class="ad-stats">
    <div style="background:var(--bg2);border:0.5px solid var(--border);border-radius:var(--r);padding:10px;text-align:center">
      <div style="font-size:7px;color:var(--muted);text-transform:uppercase;letter-spacing:0.07em">Adelanto Objetivo</div>
      <div style="font-size:17px;font-weight:700;font-family:var(--mono);color:var(--success);margin-top:2px">$150K-$500K</div>
    </div>
    <div style="background:var(--bg2);border:0.5px solid var(--border);border-radius:var(--r);padding:10px;text-align:center">
      <div style="font-size:7px;color:var(--muted);text-transform:uppercase;letter-spacing:0.07em">Plataformas</div>
      <div style="font-size:17px;font-weight:700;font-family:var(--mono);color:var(--accent);margin-top:2px">7</div>
    </div>
    <div style="background:var(--bg2);border:0.5px solid var(--border);border-radius:var(--r);padding:10px;text-align:center">
      <div style="font-size:7px;color:var(--muted);text-transform:uppercase;letter-spacing:0.07em">Retroactivo SX</div>
      <div style="font-size:17px;font-weight:700;font-family:var(--mono);color:var(--gold);margin-top:2px">$40K-$80K</div>
    </div>
    <div style="background:var(--bg2);border:0.5px solid var(--border);border-radius:var(--r);padding:10px;text-align:center">
      <div style="font-size:7px;color:var(--muted);text-transform:uppercase;letter-spacing:0.07em">Sin Ceder</div>
      <div style="font-size:17px;font-weight:700;font-family:var(--mono);color:var(--cyan);margin-top:2px">Propiedad</div>
    </div>
  </div>

  <!-- ═══ ACTIONS ═══ -->
  <div style="display:flex;justify-content:center;gap:10px;margin:14px 0;flex-wrap:wrap">
    <a href="adelantos-ejecutivo.pdf" style="display:inline-flex;align-items:center;gap:6px;padding:8px 16px;border-radius:var(--r);border:none;cursor:pointer;font-size:11px;font-weight:500;font-family:var(--font);transition:all 0.15s;text-decoration:none;background:linear-gradient(135deg,rgba(76,173,124,0.15),rgba(76,173,124,0.05));color:var(--success);border:0.5px solid rgba(76,173,124,0.3)" download>⬇ Descargar PDF</a>
    <button style="display:inline-flex;align-items:center;gap:6px;padding:8px 16px;border-radius:var(--r);border:none;cursor:pointer;font-size:11px;font-weight:500;font-family:var(--font);transition:all 0.15s;background:var(--accent);color:#0d0d0f" onclick="window.print()">🖨 Imprimir</button>
    <a href="master-plan.html" style="display:inline-flex;align-items:center;gap:6px;padding:8px 16px;border-radius:var(--r);border:none;cursor:pointer;font-size:11px;font-weight:500;font-family:var(--font);transition:all 0.15s;text-decoration:none;background:var(--bg2);color:var(--accent);border:0.5px solid rgba(201,169,110,0.2)">← Master Plan</a>
  </div>
  '''
if old_header_end in html:
    html = html.replace(old_header_end, new_header, 1)
    print("Premium header badges and action buttons added")
else:
    print("WARNING: Could not find header end to add badges/actions")

# 4. Add print styles before the closing </style>
old_style_end = '''  @media (max-width: 768px) {
    .main-content { padding: 10px; }
    .tab-btn { font-size: 9px; padding: 5px 8px; }
    .platform-card { padding: 14px; }
    .calc-row { flex-direction: column; }
    .calc-row input[type="number"] { width: 100%; }
  }\n</style>'''
new_print_styles = '''  @media (max-width: 768px) {
    .main-content { padding: 10px; }
    .tab-btn { font-size: 9px; padding: 5px 8px; }
    .platform-card { padding: 14px; }
    .calc-row { flex-direction: column; }
    .calc-row input[type="number"] { width: 100%; }
  }

  /* ── Print Styles ── */
  @media print {
    body{background:#fff;color:#111;-webkit-print-color-adjust:exact;print-color-adjust:exact}
    .main-content{max-width:100%;padding:8px}
    .ad-header{border-bottom-color:#ddd;padding:12px 0}
    .ad-header h1{font-size:22px}
    .ad-header h1 span{color:#3d8b5e}
    .ad-header p{color:#555}
    .ad-header .badge{background:#f0f0f0!important;color:#3d8b5e!important;border-color:#3d8b5e!important}
    .ad-stats > div{background:#f8f8f8!important;border-color:#ddd!important}
    .tab-nav{display:none!important}
    .tab-content{display:block!important}
    .platform-card,.calc-section,.pitch-card,.strategy-box,.highlight-box{background:#f8f8f8!important;border-color:#ddd!important;box-shadow:none!important;page-break-inside:avoid}
    .platform-card .p-metric,.calc-result,.metric-item{background:#eee!important;border-color:#ddd!important}
    .platform-card .p-step .step-num{background:#3d8b5e!important;color:#fff!important}
    .platform-card .p-step .step-text strong{color:#3d8b5e!important}
    .btn-success,.btn-primary{background:#3d8b5e!important;color:#fff!important}
    .btn-ghost-ext{background:transparent!important;color:#333!important;border-color:#ccc!important}
    .calc-section h3,.pitch-card h3{color:#3d8b5e!important}
    .calc-result .cval{color:#333!important}
    .calc-result .cval.success,.calc-result .cval.accent,.calc-result .cval.cyan,.calc-result .cval.gold{color:#3d8b5e!important}
    .calc-result .cval.danger{color:#c0392b!important}
    .strategy-box{background:#f5f5f5!important}
    .strategy-box h3{color:#3d8b5e!important}
    .strategy-box .s-item{border-left-color:#3d8b5e!important}
    .strategy-box .s-item strong{color:#333!important}
    .highlight-box .hl{color:#3d8b5e!important}
    .platform-card .p-metric .mlbl,.calc-result .clbl,.metric-item .mlbl{color:#777!important}
    .platform-card .p-metric .mval,.metric-item .mval{color:#333!important}
    .platform-card .p-metric .mval.success,.metric-item .mval.success{color:#3d8b5e!important}
    .platform-card .p-metric .mval.danger,.metric-item .mval.danger{color:#c0392b!important}
    .platform-card .p-metric .mval.cyan,.metric-item .mval.cyan{color:#1a7a8a!important}
    .platform-card .p-metric .mval.accent,.metric-item .mval.accent{color:#8a6d2b!important}
    .timeline-item .dot{background:#3d8b5e!important}
    .timeline-item .dot.success{background:#3d8b5e!important}
    .timeline-item .dot.danger{background:#c0392b!important}
    .platform-card .p-info .p-tag.advance{background:#e8f5ee!important;color:#3d8b5e!important}
    .platform-card .p-info .p-tag.dist{background:#d0f0f5!important;color:#1a7a8a!important}
    .platform-card .p-info .p-tag.royalty{background:#f5e6c8!important;color:#8a6d2b!important}
    a{color:#3d8b5e!important}
    .ns-sidebar,.ns-mobile-hamburger,#nuclear-sidebar{display:none!important}
    body.ns-sidebar-ready{margin-left:0!important}
    div[style*="border-top:0.5px"] p{color:#555!important}
    @page{margin:12mm}
    h3{page-break-after:avoid}
  }\n</style>'''
if old_style_end in html:
    html = html.replace(old_style_end, new_print_styles, 1)
    print("Print styles added")
else:
    print("WARNING: Could not find </style> to add print styles")

# 5. Update footer text
old_footer = '''    <p style="font-size:9px;color:var(--muted);font-family:var(--mono)">
      💰 Adelantos · Nuclear AIMA · Basado en datos del catálogo Ramón Orlando · Tasas de mercado 2026
    </p>'''
new_footer = '''    <p style="font-size:9px;color:var(--muted);font-family:var(--mono)">
      💰 Adelantos · Nuclear AIMA · Basado en datos del catálogo Ramón Orlando · Tasas de mercado 2026
    </p>
    <div style="display:flex;justify-content:center;gap:14px;flex-wrap:wrap;margin-top:6px">
      <a href="pasos-estrella.html" style="color:var(--accent);text-decoration:none;font-size:10px">⭐ Pasos Estrella</a>
      <a href="onapi-onda.html" style="color:var(--accent);text-decoration:none;font-size:10px">🏛️ Guía ONAPI/ONDA/SAS</a>
      <a href="master-plan.html" style="color:var(--accent);text-decoration:none;font-size:10px">⭐ Master Plan</a>
      <a href="index.html" style="color:var(--accent);text-decoration:none;font-size:10px">📊 Dashboard</a>
    </div>'''
if old_footer in html:
    html = html.replace(old_footer, new_footer, 1)
    print("Footer updated with nav links")
else:
    print("WARNING: Could not find footer to update")

# Write result
with open(PATH, "w", encoding="utf-8") as f:
    f.write(html)

print(f"\nFile written: {len(html)} bytes")
