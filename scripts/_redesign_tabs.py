#!/usr/bin/env python3
"""
Redesigns all 4 Master Plan tabs with premium look.
Adds hero sections + enhanced CSS while keeping existing JS-compatible HTML structure.
"""
import re

with open('master-plan.html', 'r', encoding='utf-8') as f:
    html = f.read()

# ============================================================
# 1. ADD PREMIUM CSS
# ============================================================
premium_css = """
  /* ── Premium Tab Hero ── */
  .mp-hero { text-align:center; padding:6px 0 14px; }
  .mp-hero-tags { display:flex; justify-content:center; gap:5px; flex-wrap:wrap; margin-bottom:8px; }
  .mp-hero-tag { display:inline-flex; align-items:center; gap:3px; font-size:7px; font-weight:600; letter-spacing:0.07em; padding:2px 8px; border-radius:10px; background:var(--bg3); color:var(--muted); border:0.5px solid var(--border); text-transform:uppercase; }
  .mp-hero-tag.accent { background:linear-gradient(135deg,rgba(201,169,110,0.12),rgba(201,169,110,0.04)); border-color:rgba(201,169,110,0.25); color:var(--accent); }
  .mp-hero-tag.cyan { background:linear-gradient(135deg,rgba(74,208,224,0.1),rgba(74,208,224,0.03)); border-color:rgba(74,208,224,0.2); color:var(--cyan); }
  .mp-hero-tag.green { background:linear-gradient(135deg,rgba(76,173,124,0.1),rgba(76,173,124,0.03)); border-color:rgba(76,173,124,0.2); color:var(--success); }
  .mp-hero-title { font-size:18px; font-weight:700; letter-spacing:-0.3px; margin-bottom:2px; }
  .mp-hero-title .hl { color:var(--gold); }
  .mp-hero-sub { font-size:9px; color:var(--muted); max-width:500px; margin:0 auto; line-height:1.5; }

  /* ── Enhanced Phase Cards ── */
  .pc { transition:all 0.25s; border-left:2px solid transparent; }
  .pc:hover { border-color:rgba(201,169,110,0.2); }
  .pc .ph .pn2 { transition:all 0.3s; }
  .pc .ph .pi2 h3 { font-size:13px; }
  .pc .ph .ps3 { font-size:8px; }
  .pc .ph .ar { font-size:10px; }
  .cl .cl2 { transition:all 0.15s; padding:5px 0; }
  .cl .cl2:hover { background:rgba(201,169,110,0.03); border-radius:4px; padding-left:4px; padding-right:4px; }

  .phase-flow { display:flex; align-items:center; justify-content:center; gap:0; margin:12px 0 16px; padding:8px 12px; background:var(--bg2); border:0.5px solid var(--border); border-radius:var(--r2); flex-wrap:wrap; }
  .phase-flow-item { display:flex; flex-direction:column; align-items:center; gap:2px; padding:3px 6px; border-radius:var(--r); }
  .phase-flow-num { width:22px; height:22px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-size:8px; font-weight:700; background:var(--bg4); color:var(--muted); border:0.5px solid var(--border); }
  .phase-flow-item.active .phase-flow-num { background:var(--accent); color:#0d0d0f; }
  .phase-flow-label { font-size:6px; font-weight:600; color:var(--muted); text-transform:uppercase; letter-spacing:0.06em; }
  .phase-flow-item.active .phase-flow-label { color:var(--text); }
  .phase-flow-arrow { color:var(--muted); font-size:10px; opacity:0.3; margin:0 1px; }

  /* ── Enhanced Timeline ── */
  .tl { padding:20px 0 16px 30px; }
  .tl::before { left:11px; width:2px; background:linear-gradient(180deg,var(--accent),var(--success),var(--gold),var(--cyan),#a855f7); }
  .tli { margin-bottom:18px; padding:10px 14px; background:var(--bg2); border:0.5px solid var(--border); border-radius:var(--r); transition:all 0.2s; }
  .tli:hover { border-color:rgba(201,169,110,0.2); transform:translateX(2px); }
  .tli .dot { left:-26px; top:14px; width:12px; height:12px; border:2px solid var(--bg); box-shadow:0 0 0 2px rgba(201,169,110,0.3); }
  .tli .dot.dn { box-shadow:0 0 0 2px rgba(76,173,124,0.4); }
  .tli h4 { font-size:11px; }
  .tli .ti { font-size:8px; }
  .tli .td2 { font-size:10px; }

  /* ── Enhanced Metrics ── */
  .mg { gap:8px; }
  .mc3 { padding:14px 10px; transition:all 0.2s; position:relative; overflow:hidden; }
  .mc3:hover { transform:translateY(-2px); border-color:rgba(201,169,110,0.3); box-shadow:0 6px 24px rgba(0,0,0,0.3); }
  .mc3 .ml { font-size:7px; }
  .mc3 .mv { font-size:20px; }
  .mc3 .mnote { font-size:8px; color:var(--muted); margin-top:4px; }
  .mc3 .mv.accent { color:var(--accent); }
  .mc3 .mv.success { color:var(--success); }
  .mc3 .mv.gold { color:var(--gold); }
  .mc3 .mv.danger { color:var(--danger); }
  .mc3 .mv.cyan { color:var(--cyan); }
  .mc3::after { content:''; position:absolute; top:0; left:0; right:0; height:2px; background:linear-gradient(90deg,transparent,var(--accent),transparent); opacity:0; transition:opacity 0.3s; }
  .mc3:hover::after { opacity:1; }

  /* ── Enhanced Templates ── */
  .tb { font-size:10px; padding:10px 12px; line-height:1.6; border-left:2px solid var(--border); }
  .tb:hover { border-left-color:var(--accent); }
  .tb .cpy { font-size:7px; padding:1px 6px; }

  /* ── Enhanced Filter / Search Bar ── */
  .sb { background:var(--bg2); border:0.5px solid var(--border); border-radius:var(--r2); padding:8px 10px; }
  .sb input { font-size:10px; padding:6px 10px; }
  .filter-btn { font-size:8px; padding:4px 8px; border-radius:var(--r); border:0.5px solid var(--border); cursor:pointer; background:var(--bg3); color:var(--muted); font-weight:500; transition:all 0.15s; font-family:var(--font); }
  .filter-btn:hover { background:var(--bg4); color:var(--text); }
  .filter-btn.act { background:var(--accent); color:#0d0d0f; border-color:var(--accent); }

  /* ── Enhanced Phase Footer ── */
  .phase-footer { display:flex; justify-content:space-between; align-items:center; padding:8px 10px; background:var(--bg3); border-radius:var(--r); margin:10px 0; border:0.5px solid var(--border); flex-wrap:wrap; gap:4px; }
  .phase-footer .pf-item { font-size:8px; color:var(--muted); display:flex; align-items:center; gap:4px; }
  .phase-footer .pf-item strong { color:var(--text); }
"""

# Insert premium CSS before the closing </style> tag
css_insert_marker = '  .pe-complete-item strong { color:var(--text); }\n</style>'
assert css_insert_marker in html, "CSS insert marker not found!"
html = html.replace(css_insert_marker, premium_css + css_insert_marker)

print("✅ Premium CSS added")

