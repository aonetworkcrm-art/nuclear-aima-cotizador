#!/usr/bin/env python3
import os, sys, json

os.chdir(os.path.dirname(os.path.abspath(__file__)))

header = '''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Star Master Plan · Nuclear AIMA · Hoja de Ruta Estratégica</title>
<script defer src="sidebar.js"></script>
<style>
  :root{--bg:#0a0a0c;--bg2:#111114;--bg3:#18181c;--bg4:#202024;--border:rgba(255,255,255,0.06);--border2:rgba(255,255,255,0.12);--text:#f0ede8;--muted:#6b6966;--accent:#c9a96e;--accent2:#e8c98a;--danger:#e05c5c;--success:#4cad7c;--cyan:#4ad0e0;--gold:#f59e0b;--font:'Inter',system-ui,sans-serif;--mono:'JetBrains Mono','Fira Code',monospace;--r:10px;--r2:16px}
  *{box-sizing:border-box;margin:0;padding:0}
  body{background:var(--bg);color:var(--text);font-family:var(--font);min-height:100vh;background-image:radial-gradient(ellipse at 0% 0%,rgba(201,169,110,0.04) 0%,transparent 50%),radial-gradient(ellipse at 100% 100%,rgba(76,173,124,0.03) 0%,transparent 50%)}
  .mc{max-width:1300px;margin:0 auto;padding:20px}
  .mh{text-align:center;padding:20px 0 14px;border-bottom:0.5px solid var(--border);margin-bottom:16px}
  .mh .bad{display:flex;justify-content:center;gap:8px;flex-wrap:wrap;margin-bottom:8px}
  .mh .bad span{display:inline-flex;align-items:center;gap:5px;background:linear-gradient(135deg,rgba(201,169,110,0.12),rgba(201,169,110,0.04));border:0.5px solid rgba(201,169,110,0.25);border-radius:20px;padding:3px 10px;font-size:9px;font-weight:500;color:var(--accent);letter-spacing:0.02em}
  .mh .bad .live{background:rgba(224,92,92,0.1);border-color:rgba(224,92,92,0.25);color:var(--danger)}
  .mh h1{font-size:28px;font-weight:600;letter-spacing:-0.5px}
  .mh h1 .gd{color:var(--gold)}
  .mh .sub{font-size:12px;color:var(--muted);margin-top:4px;max-width:700px;margin-left:auto;margin-right:auto;line-height:1.5}
  .ps{margin-bottom:16px}
  .ps .pb{background:var(--bg3);border:0.5px solid var(--border);border-radius:20px;height:24px;overflow:hidden;position:relative}
  .ps .pf{height:100%;border-radius:20px;background:linear-gradient(90deg,var(--success),var(--accent),var(--gold));transition:width 0.8s ease;position:relative}
  .ps .pf::after{content:'';position:absolute;top:0;left:0;right:0;bottom:0;background:linear-gradient(90deg,transparent,rgba(255,255,255,0.1),transparent);animation:shim 2s infinite}
  @keyframes shim{0%{transform:translateX(-100%)}100%{transform:translateX(100%)}}
  .ps .pt{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);font-size:10px;font-weight:600;color:#0d0d0f;font-family:var(--mono)}
  .ps .ps2{display:flex;gap:16px;justify-content:center;margin-top:8px;flex-wrap:wrap}
  .ps .ps2 .pi{text-align:center}
  .ps .ps2 .pi .pn{font-size:16px;font-weight:600;font-family:var(--mono)}
  .ps .ps2 .pi .pn.dn{color:var(--success)}
  .ps .ps2 .pi .pn.pd{color:var(--muted)}
  .ps .ps2 .pi .pn.ac{color:var(--accent)}
  .ps .ps2 .pi .pl{font-size:8px;color:var(--muted);text-transform:uppercase;letter-spacing:0.06em}
  .tn{display:flex;gap:4px;margin-bottom:16px;flex-wrap:wrap;background:var(--bg2);border:0.5px solid var(--border);border-radius:var(--r2);padding:4px}
  .tn button{padding:7px 12px;border-radius:var(--r);border:none;cursor:pointer;font-size:10px;font-weight:500;font-family:var(--font);background:transparent;color:var(--muted);transition:all 0.15s;display:flex;align-items:center;gap:4px}
  .tn button:hover{color:var(--text);background:var(--bg3)}
  .tn button.act{background:var(--accent);color:#0d0d0f}
  .tc{display:none}
  .tc.act{display:block}
  .pc{background:var(--bg2);border:0.5px solid var(--border);border-radius:var(--r2);margin-bottom:14px;overflow:hidden}
  .pc .ph{display:flex;align-items:center;gap:12px;padding:14px 18px;border-bottom:0.5px solid var(--border);cursor:pointer;transition:background 0.15s}
  .pc .ph:hover{background:var(--bg3)}
  .pc .ph .pn2{width:32px;height:32px;border-radius:50%;flex-shrink:0;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700;background:var(--bg4);color:var(--muted);border:1px solid var(--border)}
  .pc .ph .pn2.dn{background:var(--success);color:#0d0d0f;border-color:var(--success)}
  .pc .ph .pn2.an{background:var(--accent);color:#0d0d0f;border-color:var(--accent)}
  .pc .ph .pi2{flex:1}
  .pc .ph .pi2 h3{font-size:13px;font-weight:600}
  .pc .ph .pi2 .psb{font-size:10px;color:var(--muted);margin-top:1px}
  .pc .ph .ps3{font-size:9px;padding:2px 8px;border-radius:4px;font-weight:500}
  .pc .ph .ps3.dn{background:rgba(76,173,124,0.12);color:var(--success)}
  .pc .ph .ps3.pd{background:rgba(107,105,102,0.12);color:var(--muted)}
  .pc .ph .ps3.an{background:rgba(201,169,110,0.12);color:var(--accent)}
  .pc .ph .ar{font-size:12px;color:var(--muted);transition:transform 0.2s}
  .pc .ph .ar.op{transform:rotate(180deg)}
  .pc .pb2{display:none;padding:14px 18px}
  .pc .pb2.op{display:block}
  .pc .pb2 .pd2{font-size:11px;color:var(--muted);line-height:1.6;margin-bottom:12px}
  .cl{margin:10px 0}
  .cl .cl2{display:flex;align-items:flex-start;gap:8px;padding:6px 0;cursor:pointer;font-size:11px;line-height:1.5;border-bottom:0.5px solid rgba(255,255,255,0.03)}
  .cl .cl2 .cb{width:14px;height:14px;border-radius:3px;flex-shrink:0;border:1.5px solid var(--border2);margin-top:2px;display:flex;align-items:center;justify-content:center;font-size:8px;transition:all 0.15s}
  .cl .cl2 .cb.ch{background:var(--success);border-color:var(--success);color:#0d0d0f}
  .cl .cl2 .ct{flex:1}
  .cl .cl2 .ct.do{text-decoration:line-through;color:var(--muted);opacity:0.6}
  .pc .pb2 .mr{display:flex;gap:12px;flex-wrap:wrap;margin:8px 0 12px}
  .pc .pb2 .mc2{display:inline-flex;align-items:center;gap:3px;padding:2px 8px;border-radius:4px;font-size:9px;background:var(--bg4);color:var(--muted);border:0.5px solid var(--border)}
  .tl{padding:16px 0 16px 28px;position:relative;margin:14px 0}
  .tl::before{content:'';position:absolute;left:10px;top:0;bottom:0;width:1.5px;background:linear-gradient(180deg,var(--accent),var(--success),var(--gold),var(--cyan),var(--danger))}
  .tl .tli{position:relative;margin-bottom:20px}
  .tl .tli .dot{position:absolute;left:-24px;top:4px;width:10px;height:10px;border-radius:50%;border:2px solid var(--bg)}
  .tl .tli .dot.dn{background:var(--success)}
  .tl .tli h4{font-size:12px;font-weight:600}
  .tl .tli .ti{font-size:9px;color:var(--muted);font-family:var(--mono);margin-top:1px}
  .tl .tli .td2{font-size:10px;color:var(--muted);margin-top:3px;line-height:1.5}
  .tb{background:var(--bg3);border:0.5px solid var(--border);border-radius:var(--r);padding:12px;margin:8px 0;font-size:11px;line-height:1.7;white-space:pre-wrap;position:relative}
  .tb .cpy{position:absolute;top:6px;right:6px;padding:2px 8px;border-radius:4px;border:none;cursor:pointer;font-size:8px;font-weight:500;font-family:var(--font);background:var(--bg4);color:var(--muted);transition:all 0.15s}
  .tb .cpy:hover{background:var(--accent);color:#0d0d0f}
  .mg{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:8px;margin-bottom:14px}
  .mg .mc3{background:var(--bg3);border:0.5px solid var(--border);border-radius:var(--r);padding:12px;text-align:center}
  .mg .mc3 .ml{font-size:7px;color:var(--muted);text-transform:uppercase;letter-spacing:0.07em}
  .mg .mc3 .mv{font-size:18px;font-weight:700;font-family:var(--mono);margin-top:2px}
  .rg{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:8px;margin:10px 0}
  .rg a{display:flex;align-items:center;gap:8px;padding:8px 12px;background:var(--bg3);border:0.5px solid var(--border);border-radius:var(--r);text-decoration:none;color:var(--text);font-size:10px;transition:all 0.15s}
  .rg a:hover{border-color:var(--accent);background:var(--bg4)}
  .hb{background:linear-gradient(135deg,rgba(201,169,110,0.06),rgba(201,169,110,0.02));border-left:2px solid var(--accent);padding:10px 14px;border-radius:0 var(--r) var(--r) 0;margin:10px 0;font-size:11px;line-height:1.6}
  .hb .hl{font-size:9px;text-transform:uppercase;letter-spacing:0.06em;font-weight:600;color:var(--accent);margin-bottom:4px}
  .hb.ng{border-left-color:var(--danger);background:linear-gradient(135deg,rgba(224,92,92,0.06),rgba(224,92,92,0.02))}
  .hb.ng .hl{color:var(--danger)}
  .hb.sc{border-left-color:var(--success);background:linear-gradient(135deg,rgba(76,173,124,0.06),rgba(76,173,124,0.02))}
  .hb.sc .hl{color:var(--success)}
  .dt{width:100%;border-collapse:collapse;font-size:10px;margin:10px 0}
  .dt th{text-align:left;padding:6px 8px;color:var(--muted);font-weight:500;font-size:8px;text-transform:uppercase;letter-spacing:0.06em;border-bottom:0.5px solid var(--border);background:var(--bg3)}
  .dt td{padding:5px 8px;border-bottom:0.5px solid rgba(255,255,255,0.03)}
  .dt tr:hover td{background:rgba(201,169,110,0.03)}
  .sb{display:flex;gap:8px;margin-bottom:14px;flex-wrap:wrap;align-items:center}
  .sb input{flex:1;min-width:200px;background:var(--bg2);border:0.5px solid var(--border);border-radius:var(--r);padding:8px 12px;color:var(--text);font-size:12px;font-family:var(--font);outline:none;transition:border 0.15s}
  .sb input:focus{border-color:var(--accent)}
  .sb input::placeholder{color:var(--muted)}
  @media(max-width:768px){.mc{padding:10px}.mh h1{font-size:22px}.tn button{font-size:9px;padding:5px 8px}.pc .ph{padding:10px 14px}.pc .pb2{padding:10px 14px}.mg{grid-template-columns:1fr 1fr}}
</style>
</head>
<body>
<div class="mc">
'''

