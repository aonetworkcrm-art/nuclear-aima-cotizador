#!/usr/bin/env python3
"""
Generate a pre-loaded PDF of the Guia ONAPI-ONDA-SAS executive summary.
Usage: python generate-onapi-pdf.py
Output: onapi-onda-ejecutivo.pdf
"""

from fpdf import FPDF
import os
from datetime import date

OUTPUT = "onapi-onda-ejecutivo.pdf"

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

MESES = ["enero","febrero","marzo","abril","mayo","junio",
         "julio","agosto","septiembre","octubre","noviembre","diciembre"]

class OnapiPDF(FPDF):
    def header(self):
        if self.page_no() == 1: return
        self.set_font("Helvetica","I",7)
        self.set_text_color(*MUTED)
        self.cell(0,8,"Guia ONAPI · ONDA · SAS · Nuclear AIMA", align="L")
        self.cell(0,8,f"Pagina {self.page_no()}", align="R", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(220,220,220)
        self.line(10,14,200,14)
        self.ln(3)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica","I",6)
        self.set_text_color(*MUTED)
        d = date.today()
        self.cell(0,10,f"Nuclear AIMA · ONAPI-ONDA-SAS · {d.day} de {MESES[d.month-1]} de {d.year}", align="C")

    def section_h(self, text, icon=""):
        self.ln(4)
        self.set_font("Helvetica","B",11)
        self.set_text_color(*GOLD)
        self.cell(0,8,f"{icon} {text}", new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(*GOLD)
        self.line(10,self.get_y(),200,self.get_y())
        self.ln(3)

    def body(self, text, size=9):
        self.set_font("Helvetica","",size)
        self.set_text_color(*TEXT)
        self.multi_cell(0,4.5,text)
        self.ln(1)

    def step_block(self, num, title, cost, time, desc):
        self.ln(2)
        self.set_fill_color(*DARK2)
        self.set_draw_color(*GOLD)
        self.rect(10,self.get_y(),190,8,style="DF")
        self.set_xy(14,self.get_y()-7)
        self.set_font("Helvetica","B",9)
        self.set_text_color(*GOLD)
        self.cell(6,6,str(num))
        self.set_text_color(*WHITE)
        self.cell(0,6,f"{title}", new_x="LMARGIN", new_y="NEXT")
        self.set_xy(14,self.get_y())
        self.set_font("Helvetica","",7)
        self.set_text_color(*MUTED)
        self.cell(0,5,f"{cost} · {time}", new_x="LMARGIN", new_y="NEXT")
        self.ln(1)
        self.set_font("Helvetica","",8)
        self.set_text_color(*TEXT)
        self.multi_cell(0,4,desc)
        self.ln(2)


def generate():
    pdf = OnapiPDF("P","mm","A4")
    pdf.set_auto_page_break(auto=True, margin=20)

    # ── PAGE 1: Cover ──
    pdf.add_page()
    pdf.ln(50)
    pdf.set_draw_color(*GOLD)
    pdf.set_line_width(1.5)
    pdf.line(30,pdf.get_y(),180,pdf.get_y())
    pdf.ln(4)
    pdf.set_font("Helvetica","B",26)
    pdf.set_text_color(*DARK)
    pdf.cell(0,14,"ONAPI · ONDA · SAS", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica","",12)
    pdf.set_text_color(*MUTED)
    pdf.cell(0,8,"Guia Completa de Registro Legal para Sellos Independientes", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0,6,"en Republica Dominicana", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(6)
    pdf.set_draw_color(*GOLD)
    pdf.set_line_width(1.5)
    pdf.line(30,pdf.get_y(),180,pdf.get_y())
    pdf.ln(20)

    # Stats box
    pdf.set_fill_color(*LIGHT_BG)
    pdf.set_draw_color(*GOLD)
    pdf.rect(30,pdf.get_y(),150,30,style="DF")
    pdf.set_xy(35,pdf.get_y()+3)
    pdf.set_font("Helvetica","",9)
    pdf.set_text_color(*MUTED)
    pdf.cell(0,5,"4 pasos  ·  ~$710-$1,050 USD  ·  ~30 dias", new_x="LMARGIN", new_y="NEXT")
    pdf.set_xy(35,pdf.get_y())
    pdf.set_font("Helvetica","B",11)
    pdf.set_text_color(*DARK)
    pdf.cell(0,7,"ONAPI  >  SAS  >  ONDA  >  Contrato", new_x="LMARGIN", new_y="NEXT")
    pdf.set_xy(35,pdf.get_y())
    pdf.set_font("Helvetica","",8)
    pdf.set_text_color(*GREEN)
    pdf.cell(0,5,"Importante: Elegir SAS sobre SRL (Ley 31-11)", new_x="LMARGIN", new_y="NEXT")

    pdf.ln(35)
    pdf.set_font("Helvetica","",8)
    pdf.set_text_color(*MUTED)
    pdf.cell(0,5,"Nuclear AIMA  ·  v2.0  ·  Estrategia Hyperion", align="C", new_x="LMARGIN", new_y="NEXT")

    # ── PAGE 2: Cost Table + Steps ──
    pdf.add_page()
    pdf.set_font("Helvetica","B",16)
    pdf.set_text_color(*DARK)
    pdf.cell(0,10,"Resumen Ejecutivo", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(2)
    pdf.body("Guia paso a paso para el registro legal de un sello independiente en Republica Dominicana: "
             "desde el nombre comercial en ONAPI hasta el contrato matriz de administracion. "
             "Incluye la actualizacion critica: constituir SAS (no SRL).")

    # Cost table
    pdf.section_h("Tabla de Costos","$")
    col_w = [8,44,40,30,22,24,22]
    headers = ["#","Paso","Institucion","Costo RD$","Costo USD","Dias"]
    pdf.set_font("Helvetica","B",7)
    pdf.set_fill_color(*LIGHT_BG)
    pdf.set_text_color(*MUTED)
    for i,h in enumerate(headers):
        pdf.cell(col_w[i],7,h,fill=True,align="C" if i>2 else "L")
    pdf.ln()

    rows = [
        ("1","Nombre Comercial","ONAPI","RD$3,500-6,500","$60-110","5"),
        ("2A","Estatutos Notario","Notaria","RD$8,000-15,000","$135-255","2-3"),
        ("2B","Impuesto DGII","DGII","RD$300","~$5","1"),
        ("2C","Reg. Mercantil","Cam. Comercio","RD$5,000-10,000","$85-170","5-10"),
        ("2D","RNC","DGII","RD$2,000","~$34","3"),
        ("3","Prod. Fonografico","ONDA","RD$8,000-10,000","$135-170","10-15"),
        ("4","Contrato Matriz","Abogado","RD$15,000-18,000","$255-305","3-5"),
    ]

    pdf.set_font("Helvetica","",8)
    pdf.set_text_color(*TEXT)
    for r in rows:
        for i,v in enumerate(r):
            pdf.cell(col_w[i],6,v,align="C" if i>2 else "L")
        pdf.ln()

    pdf.set_draw_color(*GOLD)
    pdf.line(10,pdf.get_y(),200,pdf.get_y())
    pdf.set_font("Helvetica","B",9)
    pdf.set_fill_color(*LIGHT_BG)
    total = ["","TOTAL","","RD$41,800-61,800","$710-$1,050","~30"]
    for i,v in enumerate(total):
        pdf.cell(col_w[i],7,v,fill=True,align="C" if i>2 else "L")
    pdf.ln(8)

    # 4 Steps
    pdf.section_h("Los 4 Pasos","")
    steps = [
        (1,"ONAPI - Nombre Comercial",
         "RD$3,500-6,500 | $60-110 USD | 5 dias",
         "Registrar el nombre del sello en la Oficina Nacional de la Propiedad Industrial "
         "(Clase 41: produccion musical + Clase 35: gestion comercial). El certificado de "
         "ONAPI es la primera prueba de existencia formal ante distribuidoras internacionales."),
        (2,"SAS - Sociedad por Acciones Simplificada",
         "~RD$25,000 | ~$425 USD | ~15 dias",
         "Estructura legal que separa patrimonio personal del empresarial. Elegir SAS (Ley 31-11) "
         "sobre SRL: 1 solo socio suficiente, acciones transferibles libremente, marco moderno. "
         "Pasos: estatutos con notario, impuesto DGII, Registro Mercantil, RNC. Capital minimo RD$100,000."),
        (3,"ONDA - Productor Fonografico",
         "RD$8,000-10,000 | $135-170 USD | 10-15 dias",
         "El paso mas poderoso. Al registrar la SAS como Productor Fonografico, el Estado "
         "dominicano te reconoce como entidad con facultad legal para masters. YouTube procesa "
         "reclamos con prioridad institucional. Usar Obra Colectiva para ahorrar RD$290,000."),
        (4,"Contrato Matriz de Administracion",
         "RD$15,000-18,000 | $255-305 USD | 3-5 dias",
         "Activo legal mas valioso. Clausulas: Mandato Exclusivo, Claim & Monetize, Split 70/30, "
         "Duracion 10 anos, Adelanto Recuperable, Explotacion Web3. Buscar abogado especializado "
         "en entretenimiento y propiedad intelectual."),
    ]
    for num,title,meta,desc in steps:
        parts = meta.split(" | ")
        cost = parts[0] if len(parts)>0 else meta
        time = parts[1] if len(parts)>1 else ""
        pdf.step_block(num,title,cost,time,desc)

    # ── PAGE 3+: SAS vs SRL + Warning + Phases ──
    pdf.add_page()

    # SAS vs SRL
    pdf.section_h("SAS vs SRL: Cual Elegir?","")
    pdf.body("En RD existen dos figuras: SRL (Ley 479-08) y SAS (Ley 31-11). Para un sello "
             "independiente que manejara activos digitales y tokenizacion, la SAS es la unica "
             "opcion correcta. En una SRL, transferir cuotas requiere modificar estatutos. "
             "En una SAS, las acciones se transfieren con un simple endoso.")

    comp_col_w = [95,95]
    pdf.set_font("Helvetica","B",9)
    pdf.set_fill_color(*LIGHT_RED)
    pdf.set_text_color(*RED)
    pdf.cell(comp_col_w[0],7,"X  SRL (Tradicional)", fill=True, align="C")
    pdf.set_fill_color(*LIGHT_GREEN)
    pdf.set_text_color(*GREEN)
    pdf.cell(comp_col_w[1],7,"V  SAS (Recomendada)", fill=True, align="C")
    pdf.ln()

    srl_items = ["Minimo 2 socios","Cuotas no transferibles","Gobierno rigido","No emite acciones","Ley 479-08"]
    sas_items = ["1 solo socio","Acciones transferibles","Flexibilidad total","Emite acciones","Ley 31-11"]

    pdf.set_font("Helvetica","",8)
    pdf.set_text_color(*TEXT)
    for i in range(len(srl_items)):
        pdf.set_fill_color(*LIGHT_RED)
        pdf.cell(comp_col_w[0],6,f"  {srl_items[i]}", fill=True)
        pdf.set_fill_color(*LIGHT_GREEN)
        pdf.cell(comp_col_w[1],6,f"  {sas_items[i]}", fill=True)
        pdf.ln()
    pdf.ln(3)
    pdf.set_fill_color(*LIGHT_GREEN)
    pdf.set_draw_color(*GREEN)
    pdf.rect(10,pdf.get_y(),190,7,style="DF")
    pdf.set_xy(14,pdf.get_y()+1)
    pdf.set_font("Helvetica","B",8)
    pdf.set_text_color(*GREEN)
    pdf.cell(0,5,"V  RECOMENDACION: Constituye una SAS, no una SRL.", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(6)

    # Legal Warning
    pdf.section_h("Advertencia Legal","")
    pdf.set_fill_color(*LIGHT_RED)
    pdf.set_draw_color(*RED)
    y = pdf.get_y()
    pdf.rect(10,y,190,16,style="DF")
    pdf.set_line_width(0.4)
    pdf.set_draw_color(*RED)
    pdf.line(10,y,10,y+16)
    pdf.set_line_width(0.1)
    pdf.set_xy(14,y+1)
    pdf.set_font("Helvetica","B",8)
    pdf.set_text_color(*RED)
    pdf.cell(0,5,"No subas catalogos sin consentimiento firmado del artista.", new_x="LMARGIN", new_y="NEXT")
    pdf.set_xy(14,pdf.get_y())
    pdf.set_font("Helvetica","",8)
    pdf.set_text_color(*TEXT)
    pdf.multi_cell(182,4,"Declarar falsamente ser dueno legitimo es fraude ante Google. "
                        "Distribuidoras como FUGA o SonoSuite cancelaran tu cuenta si lo detectan. "
                        "Orden correcto: Contacto > Contrato > Registro > Distribucion.")
    pdf.ln(6)

    # Next Phases
    pdf.section_h("Lo que viene despues","")
    phases = [
        ("SoundExchange","$0","Retroactivo 3 a"),
        ("ASCAP/BMI","$0","Ejecucion publica"),
        ("Content ID","$20/ano","ISRCs + Distro"),
        ("Pitch Multinac.","$$$","$50K-$150K+"),
        ("LLC Wyoming","$100-300","Internacional"),
        ("Tokenizacion","$$","Smart Contracts"),
    ]
    pdf.set_font("Helvetica","",7)
    pdf.set_text_color(*TEXT)
    cols = 3
    for i in range(0, len(phases), cols):
        row = phases[i:i+cols]
        for name,cost,time in row:
            pdf.set_fill_color(*LIGHT_BG)
            pdf.set_draw_color(220,220,220)
            x0 = pdf.get_x()
            y0 = pdf.get_y()
            pdf.rect(x0,y0,62,14,style="DF")
            pdf.set_xy(x0+4,y0+1)
            pdf.set_font("Helvetica","B",7)
            pdf.set_text_color(*GOLD)
            pdf.cell(54,4,name)
            pdf.set_xy(x0+4,pdf.get_y())
            pdf.set_font("Helvetica","",7)
            pdf.set_text_color(*GREEN)
            pdf.cell(54,4,cost)
            pdf.set_xy(x0+4,pdf.get_y())
            pdf.set_font("Helvetica","",6)
            pdf.set_text_color(*MUTED)
            pdf.cell(54,4,time)
            pdf.set_xy(x0+62,y0)
        pdf.ln(14)

    pdf.ln(6)
    pdf.set_font("Helvetica","I",8)
    pdf.set_text_color(*MUTED)
    d = date.today()
    pdf.cell(0,5,f"Generado automaticamente el {d.day} de {MESES[d.month-1]} de {d.year} por Nuclear AIMA",
             align="C", new_x="LMARGIN", new_y="NEXT")

    pdf.output(OUTPUT)
    print(f"PDF generado: {OUTPUT}")
    print(f"Tamano: {os.path.getsize(OUTPUT)/1024:.1f} KB")


if __name__ == "__main__":
    generate()
