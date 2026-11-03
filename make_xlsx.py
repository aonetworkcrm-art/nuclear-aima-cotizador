# -*- coding: utf-8 -*-
"""
Genera: C:/Users/somet/Desktop/nuclear-aima-route/hoja-captura-ruta.xlsx
SMAC — Sistema Modular de Auditoría Comercial
- Cabecera operativa con guardado automático
- 8 pestañas (Bloques 1-7 + Resumen/Score)
- Checkbox = celda binaria (1/0) para análisis
- Semáforo: puntuación automática con fórmulas APARTIR DE las celdas
"""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

OUT = "C:/Users/somet/Desktop/nuclear-aima-route/hoja-captura-ruta.xlsx"

C_PRIMARY   = "1A1A2E"
C_SECONDARY = "16213E"
C_ACCENT    = "E94560"
C_BG        = "F5F5F7"
C_CARD      = "FFFFFF"
C_TEXT      = "333333"
C_LIGHT     = "F8F9FA"
C_GREY      = "A0AEC0"

def fill(hex_): return PatternFill("solid", fgColor=hex_)
def font(color=C_TEXT, bold=False, size=11, italic=False):
    return Font(color=color, bold=bold, size=size, italic=italic, name="Calibri")

thin = Side(style="thin", color="DDDDDD")
border_all = Border(left=thin, right=thin, top=thin, bottom=thin)

def style_cell(ws, r, c, value=None, bg=C_CARD, tc=C_TEXT, bold=False, sz=11,
               align="left", valign="center", wrap=False, border=True, italic=False):
    cell = ws.cell(row=r, column=c)
    if value is not None:
        cell.value = value
    cell.fill = fill(bg)
    cell.font = font(tc, bold, sz, italic)
    cell.alignment = Alignment(horizontal=align, vertical=valign, wrap_text=wrap)
    cell.border = border_all if border else Border()
    return cell

def title_block(ws, title, subtitle, ncols):
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=ncols)
    style_cell(ws, 1, 1, title, bg=C_PRIMARY, tc="FFFFFF", bold=True, sz=16,
               align="center", valign="center")
    ws.row_dimensions[1].height = 30
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=ncols)
    style_cell(ws, 2, 1, subtitle, bg=C_SECONDARY, tc="FFFFFF", sz=10,
               align="center", valign="center", italic=True)
    ws.row_dimensions[2].height = 20

def block_title(ws, row, text, ncols):
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=ncols)
    style_cell(ws, row, 1, text, bg=C_PRIMARY, tc="FFFFFF", bold=True, sz=12,
               align="left", valign="center")
    ws.row_dimensions[row].height = 26

def section_label(ws, row, text, ncols, bg=C_LIGHT):
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=ncols)
    style_cell(ws, row, 1, text, bg=bg, tc=C_TEXT, bold=True, sz=10,
               align="left", valign="center")
    ws.row_dimensions[row].height = 20

def header_row(ws, row, headers, bg=C_PRIMARY, tc="FFFFFF"):
    for i, h in enumerate(headers, start=1):
        style_cell(ws, row, i, h, bg=bg, tc=tc, bold=True, sz=10, align="center", wrap=True)
    ws.row_dimensions[row].height = 28

def set_widths(ws, widths):
    for i, w in enumerate(widths, start=1):
        ws.column_dimensions[get_column_letter(i)].width = w