# Header
header_body = '''
  <div class="mh">
    <div class="bad">
      <span class="live">HOJA DE RUTA ESTRATÉGICA</span>
      <span>8 FASES · 981 LÍNEAS DE PLAN</span>
      <span>localStorage · PROGRESO</span>
    </div>
    <h1>Master Plan <span class="gd">Ramón Orlando</span></h1>
    <div class="sub">Las 8 fases del plan integrado: desde la fundación legal y auditoría técnica hasta la distribución global, tokenización Web3 y el evento del 50 Aniversario. Basado en el documento maestro de 132KB (start.txt).</div>
  </div>

  <!-- Progress Section -->
  <div class="ps" id="progressSection">
    <div class="pb">
      <div class="pf" id="progressFill" style="width:0%"></div>
      <div class="pt" id="progressText">0% Completado</div>
    </div>
    <div class="ps2">
      <div class="pi"><div class="pn dn" id="taskDone">0</div><div class="pl">Tareas Hechas</div></div>
      <div class="pi"><div class="pn pd" id="taskTotal">52</div><div class="pl">Tareas Totales</div></div>
      <div class="pi"><div class="pn ac" id="currentPhase">—</div><div class="pl">Fase Actual</div></div>
    </div>
  </div>

  <!-- Tab Nav -->
  <div class="tn" id="tabNav">
    <button class="act" onclick="switchT(this,0)">Fases</button>
    <button onclick="switchT(this,1)">Linea de Tiempo</button>
    <button onclick="switchT(this,2)">Metricas Clave</button>
    <button onclick="switchT(this,3)">Plantillas</button>
    <button onclick="switchT(this,4)">Recursos</button>
  </div>
'''

