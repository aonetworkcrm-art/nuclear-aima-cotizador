#!/usr/bin/env python3
"""Generate adspro-estrategia-ejecutivo.pdf — comprehensive campaign strategy PDF."""
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from fpdf import FPDF

OUTPUT = 'adspro-estrategia-ejecutivo.pdf'

# Colors
BG      = (10, 10, 12)
BG2     = (17, 17, 20)
GOLD    = (245, 158, 11)
PURPLE  = (167, 139, 250)
CYAN    = (74, 208, 224)
GREEN   = (76, 173, 124)
ACCENT  = (201, 169, 110)
TEXT    = (240, 237, 232)
MUTED   = (107, 105, 102)
WHITE   = (255, 255, 255)
DANGER  = (224, 92, 92)
PINK    = (244, 114, 182)

W = 210  # A4 width mm
H = 297  # A4 height mm

class AdsProPDF(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font('Helvetica', 'I', 6)
            self.set_text_color(*MUTED)
            self.cell(0, 4, 'AdsPro · Estrategia de Campanas · Nuclear AIMA', align='C')

    def footer(self):
        if self.page_no() > 1:
            self.set_y(-10)
            self.set_font('Helvetica', '', 6)
            self.set_text_color(*MUTED)
            self.cell(0, 4, f'Pagina {self.page_no() - 1}', align='C')

    def section_title(self, text, color=PURPLE):
        self.set_font('Helvetica', 'B', 9)
        self.set_text_color(*color)
        self.cell(0, 5, text.upper())
        self.ln(3)
        self.set_draw_color(*color)
        self.set_line_width(0.3)
        self.line(self.get_x(), self.get_y(), self.get_x() + 190, self.get_y())
        self.ln(4)

    def warm_card(self, x, y, w, h, color):
        self.set_fill_color(*color)
        self.set_draw_color(*color)
        self.rect(x, y, w, h, 'DF')
        # top accent line
        self.set_fill_color(*PURPLE)
        self.rect(x, y, w, 0.8, 'F')

    def metric_box(self, label, value, x, y, w=44, vcolor=GOLD):
        self.set_fill_color(*BG2)
        self.set_draw_color(*BG2)
        self.rect(x, y, w, 12, 'DF')
        self.set_font('Helvetica', '', 5)
        self.set_text_color(*MUTED)
        self.set_xy(x + 2, y + 1)
        self.cell(w - 4, 3, label.upper())
        self.set_font('Helvetica', 'B', 9)
        self.set_text_color(*vcolor)
        self.set_xy(x + 2, y + 5)
        self.cell(w - 4, 5, value)

    def persona_box(self, num, name, age_gen, loc, platform, income, yield_val, views, nodos, songs, tags, desc, x, y, w=90, icon_color=PINK):
        h = 52
        self.set_fill_color(*BG2)
        self.set_draw_color(*(40, 40, 45))
        self.rect(x, y, w, h, 'DF')
        # icon
        self.set_fill_color(*(30, 30, 35))
        self.rect(x + 2, y + 2, 6, 6, 'DF')
        # Name
        self.set_font('Helvetica', 'B', 7)
        self.set_text_color(*icon_color)
        self.set_xy(x + 10, y + 2)
        self.cell(w - 14, 3, name)
        # Tags
        tx = x + w - 2
        for tag in tags[:3]:
            tw = self.get_string_width(tag) + 2
            tx -= tw
            self.set_fill_color(*BG)
            self.set_text_color(*MUTED)
            self.set_font('Helvetica', '', 4)
            self.set_xy(tx, y + 2)
            self.cell(tw, 3, tag, align='C')

        # Demo grid
        demos = [
            (f'Edad: {age_gen}', f'Yield: {yield_val}'),
            (f'Ubicacion: {loc}', f'Vistas: {views}'),
            (f'Plataforma: {platform}', f'Nodos: {nodos}'),
            (f'Ingresos: {income}', ''),
        ]
        dy = y + 7
        for d1, d2 in demos:
            self.set_font('Helvetica', '', 4.5)
            self.set_text_color(*MUTED)
            self.set_xy(x + 3, dy)
            self.cell(40, 2.5, d1)
            if d2:
                self.set_xy(x + w//2 + 2, dy)
                self.cell(40, 2.5, d2)
            dy += 3

        # Description line
        self.set_font('Helvetica', '', 4.5)
        self.set_text_color(*MUTED)
        self.set_xy(x + 3, dy + 1)
        # truncate desc to fit
        max_desc_w = w - 6
        desc_text = str(desc) if desc else ''
        while self.get_string_width(desc_text) > max_desc_w and len(desc_text) > 10:
            desc_text = desc_text[:-3] + '...'
        self.cell(max_desc_w, 3, desc_text)

        # Songs
        self.set_font('Helvetica', '', 4)
        self.set_text_color(*CYAN)
        self.set_xy(x + 3, dy + 5)
        song_text = songs[:80] + '...' if len(songs) > 80 else songs
        self.cell(w - 6, 3, song_text)


pdf = AdsProPDF('P', 'mm', 'A4')
pdf.set_auto_page_break(auto=True, margin=12)

# ════════════════════════════════════════════
# PAGE 1: COVER
# ════════════════════════════════════════════
pdf.add_page()
pdf.set_fill_color(*BG)
pdf.rect(0, 0, W, H, 'F')

# Decorative top bar
pdf.set_fill_color(*PURPLE)
pdf.rect(0, 0, W, 3, 'F')

# Title
pdf.set_font('Helvetica', 'B', 28)
pdf.set_text_color(*WHITE)
pdf.set_xy(0, 55)
pdf.cell(W, 12, 'AdsPro', align='C')

pdf.set_font('Helvetica', '', 14)
pdf.set_text_color(*PURPLE)
pdf.set_xy(0, 70)
pdf.cell(W, 8, 'Estrategia de Campanas Publicitarias', align='C')

pdf.set_font('Helvetica', '', 8)
pdf.set_text_color(*MUTED)
pdf.set_xy(0, 82)
pdf.cell(W, 5, 'Ramon Orlando · 178 canciones · 17 albumes · 6 epocas', align='C')

# Stats row
stats_data = [
    ('Canciones', '178', GOLD),
    ('Personas', '6', PURPLE),
    ('Grupos FB', '32', CYAN),
    ('Creativos', '12', GREEN),
    ('Presupuesto', '$2,220/mes', ACCENT),
]
sx = 14
for label, value, color in stats_data:
    pdf.set_fill_color(*BG2)
    pdf.set_draw_color(*(40, 40, 45))
    pdf.rect(sx, 100, 33, 16, 'DF')
    pdf.set_font('Helvetica', '', 4.5)
    pdf.set_text_color(*MUTED)
    pdf.set_xy(sx, 102)
    pdf.cell(33, 4, label.upper(), align='C')
    pdf.set_font('Helvetica', 'B', 10)
    pdf.set_text_color(*color)
    pdf.set_xy(sx, 107)
    pdf.cell(33, 6, value, align='C')
    sx += 36

# Badges
badges_text = '6 AUDIENCIAS  ·  16 GRUPOS FB  ·  12 CREATIVOS  ·  10 COPYS  ·  6 AD SETS  ·  6 ASSETS'
pdf.set_font('Helvetica', '', 5.5)
pdf.set_text_color(*PURPLE)
pdf.set_xy(0, 130)
pdf.cell(W, 4, badges_text, align='C')

# Description
pdf.set_font('Helvetica', '', 7)
pdf.set_text_color(*MUTED)
pdf.set_xy(20, 140)
pdf.cell(W - 40, 12, 'Centro de inteligencia publicitaria basado en el analisis del catalogo completo de Ramon Orlando. Audiencias, grupos de Facebook, conceptos creativos, plantillas de copy, estructura de campanas y guia de assets visuales.', align='C')

# Yield summary box
pdf.set_fill_color(*BG2)
pdf.set_draw_color(*(50, 50, 55))
pdf.rect(30, 162, 150, 18, 'DF')
# Top accent
pdf.set_fill_color(*PURPLE)
pdf.rect(30, 162, 150, 0.8, 'F')

pdf.set_font('Helvetica', 'B', 7)
pdf.set_text_color(*GOLD)
pdf.set_xy(30, 165)
pdf.cell(150, 4, 'Yield Total del Catalogo por Segmento', align='C')

yields = [('Nostalgico', '$10,160'), ('Fiestero', '$13,320'), ('Joven', '$3,536'),
          ('Diaspora', '$1,616'), ('Bachatero', '$1,688'), ('Cristiano', '$924')]
yx = 38
for name, val in yields:
    pdf.set_font('Helvetica', '', 5)
    pdf.set_text_color(*MUTED)
    pdf.set_xy(yx, 171)
    pdf.cell(22, 3, name, align='C')
    pdf.set_font('Helvetica', 'B', 6)
    pdf.set_text_color(*GOLD)
    pdf.set_xy(yx, 175)
    pdf.cell(22, 3, val, align='C')
    yx += 24

# Footer on cover
pdf.set_font('Helvetica', '', 6)
pdf.set_text_color(*MUTED)
pdf.set_xy(0, 280)
pdf.cell(W, 4, 'Nuclear AIMA · Estrategia basada en datos del catalogo 2026', align='C')
pdf.set_xy(0, 285)
pdf.cell(W, 4, 'nuclearaima.com', align='C')

# ════════════════════════════════════════════
# PAGE 2: AUDIENCE PERSONAS
# ════════════════════════════════════════════
pdf.add_page()
pdf.section_title('Personas de Audiencia', PURPLE)

personas = [
    ('Nostalgico Romantic', '45-65', 'RD 38% · USA 32%', 'FB 65% · YT 25%', '$28K-$48K', '$10,160/mes', '289M', '~6,800',
     'Loco de Amor · Tonto Corazon · Dos Sonambulos', 'Crecio con el merengue de los 80s. Responde a nostalgia y legado.', ['ALTA INTENCION', 'NOSTALGIA', 'TICKET $35']),
    ('Fiestero Clasico', '35-55', 'RD 45% · USA 28%', 'FB 45% · IG 30% · TT 15%', '$32K-$65K', '$13,320/mes', '326M', '~6,900',
     'Te Compro Tu Novia · Ring Ring · Cabecita Loca', 'El alma de la fiesta dominicana. Mayor potencial viral.', ['MAYOR VIRAL', 'FIESTA', '$13,320']),
    ('Joven Descubridor', '18-30', 'USA 42% · RD 22%', 'TikTok 48% · IG 35%', '$22K-$42K', '$3,536/mes', '36M+', '~870',
     'El Tiki Tiki del Amor · Mambo 2026', 'Descubrio el merengue por TikTok. +35% trimestral.', ['ALTO CRECIMIENTO', 'TIKTOK', '+35%']),
    ('Diaspora Dominicana', '30-60', 'USA 58% · Esp 15%', 'FB 50% · YT 35%', '$38K-$75K', '$1,616/mes', '6.3M+', '~474',
     'En Tierra Ajena · Un Canto a Nueva York', 'Mayor poder adquisitivo. Conecta con nostalgia patria.', ['MAYOR INGRESO', 'DIASPORA', 'EVENTOS']),
    ('Bachatero Romantic', '25-45', 'RD 32% · USA 30%', 'IG 38% · YT 35%', '$25K-$52K', '$1,688/mes', '4.3M+', '~324',
     'Bachata de Amargue · Lagrimas de Amor', 'Nicho con alta lealtad. Ideal para retargeting.', ['NICHO LEAL', 'ROMANTICO', 'PLAYLIST']),
    ('Cristiano Espiritual', '30-60', 'RD 48% · USA 28%', 'FB 58% · YT 30%', '$25K-$48K', '$924/mes', '2.7M+', '~195',
     'Adoracion en el Trono · Gracias por Tu Amor', 'Mayor lealtad y consistencia. CPA bajo.', ['MAYOR LEALTAD', 'CRISTIANO', 'BAJO CPA']),
]

for i, (name, age, loc, plat, income, y_val, views, nodos, songs, desc, tags) in enumerate(personas):
    row = i // 2
    col = i % 2
    x = 10 + col * 95
    y = 14 + row * 46

    if row * 46 + 52 > 275:
        pdf.add_page()
        y = 14
        # reset row counter
        pass

    pdf.persona_box(i+1, name, age, loc, plat, income, y_val, views, nodos, songs, desc, tags, x, y)

# ════════════════════════════════════════════
# PAGE 3: FACEBOOK GROUPS + CREATIVES
# ════════════════════════════════════════════
pdf.add_page()
pdf.section_title('Grupos de Facebook Prioritarios', CYAN)

groups = [
    ('Dominicanos en USA', '450K+', 'Comunidad de dominicanos en EE.UU.', 'diaspora'),
    ('Merengue de Coleccion', '280K+', 'Merengue clasico 70s-90s.', 'nostalgia'),
    ('Bailadores de Merengue', '180K+', 'Pasos de baile y coreografias.', 'baile'),
    ('Musica Latina 80s 90s', '350K+', 'Musica latina vintage masiva.', 'latino'),
    ('Dominicanos en NY', '320K+', 'Comunidad mas grande fuera de RD.', 'diaspora'),
    ('Bodas Dominicanas', '95K+', 'Novios planeando boda. Himno Te Compro.', 'eventos'),
    ('Cultura Dominicana', '280K+', 'Musica, comida, tradiciones.', 'cultura'),
    ('Musica Tropical Baile', '200K+', 'Salsa, merengue, bachata, cumbia.', 'tropical'),
    ('Radio Nostalgia Latina', '220K+', 'Amantes de musica clasica latina.', 'nostalgia'),
    ('Bachateros Apasionados', '190K+', 'Comunidad de bachateros.', 'bachata'),
    ('Musica Cristiana Latina', '160K+', 'Musica cristiana en espanol.', 'cristiano'),
    ('Fiestas Tematicas Latinas', '170K+', 'Organizadores de fiestas latinas.', 'eventos'),
]

gy = 14
for i, (name, members, desc, tag) in enumerate(groups):
    col = i % 3
    row = i // 3
    x = 10 + col * 63
    y = gy + row * 13

    # Check page break
    if y + 12 > 275:
        pdf.add_page()
        pdf.section_title('Grupos de Facebook Prioritarios (cont.)', CYAN)
        gy = 14
        y = gy + (i % 12) * 13

    pdf.set_fill_color(*BG2)
    pdf.set_draw_color(*(40, 40, 45))
    pdf.rect(x, y, 60, 11, 'DF')
    pdf.set_font('Helvetica', 'B', 5)
    pdf.set_text_color(*WHITE)
    pdf.set_xy(x + 2, y + 1)
    pdf.cell(40, 3, name[:28])
    pdf.set_font('Helvetica', '', 4)
    pdf.set_text_color(*CYAN)
    pdf.set_xy(x + 42, y + 1)
    pdf.cell(16, 3, members, align='R')
    pdf.set_font('Helvetica', '', 4)
    pdf.set_text_color(*MUTED)
    pdf.set_xy(x + 2, y + 5)
    pdf.cell(56, 5, desc[:55])

# Section: Creative Concepts summary
pdf.ln(6)
pdf.section_title('Conceptos Creativos Prioritarios', GREEN)

creatives = [
    ('Te Compro Tu Novia', 'Historia detras del himno', 'Fiestero', 'YT/FB/TT'),
    ('Loco de Amor', 'Parejas bailando merengue', 'Nostalgico', 'FB/IG/YT'),
    ('Ring Ring', 'Challenge telefonico viral', 'Joven', 'TT/Reels'),
    ('El Tiki Tiki', 'Coreografia facil TikTok', 'Joven', 'TT/Reels'),
    ('En Tierra Ajena', 'Testimonios diaspora', 'Diaspora', 'FB/YT'),
    ('Adoracion en el Trono', 'Fe y piano inspiracional', 'Cristiano', 'FB/YT'),
]
cy = pdf.get_y() + 2
for i, (song, concept, seg, plat) in enumerate(creatives):
    col = i % 3
    row = i // 3
    x = 10 + col * 63
    y = cy + row * 10
    pdf.set_fill_color(*BG2)
    pdf.set_draw_color(*(40, 40, 45))
    pdf.rect(x, y, 60, 8, 'DF')
    pdf.set_font('Helvetica', 'B', 4.5)
    pdf.set_text_color(*GOLD)
    pdf.set_xy(x + 2, y + 0.5)
    pdf.cell(40, 2.5, song[:22])
    pdf.set_font('Helvetica', '', 4)
    pdf.set_text_color(*MUTED)
    pdf.set_xy(x + 2, y + 3.5)
    pdf.cell(56, 4, concept[:40])

# ════════════════════════════════════════════
# PAGE 4: COPY + AD SETS
# ════════════════════════════════════════════
pdf.add_page()
pdf.section_title('Plantillas de Copy', PURPLE)

copies = [
    ('Nostalgia FB', 'FB', '"Recuerdas cuando sonaba Loco de Amor..."'),
    ('Fiesta IG', 'IG', '"La fiesta NO empieza hasta que suena Te Compro Tu Novia"'),
    ('TikTok Challenge', 'TT', '"POV: Suena El Tiki Tiki del Amor y no puedes quedarte quieto"'),
    ('Diaspora FB', 'FB', '"Desde Nueva York hasta Madrid... el merengue nos une"'),
    ('Bodas FB', 'FB', '"La cancion infaltable en tu boda dominicana"'),
    ('Industria LinkedIn', 'LI', '"178 canciones, 78M vistas, 4 decadas de legado"'),
    ('Cristiano FB', 'FB', '"Musica que toca el alma y eleva el espiritu"'),
    ('Playlist General', 'ALL', '"La playlist definitiva para tu fiesta dominicana"'),
]

cy = pdf.get_y() + 2
for i, (title, plat, preview) in enumerate(copies):
    col = i % 2
    row = i // 2
    x = 10 + col * 95
    y = cy + row * 14

    # check page break
    if y + 12 > 275:
        pdf.add_page()
        pdf.section_title('Plantillas de Copy (cont.)', PURPLE)
        cy = 14
        y = cy + (i % 8) * 14

    pdf.set_fill_color(*BG2)
    pdf.set_draw_color(*(40, 40, 45))
    pdf.rect(x, y, 90, 12, 'DF')
    # title
    pdf.set_font('Helvetica', 'B', 5.5)
    pdf.set_text_color(*PURPLE)
    pdf.set_xy(x + 3, y + 1)
    pdf.cell(40, 3, title)
    # platform badge
    pdf.set_fill_color(*BG)
    pdf.set_text_color(*MUTED)
    pdf.set_font('Helvetica', '', 4)
    pw = pdf.get_string_width(plat) + 4
    pdf.set_xy(x + 90 - pw - 3, y + 1)
    pdf.cell(pw, 3, plat, align='C')
    # preview
    pdf.set_font('Helvetica', '', 4.5)
    pdf.set_text_color(*MUTED)
    pdf.set_xy(x + 3, y + 5)
    pdf.cell(84, 6, preview[:50])

# Ad sets section
pdf.ln(4)
pdf.section_title('Estructura de Campanas', ACCENT)

adsets = [
    ('Google Ads · Top Hits', '$520/mes', '24%', '4.5x', 'Loco de Amor, Te Compro Tu Novia'),
    ('Meta · Nostalgia 80s-90s', '$400/mes', '18%', '3.5x', 'Loco de Amor, Tonto Corazon'),
    ('Meta · Fiesta y Eventos', '$350/mes', '16%', '4.0x', 'Te Compro Tu Novia, Ring Ring'),
    ('TikTok · Viral Challenge', '$400/mes', '18%', '3.0x', 'Tiki Tiki, Mambo 2026'),
    ('Meta · Diaspora', '$350/mes', '16%', '3.5x', 'En Tierra Ajena, Un Canto a NY'),
    ('Meta · Bachata Lovers', '$200/mes', '8%', '2.5x', 'Bachata de Amargue'),
]

cy = pdf.get_y() + 2
# Budget bar first
pdf.set_fill_color(*BG2)
pdf.set_draw_color(*(40, 40, 45))
pdf.rect(10, cy, 190, 26, 'DF')
pdf.set_font('Helvetica', 'B', 7)
pdf.set_text_color(*GOLD)
pdf.set_xy(10, cy + 1)
pdf.cell(190, 4, 'Distribucion de Presupuesto: $2,220/mes Total', align='C')

# Mini budget bars
bar_colors = [(245,158,11), (74,208,224), (245,158,11), (167,139,250), (201,169,110), (244,114,182)]
bar_x = 18
for i, (name, budget, pct, roas, songs) in enumerate(adsets):
    bw = 28
    pdf.set_font('Helvetica', '', 4)
    pdf.set_text_color(*MUTED)
    pdf.set_xy(bar_x, cy + 6)
    pdf.cell(bw, 3, name.split('·')[0].strip()[:14], align='C')
    pdf.set_font('Helvetica', 'B', 5)
    pdf.set_text_color(*bar_colors[i])
    pdf.set_xy(bar_x, cy + 9)
    pdf.cell(bw, 3, pct, align='C')
    # bar bg
    pdf.set_fill_color(*(30, 30, 35))
    pdf.rect(bar_x + 2, cy + 13, bw - 4, 3, 'F')
    # bar fill
    pct_val = int(pct.replace('%', ''))
    pdf.set_fill_color(*bar_colors[i])
    pdf.rect(bar_x + 2, cy + 13, (bw - 4) * pct_val / 100, 3, 'F')
    # budget
    pdf.set_font('Helvetica', '', 4)
    pdf.set_text_color(*MUTED)
    pdf.set_xy(bar_x, cy + 17)
    pdf.cell(bw, 3, budget, align='C')
    bar_x += 29 + 2

# ════════════════════════════════════════════
# PAGE 5: ASSETS GUIDE
# ════════════════════════════════════════════
pdf.add_page()
pdf.section_title('Guia de Assets Visuales por Segmento', PURPLE)

asset_segments = [
    ('Nostalgico', 'Sepia, marron, beige, cafe', 'Playfair Display serif', 'Vintage, filtro sepia, blanco y negro, bokeh', 'Edicion lenta, fade, textura granulada, piano'),
    ('Fiestero', 'Dorado, rojo, naranja', 'Montserrat Black', 'Alta saturacion, luces discoteca, confeti', 'Edicion rapida, beat sync, zoom, c. lenta'),
    ('Joven', 'Cian neon, magenta, purpura', 'Poppins Black', 'Iluminacion neon, urbano, selfies, UGC', 'Vertical 9:16, morph, trends, gancho 2s'),
    ('Diaspora', 'Azul cielo, verde, marfil', 'Merriweather Bold', 'Paisajes RD, bandera, atardeceres', 'Documental, testimonios, voiceover, emotivo'),
    ('Bachatero', 'Burdeos, plata, rosa', 'Cormorant Garamond', 'Blanco y negro, romantico, guitarras', 'Ritmo lento, letras overlay, close-ups'),
    ('Cristiano', 'Dorado claro, blanco, azul', 'Lora Bold', 'Luz natural, iglesias, naturaleza', 'Piano y cuerdas, contemplativo, timelapse'),
]

cy = pdf.get_y() + 2
for i, (seg, colors, fonts, images, videos) in enumerate(asset_segments):
    col = i % 2
    row = i // 2
    x = 10 + col * 95
    y = cy + row * 42

    pdf.set_fill_color(*BG2)
    pdf.set_draw_color(*(40, 40, 45))
    pdf.rect(x, y, 90, 39, 'DF')
    # accent top
    accent_color = [PINK, GOLD, CYAN, ACCENT, DANGER, GREEN][i]
    pdf.set_fill_color(*accent_color)
    pdf.rect(x, y, 90, 0.6, 'F')

    pdf.set_font('Helvetica', 'B', 6)
    pdf.set_text_color(*accent_color)
    pdf.set_xy(x + 3, y + 1.5)
    pdf.cell(84, 3, seg)

    # Colors
    pdf.set_font('Helvetica', '', 4)
    pdf.set_text_color(*MUTED)
    pdf.set_xy(x + 3, y + 5.5)
    pdf.cell(40, 2.5, 'Colores:')
    pdf.set_text_color(*WHITE)
    pdf.set_xy(x + 20, y + 5.5)
    pdf.cell(67, 2.5, colors[:40])

    # Fonts
    pdf.set_text_color(*MUTED)
    pdf.set_xy(x + 3, y + 8.5)
    pdf.cell(40, 2.5, 'Tipografia:')
    pdf.set_text_color(*WHITE)
    pdf.set_xy(x + 22, y + 8.5)
    pdf.cell(65, 2.5, fonts[:30])

    # Image style
    pdf.set_text_color(*MUTED)
    pdf.set_xy(x + 3, y + 11.5)
    pdf.cell(40, 2.5, 'Imagenes:')
    pdf.set_text_color(*MUTED)
    pdf.set_xy(x + 3, y + 14)
    pdf.cell(84, 5, images[:55])

    # Video style
    pdf.set_text_color(*MUTED)
    pdf.set_xy(x + 3, y + 19.5)
    pdf.cell(40, 2.5, 'Video:')
    pdf.set_text_color(*MUTED)
    pdf.set_xy(x + 3, y + 22)
    pdf.cell(84, 5, videos[:55])

# Dimensions
pdf.ln(2)
pdf.section_title('Dimensiones por Plataforma', CYAN)

dims = [('FB Feed', '1200x630'), ('IG Feed', '1080x1080'), ('IG Stories', '1080x1920'),
        ('TikTok', '1080x1920'), ('YT Thumbnail', '1280x720'), ('YT Pre-roll', '1920x1080'),
        ('Google Display', '1200x628'), ('LinkedIn', '1200x627'), ('X Card', '1200x675')]

dx = 14
for i, (plat, dim) in enumerate(dims):
    pdf.set_fill_color(*BG2)
    pdf.set_draw_color(*(40, 40, 45))
    pdf.rect(dx, pdf.get_y(), 20, 5, 'DF')
    pdf.set_font('Helvetica', '', 4)
    pdf.set_text_color(*MUTED)
    pdf.set_xy(dx, pdf.get_y() + 0.5)
    pdf.cell(20, 2, plat, align='C')
    pdf.set_font('Helvetica', '', 4)
    pdf.set_text_color(*CYAN)
    pdf.set_xy(dx, pdf.get_y() + 2.5)
    pdf.cell(20, 2, dim, align='C')
    dx += 22

# Generate PDF
pdf.output(OUTPUT)
print(f'✅ PDF generated: {OUTPUT}')
print(f'File size: {os.path.getsize(OUTPUT)} bytes')
