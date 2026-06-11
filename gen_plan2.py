#!/usr/bin/env python3
"""Generate the complete master-plan.html"""
import os, sys, json

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Phase data
phases = [
  {
    "num": 1,
    "name": "Fundacion Legal y Corporativa",
    "sub": "ONAPI, SRL, ONDA, Contrato Matriz",
    "icon": "\U0001f3db\ufe0f",
    "desc": "Establecer la infraestructura legal y corporativa necesaria para operar como sello independiente y negociar con distribuidoras internacionales.",
    "status": "active",
    "cost": "$800 - $1,200 USD",
    "time": "Semanas 1-3",
    "tasks": [
      "Registrar Nombre Comercial en ONAPI (Clase 41 y 35)",
      "Redactar estatutos SAS y pagar impuesto DGII",
      "Registro Mercantil en Camara de Comercio",
      "Obtener RNC (Registro Nacional Contribuyente)",
      "Registrar fonograma en ONDA a nombre de la empresa",
      "Firmar Contrato de Administracion con el artista",
      "Abrir cuenta bancaria corporativa",
      "Preparar lista oficial de 178 canciones"
    ]
  },
  {
    "num": 2,
    "name": "Auditoria Tecnica del Catalogo",
    "sub": "12 principales + expansion a 178",
    "icon": "\U0001f4ca",
    "desc": "Ejecutar el analisis tecnico del catalogo para documentar el valor real del activo musical.",
    "status": "active",
    "cost": "$0 (herramientas propias)",
    "time": "Semanas 2-4",
    "tasks": [
      "Auditar 12 canciones principales con The Tool",
      "Generar reporte ejecutivo de auditoria",
      "Expandir auditoria a las 178 canciones",
      "Calcular yield mensual total e ingreso fugado",
      "Identificar canales sin Content ID",
      "Preparar matriz de nodos por cancion",
      "Exportar reporte PDF ejecutivo",
      "Redactar carta de autorizacion notariada"
    ]
  },
  {
    "num": 3,
    "name": "Gestion con el Artista",
    "sub": "Expectativas, autorizacion y coordinacion",
    "icon": "\U0001f91d",
    "desc": "Gestionar la relacion con el artista de manera profesional y gradual.",
    "status": "pending",
    "cost": "$0",
    "time": "Semanas 1-2",
    "tasks": [
      "Agendar reunion con Ramon Orlando",
      "Explicar importancia del registro ONDA",
      "No revelar LLC/tokenizacion prematuramente",
      "Gestionar expectativas sobre tiempos",
      "Presentar el 23 Sept como catalizador",
      "Firmar carta de autorizacion",
      "Obtener documentos del artista",
      "Coordinar visita a ONDA"
    ]
  },
  {
    "num": 4,
    "name": "Registro en Sociedades de Gestion",
    "sub": "SoundExchange, ASCAP/BMI, SGACEDOM",
    "icon": "\U0001f3e6",
    "desc": "Registrar el catalogo en todas las sociedades de gestion colectiva.",
    "status": "pending",
    "cost": "$0 - $50",
    "time": "Semanas 3-6",
    "tasks": [
      "Registrar catalogo en SoundExchange",
      "Reclamar regalias retroactivas 3 anos",
      "Registrar en ASCAP/BMI",
      "Registrar en SGACEDOM",
      "Configurar Content ID en YouTube",
      "Dividir 178 canciones en 6 colecciones",
      "Asignar ISRCs",
      "Configurar distribucion streaming"
    ]
  },
  {
    "num": 5,
    "name": "Pitch a Multinacionales",
    "sub": "Believe, The Orchard, beatBread",
    "icon": "\U0001f4ec",
    "desc": "Ejecutar secuencia de 4 mensajes hacia multinacionales.",
    "status": "pending",
    "cost": "$0",
    "time": "Semanas 4-8",
    "tasks": [
      "Mensaje 1: Presentacion valor historico",
      "Mensaje 2: Envio auditoria + ONDA",
      "Mensaje 3: Propuesta formal + adelanto",
      "Mensaje 4: Cierre con deadline",
      "Contactar Believe Music",
      "Contactar The Orchard",
      "Evaluar beatBread como puente",
      "Negociar adelanto $500K-$1M"
    ]
  },
  {
    "num": 6,
    "name": "Infraestructura Web3 y Tokenizacion",
    "sub": "LLC, Smart Contracts, Frontend",
    "icon": "\u26a1",
    "desc": "Construir la infraestructura Web3: LLC, smart contracts, tokenizacion.",
    "status": "pending",
    "cost": "$2K - $5K",
    "time": "Meses 3-5",
    "tasks": [
      "Constituir LLC en Wyoming",
      "Abrir cuenta bancaria EE.UU.",
      "Desplegar smart contracts Base/Polygon",
      "Crear token de catalogo",
      "Frontend Next.js + wallet connect",
      "Preventa experiencias VIP",
      "Sistema de afiliados con smartlinks",
      "Boletos NFC + NFTs (Tuboleta Pass)"
    ]
  },
  {
    "num": 7,
    "name": "Evento 50 Aniversario",
    "sub": "23 Sept 2026 - Estadio Olimpico",
    "icon": "\U0001f3df\ufe0f",
    "desc": "Utilizar el concierto como catalizador para maximizar ingresos.",
    "status": "pending",
    "cost": "$5K - $15K",
    "time": "Septiembre 2026",
    "tasks": [
      "Campana marketing organico pre-evento",
      "Venta experiencias premium",
      "Smartlinks afiliados 40 artistas",
      "Acceso virtual diaspora $25",
      "Distribucion masiva post-evento",
      "Capturar pico trafico",
      "Monitoreo ingresos tiempo real",
      "Content ID en picos de reproduccion"
    ]
  },
  {
    "num": 8,
    "name": "Ejecucion y Escalabilidad",
    "sub": "MVP, documentacion, replicacion",
    "icon": "\U0001f680",
    "desc": "Cerrar acuerdo, recibir capital, y documentar modelo como MVP.",
    "status": "pending",
    "cost": "$1K - $3K",
    "time": "Mes 6+",
    "tasks": [
      "Firmar contrato distribuidora",
      "Recibir capital adelanto",
      "Activar recoleccion regalias",
      "Documentar modelo MVP",
      "Identificar proximos catalogos",
      "Refinar procesos auditoria",
      "Escalar a multiples catalogos",
      "Metricas de exito Hyperion"
    ]
  }
]