# ============================================================
# 2. REDESIGN tab-phases
# ============================================================
old_phases = """<div class="tc act" id="tab-phases">
<div class="sb"><input type="text" id="searchInput" placeholder="Buscar en fases..." oninput="filterPhases()"><button class="filter-btn act" onclick="filterStatus('all')">Todas</button><button class="filter-btn" onclick="filterStatus('active')">En Progreso</button><button class="filter-btn" onclick="filterStatus('pending')">Pendientes</button></div>
<div class="pc">
<div class="ph" onclick="togglePhase(this)">
<div class="pn2 an">🏛️</div>
<div class="pi2"><h3>Fase 1: Fundacion Legal y Corporativa</h3><div class="psb">ONAPI, SRL, ONDA, Contrato Matriz</div></div>
<div class="ps3 an">$800 - $1,200 USD</div>
<div class="ar">&#x25BC;</div>
</div>
<div class="pb2">
<div class="pd2">Establecer la infraestructura legal y corporativa necesaria para operar como sello independiente y negociar con distribuidoras internacionales.</div>
<div class="mr">
<span class="mc2 accent">Semanas 1-3</span>
<span class="mc2 success">$800 - $1,200 USD</span>
<span class="mc2">8 tareas</span>
<span class="mc2 an">En Progreso</span>
</div>
<div class="cl">
<div class="cl2" onclick="toggleTask(this, 'p1_0')"><div class="cb" id="cb_p1_0"></div><div class="ct" id="ct_p1_0">Registrar Nombre Comercial en ONAPI (Clase 41 y 35)</div></div>
<div class="cl2" onclick="toggleTask(this, 'p1_1')"><div class="cb" id="cb_p1_1"></div><div class="ct" id="ct_p1_1">Redactar estatutos SAS y pagar impuesto DGII</div></div>
<div class="cl2" onclick="toggleTask(this, 'p1_2')"><div class="cb" id="cb_p1_2"></div><div class="ct" id="ct_p1_2">Registro Mercantil en Camara de Comercio</div></div>
<div class="cl2" onclick="toggleTask(this, 'p1_3')"><div class="cb" id="cb_p1_3"></div><div class="ct" id="ct_p1_3">Obtener RNC (Registro Nacional Contribuyente)</div></div>
<div class="cl2" onclick="toggleTask(this, 'p1_4')"><div class="cb" id="cb_p1_4"></div><div class="ct" id="ct_p1_4">Registrar fonograma en ONDA a nombre de la empresa</div></div>
<div class="cl2" onclick="toggleTask(this, 'p1_5')"><div class="cb" id="cb_p1_5"></div><div class="ct" id="ct_p1_5">Firmar Contrato de Administracion con el artista</div></div>
<div class="cl2" onclick="toggleTask(this, 'p1_6')"><div class="cb" id="cb_p1_6"></div><div class="ct" id="ct_p1_6">Abrir cuenta bancaria corporativa</div></div>
<div class="cl2" onclick="toggleTask(this, 'p1_7')"><div class="cb" id="cb_p1_7"></div><div class="ct" id="ct_p1_7">Preparar lista oficial de 178 canciones</div></div>
</div>
</div>
</div>
<div class="pc">
<div class="ph" onclick="togglePhase(this)">
<div class="pn2 an">📊</div>
<div class="pi2"><h3>Fase 2: Auditoria Tecnica del Catalogo</h3><div class="psb">12 principales + expansion a 178</div></div>
<div class="ps3 an">$0 (herramientas propias)</div>
<div class="ar">&#x25BC;</div>
</div>
<div class="pb2">
<div class="pd2">Ejecutar el analisis tecnico del catalogo para documentar el valor real del activo musical.</div>
<div class="mr">
<span class="mc2 accent">Semanas 2-4</span>
<span class="mc2 success">$0 (herramientas propias)</span>
<span class="mc2">8 tareas</span>
<span class="mc2 an">En Progreso</span>
</div>
<div class="cl">
<div class="cl2" onclick="toggleTask(this, 'p2_0')"><div class="cb" id="cb_p2_0"></div><div class="ct" id="ct_p2_0">Auditar 12 canciones principales con The Tool</div></div>
<div class="cl2" onclick="toggleTask(this, 'p2_1')"><div class="cb" id="cb_p2_1"></div><div class="ct" id="ct_p2_1">Generar reporte ejecutivo de auditoria</div></div>
<div class="cl2" onclick="toggleTask(this, 'p2_2')"><div class="cb" id="cb_p2_2"></div><div class="ct" id="ct_p2_2">Expandir auditoria a las 178 canciones</div></div>
<div class="cl2" onclick="toggleTask(this, 'p2_3')"><div class="cb" id="cb_p2_3"></div><div class="ct" id="ct_p2_3">Calcular yield mensual total e ingreso fugado</div></div>
<div class="cl2" onclick="toggleTask(this, 'p2_4')"><div class="cb" id="cb_p2_4"></div><div class="ct" id="ct_p2_4">Identificar canales sin Content ID</div></div>
<div class="cl2" onclick="toggleTask(this, 'p2_5')"><div class="cb" id="cb_p2_5"></div><div class="ct" id="ct_p2_5">Preparar matriz de nodos por cancion</div></div>
<div class="cl2" onclick="toggleTask(this, 'p2_6')"><div class="cb" id="cb_p2_6"></div><div class="ct" id="ct_p2_6">Exportar reporte PDF ejecutivo</div></div>
<div class="cl2" onclick="toggleTask(this, 'p2_7')"><div class="cb" id="cb_p2_7"></div><div class="ct" id="ct_p2_7">Redactar carta de autorizacion notariada</div></div>
</div>
</div>
</div>
<div class="pc">
<div class="ph" onclick="togglePhase(this)">
<div class="pn2 pd">🤝</div>
<div class="pi2"><h3>Fase 3: Gestion con el Artista</h3><div class="psb">Expectativas, autorizacion y coordinacion</div></div>
<div class="ps3 pd">$0</div>
<div class="ar">&#x25BC;</div>
</div>
<div class="pb2">
<div class="pd2">Gestionar la relacion con el artista de manera profesional y gradual.</div>
<div class="mr">
<span class="mc2 accent">Semanas 1-2</span>
<span class="mc2 success">$0</span>
<span class="mc2">8 tareas</span>
<span class="mc2 pd">Pendiente</span>
</div>
<div class="cl">
<div class="cl2" onclick="toggleTask(this, 'p3_0')"><div class="cb" id="cb_p3_0"></div><div class="ct" id="ct_p3_0">Agendar reunion con Ramon Orlando</div></div>
<div class="cl2" onclick="toggleTask(this, 'p3_1')"><div class="cb" id="cb_p3_1"></div><div class="ct" id="ct_p3_1">Explicar importancia del registro ONDA</div></div>
<div class="cl2" onclick="toggleTask(this, 'p3_2')"><div class="cb" id="cb_p3_2"></div><div class="ct" id="ct_p3_2">No revelar LLC/tokenizacion prematuramente</div></div>
<div class="cl2" onclick="toggleTask(this, 'p3_3')"><div class="cb" id="cb_p3_3"></div><div class="ct" id="ct_p3_3">Gestionar expectativas sobre tiempos</div></div>
<div class="cl2" onclick="toggleTask(this, 'p3_4')"><div class="cb" id="cb_p3_4"></div><div class="ct" id="ct_p3_4">Presentar el 23 Sept como catalizador</div></div>
<div class="cl2" onclick="toggleTask(this, 'p3_5')"><div class="cb" id="cb_p3_5"></div><div class="ct" id="ct_p3_5">Firmar carta de autorizacion</div></div>
<div class="cl2" onclick="toggleTask(this, 'p3_6')"><div class="cb" id="cb_p3_6"></div><div class="ct" id="ct_p3_6">Obtener documentos del artista</div></div>
<div class="cl2" onclick="toggleTask(this, 'p3_7')"><div class="cb" id="cb_p3_7"></div><div class="ct" id="ct_p3_7">Coordinar visita a ONDA</div></div>
</div>
</div>
</div>
<div class="pc">
<div class="ph" onclick="togglePhase(this)">
<div class="pn2 pd">🏦</div>
<div class="pi2"><h3>Fase 4: Registro en Sociedades de Gestion</h3><div class="psb">SoundExchange, ASCAP/BMI, SGACEDOM</div></div>
<div class="ps3 pd">$0 - $50</div>
<div class="ar">&#x25BC;</div>
</div>
<div class="pb2">
<div class="pd2">Registrar el catalogo en todas las sociedades de gestion colectiva.</div>
<div class="mr">
<span class="mc2 accent">Semanas 3-6</span>
<span class="mc2 success">$0 - $50</span>
<span class="mc2">8 tareas</span>
<span class="mc2 pd">Pendiente</span>
</div>
<div class="cl">
<div class="cl2" onclick="toggleTask(this, 'p4_0')"><div class="cb" id="cb_p4_0"></div><div class="ct" id="ct_p4_0">Registrar catalogo en SoundExchange</div></div>
<div class="cl2" onclick="toggleTask(this, 'p4_1')"><div class="cb" id="cb_p4_1"></div><div class="ct" id="ct_p4_1">Reclamar regalias retroactivas 3 anos</div></div>
<div class="cl2" onclick="toggleTask(this, 'p4_2')"><div class="cb" id="cb_p4_2"></div><div class="ct" id="ct_p4_2">Registrar en ASCAP/BMI</div></div>
<div class="cl2" onclick="toggleTask(this, 'p4_3')"><div class="cb" id="cb_p4_3"></div><div class="ct" id="ct_p4_3">Registrar en SGACEDOM</div></div>
<div class="cl2" onclick="toggleTask(this, 'p4_4')"><div class="cb" id="cb_p4_4"></div><div class="ct" id="ct_p4_4">Configurar Content ID en YouTube</div></div>
<div class="cl2" onclick="toggleTask(this, 'p4_5')"><div class="cb" id="cb_p4_5"></div><div class="ct" id="ct_p4_5">Dividir 178 canciones en 6 colecciones</div></div>
<div class="cl2" onclick="toggleTask(this, 'p4_6')"><div class="cb" id="cb_p4_6"></div><div class="ct" id="ct_p4_6">Asignar ISRCs</div></div>
<div class="cl2" onclick="toggleTask(this, 'p4_7')"><div class="cb" id="cb_p4_7"></div><div class="ct" id="ct_p4_7">Configurar distribucion streaming</div></div>
</div>
</div>
</div>
<div class="pc">
<div class="ph" onclick="togglePhase(this)">
<div class="pn2 pd">📬</div>
<div class="pi2"><h3>Fase 5: Pitch a Multinacionales</h3><div class="psb">Believe, The Orchard, beatBread</div></div>
<div class="ps3 pd">$0</div>
<div class="ar">&#x25BC;</div>
</div>
<div class="pb2">
<div class="pd2">Ejecutar secuencia de 4 mensajes hacia multinacionales.</div>
<div class="mr">
<span class="mc2 accent">Semanas 4-8</span>
<span class="mc2 success">$0</span>
<span class="mc2">8 tareas</span>
<span class="mc2 pd">Pendiente</span>
</div>
<div class="cl">
<div class="cl2" onclick="toggleTask(this, 'p5_0')"><div class="cb" id="cb_p5_0"></div><div class="ct" id="ct_p5_0">Mensaje 1: Presentacion valor historico</div></div>
<div class="cl2" onclick="toggleTask(this, 'p5_1')"><div class="cb" id="cb_p5_1"></div><div class="ct" id="ct_p5_1">Mensaje 2: Envio auditoria + ONDA</div></div>
<div class="cl2" onclick="toggleTask(this, 'p5_2')"><div class="cb" id="cb_p5_2"></div><div class="ct" id="ct_p5_2">Mensaje 3: Propuesta formal + adelanto</div></div>
<div class="cl2" onclick="toggleTask(this, 'p5_3')"><div class="cb" id="cb_p5_3"></div><div class="ct" id="ct_p5_3">Mensaje 4: Cierre con deadline</div></div>
<div class="cl2" onclick="toggleTask(this, 'p5_4')"><div class="cb" id="cb_p5_4"></div><div class="ct" id="ct_p5_4">Contactar Believe Music</div></div>
<div class="cl2" onclick="toggleTask(this, 'p5_5')"><div class="cb" id="cb_p5_5"></div><div class="ct" id="ct_p5_5">Contactar The Orchard</div></div>
<div class="cl2" onclick="toggleTask(this, 'p5_6')"><div class="cb" id="cb_p5_6"></div><div class="ct" id="ct_p5_6">Evaluar beatBread como puente</div></div>
<div class="cl2" onclick="toggleTask(this, 'p5_7')"><div class="cb" id="cb_p5_7"></div><div class="ct" id="ct_p5_7">Negociar adelanto $500K-$1M</div></div>
</div>
</div>
</div>
<div class="pc">
<div class="ph" onclick="togglePhase(this)">
<div class="pn2 pd">⚡</div>
<div class="pi2"><h3>Fase 6: Infraestructura Web3 y Tokenizacion</h3><div class="psb">LLC, Smart Contracts, Frontend</div></div>
<div class="ps3 pd">$2K - $5K</div>
<div class="ar">&#x25BC;</div>
</div>
<div class="pb2">
<div class="pd2">Construir la infraestructura Web3: LLC, smart contracts, tokenizacion.</div>
<div class="mr">
<span class="mc2 accent">Meses 3-5</span>
<span class="mc2 success">$2K - $5K</span>
<span class="mc2">8 tareas</span>
<span class="mc2 pd">Pendiente</span>
</div>
<div class="cl">
<div class="cl2" onclick="toggleTask(this, 'p6_0')"><div class="cb" id="cb_p6_0"></div><div class="ct" id="ct_p6_0">Constituir LLC en Wyoming</div></div>
<div class="cl2" onclick="toggleTask(this, 'p6_1')"><div class="cb" id="cb_p6_1"></div><div class="ct" id="ct_p6_1">Abrir cuenta bancaria EE.UU.</div></div>
<div class="cl2" onclick="toggleTask(this, 'p6_2')"><div class="cb" id="cb_p6_2"></div><div class="ct" id="ct_p6_2">Desplegar smart contracts Base/Polygon</div></div>
<div class="cl2" onclick="toggleTask(this, 'p6_3')"><div class="cb" id="cb_p6_3"></div><div class="ct" id="ct_p6_3">Crear token de catalogo</div></div>
<div class="cl2" onclick="toggleTask(this, 'p6_4')"><div class="cb" id="cb_p6_4"></div><div class="ct" id="ct_p6_4">Frontend Next.js + wallet connect</div></div>
<div class="cl2" onclick="toggleTask(this, 'p6_5')"><div class="cb" id="cb_p6_5"></div><div class="ct" id="ct_p6_5">Preventa experiencias VIP</div></div>
<div class="cl2" onclick="toggleTask(this, 'p6_6')"><div class="cb" id="cb_p6_6"></div><div class="ct" id="ct_p6_6">Sistema de afiliados con smartlinks</div></div>
<div class="cl2" onclick="toggleTask(this, 'p6_7')"><div class="cb" id="cb_p6_7"></div><div class="ct" id="ct_p6_7">Boletos NFC + NFTs (Tuboleta Pass)</div></div>
</div>
</div>
</div>
<div class="pc">
<div class="ph" onclick="togglePhase(this)">
<div class="pn2 pd">🏟️</div>
<div class="pi2"><h3>Fase 7: Evento 50 Aniversario</h3><div class="psb">23 Sept 2026 - Estadio Olimpico</div></div>
<div class="ps3 pd">$5K - $15K</div>
<div class="ar">&#x25BC;</div>
</div>
<div class="pb2">
<div class="pd2">Utilizar el concierto como catalizador para maximizar ingresos.</div>
<div class="mr">
<span class="mc2 accent">Septiembre 2026</span>
<span class="mc2 success">$5K - $15K</span>
<span class="mc2">8 tareas</span>
<span class="mc2 pd">Pendiente</span>
</div>
<div class="cl">
<div class="cl2" onclick="toggleTask(this, 'p7_0')"><div class="cb" id="cb_p7_0"></div><div class="ct" id="ct_p7_0">Campana marketing organico pre-evento</div></div>
<div class="cl2" onclick="toggleTask(this, 'p7_1')"><div class="cb" id="cb_p7_1"></div><div class="ct" id="ct_p7_1">Venta experiencias premium</div></div>
<div class="cl2" onclick="toggleTask(this, 'p7_2')"><div class="cb" id="cb_p7_2"></div><div class="ct" id="ct_p7_2">Smartlinks afiliados 40 artistas</div></div>
<div class="cl2" onclick="toggleTask(this, 'p7_3')"><div class="cb" id="cb_p7_3"></div><div class="ct" id="ct_p7_3">Acceso virtual diaspora $25</div></div>
<div class="cl2" onclick="toggleTask(this, 'p7_4')"><div class="cb" id="cb_p7_4"></div><div class="ct" id="ct_p7_4">Distribucion masiva post-evento</div></div>
<div class="cl2" onclick="toggleTask(this, 'p7_5')"><div class="cb" id="cb_p7_5"></div><div class="ct" id="ct_p7_5">Capturar pico trafico</div></div>
<div class="cl2" onclick="toggleTask(this, 'p7_6')"><div class="cb" id="cb_p7_6"></div><div class="ct" id="ct_p7_6">Monitoreo ingresos tiempo real</div></div>
<div class="cl2" onclick="toggleTask(this, 'p7_7')"><div class="cb" id="cb_p7_7"></div><div class="ct" id="ct_p7_7">Content ID en picos de reproduccion</div></div>
</div>
</div>
</div>
<div class="pc">
<div class="ph" onclick="togglePhase(this)">
<div class="pn2 pd">🚀</div>
<div class="pi2"><h3>Fase 8: Ejecucion y Escalabilidad</h3><div class="psb">MVP, documentacion, replicacion</div></div>
<div class="ps3 pd">$1K - $3K</div>
<div class="ar">&#x25BC;</div>
</div>
<div class="pb2">
<div class="pd2">Cerrar acuerdo, recibir capital, y documentar modelo como MVP.</div>
<div class="mr">
<span class="mc2 accent">Mes 6+</span>
<span class="mc2 success">$1K - $3K</span>
<span class="mc2">8 tareas</span>
<span class="mc2 pd">Pendiente</span>
</div>
<div class="cl">
<div class="cl2" onclick="toggleTask(this, 'p8_0')"><div class="cb" id="cb_p8_0"></div><div class="ct" id="ct_p8_0">Firmar contrato distribuidora</div></div>
<div class="cl2" onclick="toggleTask(this, 'p8_1')"><div class="cb" id="cb_p8_1"></div><div class="ct" id="ct_p8_1">Recibir capital adelanto</div></div>
<div class="cl2" onclick="toggleTask(this, 'p8_2')"><div class="cb" id="cb_p8_2"></div><div class="ct" id="ct_p8_2">Activar recoleccion regalias</div></div>
<div class="cl2" onclick="toggleTask(this, 'p8_3')"><div class="cb" id="cb_p8_3"></div><div class="ct" id="ct_p8_3">Documentar modelo MVP</div></div>
<div class="cl2" onclick="toggleTask(this, 'p8_4')"><div class="cb" id="cb_p8_4"></div><div class="ct" id="ct_p8_4">Identificar proximos catalogos</div></div>
<div class="cl2" onclick="toggleTask(this, 'p8_5')"><div class="cb" id="cb_p8_5"></div><div class="ct" id="ct_p8_5">Refinar procesos auditoria</div></div>
<div class="cl2" onclick="toggleTask(this, 'p8_6')"><div class="cb" id="cb_p8_6"></div><div class="ct" id="ct_p8_6">Escalar a multiples catalogos</div></div>
<div class="cl2" onclick="toggleTask(this, 'p8_7')"><div class="cb" id="cb_p8_7"></div><div class="ct" id="ct_p8_7">Metricas de exito Hyperion</div></div>
</div>
</div>
</div>
</div>"""