# ================= HOJA 1: Metadatos =================
def build_meta(wb):
    ws = wb.create_sheet("1_MetaDatos")
    set_widths(ws, [4, 34, 32, 32, 22, 32])
    title_block(ws, "📍 Bloque 1 — Metadatos y Tiempo de Operación",
                "Atomicidad operativa · cada carta o dispositivo · zona: Villa Faro", 6)
    r = 4
    fields = [
        ("Fecha y Hora de Auditoría (DD/MM/AAAA — HH:MM)", "b1_fecha", "text"),
        ("Sector / Cuadrante / Calle",                       "b1_sector", "text"),
        ("Nombre del Prospectador / ID Agente",              "b1_agent", "text"),
        ("Nombre Comercial del Local",                       "b1_local", "text"),
        ("Dirección Exacta",                                 "b1_direc", "text"),
        ("Negocios Vecinos de Referencia (Contexto Físico)", "b1_vecinos", "text"),
        ("¿Es un negocio nuevo o veterano?",                 "b1_veterano", "dropdown"),
        ("Tiempo exacto en el mercado (aprox.)",             "b1_tiempo", "text"),
    ]
    row_map = {}
    for label, key, typ in fields:
        style_cell(ws, r, 2, label, bg=C_LIGHT, tc=C_TEXT, bold=True, sz=10, align="left")
        ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=4)
        style_cell(ws, r, 3, None, bg=C_CARD)
        style_cell(ws, r, 5, None, bg=C_LIGHT, tc=C_GREY, sz=9, align="left")
        ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=4)
        row_map[key] = (r, 3)
        r += 1
    dv = DataValidation(type="list", formula1='"Nuevo (&lt;6 meses),En crecimiento (6m–2 años),Consolidado (+2 años)"', allow_blank=True)
    ws.add_data_validation(dv)
    dv.add(f"D{row_map['b1_veterano'][0]}")
    r += 1
    section_label(ws, r, "Notas de la ruta / observaciones de campo", 6); r += 1
    ws.merge_cells(start_row=r, start_column=1, end_row=r+3, end_column=6)
    style_cell(ws, r, 1, None, bg=C_CARD, align="left")
    for k in range(r, r+4):
        for cc in range(1, 7):
            ws.cell(row=k, column=cc).border = border_all
    return row_map

# ================= HOJA 2: IdentidadVisual =================
def build_identidad(wb):
    ws = wb.create_sheet("2_IdentidadVisual")
    set_widths(ws, [4, 38, 26, 30, 30, 22])
    title_block(ws, "🏗️ Bloque 2 — Identidad Visual, Física y Branding Local",
                "Letrero · logo · presencia física · observación", 6)
    r = 4
    rows = [
        ("Letrero físico en la fachada", ["Sí", "No"], "b2_letrero"),
        ("Estado del letrero",
         ["Excelente", "Desactualizada / Apagada", "Necesita modificación urgente"], "b2_letrero_est"),
        ("Logotipo corporativo definido",
         ["Sí (Profesional)", "Sí (Muy amateur)", "No tienen logo"], "b2_logo"),
        ("Presencia Física", ["Local abierto al público", "Oficina cerrada", "Híbrido / casa"], "b2_pres"),
        ("Observación crítica del local", None, "b2_obs"),
    ]
    row_map = {}
    for label, op, key in rows:
        style_cell(ws, r, 2, label, bg=C_LIGHT, tc=C_TEXT, bold=True, sz=10)
        ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=4)
        style_cell(ws, r, 3, None, bg=C_CARD)
        style_cell(ws, r, 5, None, bg=C_LIGHT, tc=C_GREY, sz=9, align="left")
        ws.merge_cells(start_row=r, start_column=3, end_row=r, end_column=4)
        row_map[key] = (r, 3)
        r += 1
    dv1 = DataValidation(type="list", formula1='"Sí,No"', allow_blank=True)
    dv2 = DataValidation(type="list", formula1='"Excelente,Desactualizada / Apagada,Necesita modificación urgente"', allow_blank=True)
    dv3 = DataValidation(type="list", formula1='"Sí (Profesional),Sí (Muy amateur),No tienen logo"', allow_blank=True)
    dv4 = DataValidation(type="list", formula1='"Local abierto al público,Oficina cerrada,Híbrido / casa"', allow_blank=True)
    ws.add_data_validation(dv1); ws.add_data_validation(dv2)
    ws.add_data_validation(dv3); ws.add_data_validation(dv4)
    dv1.add(f"C{row_map['b2_letrero'][0]}")
    dv2.add(f"C{row_map['b2_letrero_est'][0]}")
    dv3.add(f"C{row_map['b2_logo'][0]}")
    dv4.add(f"C{row_map['b2_pres'][0]}")
    r += 1
    section_label(ws, r, "Checklist físico — marcar todo lo que aplique", 6); r += 1
    for txt in ["Fondo oscuro/ocre en la entrada", "Sin iluminación, sin luz de día",
                "Puerta sin marca, sin senalética de calle", "Muebles sucios o desordenados",
                "Persiana rotonda o impedimento de visibilidad", "Zona de espera trivial"]:
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=4)
        style_cell(ws, r, 2, txt, bg=C_CARD, sz=10)
        style_cell(ws, r, 5, None, bg=C_LIGHT, tc=C_GREY, sz=9, align="left")
        style_cell(ws, r, 6, None, bg=C_CARD)
        r += 1
    r += 1
    section_label(ws, r, "Observación de branding / merchandising en el día de la ruta", 6); r += 1
    ws.merge_cells(start_row=r, start_column=1, end_row=r+2, end_column=6)
    style_cell(ws, r, 1, None, bg=C_CARD, align="left")
    for k in range(r, r+3):
        for cc in range(1, 7):
            ws.cell(row=k, column=cc).border = border_all
    return row_map