print("Data loaded:", len(phases), "phases")

# Build HTML parts
parts = []

# Read existing header
with open('master-plan.html', 'r', encoding='utf-8') as f:
    existing = f.read()
    # Keep everything up to the closing div of .mc
    parts.append(existing)

# Phase cards
# First add the phases tab
parts.append('<div class="tc act" id="tab-phases">\n')
parts.append('<div class="sb"><input type="text" id="searchInput" placeholder="Buscar en fases..." oninput="filterPhases()">')
parts.append('<button class="filter-btn act" onclick="filterStatus.call({target:this}, \'all\')">Todas</button>')
parts.append('<button class="filter-btn" onclick="filterStatus.call({target:this}, \'active\')">En Progreso</button>')
parts.append('<button class="filter-btn" onclick="filterStatus.call({target:this}, \'pending\')">Pendientes</button></div>\n')

for p in phases:
    st = p['status']
    sc = 'dn' if st == 'done' else ('an' if st == 'active' else 'pd')
    sl = 'En Progreso' if st == 'active' else ('Completada' if st == 'done' else 'Pendiente')
    
    parts.append('<div class="pc">\n')
    # Header
    parts.append('<div class="ph" onclick="togglePhase(this)">\n')
    parts.append(f'<div class="pn2 {sc}">{p["icon"]}</div>\n')
    parts.append(f'<div class="pi2"><h3>Fase {p["num"]}: {p["name"]}</h3><div class="psb">{p["sub"]}</div></div>\n')
    parts.append(f'<div class="ps3 {sc}">{p["cost"]}</div>\n')
    parts.append('<div class="ar">&#x25BC;</div>\n')
    parts.append('</div>\n')
    # Body
    parts.append('<div class="pb2">\n')
    parts.append(f'<div class="pd2">{p["desc"]}</div>\n')
    parts.append('<div class="mr">\n')
    parts.append(f'<span class="mc2 accent">{p["time"]}</span>\n')
    parts.append(f'<span class="mc2 success">{p["cost"]}</span>\n')
    parts.append(f'<span class="mc2">{len(p["tasks"])} tareas</span>\n')
    parts.append(f'<span class="mc2 {sc}">{sl}</span>\n')
    parts.append('</div>\n')
    parts.append('<div class="cl">\n')
    for idx, t in enumerate(p['tasks']):
        task_id = f"p{p['num']}_{idx}"
        parts.append(f'<div class="cl2" onclick="toggleTask(this, \'{task_id}\')">')
        parts.append(f'<div class="cb" id="cb_{task_id}"></div>')
        parts.append(f'<div class="ct" id="ct_{task_id}">{t}</div>')
        parts.append('</div>\n')
    parts.append('</div>\n')
    parts.append('</div>\n')
    parts.append('</div>\n')