new_phases = """<div class="tc act" id="tab-phases">

<div class="mp-hero">
  <div class="mp-hero-tags">
    <span class="mp-hero-tag accent">8 FASES</span>
    <span class="mp-hero-tag">64 TAREAS</span>
    <span class="mp-hero-tag green">localStorage</span>
    <span class="mp-hero-tag cyan">PROGRESO EN VIVO</span>
  </div>
  <h2 class="mp-hero-title">Las <span class="hl">8 Fases</span> del Plan</h2>
  <p class="mp-hero-sub">Desde la fundaci\u00f3n legal hasta la escalabilidad. Marca tu progreso \u2014 los datos se guardan autom\u00e1ticamente.</p>
</div>

<div class="phase-flow">
  <div class="phase-flow-item active"><div class="phase-flow-num">1</div><div class="phase-flow-label">Legal</div></div>
  <div class="phase-flow-arrow">\u2192</div>
  <div class="phase-flow-item"><div class="phase-flow-num">2</div><div class="phase-flow-label">Auditor\u00eda</div></div>
  <div class="phase-flow-arrow">\u2192</div>
  <div class="phase-flow-item"><div class="phase-flow-num">3</div><div class="phase-flow-label">Artista</div></div>
  <div class="phase-flow-arrow">\u2192</div>
  <div class="phase-flow-item"><div class="phase-flow-num">4</div><div class="phase-flow-label">Gesti\u00f3n</div></div>
  <div class="phase-flow-arrow">\u2192</div>
  <div class="phase-flow-item"><div class="phase-flow-num">5</div><div class="phase-flow-label">Pitch</div></div>
  <div class="phase-flow-arrow">\u2192</div>
  <div class="phase-flow-item"><div class="phase-flow-num">6</div><div class="phase-flow-label">Web3</div></div>
  <div class="phase-flow-arrow">\u2192</div>
  <div class="phase-flow-item"><div class="phase-flow-num">7</div><div class="phase-flow-label">Evento</div></div>
  <div class="phase-flow-arrow">\u2192</div>
  <div class="phase-flow-item"><div class="phase-flow-num">8</div><div class="phase-flow-label">Escalar</div></div>
</div>

<div class="sb"><input type="text" id="searchInput" placeholder="Buscar en fases..." oninput="filterPhases()"><button class="filter-btn act" onclick="filterStatus('all')">Todas</button><button class="filter-btn" onclick="filterStatus('active')">En Progreso</button><button class="filter-btn" onclick="filterStatus('pending')">Pendientes</button></div>
<div class="pc">
<div class="ph" onclick="togglePhase(this)">
<div class="pn2 an">\U0001f3db\ufe0f</div>
<div class="pi2"><h3>Fase 1: Fundacion Legal y Corporativa</h3><div class="psb">ONAPI, SAS, ONDA, Contrato Matriz</div></div>
<div class="ps3 an">$800 - $1,200 USD</div>
<div class="ar">\u25bc</div>
</div>
<div class="pb2">
<div class="pd2">Establecer la infraestructura legal y corporativa necesaria para operar como sello independiente y negociar con distribuidoras internacionales.</div>
<div class="mr">
<span class="mc2 accent">Semanas 1-3</span>
<span class="mc2 success">$800 - $1,200 USD</span>
<span class="mc2">8 tareas</span>
<span class="mc2 an">En Progreso</span>
</div>
<div class="cl">
<div class="cl2" onclick="toggleTask(this, 'p1_0')"><div class="cb" id="cb_p1_0"></div><div class="ct" id="ct_p1_0">Registrar Nombre Comercial en ONAPI (Clase 41 y 35)</div></div>
<div class="cl2" onclick="toggleTask(this, 'p1_1')"><div class="cb" id="cb_p1_1"></div><div class="ct" id="ct_p1_1">Redactar estatutos SAS y pagar impuesto DGII</div></div>
<div class="cl2" onclick="toggleTask(this, 'p1_2')"><div class="cb" id="cb_p1_2"></div><div class="ct" id="ct_p1_2">Registro Mercantil en Camara de Comercio</div></div>
<div class="cl2" onclick="toggleTask(this, 'p1_3')"><div class="cb" id="cb_p1_3"></div><div class="ct" id="ct_p1_3">Obtener RNC (Registro Nacional Contribuyente)</div></div>
<div class="cl2" onclick="toggleTask(this, 'p1_4')"><div class="cb" id="cb_p1_4"></div><div class="ct" id="ct_p1_4">Registrar fonograma en ONDA a nombre de la empresa</div></div>
<div class="cl2" onclick="toggleTask(this, 'p1_5')"><div class="cb" id="cb_p1_5"></div><div class="ct" id="ct_p1_5">Firmar Contrato de Administracion con el artista</div></div>
<div class="cl2" onclick="toggleTask(this, 'p1_6')"><div class="cb" id="cb_p1_6"></div><div class="ct" id="ct_p1_6">Abrir cuenta bancaria corporativa</div></div>
<div class="cl2" onclick="toggleTask(this, 'p1_7')"><div class="cb" id="cb_p1_7"></div><div class="ct" id="ct_p1_7">Preparar lista oficial de 178 canciones</div></div>
</div>
</div>
</div>
<div class="pc">
<div class="ph" onclick="togglePhase(this)">
<div class="pn2 an">\U0001f4ca</div>
<div class="pi2"><h3>Fase 2: Auditoria Tecnica del Catalogo</h3><div class="psb">12 principales + expansion a 178</div></div>
<div class="ps3 an">$0 (herramientas propias)</div>
<div class="ar">\u25bc</div>
</div>
<div class="pb2">
<div class="pd2">Ejecutar el analisis tecnico del catalogo para documentar el valor real del activo musical.</div>
<div class="mr">
<span class="mc2 accent">Semanas 2-4</span>
<span class="mc2 success">$0 (herramientas propias)</span>
<span class="mc2">8 tareas</span>
<span class="mc2 an">En Progreso</span>
</div>
<div class="cl">
<div class="cl2" onclick="toggleTask(this, 'p2_0')"><div class="cb" id="cb_p2_0"></div><div class="ct" id="ct_p2_0">Auditar 12 canciones principales con The Tool</div></div>
<div class="cl2" onclick="toggleTask(this, 'p2_1')"><div class="cb" id="cb_p2_1"></div><div class="ct" id="ct_p2_1">Generar reporte ejecutivo de auditoria</div></div>
<div class="cl2" onclick="toggleTask(this, 'p2_2')"><div class="cb" id="cb_p2_2"></div><div class="ct" id="ct_p2_2">Expandir auditoria a las 178 canciones</div></div>
<div class="cl2" onclick="toggleTask(this, 'p2_3')"><div class="cb" id="cb_p2_3"></div><div class="ct" id="ct_p2_3">Calcular yield mensual total e ingreso fugado</div></div>
<div class="cl2" onclick="toggleTask(this, 'p2_4')"><div class="cb" id="cb_p2_4"></div><div class="ct" id="ct_p2_4">Identificar canales sin Content ID</div></div>
<div class="cl2" onclick="toggleTask(this, 'p2_5')"><div class="cb" id="cb_p2_5"></div><div class="ct" id="ct_p2_5">Preparar matriz de nodos por cancion</div></div>
<div class="cl2" onclick="toggleTask(this, 'p2_6')"><div class="cb" id="cb_p2_6"></div><div class="ct" id="ct_p2_6">Exportar reporte PDF ejecutivo</div></div>
<div class="cl2" onclick="toggleTask(this, 'p2_7')"><div class="cb" id="cb_p2_7"></div><div class="ct" id="ct_p2_7">Redactar carta de autorizacion notariada</div></div>
</div>
</div>
</div>
<div class="pc">
<div class="ph" onclick="togglePhase(this)">
<div class="pn2 pd">\U0001f91d</div>
<div class="pi2"><h3>Fase 3: Gestion con el Artista</h3><div class="psb">Expectativas, autorizacion y coordinacion</div></div>
<div class="ps3 pd">$0</div>
<div class="ar">\u25bc</div>
</div>
<div class="pb2">
<div class="pd2">Gestionar la relacion con el artista de manera profesional y gradual.</div>
<div class="mr">
<span class="mc2 accent">Semanas 1-2</span>
<span class="mc2 success">$0</span>
<span class="mc2">8 tareas</span>
<span class="mc2 pd">Pendiente</span>
</div>
<div class="cl">
<div class="cl2" onclick="toggleTask(this, 'p3_0')"><div class="cb" id="cb_p3_0"></div><div class="ct" id="ct_p3_0">Agendar reunion con Ramon Orlando</div></div>
<div class="cl2" onclick="toggleTask(this, 'p3_1')"><div class="cb" id="cb_p3_1"></div><div class="ct" id="ct_p3_1">Explicar importancia del registro ONDA</div></div>
<div class="cl2" onclick="toggleTask(this, 'p3_2')"><div class="cb" id="cb_p3_2"></div><div class="ct" id="ct_p3_2">No revelar LLC/tokenizacion prematuramente</div></div>
<div class="cl2" onclick="toggleTask(this, 'p3_3')"><div class="cb" id="cb_p3_3"></div><div class="ct" id="ct_p3_3">Gestionar expectativas sobre tiempos</div></div>
<div class="cl2" onclick="toggleTask(this, 'p3_4')"><div class="cb" id="cb_p3_4"></div><div class="ct" id="ct_p3_4">Presentar el 23 Sept como catalizador</div></div>
<div class="cl2" onclick="toggleTask(this, 'p3_5')"><div class="cb" id="cb_p3_5"></div><div class="ct" id="ct_p3_5">Firmar carta de autorizacion</div></div>
<div class="cl2" onclick="toggleTask(this, 'p3_6')"><div class="cb" id="cb_p3_6"></div><div class="ct" id="ct_p3_6">Obtener documentos del artista</div></div>
<div class="cl2" onclick="toggleTask(this, 'p3_7')"><div class="cb" id="cb_p3_7"></div><div class="ct" id="ct_p3_7">Coordinar visita a ONDA</div></div>
</div>
</div>
</div>
<div class="pc">
<div class="ph" onclick="togglePhase(this)">
<div class="pn2 pd">\U0001f3e6</div>
<div class="pi2"><h3>Fase 4: Registro en Sociedades de Gestion</h3><div class="psb">SoundExchange, ASCAP/BMI, SGACEDOM</div></div>
<div class="ps3 pd">$0 - $50</div>
<div class="ar">\u25bc</div>
</div>
<div class="pb2">
<div class="pd2">Registrar el catalogo en todas las sociedades de gestion colectiva.</div>
<div class="mr">
<span class="mc2 accent">Semanas 3-6</span>
<span class="mc2 success">$0 - $50</span>
<span class="mc2">8 tareas</span>
<span class="mc2 pd">Pendiente</span>
</div>
<div class="cl">
<div class="cl2" onclick="toggleTask(this, 'p4_0')"><div class="cb" id="cb_p4_0"></div><div class="ct" id="ct_p4_0">Registrar catalogo en SoundExchange</div></div>
<div class="cl2" onclick="toggleTask(this, 'p4_1')"><div class="cb" id="cb_p4_1"></div><div class="ct" id="ct_p4_1">Reclamar regalias retroactivas 3 anos</div></div>
<div class="cl2" onclick="toggleTask(this, 'p4_2')"><div class="cb" id="cb_p4_2"></div><div class="ct" id="ct_p4_2">Registrar en ASCAP/BMI</div></div>
<div class="cl2" onclick="toggleTask(this, 'p4_3')"><div class="cb" id="cb_p4_3"></div><div class="ct" id="ct_p4_3">Registrar en SGACEDOM</div></div>
<div class="cl2" onclick="toggleTask(this, 'p4_4')"><div class="cb" id="cb_p4_4"></div><div class="ct" id="ct_p4_4">Configurar Content ID en YouTube</div></div>
<div class="cl2" onclick="toggleTask(this, 'p4_5')"><div class="cb" id="cb_p4_5"></div><div class="ct" id="ct_p4_5">Dividir 178 canciones en 6 colecciones</div></div>
<div class="cl2" onclick="toggleTask(this, 'p4_6')"><div class="cb" id="cb_p4_6"></div><div class="ct" id="ct_p4_6">Asignar ISRCs</div></div>
<div class="cl2" onclick="toggleTask(this, 'p4_7')"><div class="cb" id="cb_p4_7"></div><div class="ct" id="ct_p4_7">Configurar distribucion streaming</div></div>
</div>
</div>
</div>
<div class="pc">
<div class="ph" onclick="togglePhase(this)">
<div class="pn2 pd">\U0001f4ec</div>
<div class="pi2"><h3>Fase 5: Pitch a Multinacionales</h3><div class="psb">Believe, The Orchard, beatBread</div></div>
<div class="ps3 pd">$0</div>
<div class="ar">\u25bc</div>
</div>
<div class="pb2">
<div class="pd2">Ejecutar secuencia de 4 mensajes hacia multinacionales.</div>
<div class="mr">
<span class="mc2 accent">Semanas 4-8</span>
<span class="mc2 success">$0</span>
<span class="mc2">8 tareas</span>
<span class="mc2 pd">Pendiente</span>
</div>
<div class="cl">
<div class="cl2" onclick="toggleTask(this, 'p5_0')"><div class="cb" id="cb_p5_0"></div><div class="ct" id="ct_p5_0">Mensaje 1: Presentacion valor historico</div></div>
<div class="cl2" onclick="toggleTask(this, 'p5_1')"><div class="cb" id="cb_p5_1"></div><div class="ct" id="ct_p5_1">Mensaje 2: Envio auditoria + ONDA</div></div>
<div class="cl2" onclick="toggleTask(this, 'p5_2')"><div class="cb" id="cb_p5_2"></div><div class="ct" id="ct_p5_2">Mensaje 3: Propuesta formal + adelanto</div></div>
<div class="cl2" onclick="toggleTask(this, 'p5_3')"><div class="cb" id="cb_p5_3"></div><div class="ct" id="ct_p5_3">Mensaje 4: Cierre con deadline</div></div>
<div class="cl2" onclick="toggleTask(this, 'p5_4')"><div class="cb" id="cb_p5_4"></div><div class="ct" id="ct_p5_4">Contactar Believe Music</div></div>
<div class="cl2" onclick="toggleTask(this, 'p5_5')"><div class="cb" id="cb_p5_5"></div><div class="ct" id="ct_p5_5">Contactar The Orchard</div></div>
<div class="cl2" onclick="toggleTask(this, 'p5_6')"><div class="cb" id="cb_p5_6"></div><div class="ct" id="ct_p5_6">Evaluar beatBread como puente</div></div>
<div class="cl2" onclick="toggleTask(this, 'p5_7')"><div class="cb" id="cb_p5_7"></div><div class="ct" id="ct_p5_7">Negociar adelanto $500K-$1M</div></div>
</div>
</div>
</div>
<div class="pc">
<div class="ph" onclick="togglePhase(this)">
<div class="pn2 pd">\u26a1</div>
<div class="pi2"><h3>Fase 6: Infraestructura Web3 y Tokenizacion</h3><div class="psb">LLC, Smart Contracts, Frontend</div></div>
<div class="ps3 pd">$2K - $5K</div>
<div class="ar">\u25bc</div>
</div>
<div class="pb2">
<div class="pd2">Construir la infraestructura Web3: LLC, smart contracts, tokenizacion.</div>
<div class="mr">
<span class="mc2 accent">Meses 3-5</span>
<span class="mc2 success">$2K - $5K</span>
<span class="mc2">8 tareas</span>
<span class="mc2 pd">Pendiente</span>
</div>
<div class="cl">
<div class="cl2" onclick="toggleTask(this, 'p6_0')"><div class="cb" id="cb_p6_0"></div><div class="ct" id="ct_p6_0">Constituir LLC en Wyoming</div></div>
<div class="cl2" onclick="toggleTask(this, 'p6_1')"><div class="cb" id="cb_p6_1"></div><div class="ct" id="ct_p6_1">Abrir cuenta bancaria EE.UU.</div></div>
<div class="cl2" onclick="toggleTask(this, 'p6_2')"><div class="cb" id="cb_p6_2"></div><div class="ct" id="ct_p6_2">Desplegar smart contracts Base/Polygon</div></div>
<div class="cl2" onclick="toggleTask(this, 'p6_3')"><div class="cb" id="cb_p6_3"></div><div class="ct" id="ct_p6_3">Crear token de catalogo</div></div>
<div class="cl2" onclick="toggleTask(this, 'p6_4')"><div class="cb" id="cb_p6_4"></div><div class="ct" id="ct_p6_4">Frontend Next.js + wallet connect</div></div>
<div class="cl2" onclick="toggleTask(this, 'p6_5')"><div class="cb" id="cb_p6_5"></div><div class="ct" id="ct_p6_5">Preventa experiencias VIP</div></div>
<div class="cl2" onclick="toggleTask(this, 'p6_6')"><div class="cb" id="cb_p6_6"></div><div class="ct" id="ct_p6_6">Sistema de afiliados con smartlinks</div></div>
<div class="cl2" onclick="toggleTask(this, 'p6_7')"><div class="cb" id="cb_p6_7"></div><div class="ct" id="ct_p6_7">Boletos NFC + NFTs (Tuboleta Pass)</div></div>
</div>
</div>
</div>
<div class="pc">
<div class="ph" onclick="togglePhase(this)">
<div class="pn2 pd">\U0001f3df\ufe0f</div>
<div class="pi2"><h3>Fase 7: Evento 50 Aniversario</h3><div class="psb">23 Sept 2026 - Estadio Olimpico</div></div>
<div class="ps3 pd">$5K - $15K</div>
<div class="ar">\u25bc</div>
</div>
<div class="pb2">
<div class="pd2">Utilizar el concierto como catalizador para maximizar ingresos.</div>
<div class="mr">
<span class="mc2 accent">Septiembre 2026</span>
<span class="mc2 success">$5K - $15K</span>
<span class="mc2">8 tareas</span>
<span class="mc2 pd">Pendiente</span>
</div>
<div class="cl">
<div class="cl2" onclick="toggleTask(this, 'p7_0')"><div class="cb" id="cb_p7_0"></div><div class="ct" id="ct_p7_0">Campana marketing organico pre-evento</div></div>
<div class="cl2" onclick="toggleTask(this, 'p7_1')"><div class="cb" id="cb_p7_1"></div><div class="ct" id="ct_p7_1">Venta experiencias premium</div></div>
<div class="cl2" onclick="toggleTask(this, 'p7_2')"><div class="cb" id="cb_p7_2"></div><div class="ct" id="ct_p7_2">Smartlinks afiliados 40 artistas</div></div>
<div class="cl2" onclick="toggleTask(this, 'p7_3')"><div class="cb" id="cb_p7_3"></div><div class="ct" id="ct_p7_3">Acceso virtual diaspora $25</div></div>
<div class="cl2" onclick="toggleTask(this, 'p7_4')"><div class="cb" id="cb_p7_4"></div><div class="ct" id="ct_p7_4">Distribucion masiva post-evento</div></div>
<div class="cl2" onclick="toggleTask(this, 'p7_5')"><div class="cb" id="cb_p7_5"></div><div class="ct" id="ct_p7_5">Capturar pico trafico</div></div>
<div class="cl2" onclick="toggleTask(this, 'p7_6')"><div class="cb" id="cb_p7_6"></div><div class="ct" id="ct_p7_6">Monitoreo ingresos tiempo real</div></div>
<div class="cl2" onclick="toggleTask(this, 'p7_7')"><div class="cb" id="cb_p7_7"></div><div class="ct" id="ct_p7_7">Content ID en picos de reproduccion</div></div>
</div>
</div>
</div>
<div class="pc">
<div class="ph" onclick="togglePhase(this)">
<div class="pn2 pd">\U0001f680</div>
<div class="pi2"><h3>Fase 8: Ejecucion y Escalabilidad</h3><div class="psb">MVP, documentacion, replicacion</div></div>
<div class="ps3 pd">$1K - $3K</div>
<div class="ar">\u25bc</div>
</div>
<div class="pb2">
<div class="pd2">Cerrar acuerdo, recibir capital, y documentar modelo como MVP.</div>
<div class="mr">
<span class="mc2 accent">Mes 6+</span>
<span class="mc2 success">$1K - $3K</span>
<span class="mc2">8 tareas</span>
<span class="mc2 pd">Pendiente</span>
</div>
<div class="cl">
<div class="cl2" onclick="toggleTask(this, 'p8_0')"><div class="cb" id="cb_p8_0"></div><div class="ct" id="ct_p8_0">Firmar contrato distribuidora</div></div>
<div class="cl2" onclick="toggleTask(this, 'p8_1')"><div class="cb" id="cb_p8_1"></div><div class="ct" id="ct_p8_1">Recibir capital adelanto</div></div>
<div class="cl2" onclick="toggleTask(this, 'p8_2')"><div class="cb" id="cb_p8_2"></div><div class="ct" id="ct_p8_2">Activar recoleccion regalias</div></div>
<div class="cl2" onclick="toggleTask(this, 'p8_3')"><div class="cb" id="cb_p8_3"></div><div class="ct" id="ct_p8_3">Documentar modelo MVP</div></div>
<div class="cl2" onclick="toggleTask(this, 'p8_4')"><div class="cb" id="cb_p8_4"></div><div class="ct" id="ct_p8_4">Identificar proximos catalogos</div></div>
<div class="cl2" onclick="toggleTask(this, 'p8_5')"><div class="cb" id="cb_p8_5"></div><div class="ct" id="ct_p8_5">Refinar procesos auditoria</div></div>
<div class="cl2" onclick="toggleTask(this, 'p8_6')"><div class="cb" id="cb_p8_6"></div><div class="ct" id="ct_p8_6">Escalar a multiples catalogos</div></div>
<div class="cl2" onclick="toggleTask(this, 'p8_7')"><div class="cb" id="cb_p8_7"></div><div class="ct" id="ct_p8_7">Metricas de exito Hyperion</div></div>
</div>
</div>
</div>

<div class="phase-footer">
  <div class="pf-item">\U0001f4cb <strong>64 tareas</strong> en 8 fases</div>
  <div class="pf-item">\U0001f504 Datos guardados en <strong>localStorage</strong></div>
  <div class="pf-item">\U0001f3af Objetivo: <strong>Adelanto $500K\u2013$1M</strong></div>
</div>
</div>"""