print("Header written successfully")
# Phase data
phases_data = [
    {
        "name": "Fundaci\u00f3n Legal y Corporativa",
        "sub": "ONAPI, SRL, ONDA, Contrato Matriz",
        "icon": "\U0001f3db\ufe0f",
        "desc": "Establecer la infraestructura legal y corporativa necesaria para operar como sello independiente y negociar con distribuidoras internacionales.",
        "status": "active",
        "cost": "$800 - $1,200 USD",
        "time": "Semanas 1-3",
        "tasks": ["Registrar Nombre Comercial en ONAPI (Clase 41 y 35)", "Redactar estatutos SAS y pagar impuesto DGII", "Registro Mercantil en C\u00e1mara de Comercio", "Obtener RNC", "Registrar fonograma en ONDA a nombre de la empresa", "Firmar Contrato de Administraci\u00f3n", "Abrir cuenta bancaria corporativa", "Preparar lista oficial de 178 canciones"]
    },
    {
        "name": "Auditor\u00eda T\u00e9cnica del Cat\u00e1logo",
        "sub": "12 principales + expansi\u00f3n a 178",
        "icon": "\U0001f4ca",
        "desc": "Ejecutar el an\u00e1lisis t\u00e9cnico del cat\u00e1logo para documentar el valor real del activo musical.",
        "status": "active",
        "cost": "$0 (herramientas propias)",
        "time": "Semanas 2-4",
        "tasks": ["Auditar 12 canciones principales con The Tool", "Generar reporte ejecutivo de auditor\u00eda", "Expandir auditor\u00eda a las 178 canciones", "Calcular yield mensual total e ingreso fugado", "Identificar canales sin Content ID", "Preparar matriz de nodos por canci\u00f3n", "Exportar reporte PDF ejecutivo", "Redactar carta de autorizaci\u00f3n notariada"]
    },
    {
        "name": "Gesti\u00f3n con el Artista",
        "sub": "Expectativas, autorizaci\u00f3n y coordinaci\u00f3n",
        "icon": "\U0001f91d",
        "desc": "Gestionar la relaci\u00f3n con el artista de manera profesional y gradual.",
        "status": "pending",
        "cost": "$0",
        "time": "Semanas 1-2",
        "tasks": ["Agendar reuni\u00f3n con Ram\u00f3n Orlando", "Explicar importancia del registro ONDA", "No revelar LLC/tokenizaci\u00f3n prematuramente", "Gestionar expectativas sobre tiempos", "Presentar el 23 Sept como catalizador", "Firmar carta de autorizaci\u00f3n", "Obtener documentos del artista", "Coordinar visita a ONDA"]
    },
    {
        "name": "Registro en Sociedades de Gesti\u00f3n",
        "sub": "SoundExchange, ASCAP/BMI, SGACEDOM",
        "icon": "\U0001f3e6",
        "desc": "Registrar el cat\u00e1logo en todas las sociedades de gesti\u00f3n colectiva y plataformas de monetizaci\u00f3n.",
        "status": "pending",
        "cost": "$0 - $50",
        "time": "Semanas 3-6",
        "tasks": ["Registrar cat\u00e1logo en SoundExchange", "Reclamar regal\u00edas retroactivas 3 a\u00f1os", "Registrar en ASCAP/BMI", "Registrar en SGACEDOM", "Configurar Content ID en YouTube", "Dividir 178 canciones en 6 colecciones", "Asignar ISRCs", "Configurar distribuci\u00f3n streaming"]
    },
    {
        "name": "Pitch a Multinacionales",
        "sub": "Believe, The Orchard, beatBread",
        "icon": "\U0001f4ec",
        "desc": "Ejecutar secuencia de 4 mensajes hacia multinacionales usando auditor\u00eda como prueba.",
        "status": "pending",
        "cost": "$0",
        "time": "Semanas 4-8",
        "tasks": ["Mensaje 1: Presentaci\u00f3n valor hist\u00f3rico", "Mensaje 2: Env\u00edo auditor\u00eda + ONDA", "Mensaje 3: Propuesta formal + adelanto", "Mensaje 4: Cierre con deadline", "Contactar Believe Music", "Contactar The Orchard", "Evaluar beatBread como puente", "Negociar adelanto $500K-$1M"]
    },
    {
        "name": "Infraestructura Web3 y Tokenizaci\u00f3n",
        "sub": "LLC, Smart Contracts, Frontend",
        "icon": "\u26a1",
        "desc": "Construir la infraestructura Web3: LLC, smart contracts, tokenizaci\u00f3n y boletos inteligentes.",
        "status": "pending",
        "cost": "$2K - $5K",
        "time": "Meses 3-5",
        "tasks": ["Constituir LLC en Wyoming", "Abrir cuenta bancaria EE.UU.", "Desplegar smart contracts Base/Polygon", "Crear token de cat\u00e1logo", "Frontend Next.js + wallet connect", "Preventa experiencias VIP", "Sistema de afiliados con smartlinks", "Boletos NFC + NFTs (Tuboleta Pass)"]
    },
    {
        "name": "Evento 50 Aniversario",
        "sub": "23 Sept 2026 - Estadio Ol\u00edmpico",
        "icon": "\U0001f3df\ufe0f",
        "desc": "Utilizar el concierto como catalizador para maximizar ingresos y urgencia.",
        "status": "pending",
        "cost": "$5K - $15K",
        "time": "Septiembre 2026",
        "tasks": ["Campa\u00f1a marketing org\u00e1nico pre-evento", "Venta experiencias premium", "Smartlinks afiliados 40 artistas", "Acceso virtual di\u00e1spora $25", "Distribuci\u00f3n masiva post-evento", "Capturar pico tr\u00e1fico", "Monitoreo ingresos tiempo real", "Content ID en picos de reproducci\u00f3n"]
    },
    {
        "name": "Ejecuci\u00f3n y Escalabilidad",
        "sub": "MVP, documentaci\u00f3n, replicaci\u00f3n",
        "icon": "\U0001f680",
        "desc": "Cerrar acuerdo, recibir capital, y documentar modelo como MVP replicable.",
        "status": "pending",
        "cost": "$1K - $3K",
        "time": "Mes 6+",
        "tasks": ["Firmar contrato distribuidora", "Recibir capital adelanto", "Activar recolecci\u00f3n regal\u00edas", "Documentar modelo MVP", "Identificar pr\u00f3ximos cat\u00e1logos", "Refinar procesos auditor\u00eda", "Escalar a m\u00faltiples cat\u00e1logos", "M\u00e9tricas de \u00e9xito Hyperion"]
    }
]