parts.append('</div>\n')

# Timeline tab
parts.append('<div class="tc" id="tab-timeline">\n')
parts.append('<div class="pc"><div class="ph"><div class="pn2 an">\U0001f4c5</div><div class="pi2"><h3>Linea de Tiempo del Plan</h3><div class="psb">8 fases desde la fundacion legal hasta la escalabilidad</div></div></div><div class="pb2 op"><div class="tl">\n')

timeline_items = [
    ("Semanas 1-3", "Fase 1: Fundacion Legal", "\U0001f3db\ufe0f Registrar ONAPI, SRL, ONDA, Contrato Matriz", "phase1"),
    ("Semanas 2-4", "Fase 2: Auditoria Tecnica", "\U0001f4ca Auditar 12 canciones principales, generar reporte", "phase2"),
    ("Semanas 1-2", "Fase 3: Gestion Artista", "\U0001f91d Presentar plan, firmar autorizacion", "phase3"),
    ("Semanas 3-6", "Fase 4: Registro Gestion Colectiva", "\U0001f3e6 SoundExchange, ASCAP/BMI, SGACEDOM", "phase4"),
    ("Semanas 4-8", "Fase 5: Pitch a Multinacionales", "\U0001f4ec Secuencia 4 mensajes + negociacion adelanto", "phase5"),
    ("Meses 3-5", "Fase 6: Infraestructura Web3", "\u26a1 LLC Wyoming, Smart Contracts, Tokenizacion", "phase6"),
    ("Septiembre 2026", "Fase 7: Evento 50 Aniversario", "\U0001f3df\ufe0f Estadio Olimpico, experiencias VIP, afiliados", "phase7"),
    ("Mes 6+", "Fase 8: Ejecucion y Escalabilidad", "\U0001f680 Cierre, capital, replicacion del modelo", "phase8")
]

for t in timeline_items:
    parts.append(f'<div class="tli">\n')
    parts.append(f'<div class="dot {t[3]}"></div>\n')
    parts.append(f'<h4>{t[1]}</h4>\n')
    parts.append(f'<div class="ti">{t[0]}</div>\n')
    parts.append(f'<div class="td2">{t[2]}</div>\n')
    parts.append('</div>\n')

parts.append('</div></div></div></div>\n')

# Metrics tab
parts.append('<div class="tc" id="tab-metrics">\n')
parts.append('<div class="mg">\n')
metrics = [
    ("Canciones", "190", "accent", "Catalogo completo"),
    ("Albumes", "17", "accent", "Discografia oficial"),
    ("Yield/mes", "$66.8K", "success", "Ingreso fugado actual"),
    ("Proy. Anual", "$801K", "gold", "Yield x 12 meses"),
    ("Adelanto 3yr", "$1.68M", "success", "70% flujo proyectado"),
    ("Nodos", "15K+", "danger", "Canales detectados"),
    ("Views/mes", "55.7M", "cyan", "eCPM $1.20"),
    ("Tareas Plan", "64", "accent", "8 fases x 8 tareas")
]
for m in metrics:
    parts.append(f'<div class="mc3"><div class="ml">{m[0]}</div><div class="mv {m[1]}">{m[2]}</div><div class="mnote">{m[3]}</div></div>\n')