assert old_phases in html, "tab-phases old content not found!"
html = html.replace(old_phases, new_phases)
print("✅ tab-phases redesigned")

# ============================================================
# 3. REDESIGN tab-timeline
# ============================================================
old_timeline = """<div class="tc" id="tab-timeline">
<div class="pc"><div class="ph"><div class="pn2 an">📅</div><div class="pi2"><h3>Linea de Tiempo del Plan</h3><div class="psb">8 fases desde la fundacion legal hasta la escalabilidad</div></div></div><div class="pb2 op"><div class="tl">
<div class="tli">
<div class="dot phase1"></div>
<h4>Fase 1: Fundacion Legal</h4>
<div class="ti">Semanas 1-3</div>
<div class="td2">🏛️ Registrar ONAPI, SRL, ONDA, Contrato Matriz</div>
</div>
<div class="tli">
<div class="dot phase2"></div>
<h4>Fase 2: Auditoria Tecnica</h4>
<div class="ti">Semanas 2-4</div>
<div class="td2">📊 Auditar 12 canciones principales, generar reporte</div>
</div>
<div class="tli">
<div class="dot phase3"></div>
<h4>Fase 3: Gestion Artista</h4>
<div class="ti">Semanas 1-2</div>
<div class="td2">🤝 Presentar plan, firmar autorizacion</div>
</div>
<div class="tli">
<div class="dot phase4"></div>
<h4>Fase 4: Registro Gestion Colectiva</h4>
<div class="ti">Semanas 3-6</div>
<div class="td2">🏦 SoundExchange, ASCAP/BMI, SGACEDOM</div>
</div>
<div class="tli">
<div class="dot phase5"></div>
<h4>Fase 5: Pitch a Multinacionales</h4>
<div class="ti">Semanas 4-8</div>
<div class="td2">📬 Secuencia 4 mensajes + negociacion adelanto</div>
</div>
<div class="tli">
<div class="dot phase6"></div>
<h4>Fase 6: Infraestructura Web3</h4>
<div class="ti">Meses 3-5</div>
<div class="td2">⚡ LLC Wyoming, Smart Contracts, Tokenizacion</div>
</div>
<div class="tli">
<div class="dot phase7"></div>
<h4>Fase 7: Evento 50 Aniversario</h4>
<div class="ti">Septiembre 2026</div>
<div class="td2">🏟️ Estadio Olimpico, experiencias VIP, afiliados</div>
</div>
<div class="tli">
<div class="dot phase8"></div>
<h4>Fase 8: Ejecucion y Escalabilidad</h4>
<div class="ti">Mes 6+</div>
<div class="td2">🚀 Cierre, capital, replicacion del modelo</div>
</div>
</div></div></div></div>"""

