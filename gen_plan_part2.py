# Append phase content, timeline, templates, JS to master-plan.html
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

phase1_checklist = {
    "tasks": [
        "Registrar Nombre Comercial en ONAPI (Clase 41 y 35)",
        "Redactar estatutos SAS y pagar impuesto DGII",
        "Registro Mercantil en Cámara de Comercio",
        "Obtener RNC (Registro Nacional Contribuyente)",
        "Registrar fonograma en ONDA a nombre de la empresa",
        "Firmar Contrato de Administración con el artista",
        "Abrir cuenta bancaria corporativa",
        "Preparar lista oficial de 178 canciones"
    ],
    "desc": "Establecer la infraestructura legal y corporativa necesaria para operar como sello independiente y negociar con distribuidoras internacionales.",
    "status": "active",
    "cost": "$800 - $1,200 USD",
    "timeline": "Semanas 1-3",
    "icon": "\U0001f3db\ufe0f"
}

phase2_checklist = {
    "tasks": [
        "Auditar las 12 canciones principales con herramienta de detecci\u00f3n",
        "Generar reporte ejecutivo de auditor\u00eda (nodos, vistas, yield, fuga)",
        "Expandir auditor\u00eda a las 178 canciones del cat\u00e1logo",
        "Calcular yield mensual total e ingreso fugado",
        "Identificar canales sin Content ID activo",
        "Preparar matriz de nodos por canci\u00f3n",
        "Exportar reporte en formato PDF ejecutivo",
        "Redactar carta de autorizaci\u00f3n notariada"
    ],
    "desc": "Ejecutar el an\u00e1lisis t\u00e9cnico del cat\u00e1logo para documentar el valor real del activo musical y generar el documento de negociaci\u00f3n.",
    "status": "active",
    "cost": "$0 (herramientas propias)",
    "timeline": "Semanas 2-4",
    "icon": "\U0001f4ca"
}

phase3_checklist = {
    "tasks": [
        "Agendar reuni\u00f3n con Ram\u00f3n Orlando para presentar el plan",
        "Explicar la importancia del registro ONDA como t\u00edtulo de propiedad",
        "No revelar detalles t\u00e9cnicos (LLC, tokenizaci\u00f3n) prematuramente",
        "Gestionar expectativas sobre tiempos y montos",
        "Presentar el concierto del 23 Sept como catalizador de urgencia",
        "Firmar carta de autorizaci\u00f3n para negociaciones",
        "Obtener c\u00e9dula y documentos personales del artista",
        "Coordinar visita a ONDA con el artista"
    ],
    "desc": "Gestionar la relaci\u00f3n con el artista de manera profesional, presentando la informaci\u00f3n de forma gradual y asegurando su colaboraci\u00f3n.",
    "status": "pending",
    "cost": "$0",
    "timeline": "Semanas 1-2",
    "icon": "\U0001f91d"
}

phase4_checklist = {
    "tasks": [
        "Registrar cat\u00e1logo en SoundExchange",
        "Reclamar regal\u00edas retroactivas (3 a\u00f1os)",
        "Registrar en ASCAP/BMI (si aplica)",
        "Registrar en SGACEDOM",
        "Configurar Content ID en YouTube",
        "Dividir las 178 canciones en 6 colecciones estrat\u00e9gicas",
        "Asignar ISRCs a trav\u00e9s de distribuidor temporal",
        "Configurar distrbuci\u00f3n en plataformas streaming"
    ],
    "desc": "Registrar el cat\u00e1logo en todas las sociedades de gesti\u00f3n colectiva y plataformas de monetizaci\u00f3n para empezar a capturar ingresos.",
    "status": "pending",
    "cost": "$0 - $50 (registros)",
    "timeline": "Semanas 3-6",
    "icon": "\U0001f3e6"
}

phase5_checklist = {
    "tasks": [
        "Mensaje 1: Presentaci\u00f3n del valor hist\u00f3rico y volumen de reproducciones",
        "Mensaje 2: Env\u00edo de resumen de auditor\u00eda con prueba ONDA",
        "Mensaje 3: Propuesta formal con expediente completo y solicitud de adelanto",
        "Mensaje 4: Cierre con fecha l\u00edmite previa al evento",
        "Contactar a Believe Music",
        "Contactar a The Orchard",
        "Evaluar ofertas de beatBread como puente",
        "Negociar t\u00e9rminos del adelanto (500K-1M USD)"
    ],
    "desc": "Ejecutar la secuencia de comunicaci\u00f3n de 4 mensajes hacia las multinacionales usando el reporte de auditor\u00eda como prueba de valor.",
    "status": "pending",
    "cost": "$0",
    "timeline": "Semanas 4-8",
    "icon": "\U0001f4ec"
}