parts.append('</div>\n')
parts.append('<div class="hb"><div class="hl">Nota Estrategica</div>El orden de las fases es critico. SoundExchange (Fase 4) puede comenzar en paralelo con Fase 1. El Pitch a Multinacionales (Fase 5) requiere auditoria completa (Fase 2) y registro ONDA (Fase 1).</div>\n')
parts.append('</div>\n')

# Templates tab
parts.append('<div class="tc" id="tab-templates">\n')
parts.append('<div class="pc"><div class="ph" onclick="togglePhase(this)"><div class="pn2 an">\U0001f4ec</div><div class="pi2"><h3>Secuencia de 4 Mensajes para Multinacionales</h3><div class="psb">Believe, The Orchard y otras distribuidoras</div></div><div class="ar">&#x25BC;</div></div><div class="pb2 op">\n')
parts.append('<div class="pd2">Esta secuencia de mensajes progresivos esta disenada para pasar de un sondeo inicial a una propuesta formal de adelanto sin revelar toda la estrategia tecnica prematuramente.</div>\n')

msg_titles = ["Mensaje 1: Sondeo Inicial", "Mensaje 2: Confirmacion + Datos", "Mensaje 3: Propuesta Formal", "Mensaje 4: Cierre con Deadline"]
messages = [
    'Hola [Nombre], te contactamos desde Nuclear AIMA, representando el catalogo de Ramon Orlando, leyenda del merengue dominicano con 50+ anos de carrera. Estamos preparando el lanzamiento digital de su catalogo completo de 190 canciones para su 50 Aniversario (23 Sept 2026, Estadio Olimpico). El catalogo ya genera +15M views/mes organicamente en YouTube. Nos gustaria explorar una posible colaboracion para la distribucion global. Estarian abiertos a una conversacion preliminar?',
    
    'Gracias por su respuesta. Adjuntamos un resumen ejecutivo de nuestra auditoria tecnica, que documenta el rendimiento actual del catalogo en YouTube (nodos, vistas, ingresos fugados). Tambien confirmamos que el catalogo esta siendo registrado en ONDA (Oficina Nacional de Derecho de Autor) y contamos con carta de autorizacion notariada del artista. El potencial de recuperacion de ingresos es significativo. Nos gustaria compartir el detalle completo en una reunion virtual.',
    
    'Estimado/a [Nombre], tras nuestra conversacion, formalizamos nuestra propuesta: ofrecemos el catalogo completo de Ramon Orlando (190 canciones, 17 albumes, categoria merengue/tropical) para distribucion global con Content ID activo, a cambio de un adelanto (signing bonus) en el rango de $500,000 - $1,000,000 USD. El catalogo tiene un yield mensual estimado de $66,824 y proyecta +$800K anuales en ingresos recuperables. Adjuntamos expediente completo con auditoria, registros ONDA y proyecciones financieras.',
    
    'Hola [Nombre], queremos informarles que estamos evaluando multiples ofertas y hemos establecido el [Fecha] como fecha limite para recibir propuestas formales. El concierto del 23 de septiembre generara un pico masivo de trafico y reproducciones, y necesitamos tener la distribucion activada antes de esa fecha para maximizar la captura de ingresos. Agradeceriamos su respuesta a la brevedad para continuar las conversaciones.'
]

for i in range(4):
    parts.append(f'<div style="font-size:11px;font-weight:600;color:var(--accent);margin:8px 0 4px">{msg_titles[i]}</div>\n')
    parts.append(f'<div class="tb">{messages[i]}<button class="cpy" onclick="copyMsg(this)">Copiar</button></div>\n')

parts.append('</div></div>\n')

# Executive Summary template
parts.append('<div class="pc"><div class="ph" onclick="togglePhase(this)"><div class="pn2 an">\U0001f4cb</div><div class="pi2"><h3>Resumen Ejecutivo de Auditoria</h3><div class="psb">Argumento central para negociacion</div></div><div class="ar">&#x25BC;</div></div><div class="pb2 op">\n')
parts.append('<div class="pd2">El resumen ejecutivo es el documento que abre las puertas. Debe ser una pagina, maximo dos, con los datos clave del catalogo.</div>\n')
parts.append('<div class="hb"><div class="hl">El Argumento de Apertura</div><strong>"Este catalogo de 190 canciones esta generando $66,824/mes en ingresos no reclamados. Con 12 canciones auditadas que muestran $34,700/mes en fuga solo de nodos identificados. El potencial de recuperacion anual es de $800,000+. Ofrecemos el 100% del catalogo para distribucion con Content ID activo a cambio de un adelanto de $500K-$1M."</strong></div>\n')