new_timeline = """<div class="tc" id="tab-timeline">

<div class="mp-hero">
  <div class="mp-hero-tags">
    <span class="mp-hero-tag accent">8 HITOS</span>
    <span class="mp-hero-tag">SEMANA 1 \u2192 MES 6+</span>
    <span class="mp-hero-tag cyan">23 SEP 2026</span>
    <span class="mp-hero-tag green">FECHAS CLAVE</span>
  </div>
  <h2 class="mp-hero-title">L\u00ednea de <span class="hl">Tiempo</span></h2>
  <p class="mp-hero-sub">La secuencia temporal de las 8 fases. Algunas fases se ejecutan en paralelo para maximizar la velocidad.</p>
</div>

<div class="pc"><div class="ph"><div class="pn2 an">\U0001f4c5</div><div class="pi2"><h3>Linea de Tiempo del Plan</h3><div class="psb">8 fases desde la fundacion legal hasta la escalabilidad</div></div></div><div class="pb2 op"><div class="tl">
<div class="tli">
<div class="dot dn"></div>
<h4>Fase 1: Fundacion Legal</h4>
<div class="ti">Semanas 1\u20133</div>
<div class="td2">\U0001f3db\ufe0f ONAPI, SAS, ONDA, Contrato Matriz</div>
</div>
<div class="tli">
<div class="dot"></div>
<h4>Fase 2: Auditoria Tecnica</h4>
<div class="ti">Semanas 2\u20134 <span style="color:var(--accent);font-size:7px">(paralela a Fase 1)</span></div>
<div class="td2">\U0001f4ca Auditar 12 canciones principales, generar reporte ejecutivo</div>
</div>
<div class="tli">
<div class="dot"></div>
<h4>Fase 3: Gestion con el Artista</h4>
<div class="ti">Semanas 1\u20132 <span style="color:var(--accent);font-size:7px">(temprano)</span></div>
<div class="td2">\U0001f91d Presentar plan, firmar autorizacion, coordinar ONDA</div>
</div>
<div class="tli">
<div class="dot"></div>
<h4>Fase 4: Registro en Sociedades de Gestion</h4>
<div class="ti">Semanas 3\u20136</div>
<div class="td2">\U0001f3e6 SoundExchange, ASCAP/BMI, SGACEDOM</div>
</div>
<div class="tli">
<div class="dot"></div>
<h4>Fase 5: Pitch a Multinacionales</h4>
<div class="ti">Semanas 4\u20138</div>
<div class="td2">\U0001f4ec Secuencia 4 mensajes + negociacion adelanto $500K\u2013$1M</div>
</div>
<div class="tli">
<div class="dot"></div>
<h4>Fase 6: Infraestructura Web3 y Tokenizacion</h4>
<div class="ti">Meses 3\u20135</div>
<div class="td2">\u26a1 LLC Wyoming, Smart Contracts, 6 catalogos tokenizados</div>
</div>
<div class="tli">
<div class="dot gold"></div>
<h4>Fase 7: Evento 50 Aniversario</h4>
<div class="ti" style="color:var(--gold);font-weight:600">23 Septiembre 2026</div>
<div class="td2">\U0001f3df\ufe0f Estadio Olimpico, experiencias VIP, afiliados, streaming</div>
</div>
<div class="tli">
<div class="dot"></div>
<h4>Fase 8: Ejecucion y Escalabilidad</h4>
<div class="ti">Mes 6+</div>
<div class="td2">\U0001f680 Cierre acuerdo, capital, replicacion del modelo MVP</div>
</div>
</div></div></div></div>"""