# ================= HOJA 3: WebEmbudos =================
def build_web(wb):
    ws = wb.create_sheet("3_WebEmbudos")
    set_widths(ws, [4, 44, 20, 30, 30, 28, 22])
    title_block(ws, "🌐 Bloque 3 — Ecosistema Web, Embudos y Pasarela",
                "Google Maps · web · checkout · facturación · biolink", 7)
    r = 4
    rows = [
        ("¿Aparece en Google Maps?",       ["Sí", "No"], "b3_gmaps"),
        ("Ficha Google reclamada/verificada", ["Sí", "No"], "b3_gm_ficha"),
        ("Ventas mensuales estimadas de GM", None, "b3_ventas_gm"),
        ("Sitio web propio", ["Sí", "No"], "b3_web"),
        ("Página de venta optimizada", ["Sí", "No"], "b3_pventa"),
        ("Página de gracias configurada",  ["Sí", "No"], "b3_gracias"),
        ("Pasarela de pagos integrada", ["Sí (Tarjeta/PayPal/Trans.)", "No"], "b3_pago"),
        ("Sistema de facturación digital", ["Sí", "No"], "b3_fact"),
        ("Base de datos digital de productos", ["Sí", "No"], "b3_bdd"),
        ("Biolink / Linktree", ["Sí", "No"], "b3_bio"),
    ]
    row_map = {}
    for label, op, key in rows:
        style_cell(ws, r, 2, label, bg=C_LIGHT, tc=C_TEXT, bold=True, sz=10)
        if op is None:
            style_cell(ws, r, 3, None, bg=C_CARD)
            style_cell(ws, r, 4, None, bg=C_LIGHT, tc=C_GREY, sz=9, align="left")
        else:
            dv = DataValidation(type="list", formula1='"' + ",".join(op) + '"', allow_blank=True)
            ws.add_data_validation(dv); dv.add(f"C{r}")
            style_cell(ws, r, 4, None, bg=C_LIGHT, tc=C_GREY, sz=9, align="left")
        row_map[key] = (r, 3)
        r += 1
    r += 1
    section_label(ws, r, "Link URL: web / bio / pasarela / facturación", 7); r += 1
    ws.merge_cells(start_row=r, start_column=1, end_row=r+1, end_column=7)
    style_cell(ws, r, 1, None, bg=C_CARD, align="left")
    for k in range(r, r+2):
        for cc in range(1, 8):
            ws.cell(row=k, column=cc).border = border_all
    return row_map

# ================= HOJA 4: RedesAds =================
def build_redes(wb):
    ws = wb.create_sheet("4_RedesAds")
    set_widths(ws, [4, 30, 18, 18, 18, 18, 18])
    title_block(ws, "📱 Bloque 4 — Redes Sociales, Tráfico, Contenido y Ads",
                "Actividad, viralidad, metas, pixel, presupuesto", 7)
    r = 4
    section_label(ws, r, "Redes Sociales — estado de cada red", 7); r += 1
    header_row(ws, r, ["Red", "Estado", "Última publicación", "Optimización perfil", "Viral detectado", "Ventas RS/mes", "Nota"]); r += 1
    for red, estados in [("Instagram",["Activa","Abandonada","No la tienen"]),
                          ("TikTok",["Activa","Abandonada","No la tienen"]),
                          ("Facebook",["Activa","Abandonada","No la tienen"]),
                          ("YouTube",["Activa","Abandonada","No la tienen"])]:
        style_cell(ws, r, 1, red, bg=C_LIGHT, tc=C_TEXT, bold=True, sz=10)
        dv = DataValidation(type="list", formula1='"' + ",".join(estados) + '"', allow_blank=True)
        ws.add_data_validation(dv); dv.add(f"B{r}")
        for cc in range(2, 8):
            style_cell(ws, r, cc, None, bg=C_CARD)
        r += 1
    r += 1
    section_label(ws, r, "Publicidad pagada — Meta/TikTok/Google", 7); r += 1
    header_row(ws, r, ["Campo", "Respuesta", "", "", "", "", "Nota"]); r += 1
    for n in ["¿Están haciendo pausa activa actualmente?",
              "¿Dónde la hacen?",
              "Cantidad de campañas activas en Meta",
              "Presupuesto estimado de publicidad al mes ($)"]:
        style_cell(ws, r, 2, n, bg=C_LIGHT, tc=C_TEXT, bold=True, sz=10)
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
        for cc in range(3, 8):
            style_cell(ws, r, cc, None, bg=C_CARD)
        r += 1
    r += 1
    section_label(ws, r, "Interacción y conversión real en redes", 7); r += 1
    header_row(ws, r, ["Campo", "Respuesta", "", "", "", "", "Nota"]); r += 1
    for n in ["Interacción (comentarios, me gusta, compartidos)",
              "Crecimiento orgánico reciente",
              "Conversión de seguidores (compran / solo like / ninguno)",
              "Experiencia de usuario (UX)"]:
        style_cell(ws, r, 2, n, bg=C_LIGHT, tc=C_TEXT, bold=True, sz=10)
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
        for cc in range(3, 8):
            style_cell(ws, r, cc, None, bg=C_CARD)
        r += 1
    return row_map