# Executive summary metrics
exec_metrics = [
    ("Canciones", "190", "accent", "Catalogo completo"),
    ("Yield/Mes", "$66.8K", "success", "Ingreso fugado"),
    ("Proy. Anual", "$801K", "gold", "Yield x 12"),
    ("Adelanto", "$500K-$1M", "success", "Rango objetivo"),
    ("Nodos", "15K+", "danger", "Canales sin monetizar"),
    ("Views/Mes", "55.7M", "cyan", "Estimadas eCPM $1.20")
]
parts.append('<div class="mg" style="margin-top:10px">\n')
for m in exec_metrics:
    v_class = m[1].replace("$", "").replace("K", "").replace("M", "").replace("+", "").replace("-", "")
    color = m[2]
    parts.append(f'<div class="mc3"><div class="ml">{m[0]}</div><div class="mv {color}">{m[1]}</div><div class="mnote">{m[3]}</div></div>\n')
parts.append('</div>\n')

parts.append('</div></div>\n')
parts.append('</div>\n')

# Resources tab
parts.append('<div class="tc" id="tab-resources">\n')
parts.append('<div class="pc"><div class="ph"><div class="pn2 an">\U0001f4c1</div><div class="pi2"><h3>Recursos Relacionados</h3><div class="psb">Herramientas del ecosistema Nuclear AIMA</div></div></div><div class="pb2 op">\n')
parts.append('<div class="rg">\n')

resources = [
    ("oraculo.html", "\U0001f52e", "Oraculo en Vivo - Yield y datos tiempo real"),
    ("adelantos.html", "\U0001f4b0", "Adelantos - Plataformas de financiamiento"),
    ("onapi-onda.html", "\U0001f3db\ufe0f", "ONAPI/ONDA - Guia legal paso a paso"),
    ("short-tracker.html", "\U0001f3ac", "Short Tracker - Replicas virales YouTube"),
    ("osint-center.html", "\U0001f575\ufe0f", "OSINT Center - Dorks, Keywords, Dominios"),
    ("index.html", "\U0001f4ca", "Dashboard Principal - Centro de Comando"),
    ("data/catalogo-completo-ramon-orlando.csv", "\U0001f4c4", "Catalogo Completo CSV"),
    ("ramon-orlando/CONTRATO%20DE%20ASESORAMIENTO%20ESTRAT%C3%89GI.txt", "\U0001f4dc", "Contrato de Asesoramiento")
]

for r in resources:
    parts.append(f'<a href="{r[0]}"><span class="r-icon">{r[1]}</span>{r[2]}</a>\n')

parts.append('</div>\n')
parts.append('</div></div>\n')
parts.append('</div>\n')

# Footer
parts.append('<div style="text-align:center;padding:16px 0;border-top:0.5px solid var(--border);margin-top:8px">')
parts.append('<p style="font-size:9px;color:var(--muted);font-family:var(--mono)">Master Plan · Nuclear AIMA · Basado en start.txt (981 lineas) · Progreso guardado en localStorage</p>')
parts.append('</div>\n')

# JavaScript
parts.append('''<script>
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
    cb.textContent = '\\u2713';
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
  document.getElementById('currentPhase').textContent = 'Fase 1-2';
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
    btn.textContent = '\\u2713 Copiado';
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
  const checks = getChecks();
  Object.keys(checks).forEach(id => {
    const cb = document.getElementById('cb_' + id);
    const ct = document.getElementById('ct_' + id);
    if (cb) { cb.classList.add('ch'); cb.textContent = '\\u2713'; }
    if (ct) ct.classList.add('do');
  });
  updateProgress();
});
</script>
</div>
</body>
</html>''')

# Write the complete file
with open('master-plan.html', 'w', encoding='utf-8') as f:
    f.write(''.join(parts))

print(f"Master plan HTML generated: {os.path.getsize('master-plan.html')} bytes")
print("Done!")