assert old_timeline in html, "tab-timeline old content not found!"
html = html.replace(old_timeline, new_timeline)
print("✅ tab-timeline redesigned")

# ============================================================
# 4. REDESIGN tab-metrics
# ============================================================
old_metrics = """<div class="tc" id="tab-metrics">
<div class="mg">
<div class="mc3"><div class="ml">Canciones</div><div class="mv 190">accent</div><div class="mnote">Catalogo completo</div></div>
<div class="mc3"><div class="ml">Albumes</div><div class="mv 17">accent</div><div class="mnote">Discografia oficial</div></div>
<div class="mc3"><div class="ml">Yield/mes</div><div class="mv $66.8K">success</div><div class="mnote">Ingreso fugado actual</div></div>
<div class="mc3"><div class="ml">Proy. Anual</div><div class="mv $801K">gold</div><div class="mnote">Yield x 12 meses</div></div>
<div class="mc3"><div class="ml">Adelanto 3yr</div><div class="mv $1.68M">success</div><div class="mnote">70% flujo proyectado</div></div>
<div class="mc3"><div class="ml">Nodos</div><div class="mv 15K+">danger</div><div class="mnote">Canales detectados</div></div>
<div class="mc3"><div class="ml">Views/mes</div><div class="mv 55.7M">cyan</div><div class="mnote">eCPM $1.20</div></div>
<div class="mc3"><div class="ml">Tareas Plan</div><div class="mv 64">accent</div><div class="mnote">8 fases x 8 tareas</div></div>
</div>
<div class="hb"><div class="hl">Nota Estrategica</div>El orden de las fases es critico. SoundExchange (Fase 4) puede comenzar en paralelo con Fase 1. El Pitch a Multinacionales (Fase 5) requiere auditoria completa (Fase 2) y registro ONDA (Fase 1).</div>
</div>"""