# Generate phase cards HTML
phases_html = ''
for i, p in enumerate(phases_data):
    num = i + 1
    status_class = 'dn' if p['status'] == 'done' else ('an' if p['status'] == 'active' else 'pd')
    status_label = 'En Progreso' if p['status'] == 'active' else ('Completada' if p['status'] == 'done' else 'Pendiente')
    
    tasks_html = ''
    for t in p['tasks']:
        tasks_html += f'<div class=\"cl2\" onclick=\"toggleTask(this,\'p{num}_{p[\"tasks\"].index(t)}\')\"><div class=\"cb\" id=\"cb_p{num}_{p[\"tasks\"].index(t)}\"></div><div class=\"ct\" id=\"ct_p{num}_{p[\"tasks\"].index(t)}\">{t}</div></div>\n'
    
    phases_html += f'''
  <div class=\"pc\">
    <div class=\"ph\" onclick=\"togglePhase(this)\">
      <div class=\"pn2 {status_class}\">{p['icon']}</div>
      <div class=\"pi2\">
        <h3>Fase {num}: {p['name']}</h3>
        <div class=\"psb\">{p['sub']}</div>
      </div>
      <div class=\"ps3 {status_class}\">{p['cost']}</div>
      <div class=\"ar\">\u25bc</div>
    </div>
    <div class=\"pb2\">
      <div class=\"pd2\">{p['desc']}</div>
      <div class=\"mr\">
        <span class=\"mc2 accent\">{p['time']}</span>
        <span class=\"mc2 success\">{p['cost']}</span>
        <span class=\"mc2\">{len(p['tasks'])} tareas</span>
        <span class=\"mc2 {status_class}\">{status_label}</span>
      </div>
      <div class=\"cl\">{tasks_html}</div>
    </div>
  </div>'''