# ================= HOJA 5: WhatsAppAuto =================
def build_whatsapp(wb):
    ws = wb.create_sheet("5_WhatsAppAuto")
    set_widths(ws, [4, 42, 22, 30, 30, 30, 24])
    title_block(ws, "💬 Bloque 5 — Canales de Comunicación, Automatización y WhatsApp",
                "Número, visibilidad, chat, grupos, email, SMS", 7)
    r = 4
    row_map = {}
    items = [
        ("¿Tienen número de WhatsApp corporativo?", ["Sí", "No"], "b5_wa"),
        ("WhatsApp visible en la Ficha de Google", ["Sí", "No"], "b5_wa_gm"),
        ("WhatsApp visible en sus Redes Sociales", ["Sí", "No"], "b5_wa_rs"),
        ("Utilizan enlaces directos tipo Wa.link?", ["Sí", "No"], "b5_walink"),
        ("Chatbot automatizado configurado", ["Sí", "No"], "b5_chatbot"),
        ("Comportamiento del chatbot actual", None, "b5_chab"),
        ("Grupos de WhatsApp/Telegram para comunidad", ["Sí", "No"], "b5_grupo"),
        ("¿Hacen Email Marketing?", ["Sí", "No"], "b5_email"),
        ("¿Hacen marketing por SMS?", ["Sí", "No"], "b5_sms"),
        ("Micro-lanzamientos semanales a comunidad WhatsApp", ["Sí", "No"], "b5_micro"),
    ]
    for label, op, key in items:
        style_cell(ws, r, 2, label, bg=C_LIGHT, tc=C_TEXT, bold=True, sz=10)
        if op is None:
            style_cell(ws, r, 3, None, bg=C_CARD)
            style_cell(ws, r, 4, None, bg=C_LIGHT, tc=C_GREY, sz=9, align="left")
        else:
            dv = DataValidation(type="list", formula1='"' + ",".join(op) + '"', allow_blank=True)
            ws.add_data_validation(dv); dv.add(f"C{r}")
            style_cell(ws, r, 4, None, bg=C_LIGHT, tc=C_GREY, sz=9, align="left")
        row_map[key] = (r, 3)
        r += 1
    r += 1
    section_label(ws, r, "Observación del canal de comunicación", 7); r += 1
    ws.merge_cells(start_row=r, start_column=2, end_row=r+2, end_column=6)
    style_cell(ws, r, 2, "Respuesta del dueño / defectos de atención / nodo de fricción",
               bg=C_CARD, align="left")
    for k in range(r, r+3):
        for cc in range(2, 7):
            ws.cell(row=k, column=cc).border = border_all
    return row_map