new_metrics = """<div class="tc" id="tab-metrics">

<div class="mp-hero">
  <div class="mp-hero-tags">
    <span class="mp-hero-tag accent">KPIs</span>
    <span class="mp-hero-tag">DATOS AUDITADOS</span>
    <span class="mp-hero-tag cyan">PROYECCIONES</span>
    <span class="mp-hero-tag green">eCPM $1.20</span>
  </div>
  <h2 class="mp-hero-title">M\u00e9tricas <span class="hl">Clave</span></h2>
  <p class="mp-hero-sub">Indicadores financieros y de volumen del cat\u00e1logo de Ram\u00f3n Orlando basados en la auditor\u00eda t\u00e9cnica.</p>
</div>

<div class="mg">
<div class="mc3"><div class="ml">Canciones</div><div class="mv accent">190</div><div class="mnote">Catalogo completo registrado</div></div>
<div class="mc3"><div class="ml">Albumes</div><div class="mv accent">17</div><div class="mnote">Discografia oficial</div></div>
<div class="mc3"><div class="ml">Yield/mes</div><div class="mv success">$66.8K</div><div class="mnote">Ingreso fugado actualmente</div></div>
<div class="mc3"><div class="ml">Proy. Anual</div><div class="mv gold">$801K</div><div class="mnote">Yield x 12 meses</div></div>
<div class="mc3"><div class="ml">Adelanto 3yr</div><div class="mv success">$1.68M</div><div class="mnote">70% del flujo proyectado a 3 a\u00f1os</div></div>
<div class="mc3"><div class="ml">Nodos</div><div class="mv danger">15K+</div><div class="mnote">Canales detectados sin monetizar</div></div>
<div class="mc3"><div class="ml">Views/mes</div><div class="mv cyan">55.7M</div><div class="mnote">eCPM promedio $1.20 USD</div></div>
<div class="mc3"><div class="ml">Tareas Plan</div><div class="mv accent">64</div><div class="mnote">8 fases x 8 tareas c/u</div></div>
</div>

<div class="hb"><div class="hl">\U0001f4a1 Nota Estrategica</div>El orden de las fases es critico. <strong>SoundExchange (Fase 4)</strong> puede comenzar en paralelo con Fase 1. El <strong>Pitch a Multinacionales (Fase 5)</strong> requiere auditoria completa (Fase 2) y registro ONDA (Fase 1).</div>
</div>"""

assert old_metrics in html, "tab-metrics old content not found!"
html = html.replace(old_metrics, new_metrics)
print("✅ tab-metrics redesigned")

# ============================================================
# 5. REDESIGN tab-templates
# ============================================================
old_templates = """<div class="tc" id="tab-templates">
<div class="pc"><div class="ph" onclick="togglePhase(this)"><div class="pn2 an">📬</div><div class="pi2"><h3>Secuencia de 4 Mensajes para Multinacionales</h3><div class="psb">Believe, The Orchard y otras distribuidoras</div></div><div class="ar">&#x25BC;</div></div><div class="pb2 op">
<div class="pd2">Esta secuencia de mensajes progresivos esta disenada para pasar de un sondeo inicial a una propuesta formal de adelanto sin revelar toda la estrategia tecnica prematuramente.</div>
<div style="font-size:11px;font-weight:600;color:var(--accent);margin:8px 0 4px">Mensaje 1: Sondeo Inicial</div>
<div class="tb">Hola [Nombre], te contactamos desde Nuclear AIMA, representando el catalogo de Ramon Orlando, leyenda del merengue dominicano con 50+ anos de carrera. Estamos preparando el lanzamiento digital de su catalogo completo de 190 canciones para su 50 Aniversario (23 Sept 2026, Estadio Olimpico). El catalogo ya genera +15M views/mes organicamente en YouTube. Nos gustaria explorar una posible colaboracion para la distribucion global. Estarian abiertos a una conversacion preliminar?<button class="cpy" onclick="copyMsg(this)">Copiar</button></div>
<div style="font-size:11px;font-weight:600;color:var(--accent);margin:8px 0 4px">Mensaje 2: Confirmacion + Datos</div>
<div class="tb">Gracias por su respuesta. Adjuntamos un resumen ejecutivo de nuestra auditoria tecnica, que documenta el rendimiento actual del catalogo en YouTube (nodos, vistas, ingresos fugados). Tambien confirmamos que el catalogo esta siendo registrado en ONDA (Oficina Nacional de Derecho de Autor) y contamos con carta de autorizacion notariada del artista. El potencial de recuperacion de ingresos es significativo. Nos gustaria compartir el detalle completo en una reunion virtual.<button class="cpy" onclick="copyMsg(this)">Copiar</button></div>
<div style="font-size:11px;font-weight:600;color:var(--accent);margin:8px 0 4px">Mensaje 3: Propuesta Formal</div>
<div class="tb">Estimado/a [Nombre], tras nuestra conversacion, formalizamos nuestra propuesta: ofrecemos el catalogo completo de Ramon Orlando (190 canciones, 17 albumes, categoria merengue/tropical) para distribucion global con Content ID activo, a cambio de un adelanto (signing bonus) en el rango de $500,000 - $1,000,000 USD. El catalogo tiene un yield mensual estimado de $66,824 y proyecta +$800K anuales en ingresos recuperables. Adjuntamos expediente completo con auditoria, registros ONDA y proyecciones financieras.<button class="cpy" onclick="copyMsg(this)">Copiar</button></div>
<div style="font-size:11px;font-weight:600;color:var(--accent);margin:8px 0 4px">Mensaje 4: Cierre con Deadline</div>
<div class="tb">Hola [Nombre], queremos informarles que estamos evaluando multiples ofertas y hemos establecido el [Fecha] como fecha limite para recibir propuestas formales. El concierto del 23 de septiembre generara un pico masivo de trafico y reproducciones, y necesitamos tener la distribucion activada antes de esa fecha para maximizar la captura de ingresos. Agradeceriamos su respuesta a la brevedad para continuar las conversaciones.<button class="cpy" onclick="copyMsg(this)">Copiar</button></div>
</div></div>
<div class="pc"><div class="ph" onclick="togglePhase(this)"><div class="pn2 an">📋</div><div class="pi2"><h3>Resumen Ejecutivo de Auditoria</h3><div class="psb">Argumento central para negociacion</div></div><div class="ar">&#x25BC;</div></div><div class="pb2 op">
<div class="pd2">El resumen ejecutivo es el documento que abre las puertas. Debe ser una pagina, maximo dos, con los datos clave del catalogo.</div>
<div class="hb"><div class="hl">El Argumento de Apertura</div><strong>\"Este catalogo de 190 canciones esta generando $66,824/mes en ingresos no reclamados. Con 12 canciones auditadas que muestran $34,700/mes en fuga solo de nodos identificados. El potencial de recuperacion anual es de $800,000+. Ofrecemos el 100% del catalogo para distribucion con Content ID activo a cambio de un adelanto de $500K-$1M.\"</strong></div>
<div class="mg" style="margin-top:10px">
<div class="mc3"><div class="ml">Canciones</div><div class="mv accent">190</div><div class="mnote">Catalogo completo</div></div>
<div class="mc3"><div class="ml">Yield/Mes</div><div class="mv success">$66.8K</div><div class="mnote">Ingreso fugado</div></div>
<div class="mc3"><div class="ml">Proy. Anual</div><div class="mv gold">$801K</div><div class="mnote">Yield x 12</div></div>
<div class="mc3"><div class="ml">Adelanto</div><div class="mv success">$500K-$1M</div><div class="mnote">Rango objetivo</div></div>
<div class="mc3"><div class="ml">Nodos</div><div class="mv danger">15K+</div><div class="mnote">Canales sin monetizar</div></div>
<div class="mc3"><div class="ml">Views/Mes</div><div class="mv cyan">55.7M</div><div class="mnote">Estimadas eCPM $1.20</div></div>
</div>
</div></div>
</div>"""

