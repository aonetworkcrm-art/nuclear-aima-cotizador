#!/usr/bin/env python3
"""
Generate a pre-loaded PDF of the Pasos Estrella executive summary.
Usage: python generate-pasos-pdf.py
Output: pasos-estrella-ejecutivo.pdf
"""

from fpdf import FPDF
import os

OUTPUT = "pasos-estrella-ejecutivo.pdf"

# Brand colors
GOLD = (185, 148, 78)
DARK = (10, 10, 12)
DARK2 = (17, 17, 20)
GREEN = (76, 173, 124)
RED = (224, 92, 92)
TEXT = (30, 30, 30)
MUTED = (100, 100, 100)
WHITE = (255, 255, 255)
LIGHT_BG = (245, 242, 237)
LIGHT_GREEN = (232, 245, 238)
LIGHT_RED = (254, 242, 242)


class PasosPDF(FPDF):
    def header(self):
        if self.page_no() == 1:
            return
        self.set_font("Helvetica", "I", 7)
        self.set_text_color(*MUTED)
        self.cell(0, 8, "Pasos Estrella · Nuclear AIMA", align="L")
        self.cell(0, 8, f"Pagina {self.page_no()}", align="R", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(220, 220, 220)
        self.line(10, 14, 200, 14)
        self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 6)
        self.set_text_color(*MUTED)
        self.cell(0, 10, "Nuclear AIMA · Pasos Estrella · Generado el " + self._date_str(), align="C")

    def _date_str(self):
        from datetime import date
        meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
                 "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
        d = date.today()
        return f"{d.day} de {meses[d.month-1]} de {d.year}"

    def section_title(self, text, icon=""):
        self.ln(4)
        self.set_font("Helvetica", "B", 11)
        self.set_text_color(*GOLD)
        self.cell(0, 8, f"{icon} {text}", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(*GOLD)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(3)

    def body_text(self, text, size=9):
        self.set_font("Helvetica", "", size)
        self.set_text_color(*TEXT)
        self.multi_cell(0, 4.5, text)
        self.ln(1)

    def highlight_box(self, text, color=GOLD):
        x = self.get_x()
        y = self.get_y()
        self.set_fill_color(*LIGHT_BG)
        self.set_draw_color(*color)
        self.rect(10, y, 190, 12, style="DF")
        self.set_line_width(0.4)
        self.set_draw_color(*color)
        self.line(10, y, 10, y + 12)
        self.set_line_width(0.1)
        self.set_xy(14, y + 1)
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*TEXT)
        self.multi_cell(182, 4.5, text)
        self.ln(2)

    def step_block(self, num, title, cost, time, desc):
        self.ln(2)
        # Step header
        self.set_fill_color(*DARK2)
        self.set_draw_color(*GOLD)
        self.rect(10, self.get_y(), 190, 8, style="DF")
        self.set_xy(14, self.get_y() - 7)
        self.set_font("Helvetica", "B", 9)
        self.set_text_color(*GOLD)
        self.cell(6, 6, str(num))
        self.set_text_color(*WHITE)
        self.cell(0, 6, f"{title}", new_x="LMARGIN", new_y="NEXT")
        self.set_xy(14, self.get_y())
        self.set_font("Helvetica", "", 7)
        self.set_text_color(*MUTED)
        self.cell(0, 5, f"{cost} · {time}", new_x="LMARGIN", new_y="NEXT")
        self.ln(1)
        # Description
        self.set_font("Helvetica", "", 8)
        self.set_text_color(*TEXT)
        self.multi_cell(0, 4, desc)
        self.ln(2)