# Timeline HTML
timeline_items = [
    ("Semanas 1-3", "Fase 1: Fundaci\u00f3n Legal", "\U0001f3db\ufe0f Registrar ONAPI, SRL, ONDA, Contrato Matriz", "phase1"),
    ("Semanas 2-4", "Fase 2: Auditor\u00eda T\u00e9cnica", "\U0001f4ca Auditar 12 canciones principales, generar reporte", "phase2"),
    ("Semanas 1-2", "Fase 3: Gesti\u00f3n Artista", "\U0001f91d Presentar plan, firmar autorizaci\u00f3n", "phase3"),
    ("Semanas 3-6", "Fase 4: Registro Gesti\u00f3n Colectiva", "\U0001f3e6 SoundExchange, ASCAP/BMI, SGACEDOM", "phase4"),
    ("Semanas 4-8", "Fase 5: Pitch a Multinacionales", "\U0001f4ec Secuencia 4 mensajes + negociaci\u00f3n adelanto", "phase5"),
    ("Meses 3-5", "Fase 6: Infraestructura Web3", "\u26a1 LLC Wyoming, Smart Contracts, Tokenizaci\u00f3n", "phase6"),
    ("Septiembre 2026", "Fase 7: Evento 50 Aniversario", "\U0001f3df\ufe0f Estadio Ol\u00edmpico, experiencias VIP, afiliados", "phase7"),
    ("Mes 6+", "Fase 8: Ejecuci\u00f3n y Escalabilidad", "\U0001f680 Cierre, capital, replicaci\u00f3n del modelo", "phase8")
]

timeline_html = ''
for t in timeline_items:
    timeline_html += f'''
  <div class=\"tli\">
    <div class=\"dot {t[3]}\"></div>
    <h4>{t[1]}</h4>
    <div class=\"ti\">{t[0]}</div>
    <div class=\"td2\">{t[2]}</div>
  </div>'''