new_templates = """<div class="tc" id="tab-templates">

<div class="mp-hero">
  <div class="mp-hero-tags">
    <span class="mp-hero-tag accent">4 MENSAJES</span>
    <span class="mp-hero-tag">PITCH DECK</span>
    <span class="mp-hero-tag cyan">AUDITOR\u00cdA</span>
    <span class="mp-hero-tag green">LISTO PARA ENVIAR</span>
  </div>
  <h2 class="mp-hero-title">Plantillas <span class="hl">Ejecutivas</span></h2>
  <p class="mp-hero-sub">Mensajes redactados para la negociaci\u00f3n con distribuidoras multinacionales. Secuencia progresiva: de sondeo inicial a cierre con deadline.</p>
</div>

<div class="pc"><div class="ph" onclick="togglePhase(this)"><div class="pn2 an">\U0001f4ec</div><div class="pi2"><h3>Secuencia de 4 Mensajes para Multinacionales</h3><div class="psb">Believe, The Orchard y otras distribuidoras</div></div><div class="ar">\u25bc</div></div><div class="pb2 op">
<div class="pd2">Esta secuencia de mensajes progresivos esta disenada para pasar de un sondeo inicial a una propuesta formal de adelanto sin revelar toda la estrategia tecnica prematuramente. Usa el bot\u00f3n <strong>Copiar</strong> para llevar cada mensaje a tu bandeja de correo.</div>
<div style="font-size:11px;font-weight:600;color:var(--accent);margin:10px 0 4px;display:flex;align-items:center;gap:6px"><span style="display:inline-flex;align-items:center;justify-content:center;width:20px;height:20px;border-radius:50%;background:var(--accent);color:#0d0d0f;font-size:9px;font-weight:700">1</span> Mensaje 1: Sondeo Inicial</div>
<div class="tb">Hola [Nombre], te contactamos desde Nuclear AIMA, representando el catalogo de Ramon Orlando, leyenda del merengue dominicano con 50+ anos de carrera. Estamos preparando el lanzamiento digital de su catalogo completo de 190 canciones para su 50 Aniversario (23 Sept 2026, Estadio Olimpico). El catalogo ya genera +15M views/mes organicamente en YouTube. Nos gustaria explorar una posible colaboracion para la distribucion global. Estarian abiertos a una conversacion preliminar?<button class="cpy" onclick="copyMsg(this)">Copiar</button></div>
<div style="font-size:11px;font-weight:600;color:var(--accent);margin:10px 0 4px;display:flex;align-items:center;gap:6px"><span style="display:inline-flex;align-items:center;justify-content:center;width:20px;height:20px;border-radius:50%;background:var(--accent);color:#0d0d0f;font-size:9px;font-weight:700">2</span> Mensaje 2: Confirmacion + Datos</div>
<div class="tb">Gracias por su respuesta. Adjuntamos un resumen ejecutivo de nuestra auditoria tecnica, que documenta el rendimiento actual del catalogo en YouTube (nodos, vistas, ingresos fugados). Tambien confirmamos que el catalogo esta siendo registrado en ONDA (Oficina Nacional de Derecho de Autor) y contamos con carta de autorizacion notariada del artista. El potencial de recuperacion de ingresos es significativo. Nos gustaria compartir el detalle completo en una reunion virtual.<button class="cpy" onclick="copyMsg(this)">Copiar</button></div>
<div style="font-size:11px;font-weight:600;color:var(--accent);margin:10px 0 4px;display:flex;align-items:center;gap:6px"><span style="display:inline-flex;align-items:center;justify-content:center;width:20px;height:20px;border-radius:50%;background:var(--accent);color:#0d0d0f;font-size:9px;font-weight:700">3</span> Mensaje 3: Propuesta Formal</div>
<div class="tb">Estimado/a [Nombre], tras nuestra conversacion, formalizamos nuestra propuesta: ofrecemos el catalogo completo de Ramon Orlando (190 canciones, 17 albumes, categoria merengue/tropical) para distribucion global con Content ID activo, a cambio de un adelanto (signing bonus) en el rango de $500,000 - $1,000,000 USD. El catalogo tiene un yield mensual estimado de $66,824 y proyecta +$800K anuales en ingresos recuperables. Adjuntamos expediente completo con auditoria, registros ONDA y proyecciones financieras.<button class="cpy" onclick="copyMsg(this)">Copiar</button></div>
<div style="font-size:11px;font-weight:600;color:var(--accent);margin:10px 0 4px;display:flex;align-items:center;gap:6px"><span style="display:inline-flex;align-items:center;justify-content:center;width:20px;height:20px;border-radius:50%;background:var(--danger);color:#0d0d0f;font-size:9px;font-weight:700">4</span> Mensaje 4: Cierre con Deadline</div>
<div class="tb">Hola [Nombre], queremos informarles que estamos evaluando multiples ofertas y hemos establecido el [Fecha] como fecha limite para recibir propuestas formales. El concierto del 23 de septiembre generara un pico masivo de trafico y reproducciones, y necesitamos tener la distribucion activada antes de esa fecha para maximizar la captura de ingresos. Agradeceriamos su respuesta a la brevedad para continuar las conversaciones.<button class="cpy" onclick="copyMsg(this)">Copiar</button></div>
</div></div>
<div class="pc"><div class="ph" onclick="togglePhase(this)"><div class="pn2 an">\U0001f4cb</div><div class="pi2"><h3>Resumen Ejecutivo de Auditoria</h3><div class="psb">Argumento central para negociacion</div></div><div class="ar">\u25bc</div></div><div class="pb2 op">
<div class="pd2">El resumen ejecutivo es el documento que abre las puertas. Debe ser una pagina, maximo dos, con los datos clave del catalogo. Este es tu <strong>argumento de apertura</strong> ante cualquier distribuidora.</div>
<div class="hb"><div class="hl">\U0001f4a1 El Argumento de Apertura</div><strong>\"Este catalogo de 190 canciones esta generando $66,824/mes en ingresos no reclamados. Con 12 canciones auditadas que muestran $34,700/mes en fuga solo de nodos identificados. El potencial de recuperacion anual es de $800,000+. Ofrecemos el 100% del catalogo para distribucion con Content ID activo a cambio de un adelanto de $500K-$1M.\"</strong></div>
<div class="mg" style="margin-top:10px">
<div class="mc3"><div class="ml">Canciones</div><div class="mv accent">190</div><div class="mnote">Catalogo completo registrado</div></div>
<div class="mc3"><div class="ml">Yield/Mes</div><div class="mv success">$66.8K</div><div class="mnote">Ingreso fugado actual</div></div>
<div class="mc3"><div class="ml">Proy. Anual</div><div class="mv gold">$801K</div><div class="mnote">Yield x 12 meses</div></div>
<div class="mc3"><div class="ml">Adelanto</div><div class="mv success">$500K\u2013$1M</div><div class="mnote">Rango objetivo negociaci\u00f3n</div></div>
<div class="mc3"><div class="ml">Nodos</div><div class="mv danger">15K+</div><div class="mnote">Canales sin monetizar</div></div>
<div class="mc3"><div class="ml">Views/Mes</div><div class="mv cyan">55.7M</div><div class="mnote">eCPM estimado $1.20</div></div>
</div>
</div></div>
</div>"""

assert old_templates in html, "tab-templates old content not found!"
html = html.replace(old_templates, new_templates)
print("✅ tab-templates redesigned")

# ============================================================
# 6. WRITE FILE
# ============================================================
with open('master-plan.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\n✅ DONE! New file size: {len(html)} bytes")
print("All 4 tabs redesigned with premium look while preserving JS functionality.")
