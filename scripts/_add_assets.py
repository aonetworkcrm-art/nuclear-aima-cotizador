#!/usr/bin/env python3
import os, re

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('adspro-estrategia.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add CSS for assets section
asset_css = '''
  /* ── Asset Cards ── */
  .ap-assets{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:10px;margin:8px 0 14px}
  .ap-acard{background:var(--bg2);border:0.5px solid var(--border);border-radius:var(--r2);overflow:hidden;transition:all 0.15s}
  .ap-acard:hover{border-color:rgba(167,139,250,0.2);transform:translateY(-1px)}
  .ap-acard .ac-head{padding:10px 14px;border-bottom:0.5px solid var(--border);display:flex;align-items:center;gap:8px}
  .ap-acard .ac-head .ac-icon{font-size:18px;width:32px;height:32px;border-radius:50%;display:flex;align-items:center;justify-content:center;background:var(--bg4);border:0.5px solid var(--border);flex-shrink:0}
  .ap-acard .ac-head .ac-name{font-size:10px;font-weight:600}
  .ap-acard .ac-body{padding:8px 14px}
  .ap-acard .ac-body .ac-section{margin-bottom:6px}
  .ap-acard .ac-body .ac-section .ac-label{font-size:6px;color:var(--muted);text-transform:uppercase;letter-spacing:0.06em;margin-bottom:2px}
  .ap-acard .ac-body .ac-section .ac-text{font-size:8px;color:var(--muted);line-height:1.6}
  .ap-acard .ac-body .ac-section .ac-swatch{display:inline-block;width:12px;height:12px;border-radius:3px;margin-right:3px;vertical-align:middle;border:0.5px solid rgba(255,255,255,0.1)}
  .ap-acard .ac-foot{padding:6px 14px;border-top:0.5px solid var(--border);font-size:7px;color:var(--muted);display:flex;gap:6px;flex-wrap:wrap}
  .ap-acard .ac-foot span{padding:1px 5px;border-radius:3px;background:var(--bg4);border:0.5px solid var(--border)}
  .ap-dimensions{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:6px;margin:8px 0}
  .ap-dim{background:var(--bg2);border:0.5px solid var(--border);border-radius:var(--r);padding:8px 10px;display:flex;justify-content:space-between;align-items:center}
  .ap-dim .dm-label{font-size:7px;color:var(--muted);text-transform:uppercase;letter-spacing:0.06em}
  .ap-dim .dm-value{font-size:8px;font-family:var(--mono);color:var(--text);font-weight:500}
  .ap-mood{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:6px;margin:8px 0}
  .ap-mood-item{background:var(--bg2);border:0.5px solid var(--border);border-radius:var(--r);padding:10px;border-left:3px solid var(--border2)}
  .ap-mood-item .mm-label{font-size:7px;color:var(--muted);text-transform:uppercase;letter-spacing:0.06em;margin-bottom:3px}
  .ap-mood-item .mm-text{font-size:8px;color:var(--muted);line-height:1.6}
  .ap-mood-item .mm-tags{display:flex;gap:3px;flex-wrap:wrap;margin-top:4px}
  .ap-mood-item .mm-tag{font-size:6px;padding:1px 5px;border-radius:3px;background:var(--bg4);color:var(--muted)}'''

# Insert CSS before the existing ap-creatives CSS block
css_pattern = r'(  /\* ── Creative Cards ── \*/.*?)(  /\* ── Copy Templates ── \*/)'
html = re.sub(css_pattern, asset_css + r'\n\n\1\2', html, flags=re.DOTALL)

# Assets HTML section to insert after Format Guide and before TAB 4
assets_html = '''    <!-- ═══ ASSETS ═══ -->
    <div class="ap-st"><span class="hl">🎨</span> Guía de Assets Visuales por Segmento</div>
    <p style="font-size:9px;color:var(--muted);margin-bottom:10px;line-height:1.6">
      Recomendaciones específicas de colores, tipografía, estilos de imagen y video para cada segmento de audiencia. Usa esta guía para mantener consistencia visual en todos los creativos de campañas pagas.
    </p>

    <div class="ap-assets">

      <!-- Asset 1: Nostálgico -->
      <div class="ap-acard">
        <div class="ac-head"><span class="ac-icon" style="color:var(--pink)">💔</span><span class="ac-name">Nostálgico Romántico</span></div>
        <div class="ac-body">
          <div class="ac-section">
            <div class="ac-label">Paleta de Colores</div>
            <div class="ac-text">
              <span class="ac-swatch" style="background:#8B4513"></span> #8B4513 Marrón sepia ·
              <span class="ac-swatch" style="background:#D4A574"></span> #D4A574 Beige vintage ·
              <span class="ac-swatch" style="background:#2C1810"></span> #2C1810 Café oscuro ·
              <span class="ac-swatch" style="background:#F5DEB3"></span> #F5DEB3 Trigo ·
              <span class="ac-swatch" style="background:#C0392B"></span> #C0392B Rojo acento
            </div>
          </div>
          <div class="ac-section">
            <div class="ac-label">Tipografía</div>
            <div class="ac-text"><strong>Títulos:</strong> Playfair Display o Georgia (serif clásica) · <strong>Cuerpo:</strong> Inter o Lato (sans-serif limpia) · <strong>CTA:</strong> Bold, mayúsculas, tracking 0.05em</div>
          </div>
          <div class="ac-section">
            <div class="ac-label">Estilo de Imagen</div>
            <div class="ac-text">Fotos vintage con filtro sepia suave. Retratos en blanco y negro con viñeta. Texturas de papel añejo. Iluminación cálida y dorada (golden hour). Composición centrada, planos medios de parejas bailando o abrazándose. Fondo desenfocado (bokeh). </div>
          </div>
          <div class="ac-section">
            <div class="ac-label">Estilo de Video</div>
            <div class="ac-text">Edición lenta (cortes cada 3-5s). Transiciones con fade y dissolve. Música suave de piano de fondo. Superposición de textura granulada 8mm. Texto en overlay con letras tipo máquina de escribir. Ritmo pausado.</div>
          </div>
        </div>
        <div class="ac-foot"><span>Sepia</span><span>Vintage</span><span>Cálido</span><span>Romántico</span><span>Piano</span></div>
      </div>

      <!-- Asset 2: Fiestero -->
      <div class="ap-acard">
        <div class="ac-head"><span class="ac-icon" style="color:var(--gold)">🎉</span><span class="ac-name">Fiestero Clásico</span></div>
        <div class="ac-body">
          <div class="ac-section">
            <div class="ac-label">Paleta de Colores</div>
            <div class="ac-text">
              <span class="ac-swatch" style="background:#FFD700"></span> #FFD700 Dorado ·
              <span class="ac-swatch" style="background:#DC143C"></span> #DC143C Rojo festivo ·
              <span class="ac-swatch" style="background:#1a1a2e"></span> #1a1a2e Noche profunda ·
              <span class="ac-swatch" style="background:#FF6B35"></span> #FF6B35 Naranja energía ·
              <span class="ac-swatch" style="background:#FFFFFF"></span> #FFFFFF Blanco luz
            </div>
          </div>
          <div class="ac-section">
            <div class="ac-label">Tipografía</div>
            <div class="ac-text"><strong>Títulos:</strong> Montserrat Black o Bebas Neue (negrita impactante) · <strong>Cuerpo:</strong> Inter Medium · <strong>CTA:</strong> All caps, tracking 0.1em, con subrayado animado</div>
          </div>
          <div class="ac-section">
            <div class="ac-label">Estilo de Imagen</div>
            <div class="ac-text">Fotos de alta energía: gente bailando, multitudes, luces de discoteca. Colores saturados con contraste alto. Ángulo picado (desde arriba) para tomas de pista de baile. Flash directo estilo fiesta. Incluir elementos de celebración: confeti, luces, micrófonos.</div>
          </div>
          <div class="ac-section">
            <div class="ac-label">Estilo de Video</div>
            <div class="ac-text">Edición rápida y dinámica (cortes cada 1-2s). Transiciones con zoom y swipe. Beat sincronizado con la música (cortes en cada downbeat). Overlay de texto animado con entrada explosiva. Incluir reacciones de gente riendo y bailando en cámara lenta.</div>
          </div>
        </div>
        <div class="ac-foot"><span>Energía</span><span>Dorado</span><span>Fiesta</span><span>Baile</span><span>Beat</span></div>
      </div>

      <!-- Asset 3: Joven -->
      <div class="ap-acard">
        <div class="ac-head"><span class="ac-icon" style="color:var(--cyan)">🔮</span><span class="ac-name">Joven Descubridor</span></div>
        <div class="ac-body">
          <div class="ac-section">
            <div class="ac-label">Paleta de Colores</div>
            <div class="ac-text">
              <span class="ac-swatch" style="background:#00CED1"></span> #00CED1 Cian neón ·
              <span class="ac-swatch" style="background:#FF1493"></span> #FF1493 Rosa magenta ·
              <span class="ac-swatch" style="background:#121212"></span> #121212 Casi negro ·
              <span class="ac-swatch" style="background:#7B2FBE"></span> #7B2FBE Púrpura ·
              <span class="ac-swatch" style="background:#39FF14"></span> #39FF14 Verde neón acento
            </div>
          </div>
          <div class="ac-section">
            <div class="ac-label">Tipografía</div>
            <div class="ac-text"><strong>Títulos:</strong> Poppins Black o TT Norms Pro Bold · <strong>Cuerpo:</strong> Inter Light · <strong>CTA:</strong> Bold con tracking suelto, estilo TikTok (texto en pantalla completo, mayúscula inicial)</div>
          </div>
          <div class="ac-section">
            <div class="ac-label">Estilo de Imagen</div>
            <div class="ac-text">Estilo urbano y moderno. Fotos con iluminación neón, contraluces y siluetas. Selfies y contenido UGC (user-generated). Collages digitales con recortes. Textura granulada estilo film. Primer plano de rostros con expresiones auténticas. Incluir elementos de cultura latina joven.</div>
          </div>
          <div class="ac-section">
            <div class="ac-label">Estilo de Video</div>
            <div class="ac-text">Formato vertical 9:16 obligatorio. Edición rápida tipo TikTok (cortes cada 0.5-1.5s). Transiciones con swipe, zoom, y morph. Texto en overlay dinámico (una palabra a la vez). Incluir trending sounds y efectos de sonido. Gancho en los primeros 2 segundos. Subtítulos automáticos siempre visibles.</div>
          </div>
        </div>
        <div class="ac-foot"><span>Neón</span><span>Urbano</span><span>Vertical</span><span>Trends</span><span>UGC</span></div>
      </div>

      <!-- Asset 4: Diáspora -->
      <div class="ap-acard">
        <div class="ac-head"><span class="ac-icon" style="color:var(--accent)">🌎</span><span class="ac-name">Diáspora Dominicana</span></div>
        <div class="ac-body">
          <div class="ac-section">
            <div class="ac-label">Paleta de Colores</div>
            <div class="ac-text">
              <span class="ac-swatch" style="background:#1E90FF"></span> #1E90FF Azul cielo ·
              <span class="ac-swatch" style="background:#228B22"></span> #228B22 Verde palmera ·
              <span class="ac-swatch" style="background:#FF6347"></span> #FF6347 Rojo atardecer ·
              <span class="ac-swatch" style="background:#FDF5E6"></span> #FDF5E6 Marfil ·
              <span class="ac-swatch" style="background:#003366"></span> #003366 Azul profundo bandera
            </div>
          </div>
          <div class="ac-section">
            <div class="ac-label">Tipografía</div>
            <div class="ac-text"><strong>Títulos:</strong> Merriweather Bold (formal/serio) o Abril Fatface · <strong>Cuerpo:</strong> Inter Regular · <strong>CTA:</strong> Semi-bold con tono emotivo, evitar mayúsculas agresivas</div>
          </div>
          <div class="ac-section">
            <div class="ac-label">Estilo de Imagen</div>
            <div class="ac-text">Fotografía de paisajes: playas dominicanas, campos, ciudades con skyline. Gente dominicana en el exterior mostrando orgullo cultural. Bandera dominicana como elemento recurrente pero sutil. Atardeceres, palmeras, calles coloniales. Composición amplia (wide shot) para transmitir inmensidad de la distancia.</div>
          </div>
          <div class="ac-section">
            <div class="ac-label">Estilo de Video</div>
            <div class="ac-text">Ritmo medio-pausado con transiciones suaves. Testimonios reales de dominicanos en el exterior. Montaje tipo documental con voiceover. Música emotiva de piano/guitarra de fondo. Incluir texto con #orgullodominicano. Cierre con llamado a la unidad y la nostalgia positiva.</div>
          </div>
        </div>
        <div class="ac-foot"><span>Patriótico</span><span>Atardecer</span><span>Bandera</span><span>Emotivo</span><span>Testimonial</span></div>
      </div>

      <!-- Asset 5: Bachatero -->
      <div class="ap-acard">
        <div class="ac-head"><span class="ac-icon" style="color:var(--danger)">🎸</span><span class="ac-name">Bachatero Romántico</span></div>
        <div class="ac-body">
          <div class="ac-section">
            <div class="ac-label">Paleta de Colores</div>
            <div class="ac-text">
              <span class="ac-swatch" style="background:#800020"></span> #800020 Burdeos ·
              <span class="ac-swatch" style="background:#C0C0C0"></span> #C0C0C0 Plata ·
              <span class="ac-swatch" style="background:#1C1C1C"></span> #1C1C1C Negro profundo ·
              <span class="ac-swatch" style="background:#FF69B4"></span> #FF69B4 Rosa romántico ·
              <span class="ac-swatch" style="background:#FAEBD7"></span> #FAEBD7 Blanco antiguo
            </div>
          </div>
          <div class="ac-section">
            <div class="ac-label">Tipografía</div>
            <div class="ac-text"><strong>Títulos:</strong> Cormorant Garamond o Playfair Display (elegante, itálica) · <strong>Cuerpo:</strong> Inter Light · <strong>CTA:</strong> Ligera inclinación (italic), tono íntimo y personal</div>
          </div>
          <div class="ac-section">
            <div class="ac-label">Estilo de Imagen</div>
            <div class="ac-text">Imágenes románticas y melancólicas. Parejas en blanco y negro o con tonos fríos. Lluvia, atardeceres, faroles, guitarras. Textura de vinilo o disco. Iluminación low-key con foco direccional. Primeros planos de manos entrelazadas, rosas, cartas de amor.</div>
          </div>
          <div class="ac-section">
            <div class="ac-label">Estilo de Video</div>
            <div class="ac-text">Ritmo lento y cadencioso. Transiciones con fade y blur. La letra de la canción como overlay central. Close-ups de cuerdas de guitarra, voz, lágrimas. Edición tipo lyric video. Misma velocidad que el tempo de la bachata. CTA suave.</div>
          </div>
        </div>
        <div class="ac-foot"><span>Romántico</span><span>Melancólico</span><span>Guitarra</span><span>Elegante</span><span>Low-key</span></div>
      </div>

      <!-- Asset 6: Cristiano -->
      <div class="ap-acard">
        <div class="ac-head"><span class="ac-icon" style="color:var(--success)">🙏</span><span class="ac-name">Cristiano Espiritual</span></div>
        <div class="ac-body">
          <div class="ac-section">
            <div class="ac-label">Paleta de Colores</div>
            <div class="ac-text">
              <span class="ac-swatch" style="background:#F0E68C"></span> #F0E68C Luz dorada ·
              <span class="ac-swatch" style="background:#FFFFFF"></span> #FFFFFF Blanco pureza ·
              <span class="ac-swatch" style="background:#B0C4DE"></span> #B0C4DE Azul cielo claro ·
              <span class="ac-swatch" style="background:#8B7355"></span> #8B7355 Madera ·
              <span class="ac-swatch" style="background:#2F4F4F"></span> #2F4F4F Verde bosque
            </div>
          </div>
          <div class="ac-section">
            <div class="ac-label">Tipografía</div>
            <div class="ac-text"><strong>Títulos:</strong> Lora Bold o Cardo (serif clásica con carácter espiritual) · <strong>Cuerpo:</strong> Inter Regular · <strong>CTA:</strong> Suave, sin agresividad, tono de invitación</div>
          </div>
          <div class="ac-section">
            <div class="ac-label">Estilo de Imagen</div>
            <div class="ac-text">Luz natural suave. Amaneceres, atardeceres con rayos de sol. Manos alzadas en señal de alabanza. Iglesias, vitrales, montañas, naturaleza. Siluetas de personas con luz detrás. Composiciones simétricas (estilo renacentista). Saturación baja con tonos cálidos.</div>
          </div>
          <div class="ac-section">
            <div class="ac-label">Estilo de Video</div>
            <div class="ac-text">Ritmo pausado y contemplativo. Time-lapses de nubes y amaneceres. Transiciones lentas con cross-dissolve. Música de piano y cuerdas. Letras de alabanza en overlay con tipografía serif elegante. Cierre con frase de gratitud. Evitar CTA agresivos — priorizar "comparte esta bendición".</div>
          </div>
        </div>
        <div class="ac-foot"><span>Luz</span><span>Paz</span><span>Naturaleza</span><span>Piano</span><span>Serif</span></div>
      </div>

    </div>

    <!-- Dimensiones -->
    <div class="ap-st"><span class="hl">📐</span> Dimensiones y Especificaciones Técnicas</div>
    <div class="ap-dimensions">
      <div class="ap-dim"><span class="dm-label">Facebook Feed</span><span class="dm-value">1200×630 px</span></div>
      <div class="ap-dim"><span class="dm-label">Instagram Feed</span><span class="dm-value">1080×1080 px</span></div>
      <div class="ap-dim"><span class="dm-label">Instagram Stories</span><span class="dm-value">1080×1920 px</span></div>
      <div class="ap-dim"><span class="dm-label">Facebook Stories</span><span class="dm-value">1080×1920 px</span></div>
      <div class="ap-dim"><span class="dm-label">TikTok Video</span><span class="dm-value">1080×1920 px</span></div>
      <div class="ap-dim"><span class="dm-label">YouTube Thumbnail</span><span class="dm-value">1280×720 px</span></div>
      <div class="ap-dim"><span class="dm-label">YouTube Pre-roll</span><span class="dm-value">1920×1080 px</span></div>
      <div class="ap-dim"><span class="dm-label">Google Display</span><span class="dm-value">1200×628 px</span></div>
      <div class="ap-dim"><span class="dm-label">LinkedIn Feed</span><span class="dm-value">1200×627 px</span></div>
      <div class="ap-dim"><span class="dm-label">X (Twitter) Card</span><span class="dm-value">1200×675 px</span></div>
    </div>

    <!-- Inspiración / Mood -->
    <div class="ap-st"><span class="hl">🎬</span> Referencias de Estilo y Mood</div>
    <div class="ap-mood">
      <div class="ap-mood-item" style="border-left-color:var(--gold)">
        <div class="mm-label">🔥 Alta Energía (Fiesta)</div>
        <div class="mm-text">Videos de fiestas dominicanas con luces de colores, gente bailando en cámara lenta, confeti. Referencia: conciertos de merengue en vivo, videos de bodas dominicanas en YouTube.</div>
        <div class="mm-tags"><span class="mm-tag">Baile</span><span class="mm-tag">Luces</span><span class="mm-tag">Cámara lenta</span></div>
      </div>
      <div class="ap-mood-item" style="border-left-color:var(--pink)">
        <div class="mm-label">💔 Nostalgia Añeja</div>
        <div class="mm-text">Fotografía vintage estilo años 80, álbumes familiares, vinilos girando, cassettes. Filtro granuloso con colores desaturados. Referencia: documentales de música latina de los 80s.</div>
        <div class="mm-tags"><span class="mm-tag">Vinilo</span><span class="mm-tag">80s</span><span class="mm-tag">Sepia</span></div>
      </div>
      <div class="ap-mood-item" style="border-left-color:var(--cyan)">
        <div class="mm-label">🔮 TikTok Urbano</div>
        <div class="mm-text">Iluminación neón púrpura y cian, transiciones rápidas con efecto morph, texto grande en pantalla, música trending. Referencia: videos de baile latino en TikTok con >1M views.</div>
        <div class="mm-tags"><span class="mm-tag">Neón</span><span class="mm-tag">Morph</span><span class="mm-tag">Trending</span></div>
      </div>
      <div class="ap-mood-item" style="border-left-color:var(--accent)">
        <div class="mm-label">🌎 Diáspora Emotiva</div>
        <div class="mm-text">Atardeceres costeros, bandera dominicana ondeando, gente abrazándose en aeropuertos, llamadas por video. Referencia: anuncios de "Viva la República Dominicana" del Ministerio de Turismo.</div>
        <div class="mm-tags"><span class="mm-tag">Atardecer</span><span class="mm-tag">Bandera</span><span class="mm-tag">Emoción</span></div>
      </div>
      <div class="ap-mood-item" style="border-left-color:var(--success)">
        <div class="mm-label">🙏 Espiritual Sereno</div>
        <div class="mm-text">Luz de amanecer entrando por vitrales de iglesia, manos en oración, naturaleza en time-lapse, piano en sala vacía. Referencia: videos de alabanza cristiana con estilo cinematográfico.</div>
        <div class="mm-tags"><span class="mm-tag">Luz</span><span class="mm-tag">Paz</span><span class="mm-tag">Vitral</span></div>
      </div>
    </div>

    <div style="background:linear-gradient(135deg,rgba(167,139,250,0.06),rgba(167,139,250,0.02));border-left:2px solid var(--purple);padding:10px 14px;border-radius:0 var(--r) var(--r) 0;margin:8px 0;font-size:9px;color:var(--muted);line-height:1.6">
      <strong style="color:var(--text);">💡 Recomendación de producción:</strong> Crea un banco de assets (biblioteca de imágenes y videos) categorizado por segmento antes de lanzar campañas. Prioriza la producción de los segmentos Nostálgico y Fiestero (suman $23,480 yield/mes combinado). Usa herramientas como Canva para adaptar dimensiones rápidamente. Para video, prioriza formato vertical (9:16) sobre horizontal — el 80% del consumo es mobile.
    </div>

'''

# Insert the assets section after the Format Guide and before TAB 4
tab3_close = '  </div>\n\n  <!-- ════════════════════════════════════════════ -->\n  <!-- TAB 4: COPYS -->'
html = html.replace(tab3_close, assets_html + tab3_close)

with open('adspro-estrategia.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("✅ Assets section added successfully")
print(f"File size: {len(html)} bytes")