# Templates HTML
templates_html = '''
  <div class=\"pc\">
    <div class=\"ph\" onclick=\"togglePhase(this)\">
      <div class=\"pn2 an\">\U0001f4ec</div>
      <div class=\"pi2\"><h3>Secuencia de 4 Mensajes para Multinacionales</h3><div class=\"psb\">Believe, The Orchard y otras distribuidoras</div></div>
      <div class=\"ar\">\u25bc</div>
    </div>
    <div class=\"pb2 op\">
      <div class=\"pd2\">Esta secuencia de mensajes progresivos est\u00e1 dise\u00f1ada para pasar de un sondeo inicial a una propuesta formal de adelanto sin revelar toda la estrategia t\u00e9cnica prematuramente.</div>
      
      <div style=\"font-size:11px;font-weight:600;color:var(--accent);margin:8px 0 4px\">Mensaje 1: Sondeo Inicial</div>
      <div class=\"tb\">Hola [Nombre], te contactamos desde Nuclear AIMA, representando el cat\u00e1logo de Ram\u00f3n Orlando, leyenda del merengue dominicano con 50+ a\u00f1os de carrera. Estamos preparando el lanzamiento digital de su cat\u00e1logo completo de 190 canciones para su 50 Aniversario (23 Sept 2026, Estadio Ol\u00edmpico). El cat\u00e1logo ya genera +15M views/mes org\u00e1nicamente en YouTube. Nos gustar\u00eda explorar una posible colaboraci\u00f3n para la distribuci\u00f3n global. \u00bfEstar\u00edan abiertos a una conversaci\u00f3n preliminar?<button class=\"cpy\" onclick=\"copyMsg(this)\">Copiar</button></div>
      
      <div style=\"font-size:11px;font-weight:600;color:var(--accent);margin:8px 0 4px\">Mensaje 2: Confirmaci\u00f3n + Datos</div>
      <div class=\"tb\">Gracias por su respuesta. Adjuntamos un resumen ejecutivo de nuestra auditor\u00eda t\u00e9cnica, que documenta el rendimiento actual del cat\u00e1logo en YouTube (nodos, vistas, ingresos fugados). Tambi\u00e9n confirmamos que el cat\u00e1logo est\u00e1 siendo registrado en ONDA (Oficina Nacional de Derecho de Autor) y contamos con carta de autorizaci\u00f3n notariada del artista. El potencial de recuperaci\u00f3n de ingresos es significativo. Nos gustar\u00eda compartir el detalle completo en una reuni\u00f3n virtual.<button class=\"cpy\" onclick=\"copyMsg(this)\">Copiar</button></div>
      
      <div style=\"font-size:11px;font-weight:600;color:var(--accent);margin:8px 0 4px\">Mensaje 3: Propuesta Formal</div>
      <div class=\"tb\">Estimado/a [Nombre], tras nuestra conversaci\u00f3n, formalizamos nuestra propuesta: ofrecemos el cat\u00e1logo completo de Ram\u00f3n Orlando (190 canciones, 17 \u00e1lbumes, categor\u00eda merengue/tropical) para distribuci\u00f3n global con Content ID activo, a cambio de un adelanto (signing bonus) en el rango de $500,000 - $1,000,000 USD. El cat\u00e1logo tiene un yield mensual estimado de $66,824 y proyecta +$800K anuales en ingresos recuperables. Adjuntamos expediente completo con auditor\u00eda, registros ONDA y proyecciones financieras.<button class=\"cpy\" onclick=\"copyMsg(this)\">Copiar</button></div>
      
      <div style=\"font-size:11px;font-weight:600;color:var(--accent);margin:8px 0 4px\">Mensaje 4: Cierre con Deadline</div>
      <div class=\"tb\">Hola [Nombre], queremos informarles que estamos evaluando m\u00faltiples ofertas y hemos establecido el [Fecha] como fecha l\u00edmite para recibir propuestas formales. El concierto del 23 de septiembre generar\u00e1 un pico masivo de tr\u00e1fico y reproducciones, y necesitamos tener la distribuci\u00f3n activada antes de esa fecha para maximizar la captura de ingresos. Agradecer\u00edamos su respuesta a la brevedad para continuar las conversaciones.<button class=\"cpy\" onclick=\"copyMsg(this)\">Copiar</button></div>
    </div>
  </div>
  
  <div class=\"pc\">
    <div class=\"ph\" onclick=\"togglePhase(this)\">
      <div class=\"pn2 an\">\U0001f4cb</div>
      <div class=\"pi2\"><h3>Resumen Ejecutivo de Auditor\u00eda</h3><div class=\"psb\">Argumento central para negociaci\u00f3n</div></div>
      <div class=\"ar\">\u25bc</div>
    </div>
    <div class=\"pb2 op\">
      <div class=\"pd2\">El resumen ejecutivo es el documento que abre las puertas. Debe ser una p\u00e1gina, m\u00e1ximo dos, con los datos clave del cat\u00e1logo.</div>
      <div class=\"hb\">
        <div class=\"hl\">El Argumento de Apertura</div>
        <strong>\"Este cat\u00e1logo de 190 canciones est\u00e1 generando $66,824/mes en ingresos no reclamados. Con 12 canciones auditadas que muestran $34,700/mes en fuga solo de nodos identificados. El potencial de recuperaci\u00f3n anual es de $800,000+. Ofrecemos el 100% del cat\u00e1logo para distribuci\u00f3n con Content ID activo a cambio de un adelanto de $500K-$1M.\"</strong>
      </div>
      <div class=\"mg\" style=\"margin-top:10px\">
        <div class=\"mc3\"><div class=\"ml\">Canciones</div><div class=\"mv accent\">190</div><div class=\"mnote\">Cat\u00e1logo completo</div></div>
        <div class=\"mc3\"><div class=\"ml\">Yield/Mes</div><div class=\"mv success\">$66.8K</div><div class=\"mnote\">Ingreso fugado</div></div>
        <div class=\"mc3\"><div class=\"ml\">Proyecci\u00f3n Anual</div><div class=\"mv gold\">$801K</div><div class=\"mnote\">Yield x 12</div></div>
        <div class=\"mc3\"><div class=\"ml\">Adelanto</div><div class=\"mv success\">$500K-$1M</div><div class=\"mnote\">Rango objetivo</div></div>
        <div class=\"mc3\"><div class=\"ml\">Nodos</div><div class=\"mv danger\">15K+</div><div class=\"mnote\">Canales sin monetizar</div></div>
        <div class=\"mc3\"><div class=\"ml\">Views/Mes</div><div class=\"mv cyan\">55.7M</div><div class=\"mnote\">Estimadas eCPM $1.20</div></div>
      </div>
    </div>
  </div>'''

