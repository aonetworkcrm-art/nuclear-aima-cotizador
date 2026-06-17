#!/usr/bin/env python3
"""Generate adelantos-ejecutivo.pdf"""
from fpdf import FPDF
import os
from datetime import date

OUTPUT = "adelantos-ejecutivo.pdf"
GOLD=(185,148,78); DARK=(10,10,12); DARK2=(17,17,20); GREEN=(76,173,124)
RED=(224,92,92); TEXT=(30,30,30); MUTED=(100,100,100); WHITE=(255,255,255)
LIGHT_BG=(245,242,237); LIGHT_GREEN=(232,245,238); LIGHT_RED=(254,242,242)
MESES=["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]

class AdPDF(FPDF):
    def header(self):
        if self.page_no()==1: return
        self.set_font("Helvetica","I",7); self.set_text_color(*MUTED)
        self.cell(0,8,"Adelantos · Nuclear AIMA",align="L")
        self.cell(0,8,f"Pagina {self.page_no()}",align="R",new_x="LMARGIN",new_y="NEXT")
        self.set_draw_color(220,220,220); self.line(10,14,200,14); self.ln(3)
    def footer(self):
        self.set_y(-15); self.set_font("Helvetica","I",6); self.set_text_color(*MUTED)
        d=date.today(); self.cell(0,10,f"Nuclear AIMA · Adelantos · {d.day} de {MESES[d.month-1]} de {d.year}",align="C")
    def sh(self,t,i=""):
        self.ln(3); self.set_font("Helvetica","B",11); self.set_text_color(*GREEN)
        self.cell(0,8,f"{i} {t}",new_x="LMARGIN",new_y="NEXT")
        self.set_draw_color(*GREEN); self.line(10,self.get_y(),200,self.get_y()); self.ln(2)
    def body(self,t,s=9):
        self.set_font("Helvetica","",s); self.set_text_color(*TEXT); self.multi_cell(0,4.5,t); self.ln(1)
    def card(self,n,t,c,d,desc):
        self.ln(2)
        self.set_fill_color(*DARK2); self.set_draw_color(*GREEN)
        self.rect(10,self.get_y(),190,8,style="DF")
        self.set_xy(14,self.get_y()-7)
        self.set_font("Helvetica","B",9); self.set_text_color(*GREEN)
        self.cell(6,6,str(n)); self.set_text_color(*WHITE); self.cell(0,6,t,new_x="LMARGIN",new_y="NEXT")
        self.set_xy(14,self.get_y())
        self.set_font("Helvetica","",7); self.set_text_color(*MUTED)
        self.cell(0,5,f"{c} · {d}",new_x="LMARGIN",new_y="NEXT"); self.ln(1)
        self.set_font("Helvetica","",8); self.set_text_color(*TEXT); self.multi_cell(0,4,desc); self.ln(2)

pdf=AdPDF("P","mm","A4")
pdf.set_auto_page_break(auto=True,margin=20)

# Cover
pdf.add_page(); pdf.ln(50)
pdf.set_draw_color(*GREEN); pdf.set_line_width(1.5); pdf.line(30,pdf.get_y(),180,pdf.get_y()); pdf.ln(4)
pdf.set_font("Helvetica","B",28); pdf.set_text_color(*DARK)
pdf.cell(0,14,"Adelantos",align="C",new_x="LMARGIN",new_y="NEXT")
pdf.set_font("Helvetica","",12); pdf.set_text_color(*MUTED)
pdf.cell(0,8,"Guia de Plataformas de Financiamiento",align="C",new_x="LMARGIN",new_y="NEXT")
pdf.cell(0,6,"para Catalogos Musicales",align="C",new_x="LMARGIN",new_y="NEXT")
pdf.ln(6); pdf.set_draw_color(*GREEN); pdf.set_line_width(1.5); pdf.line(30,pdf.get_y(),180,pdf.get_y()); pdf.ln(20)

pdf.set_fill_color(*LIGHT_BG); pdf.set_draw_color(*GREEN)
pdf.rect(30,pdf.get_y(),150,30,style="DF")
pdf.set_xy(35,pdf.get_y()+3)
pdf.set_font("Helvetica","",9); pdf.set_text_color(*MUTED)
pdf.cell(0,5,"Adelanto objetivo: $150K-$500K  ·  Retroactivo SX: $40K-$80K",new_x="LMARGIN",new_y="NEXT")
pdf.set_xy(35,pdf.get_y())
pdf.set_font("Helvetica","B",11); pdf.set_text_color(*DARK)
pdf.cell(0,7,"SoundExchange  >  beatBread  >  Believe  >  The Orchard",new_x="LMARGIN",new_y="NEXT")
pdf.set_xy(35,pdf.get_y())
pdf.set_font("Helvetica","",8); pdf.set_text_color(*GREEN)
pdf.cell(0,5,"+ Content ID · ASCAP · BMI · SGACEDOM",new_x="LMARGIN",new_y="NEXT")
pdf.ln(35)
pdf.set_font("Helvetica","",8); pdf.set_text_color(*MUTED)
pdf.cell(0,5,"Nuclear AIMA  ·  v2.0  ·  Estrategia Hyperion",align="C",new_x="LMARGIN",new_y="NEXT")

# Page 2: Strategy overview + SX + beatBread
pdf.add_page()
pdf.set_font("Helvetica","B",16); pdf.set_text_color(*DARK)
pdf.cell(0,10,"Resumen Ejecutivo",new_x="LMARGIN",new_y="NEXT"); pdf.ln(2)
pdf.body("Guia completa de plataformas de financiamiento para catalogos musicales, "
         "con el orden estrategico correcto: desde SoundExchange (retroactivo sin costo) "
         "hasta negociacion con multinacionales como Believe y The Orchard.")

pdf.sh("Estrategia - El Orden Correcto","")

steps=[
    ("1. SoundExchange","$40K-$80K","Retroactivo","Regalias digitales no reclamadas de los ultimos 3 anos. Sin costo, sin contrato."),
    ("2. Registro Legal","~$1,000","~30 dias","ONAPI + SAS + ONDA. Sin esto, ninguna distribuidora seria te firma."),
    ("3. Auditoria Catalogo","$0","2-4 semanas","Documentar los 178 temas con The Tool: nodos, vistas, yield mensual, ingreso fugado."),
    ("4. Distribucion Inicial","$20/ano","3-6 meses","Subir a DistroKid/TuneCore para generar ISRCs e historial de ingresos verificable."),
    ("5. Acercamiento Multinac.","$150K-$500K","4-8 semanas","Con auditoria + ONDA + historial, contactar Believe/The Orchard."),
    ("6. beatBread (Puente)","$1K-$10M+","1-4 semanas","Adelanto rapido sin ceder propiedad. Ideal como puente mientras negocias."),
]
pdf.set_font("Helvetica","",8); pdf.set_text_color(*TEXT)
for t,c,d,desc in steps:
    pdf.set_fill_color(*LIGHT_BG); pdf.set_draw_color(220,220,220)
    y=pdf.get_y(); pdf.rect(10,y,190,12,style="DF")
    pdf.set_xy(12,y+1)
    pdf.set_font("Helvetica","B",8); pdf.set_text_color(*GREEN); pdf.cell(50,4,t)
    pdf.set_font("Helvetica","",7); pdf.set_text_color(*GOLD); pdf.cell(25,4,c)
    pdf.set_text_color(*MUTED); pdf.cell(20,4,d)
    pdf.set_xy(12,y+5.5)
    pdf.set_font("Helvetica","",7); pdf.set_text_color(*TEXT); pdf.multi_cell(186,3.5,desc)
    pdf.set_xy(10,y+12)

pdf.ln(6)
pdf.body("Metrica clave: No es el total de vistas lo que importa. El numero que abre "
         "las puertas de Believe y The Orchard es el ingreso mensual fugado.")

# Page 3: Platform summaries
pdf.add_page()
pdf.sh("Plataformas de Financiamiento","")

platforms=[
    ("SoundExchange","Regalias Retroactivas",
     "$40K-$80K sin costo. Registrar cuenta, ingresar ISRCs, auditan y pagan hasta 3 anos de regalias no reclamadas."),
    ("beatBread","Adelanto Flexible sin Ownership",
     "$1K-$10M+. Subir catalogo, conectan con su red de financiamiento, comparas ofertas, sin ceder propiedad."),
    ("Believe Music","Distribuidora + Adelanto",
     "$150K-$500K. Requiere: empresa constituida, ISRCs activos, historial 6-12 meses, reporte de auditoria profesional."),
    ("The Orchard","Distribuidora + Adelanto (Sony)",
     "$150K-$500K+. Filial de Sony Music. Requisitos similares a Believe. Red global."),
    ("YouTube Content ID","Monetizacion Automatica",
     "$34,700/mes en fuga detectada. 15K+ nodos. Subir via distribuidor con Content ID. Estrategia: Claim > Monetize."),
    ("ASCAP","Sociedad Gestion EE.UU.",
     "Gratis. 925K+ miembros. Recauda regalias por ejecucion publica en EE.UU. Radio, TV, streaming, conciertos."),
    ("BMI","Sociedad Gestion EE.UU.",
     "Gratis. 1.4M+ miembros. Alternativa a ASCAP. Sin fines de lucro. Programas especiales para compositores latinos."),
    ("SGACEDOM","Sociedad Gestion RD",
     "Gratis. Unica entidad facultada en RD para gestionar derechos de autor. RD$135M+ distribuidos. Registro obligatorio."),
]
for t,sub,desc in platforms:
    pdf.set_fill_color(*LIGHT_BG); pdf.set_draw_color(*GREEN)
    y=pdf.get_y(); pdf.rect(10,y,190,11,style="DF")
    pdf.set_line_width(0.3); pdf.set_draw_color(*GREEN); pdf.line(10,y,10,y+11); pdf.set_line_width(0.1)
    pdf.set_xy(13,y+1)
    pdf.set_font("Helvetica","B",8); pdf.set_text_color(*GREEN); pdf.cell(0,4,t,new_x="LMARGIN",new_y="NEXT")
    pdf.set_xy(13,pdf.get_y())
    pdf.set_font("Helvetica","",7); pdf.set_text_color(*MUTED); pdf.multi_cell(0,3.5,desc)
    pdf.ln(1)

# Page 4: Calculator + Pitch
pdf.add_page()
pdf.sh("Calculadora de Adelanto Estimado","")
pdf.body("Basada en yield mensual del catalogo y tasas de mercado. "
         "Rango realista sin ISRC activo: $50K-$150K. Con historial: $150K-$500K.")

pdf.set_fill_color(*LIGHT_BG); pdf.set_draw_color(*GREEN)
y=pdf.get_y(); pdf.rect(10,y,190,20,style="DF")
pdf.set_xy(14,y+1)
pdf.set_font("Helvetica","B",8); pdf.set_text_color(*GREEN)
pdf.cell(0,4,"Metodo de Calculo",new_x="LMARGIN",new_y="NEXT")
pdf.set_xy(14,pdf.get_y())
pdf.set_font("Helvetica","",7); pdf.set_text_color(*TEXT)
pdf.multi_cell(182,3.5,"Yield mensual del catalogo x 12 meses = proyeccion anual. "
             "Adelanto a 3 anos = flujo anual x 3 x 0.7 (70%). "
             "Rango realista: $150K-$500K para catalogos con historial. "
             "SoundExchange retroactivo: 60-120% del yield mensual.")
pdf.ln(4)

pdf.sh("Pitch Deck - Datos Clave","")
pdf.body("Para presentarte ante distribuidoras necesitas: Reporte de auditoria de las "
         "12 canciones principales, ingreso mensual fugado como metrica #1, certificado "
         "ONDA/ONAPI, carta de autorizacion notariada, y lista oficial del catalogo.")

pdf.set_fill_color(*LIGHT_GREEN); pdf.set_draw_color(*GREEN)
y=pdf.get_y(); pdf.rect(10,y,190,12,style="DF")
pdf.set_line_width(0.4); pdf.set_draw_color(*GREEN); pdf.line(10,y,10,y+12); pdf.set_line_width(0.1)
pdf.set_xy(14,y+1)
pdf.set_font("Helvetica","B",8); pdf.set_text_color(*GREEN)
pdf.cell(0,4,"El Argumento de Apertura",new_x="LMARGIN",new_y="NEXT")
pdf.set_xy(14,pdf.get_y())
pdf.set_font("Helvetica","I",7); pdf.set_text_color(*TEXT)
pdf.multi_cell(182,3.5,"'Este catalogo de 190 canciones genera $66,824/mes en ingresos no reclamados. "
             "Potencial de recuperacion anual de $800,000+. Ofrecemos el 100% del catalogo "
             "para distribucion con Content ID activo a cambio de un adelanto de $150K-$500K.'")

pdf.ln(8)
pdf.set_font("Helvetica","I",8); pdf.set_text_color(*MUTED)
d=date.today(); pdf.cell(0,5,f"Generado el {d.day} de {MESES[d.month-1]} de {d.year} por Nuclear AIMA",align="C")

pdf.output(OUTPUT)
print(f"PDF: {OUTPUT} ({os.path.getsize(OUTPUT)/1024:.1f} KB)")