def generate():
    pdf = PasosPDF("P", "mm", "A4")
    pdf.set_auto_page_break(auto=True, margin=20)

    # ────────────────────── PAGE 1: Cover ──────────────────────
    pdf.add_page()
    pdf.ln(50)
    # Gold accent line
    pdf.set_draw_color(*GOLD)
    pdf.set_line_width(1.5)
    pdf.line(30, pdf.get_y(), 180, pdf.get_y())
    pdf.ln(4)

    # Title
    pdf.set_font("Helvetica", "B", 28)
    pdf.set_text_color(*DARK)
    pdf.cell(0, 14, "Pasos Estrella", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", "", 12)
    pdf.set_text_color(*MUTED)
    pdf.cell(0, 8, "Guia Definitiva para Fundar un Sello Independiente", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 6, "en Republica Dominicana", align="C", new_x="LMARGIN", new_y="NEXT")

    pdf.ln(6)
    pdf.set_draw_color(*GOLD)
    pdf.set_line_width(1.5)
    pdf.line(30, pdf.get_y(), 180, pdf.get_y())
    pdf.ln(20)

    # Key metrics box
    pdf.set_fill_color(*LIGHT_BG)
    pdf.set_draw_color(*GOLD)
    pdf.rect(30, pdf.get_y(), 150, 30, style="DF")
    pdf.set_xy(35, pdf.get_y() + 3)
    pdf.set_font("Helvetica", "", 9)
    pdf.set_text_color(*MUTED)
    pdf.cell(0, 5, "4 pasos  ·  ~$1,050 USD  ·  ~30 dias", new_x="LMARGIN", new_y="NEXT")
    pdf.set_xy(35, pdf.get_y())
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(*DARK)
    pdf.cell(0, 7, "ONAPI  >  SAS  >  ONDA  >  Contrato", new_x="LMARGIN", new_y="NEXT")
    pdf.set_xy(35, pdf.get_y())
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(*GREEN)
    pdf.cell(0, 5, "Basado en el documento maestro start.txt (981 lineas)", new_x="LMARGIN", new_y="NEXT")

    pdf.ln(35)
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(*MUTED)
    pdf.cell(0, 5, "Nuclear AIMA  ·  v2.0  ·  Estrategia Hyperion", align="C", new_x="LMARGIN", new_y="NEXT")

    # ────────────────────── PAGE 2: Investment Table ──────────────────────
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.set_text_color(*DARK)
    pdf.cell(0, 10, "Resumen Ejecutivo", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)

    pdf.body_text(
        "El metodo definitivo para establecer la infraestructura legal y corporativa "
        "necesaria para operar como sello independiente y negociar con distribuidoras "
        "internacionales. Cada paso depende del anterior. El orden es irrompible."
    )

    # Investment Table
    pdf.section_title("Inversion Total", "$")
    pdf.ln(1)

    # Table header
    col_w = [8, 52, 44, 30, 22, 34]
    headers = ["#", "Paso", "Institucion", "Costo RD$", "Costo USD", "Tiempo"]
    pdf.set_font("Helvetica", "B", 8)
    pdf.set_fill_color(*LIGHT_BG)
    pdf.set_text_color(*MUTED)
    for i, h in enumerate(headers):
        pdf.cell(col_w[i], 7, h, border=0, fill=True, align="C" if i > 2 else "L")
    pdf.ln()

    rows = [
        ("1", "Nombre Comercial", "ONAPI", "RD$3,500-6,500", "~$100", "5-10 dias"),
        ("2", "Constitucion SAS", "Cam. Comercio+DGII", "RD$24,000-30,000", "~$500", "15-20 dias"),
        ("3", "Productor Fonografico", "ONDA", "RD$8,000-10,000", "~$150", "10-15 dias"),
        ("4", "Contrato Matriz", "Abogado Especializado", "RD$15,000-18,000", "~$300", "3-5 dias"),
    ]

    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(*TEXT)
    for r in rows:
        for i, v in enumerate(r):
            align = "C" if i > 2 else "L"
            pdf.cell(col_w[i], 6, v, border=0, align=align)
        pdf.ln()

    # Total row
    pdf.set_draw_color(*GOLD)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_fill_color(*LIGHT_BG)
    total_row = ["", "TOTAL", "", "~RD$52,000", "~$1,050", "~30 dias"]
    for i, v in enumerate(total_row):
        align = "C" if i > 2 else "L"
        pdf.cell(col_w[i], 7, v, border=0, fill=True, align=align)
    pdf.ln(8)

    # ────────────────────── 4 Steps ──────────────────────
    pdf.section_title("Los 4 Pasos", "")
    pdf.ln(1)

    steps = [
        (1, "ONAPI - Nombre Comercial",
         "RD$3,500-6,500 | 5-10 dias",
         "Registrar el nombre del sello como marca protegida en la "
         "Oficina Nacional de la Propiedad Industrial (Clase 41: produccion musical, "
         "Clase 35: gestion comercial). El certificado de ONAPI es la primera prueba "
         "de que existes como entidad formal ante distribuidoras internacionales. "
         "Sin este papel, no puedes constituir la empresa."),
        (2, "SAS - Sociedad por Acciones Simplificada",
         "~RD$28,000 | 15-20 dias",
         "Estructura legal que separa tu patrimonio personal del empresarial. "
         "En RD, la SAS es superior a la SRL para catalogos musicales: 1 solo socio "
         "es suficiente, acciones transferibles libremente, marco legal moderno (Ley 31-11) "
         "alineado con estandares internacionales. Pasos: (A) Redactar estatutos con "
         "notario, (B) Pagar impuesto DGII, (C) Registrar en Camara de Comercio, "
         "(D) Solicitar RNC. El capital social minimo es RD$100,000 (1% impuesto = RD$1,000)."),
        (3, "ONDA - Productor Fonografico",
         "RD$8,000-10,000 | 10-15 dias",
         "El paso mas poderoso y el que casi todos omiten. La ONDA reconoce a los "
         "Productores Fonograficos (duenos de las grabaciones/masters). Al registrar "
         "tu SAS bajo esta categoria, el Estado dominicano te reconoce como entidad "
         "con facultad legal para poseer, distribuir y reclamar masters internacionalmente. "
         "Truco clave: registrar como Obra Colectiva (compilacion) en lugar de una por "
         "una reduce el costo de RD$300,000 a menos de RD$10,000."),
        (4, "Contrato Matriz de Administracion",
         "RD$15,000-18,000 | 3-5 dias",
         "Tu activo legal mas valioso. Lo pagas una vez y lo usas con cada artista "
         "que incorpores al sello. Clausulas clave: (1) Mandato de Administracion "
         "Exclusiva, (2) Claim & Monetize (no bloquear, solo monetizar), "
         "(3) Split 70% artista / 30% sello, (4) Duracion 10 anos con renovacion, "
         "(5) Adelanto Recuperable, (6) Explotacion Web3. Busca un abogado "
         "especializado en entretenimiento y propiedad intelectual."),
    ]

    for num, title, meta, desc in steps:
        # meta format: "RD$3,500-6,500 | 5-10 dias"
        parts = meta.split(" | ")
        cost = parts[0] if len(parts) > 0 else meta
        time = parts[1] if len(parts) > 1 else ""
        pdf.step_block(num, title, cost, time, desc)

    # ────────────────────── Page 3+: Bottleneck + SAS vs SRL + Checklist ──────────────────────
    pdf.add_page()

    # Bottleneck
    pdf.section_title("Cuello de Botella - Orden Irrompible", "")
    pdf.ln(1)
    pdf.set_fill_color(*LIGHT_RED)
    pdf.set_draw_color(*RED)
    y = pdf.get_y()
    pdf.rect(10, y, 190, 18, style="DF")
    pdf.set_line_width(0.4)
    pdf.set_draw_color(*RED)
    pdf.line(10, y, 10, y + 18)
    pdf.set_line_width(0.1)
    pdf.set_xy(14, y + 1)
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(*RED)
    pdf.cell(0, 5, "ONAPI -> SAS -> RNC -> Cuenta Bancaria -> ONDA -> Contrato -> Pitch", new_x="LMARGIN", new_y="NEXT")
    pdf.set_xy(14, pdf.get_y())
    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(*TEXT)
    pdf.multi_cell(182, 4, "Cada paso depende del anterior. No puedes ir a la ONDA como empresa sin el RNC. "
                          "No puedes pedir el RNC sin el Registro Mercantil. No puedes hacer el Registro "
                          "Mercantil sin un nombre de ONAPI registrado. Saltarse uno es perder semanas en devoluciones.")
    pdf.ln(6)

    # SAS vs SRL
    pdf.section_title("SAS vs SRL: Cual Elegir?", "")
    pdf.body_text(
        "En Republica Dominicana existen dos figuras juridicas para empresas privadas: "
        "la SRL (Sociedad de Responsabilidad Limitada, Ley 479-08) y la SAS (Sociedad "
        "por Acciones Simplificada, Ley 31-11). Para un sello independiente que manejara "
        "activos digitales, contratos internacionales y tokenizacion Web3, la SAS es la "
        "unica opcion correcta. La SRL fue disenada para negocios tradicionales; la SAS "
        "para startups y empresas de propiedad intelectual."
    )

    # Comparison table
    comp_col_w = [95, 95]
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_fill_color(*LIGHT_RED)
    pdf.set_text_color(*RED)
    pdf.cell(comp_col_w[0], 7, "X  SRL (Tradicional)", fill=True, align="C")
    pdf.set_fill_color(*LIGHT_GREEN)
    pdf.set_text_color(*GREEN)
    pdf.cell(comp_col_w[1], 7, "V  SAS (Recomendada)", fill=True, align="C")
    pdf.ln()

    srl_items = [
        "Minimo 2 socios requeridos",
        "Cuotas no transferibles sin asamblea",
        "Estructura de gobierno rigida",
        "No puede emitir acciones",
        "Ley 479-08 (marco tradicional)",
    ]
    sas_items = [
        "1 solo socio es suficiente",
        "Acciones transferibles libremente",
        "Flexibilidad total en estatutos",
        "Emite acciones para inversion",
        "Ley 31-11 (marco moderno)",
    ]

    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(*TEXT)
    for i in range(len(srl_items)):
        pdf.set_fill_color(*LIGHT_RED)
        pdf.cell(comp_col_w[0], 6, f"  {srl_items[i]}", fill=True)
        pdf.set_fill_color(*LIGHT_GREEN)
        pdf.cell(comp_col_w[1], 6, f"  {sas_items[i]}", fill=True)
        pdf.ln()

    pdf.ln(4)
    pdf.set_fill_color(*LIGHT_GREEN)
    pdf.set_draw_color(*GREEN)
    pdf.rect(10, pdf.get_y(), 190, 7, style="DF")
    pdf.set_xy(14, pdf.get_y() + 1)
    pdf.set_font("Helvetica", "B", 8)
    pdf.set_text_color(*GREEN)
    pdf.cell(0, 5, "V  RECOMENDACION: Constituye una SAS, no una SRL.", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(6)

    # Completion Checklist
    pdf.section_title("Al Completar Esta Fase Tienes:", "")
    pdf.ln(1)

    checklist = [
        "Certificado de ONAPI - Nombre comercial protegido en todo RD",
        "RNC y Registro Mercantil - Tu SAS existe legalmente ante el Estado",
        "Certificacion ONDA - Facultad legal para administrar masters internacionalmente",
        "Contrato Matriz firmado - Terminos claros con cada artista del sello",
        "Cuenta Bancaria Corporativa - Lista para recibir pagos internacionales",
        "Documentacion para Pitch - Lista para Believe / The Orchard",
    ]

    pdf.set_font("Helvetica", "", 8)
    pdf.set_text_color(*TEXT)
    for item in checklist:
        pdf.set_fill_color(*LIGHT_GREEN)
        pdf.set_draw_color(*GREEN)
        y = pdf.get_y()
        pdf.set_fill_color(240, 248, 240)
        pdf.cell(6, 6, " V", fill=True)
        pdf.set_fill_color(255, 255, 255)
        pdf.cell(0, 6, f"  {item}", fill=True)
        pdf.ln()

    pdf.ln(10)
    pdf.set_font("Helvetica", "I", 8)
    pdf.set_text_color(*MUTED)
    pdf.cell(0, 5, f"Generado automaticamente el {pdf._date_str()} por Nuclear AIMA", align="C", new_x="LMARGIN", new_y="NEXT")

    # Save
    pdf.output(OUTPUT)
    print(f"PDF generated: {OUTPUT}")
    print(f"Size: {os.path.getsize(OUTPUT) / 1024:.1f} KB")


if __name__ == "__main__":
    generate()