# Recursos HTML
resources_html = '''
  <div class=\"rg\">
    <a href=\"oraculo.html\"><span class=\"r-icon\">\U0001f52e</span> Or\u00e1culo en Vivo - Yield y datos tiempo real</a>
    <a href=\"adelantos.html\"><span class=\"r-icon\">\U0001f4b0</span> Adelantos - Plataformas de financiamiento</a>
    <a href=\"onapi-onda.html\"><span class=\"r-icon\">\U0001f3db\ufe0f</span> ONAPI/ONDA - Gu\u00eda legal paso a paso</a>
    <a href=\"short-tracker.html\"><span class=\"r-icon\">\U0001f3ac</span> Short Tracker - R\u00e9plicas virales YouTube</a>
    <a href=\"osint-center.html\"><span class=\"r-icon\">\U0001f575\ufe0f</span> OSINT Center - Dorks, Keywords, Dominios</a>
    <a href=\"index.html\"><span class=\"r-icon\">\U0001f4ca</span> Dashboard Principal - Centro de Comando</a>
    <a href=\"data/catalogo-completo-ramon-orlando.csv\"><span class=\"r-icon\">\U0001f4c4</span> Cat\u00e1logo Completo CSV</a>
    <a href=\"ramon-orlando/CONTRATO%20DE%20ASESORAMIENTO%20ESTRAT%C3%89GI.txt\"><span class=\"r-icon\">\U0001f4dc</span> Contrato de Asesoramiento</a>
  </div>'''

# JavaScript
js = '''
<script>
const STORAGE_KEY = 'nuclear-masterplan-check';
const TOTAL_TASKS = 64;

function getChecks() {
  try { return JSON.parse(localStorage.getItem(STORAGE_KEY)) || {}; }
  catch { return {}; }
}
function saveChecks(d) {
  try { localStorage.setItem(STORAGE_KEY, JSON.stringify(d)); }
  catch {}
}
function toggleTask(el, id) {
  const checks = getChecks();
  const cb = document.getElementById('cb_' + id);
  const ct = document.getElementById('ct_' + id);
  if (checks[id]) {
    delete checks[id];
    cb.classList.remove('ch');
    cb.textContent = '';
    ct.classList.remove('do');
  } else {
    checks[id] = true;
    cb.classList.add('ch');
    cb.textContent = '\u2713';
    ct.classList.add('do');
  }
  saveChecks(checks);
  updateProgress();
}
function togglePhase(el) {
  const body = el.nextElementSibling;
  const arrow = el.querySelector('.ar');
  body.classList.toggle('op');
  arrow.classList.toggle('op');
}
function updateProgress() {
  const checks = getChecks();
  const done = Object.keys(checks).length;
  const pct = Math.round((done / TOTAL_TASKS) * 100);
  document.getElementById('progressFill').style.width = pct + '%';
  document.getElementById('progressText').textContent = pct + '% Completado';
  document.getElementById('taskDone').textContent = done;
  document.getElementById('taskTotal').textContent = TOTAL_TASKS;
  
  // Current phase
  const activePhases = [1, 2]; // Phases 1 and 2 are active
  const cp = activePhases[0];
  document.getElementById('currentPhase').textContent = 'Fase ' + cp;
}
function switchT(btn, idx) {
  document.querySelectorAll('.tn button').forEach(b => b.classList.remove('act'));
  document.querySelectorAll('.tc').forEach(t => t.classList.remove('act'));
  btn.classList.add('act');
  const tabs = ['tab-phases', 'tab-timeline', 'tab-metrics', 'tab-templates', 'tab-resources'];
  document.getElementById(tabs[idx]).classList.add('act');
}
function copyMsg(btn) {
  const text = btn.parentNode.textContent.replace('Copiar', '').trim();
  navigator.clipboard.writeText(text).then(() => {
    btn.textContent = '\u2713 Copiado';
    setTimeout(() => { btn.textContent = 'Copiar'; }, 2000);
  });
}
function filterPhases() {
  const q = document.getElementById('searchInput').value.toLowerCase();
  document.querySelectorAll('.pc').forEach(card => {
    const text = card.textContent.toLowerCase();
    card.style.display = text.includes(q) ? '' : 'none';
  });
}
function filterStatus(s) {
  document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('act'));
  event.target.classList.add('act');
  document.querySelectorAll('.pc').forEach(card => {
    if (s === 'all') { card.style.display = ''; return; }
    const status = card.querySelector('.ps3');
    if (!status) { card.style.display = ''; return; }
    const txt = status.textContent.toLowerCase();
    if (s === 'active') card.style.display = txt.includes('progreso') ? '' : 'none';
    else if (s === 'done') card.style.display = txt.includes('completada') ? '' : 'none';
    else card.style.display = txt.includes('pendiente') ? '' : 'none';
  });
}

document.addEventListener('DOMContentLoaded', function() {
  // Restore checkmarks
  const checks = getChecks();
  Object.keys(checks).forEach(id => {
    const cb = document.getElementById('cb_' + id);
    const ct = document.getElementById('ct_' + id);
    if (cb) { cb.classList.add('ch'); cb.textContent = '\u2713'; }
    if (ct) ct.classList.add('do');
  });
  updateProgress();
});
</script>

</div>
</body>
</html>'''