phase6_checklist = {
    "tasks": [
        "Constituir LLC en Wyoming",
        "Abrir cuenta bancaria empresarial en EE.UU.",
        "Desplegar smart contracts en Base/Polygon",
        "Crear token de cat\u00e1logo para distribuci\u00f3n de regal\u00edas",
        "Implementar frontend Next.js con wallet connect",
        "Configurar preventa de experiencias VIP para el evento",
        "Dise\u00f1ar sistema de afiliados con smartlinks",
        "Integrar boletos NFC con NFTs (Tuboleta Pass)"
    ],
    "desc": "Construir la infraestructura Web3: LLC, smart contracts, tokenizaci\u00f3n del cat\u00e1logo y sistema de boletos inteligentes para el evento.",
    "status": "pending",
    "cost": "$2,000 - $5,000",
    "timeline": "Meses 3-5",
    "icon": "\u26a1"
}

phase7_checklist = {
    "tasks": [
        "Activar campa\u00f1a de marketing org\u00e1nico pre-evento",
        "Lanzar venta de experiencias premium paquetizadas",
        "Configurar smartlinks de afiliados para los 40 artistas invitados",
        "Ofrecer acceso virtual para la di\u00e1spora ($25 USD)",
        "Activar distribuci\u00f3n masiva post-evento",
        "Capturar pico de tr\u00e1fico post-concierto",
        "Monitorear ingresos y m\u00e9tricas en tiempo real",
        "Activar Content ID en los picos de reproducci\u00f3n"
    ],
    "desc": "Utilizar el concierto del 50 Aniversario como catalizador para maximizar ingresos, tr\u00e1fico y urgencia en las negociaciones.",
    "status": "pending",
    "cost": "$5,000 - $15,000",
    "timeline": "Septiembre 2026",
    "icon": "\U0001f3df\ufe0f"
}

phase8_checklist = {
    "tasks": [
        "Firmar contrato con distribuidora seleccionada",
        "Recibir capital del adelanto",
        "Activar recolecci\u00f3n autom\u00e1tica de regal\u00edas",
        "Documentar el modelo como MVP replicable",
        "Identificar pr\u00f3ximos artistas/cat\u00e1logos para replicar",
        "Refinar procesos de auditor\u00eda y onboarding",
        "Escalar a m\u00faltiples cat\u00e1logos hist\u00f3ricos",
        "Establecer m\u00e9tricas de \u00e9xito del modelo Hyperion"
    ],
    "desc": "Cerrar el acuerdo, recibir el capital, y documentar el modelo como MVP para replicarlo con otros cat\u00e1logos hist\u00f3ricos.",
    "status": "pending",
    "cost": "$1,000 - $3,000",
    "timeline": "Mes 6+",
    "icon": "\u26a1"
}

phases = [phase1_checklist, phase2_checklist, phase3_checklist, phase4_checklist, phase5_checklist, phase6_checklist, phase7_checklist, phase8_checklist]

phase_names = [
    "Fundaci\u00f3n Legal y Corporativa",
    "Auditor\u00eda T\u00e9cnica del Cat\u00e1logo",
    "Gesti\u00f3n con el Artista",
    "Registro en Sociedades de Gesti\u00f3n",
    "Pitch a Multinacionales",
    "Infraestructura Web3 y Tokenizaci\u00f3n",
    "Evento 50 Aniversario",
    "Ejecuci\u00f3n y Escalabilidad"
]

phase_subtitles = [
    "ONAPI, SRL, ONDA, Contrato Matriz",
    "12 canciones principales + expansi\u00f3n a 178",
    "Expectativas, autorizaci\u00f3n y coordinaci\u00f3n",
    "SoundExchange, ASCAP/BMI, SGACEDOM, Content ID",
    "Believe, The Orchard, beatBread",
    "LLC Wyoming, Smart Contracts, Frontend",
    "23 Sept 2026 - Estadio Ol\u00edmpico",
    "MVP, documentaci\u00f3n, replicaci\u00f3n"
]

phase_descs = [p["desc"] for p in phases]
phase_statuses = [p["status"] for p in phases]
phase_costs = [p["cost"] for p in phases]
phase_times = [p["timeline"] for p in phases]
phase_icons = [p["icon"] for p in phases]
print("Data prepared")
print(f"Phases: {len(phases)}")
print(f"Total tasks: {sum(len(p['tasks']) for p in phases)}")