# ================= HOJA 6: OfertaFinanzas =================
def build_oferta(wb):
    ws = wb.create_sheet("6_OfertaFinanzas")
    set_widths(ws, [4, 40, 20, 30, 30, 28, 20])
    title_block(ws, "🎯 Bloque 6 — Oferta, Monetización Interna y Necesidades Comerciales",
                "Ticket, flujo de caja, dolor, monetización, lead magnet", 7)
    r = 4
    section_label(ws, r, "Oferta y ticket", 7); r += 1
    header_row(ws, r, ["Dato", "Respuesta", "", "", "", "", "Nota"]); r += 1
    for n in ["Rango de precio de productos/servicios",
              "¿Tienen flujo de caja saludable o estrangulamiento?",
              "Buyer Persona / Cliente Ideal",
              "Dolor o problema principal que resuelven",
              "Monetización interna (YouTube/FB propios)",
              "Infoproductos (cursos, talleres, webinars grabados)",
              "Lead Magnet (recurso gratuito)",
              "Eventos y promociones (rifas, sorteos, patrocinios)",
              "¿Necesitan patrocinadores externos?",
              "¿Necesitan nuevos proveedores o importadores?"]:
        style_cell(ws, r, 2, n, bg=C_LIGHT, tc=C_TEXT, bold=True, sz=10)
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
        for cc in range(3, 8):
            style_cell(ws, r, cc, None, bg=C_CARD)
        r += 1
    r += 1
    section_label(ws, r, "Salud financiera y flujo de caja", 7); r += 1
    header_row(ws, r, ["Dato", "Respuesta", "", "", "", "", "Nota"]); r += 1
    for n in ["Clientes aproximados atendidos al mes",
              "Volumen de ganancias estimadas al mes ($)",
              "¿El negocio cubre su nómina? (Sí / Límite / Crisis)"]:
        style_cell(ws, r, 2, n, bg=C_LIGHT, tc=C_TEXT, bold=True, sz=10)
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
        for cc in range(3, 8):
            style_cell(ws, r, cc, None, bg=C_CARD)
        r += 1
    r += 1
    section_label(ws, r, "Estrategia y objetivos de crecimiento", 7); r += 1
    header_row(ws, r, ["Campo", "¿Sí?", "¿No?", "", "", "", "Nota"]); r += 1
    for n in ["Posicionamiento SEO / Google Index",
              "Equipo interno para lo digital",
              "Bases de datos para sincronizar contactos",
              "Automatizaciones especiales",
              "Idea de nuevos productos / líneas",
              "Crecer en Facebook", "Crecer en YouTube",
              "Crecer en TikTok", "Crecer en Instagram"]:
        style_cell(ws, r, 2, n, bg=C_LIGHT, tc=C_TEXT, bold=True, sz=10)
        dv = DataValidation(type="list", formula1='"Sí,No"', allow_blank=True)
        ws.add_data_validation(dv); dv.add(f"B{r}")
        for cc in range(3, 8):
            style_cell(ws, r, cc, None, bg=C_CARD)
        r += 1
    return row_map

# ================= HOJA 7: MerchInfra =================
def build_merch(wb):
    ws = wb.create_sheet("7_MerchInfra")
    set_widths(ws, [4, 38, 24, 30, 30, 28, 20])
    title_block(ws, "🏬💡 Bloque 2.1 — Infraestructura Física · 6.2 — Capital Físico y Publicidad Tradicional",
                "Espacio · AC · almacen · POP · gorras · banners · guaguas", 7)
    r = 4
    section_label(ws, r, "Infraestructura física y espacio", 7); r += 1
    header_row(ws, r, ["Dato", "Respuesta", "", "", "", "", "Nota"]); r += 1
    for n in ["El local es amplio o reducido",
              "Aire acondicionado funcional",
              "Área de recepción o sala de espera",
              "Almacén o depósito de mercancía separado"]:
        style_cell(ws, r, 2, n, bg=C_LIGHT, tc=C_TEXT, bold=True, sz=10)
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
        for cc in range(3, 8):
            style_cell(ws, r, cc, None, bg=C_CARD)
        r += 1
    r += 1
    section_label(ws, r, "Merchandising, branding y material físico", 7); r += 1
    header_row(ws, r, ["Dato", "Respuesta", "", "", "", "", "Nota"]); r += 1
    for n in ["Branding físico unificado",
              "Folletos, volantes o plegables actualizados",
              "Tarjetas de presentación físicas",
              "Banners, bajantes o roll-ups visibles",
              "Gorras, poloches o uniformes",
              "Mercancías / souvenirs con marca",
              "Logo / branding físico en la fachada"]:
        style_cell(ws, r, 2, n, bg=C_LIGHT, tc=C_TEXT, bold=True, sz=10)
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
        for cc in range(3, 8):
            style_cell(ws, r, cc, None, bg=C_CARD)
        r += 1
    r += 1
    section_label(ws, r, "Publicidad tradicional complementaria", 7); r += 1
    header_row(ws, r, ["Dato", "Respuesta", "", "", "", "", "Nota"]); r += 1
    for n in ["Guaguas anunciadoras o altoparlantes locales",
              "Otros medios tradicionales (radio, flyers,etc.)"]:
        style_cell(ws, r, 2, n, bg=C_LIGHT, tc=C_TEXT, bold=True, sz=10)
        ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=3)
        for cc in range(3, 8):
            style_cell(ws, r, cc, None, bg=C_CARD)
        r += 1
    return row_map