# Assemble and write final HTML
with open('master-plan.html', 'w', encoding='utf-8') as f:
    f.write(header)
    f.write(header_body)
    f.write('<div class=\"tc act\" id=\"tab-phases\">')
    f.write('<div class=\"sb\"><input type=\"text\" id=\"searchInput\" placeholder=\"Buscar en fases...\" oninput=\"filterPhases()\"><button class=\"filter-btn act\" onclick=\"filterStatus.call({target:this}, \\'all\\')\">Todas</button><button class=\"filter-btn\" onclick=\"filterStatus.call({target:this}, \\'active\\')\">En Progreso</button><button class=\"filter-btn\" onclick=\"filterStatus.call({target:this}, \\'pending\\')\">Pendientes</button></div>')
    f.write(phases_html)
    f.write('</div>')
    
    f.write('<div class=\"tc\" id=\"tab-timeline\"><div class=\"pc\"><div class=\"ph\"><div class=\"pn2 an\">\U0001f4c5</div><div class=\"pi2\"><h3>L\u00ednea de Tiempo del Plan</h3><div class=\"psb\">8 fases desde la fundaci\u00f3n legal hasta la escalabilidad</div></div></div><div class=\"pb2 op\"><div class=\"tl\">')
    f.write(timeline_html)
    f.write('</div></div></div></div>')
    
    f.write('<div class=\"tc\" id=\"tab-metrics\">')
    f.write('<div class=\"mg\"><div class=\"mc3\"><div class=\"ml\">Canciones</div><div class=\"mv accent\">190</div><div class=\"mnote\">Cat\u00e1logo completo</div></div>')
    f.write('<div class=\"mc3\"><div class=\"ml\">\u00c1lbumes</div><div class=\"mv accent\">17</div><div class=\"mnote\">Discograf\u00eda oficial</div></div>')
    f.write('<div class=\"mc3\"><div class=\"ml\">Yield/mes</div><div class=\"mv success\">$66.8K</div><div class=\"mnote\">Ingreso fugado actual</div></div>')
    f.write('<div class=\"mc3\"><div class=\"ml\">Proy. Anual</div><div class=\"mv gold\">$801K</div><div class=\"mnote\">Yield x 12 meses</div></div>')
    f.write('<div class=\"mc3\"><div class=\"ml\">Adelanto 3yr</div><div class=\"mv success\">$1.68M</div><div class=\"mnote\">70% flujo proyectado</div></div>')
    f.write('<div class=\"mc3\"><div class=\"ml\">Nodos</div><div class=\"mv danger\">15K+</div><div class=\"mnote\">Canales detectados</div></div>')
    f.write('<div class=\"mc3\"><div class=\"ml\">Views/mes</div><div class=\"mv cyan\">55.7M</div><div class=\"mnote\">eCPM $1.20</div></div>')
    f.write('<div class=\"mc3\"><div class=\"ml\">Tareas Plan</div><div class=\"mv accent\">64</div><div class=\"mnote\">8 fases x 8 tareas</div></div></div>')
    
    f.write('<div class=\"hb\"><div class=\"hl\">\U0001f4a1 Nota Estrat\u00e9gica</div>El orden de las fases es cr\u00edtico. SoundExchange (Fase 4) puede comenzar en paralelo con la Fase 1. El Pitch a Multinacionales (Fase 5) requiere haber completado la auditor\u00eda (Fase 2) y tener al menos el registro ONDA iniciado (Fase 1).</div>')
    f.write('</div>')
    
    f.write('<div class=\"tc\" id=\"tab-templates\">')
    f.write(templates_html)
    f.write('</div>')
    
    f.write('<div class=\"tc\" id=\"tab-resources\">')
    f.write('<div class=\"pc\"><div class=\"ph\"><div class=\"pn2 an\">\U0001f4c1</div><div class=\"pi2\"><h3>Recursos Relacionados</h3><div class=\"psb\">Herramientas del ecosistema Nuclear AIMA</div></div></div><div class=\"pb2 op\">')
    f.write(resources_html)
    f.write('</div></div></div>')
    
    f.write('<div style=\"text-align:center;padding:16px 0;border-top:0.5px solid var(--border);margin-top:8px\"><p style=\"font-size:9px;color:var(--muted);font-family:var(--mono)\">Master Plan · Nuclear AIMA · Basado en start.txt (981 l\u00edneas) · Progreso guardado en localStorage</p></div>')
    f.write(js)

print("Master plan HTML generated:", os.path.getsize('master-plan.html'), 'bytes')