# ================= HOJA 8: ResumenScore =================
def build_resumen(wb):
    ws = wb.create_sheet("ResumenScore")
    set_widths(ws, [4, 46, 20, 24, 30, 24, 24])
    title_block(ws, "📊 Resumen y Semáforo de Urgencia Comercial",
                "Puntuación automática por celdas 1/0 · parte superior de la hoja", 7)
    r = 4
    section_label(ws, r, "Puntuación por fallas — suma los puntos que aplica (1 = sí, 0 = no)", 7); r += 1
    header_row(ws, r, ["Falla detectada", "Puntos", "", "Selecciona (1/0)", "", "", "Nota"]); r += 1
    fallas = [
        ("No tiene Google Maps", 20, "b8_gmaps", ""),
        ("Ficha de Google NO reclamada", 15, "b8_gmf", ""),
        ("No tienen website / página de venta", 15, "b8_web", "No tienen web/page de venta"),
        ("WhatsApp NO visible en redes ni Google", 12, "b8_wa_vis", ""),
        ("Instagram abandonada", 10, "b8_ig", "No tienen o abandonada"),
        ("No tienen pasarela de pagos", 10, "b8_pago", ""),
        ("No tienen chatbot", 8, "b8_chat", ""),
        ("Ni folletos ni merchandising", 8, "b8_merch", ""),
        ("Local pequeño / sin AC", 5, "b8_ac", ""),
        ("Sin logos / branding físico", 8, "b8_logo", ""),
    ]
    for nombre, pts, key, obs in fallas:
        style_cell(ws, r, 2, nombre, bg=C_LIGHT, tc=C_TEXT, bold=True, sz=10)
        style_cell(ws, r, 3, pts, bg=C_CARD, tc=C_TEXT, bold=True, sz=11, align="center")
        style_cell(ws, r, 4, None, bg=C_CARD)
        style_cell(ws, r, 5, None, bg=C_LIGHT, tc=C_GREY, sz=9, align="left")
        if obs:
            style_cell(ws, r, 5, obs, bg=C_LIGHT, tc=C_GREY, sz=8, align="left")
        else:
            style_cell(ws, r, 5, None, bg=C_CARD)
        row_map[key] = (r, 4)
        r += 1
    # fórmulas de semáforo
    r += 1
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=7)
    style_cell(ws, r, 1, "RESULTADO AUTOMÁTICO (rellena las celdas de verdad con 1/0)",
               bg=C_LIGHT, tc=C_TEXT, bold=True, sz=10, align="left")
    r += 1
    style_cell(ws, r, 1, "Puntuación total", bg=C_LIGHT, tc=C_TEXT, bold=True, sz=11)
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=4)
    fc = style_cell(ws, r, 2, None, bg=C_CARD, bold=True, sz=13, align="center")
    ws.cell(row=r, column=5).border = border_all
    style_cell(ws, r, 5, None, bg=C_LIGHT, tc=C_GREY, sz=9, align="left")
    ws.merge_cells(start_row=r, start_column=6, end_row=r, end_column=7)
    style_cell(ws, r, 6, None, bg=C_LIGHT, tc=C_GREY, sz=9, align="left")
    r += 1
    style_cell(ws, r, 1, "Semáforo", bg=C_LIGHT, tc=C_TEXT, bold=True, sz=11)
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=4)
    sc = style_cell(ws, r, 2, None, bg=C_CARD, bold=True, sz=12, align="center")
    ws.cell(row=r, column=5).border = border_all
    style_cell(ws, r, 5, None, bg=C_LIGHT, tc=C_GREY, sz=9, align="left")
    ws.merge_cells(start_row=r, start_column=6, end_row=r, end_column=7)
    style_cell(ws, r, 6, None, bg=C_LIGHT, tc=C_GREY, sz=9, align="left")
    r += 1
    style_cell(ws, r, 1, "Etiqueta", bg=C_LIGHT, tc=C_TEXT, bold=True, sz=11)
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=4)
    et = style_cell(ws, r, 2, None, bg=C_CARD, bold=True, sz=11, align="center")
    ws.cell(row=r, column=5).border = border_all
    style_cell(ws, r, 5, None, bg=C_LIGHT, tc=C_GREY, sz=9, align="left")
    ws.merge_cells(start_row=r, start_column=6, end_row=r, end_column=7)
    style_cell(ws, r, 6, None, bg=C_LIGHT, tc=C_GREY, sz=9, align="left")

    first_falla = row_map['b8_gmaps'][0]
    last_falla  = row_map['b8_logo'][0]
    score_row   = r - 3
    fc.value = f"=SUM(D{first_falla}:D{last_falla})"
    # Puntuación total está fija en B18; el semáforo y la etiqueta usan B18
    sc.value = f'=IF(B18>=20,"🔴 ALERTA ROJA",IF(B18>=10,"🟠 ALERTA NARANJA","🟢 VERDE"))'
    et.value = f'=IF(B18>=20,"&ge;20 · Contáctate hoy mismo",IF(B18>=10,"10–19 · Prioridad media","&lt;10 · Buen estado · seguimiento normal"))'

    r += 2
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=7)
    style_cell(ws, r, 1, "Instrucciones: marque con 1 en cada falta; la puntuación se calcula sola. Este bloque también puede usarse como control de expediente.",
               bg=C_LIGHT, tc=C_GREY, sz=9, align="left", italic=True)
    ws.row_dimensions[r].height = 28

    r += 2
    section_label(ws, r, "Índice rápido de la ruta", 7); r += 1
    header_row(ws, r, ["Campo", "Dato", "", "Campo", "Dato", "", "Nota"]); r += 1
    index = [("Fecha/Hora", "b1_fecha"), ("Sector/Calle", "b1_sector"), ("Agente", "b1_agent"),
             ("Local com.", "b1_local"), ("Dirección", "b1_direc"), ("Crece/veterano", "b1_veterano"),
             ("Verificado en Google Maps", "b3_gmaps"), ("Ficha Google", "b3_gm_ficha"),
             ("WhatsApp corporativo", "b5_wa"), ("WhatsApp visible", "b5_wa_rs"),
             ("Website", "b3_web"), ("Pasarela de pagos", "b3_pago"),
             ("Instagram", "b4_ig_act"), ("TikTok", "b4_tt_act"), ("Facebook", "b4_fb_act"),
             ("Chatbot", "b5_chatbot"), ("Pago adicional mensual $", "b4_presupuesto")]
    for a, ka in index:
        style_cell(ws, r, 2, a, bg=C_LIGHT, tc=C_TEXT, bold=True, sz=9)
        style_cell(ws, r, 3, None, bg=C_LIGHT, tc=C_GREY, sz=9, align="left")
        style_cell(ws, r, 4, a, bg=C_LIGHT, tc=C_TEXT, bold=True, sz=9)
        ws.merge_cells(start_row=r, start_column=4, end_row=r, end_column=5)
        style_cell(ws, r, 6, None, bg=C_LIGHT, tc=C_GREY, sz=9)
        ws.merge_cells(start_row=r, start_column=6, end_row=r, end_column=7)
        row_map[ka] = (r, 3) if ka not in row_map else row_map[ka]
        r += 1

    for a, ka in index:
        if ka in row_map:
            rr = row_map[ka][0]
            col_a = get_column_letter(row_map[ka][1])
            if ws.cell(row=rr, column=3).value is None:
                ws.cell(row=rr, column=3).value = f'=IF({col_a}{rr}="","—",{col_a}{rr})'
    return row_map

if __name__ == "__main__":
    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    globals()['row_map'] = {}
    build_meta(wb)
    build_identidad(wb)
    build_web(wb)
    build_redes(wb)
    build_whatsapp(wb)
    build_oferta(wb)
    build_merch(wb)
    build_resumen(wb)
    wb.save(OUT)
    print("Guardado:", OUT)
