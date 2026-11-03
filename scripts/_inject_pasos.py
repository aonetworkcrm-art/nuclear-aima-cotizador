#!/usr/bin/env python3
import re

with open('master-plan.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The old content starts at <div class="tc" id="tab-pasos-estrella">
# and ends right before <div class="tc" id="tab-resources">

old_start = '<div class="tc" id="tab-pasos-estrella">'
old_end = '<div class="tc" id="tab-resources">'

# Find the exact positions
start_idx = html.find(old_start)
end_idx = html.find(old_end)

if start_idx == -1 or end_idx == -1:
    print("ERROR: Could not find tab-pasos-estrella boundaries")
    exit(1)

new_content = """<div class="tc" id="tab-pasos-estrella">

  <!-- ═══ HERO ═══ -->
  <div class="pe-hero">
    <div class="pe-badges">
      <span class="pe-badge gold">⭐ 4 PASOS</span>
      <span class="pe-badge">~$1,050 USD</span>
      <span class="pe-badge">~30 DÍAS</span>
      <span class="pe-badge cyan">BASE LEGAL</span>
    </div>
    <h2 class="pe-title">Pasos <span>Estrella</span></h2>
    <p class="pe-sub">El m\u00e9todo definitivo para fundar un sello independiente en Rep\u00fablica Dominicana. Cada paso depende del anterior. El orden es irrompible.</p>
  </div>

  <!-- ═══ FLOW NAV ═══ -->
  <div class="pe-flow" id="peFlow">
    <div class="pe-flow-step active" onclick="document.querySelector('.pe-step[data-step=\\'1\\']').classList.toggle('open');this.classList.toggle('active')" data-flow="1">
      <div class="pe-flow-num">1</div>
      <div class="pe-flow-label">ONAPI</div>
    </div>
    <div class="pe-flow-arrow">\u2192</div>
    <div class="pe-flow-step" onclick="document.querySelector('.pe-step[data-step=\\'2\\']').classList.toggle('open');this.classList.toggle('active')" data-flow="2">
      <div class="pe-flow-num">2</div>
      <div class="pe-flow-label">SAS</div>
    </div>
    <div class="pe-flow-arrow">\u2192</div>
    <div class="pe-flow-step" onclick="document.querySelector('.pe-step[data-step=\\'3\\']').classList.toggle('open');this.classList.toggle('active')" data-flow="3">
      <div class="pe-flow-num">3</div>
      <div class="pe-flow-label">ONDA</div>
    </div>
    <div class="pe-flow-arrow">\u2192</div>
    <div class="pe-flow-step" onclick="document.querySelector('.pe-step[data-step=\\'4\\']').classList.toggle('open');this.classList.toggle('active')" data-flow="4">
      <div class="pe-flow-num">4</div>
      <div class="pe-flow-label">Contrato</div>
    </div>
  </div>

  <!-- ═══ STEP 1: ONAPI ═══ -->
  <div class="pe-step" data-step="1">
    <div class="pe-step-header" onclick="this.parentElement.classList.toggle('open')">
      <div class="pe-step-icon">\U0001f3db\ufe0f</div>
      <div class="pe-step-info">
        <div class="pe-step-num">PASO 1 \u00b7 Semana 1</div>
        <h3 class="pe-step-title">Registrar Nombre Comercial en ONAPI</h3>
        <div class="pe-step-meta">
          <span class="pe-meta">RD$3,500\u2013RD$6,500</span>
          <span class="pe-meta">5\u201310 d\u00edas</span>
          <span class="pe-meta">Clase 41 + 35</span>
        </div>
      </div>
      <div class="pe-step-arrow">\u25bc</div>
    </div>
    <div class="pe-step-body">
      <p>La <strong>Oficina Nacional de la Propiedad Industrial</strong> es donde registras el nombre de tu sello como marca protegida en Rep\u00fablica Dominicana. El certificado de ONAPI es la primera prueba de que existes como entidad formal ante distribuidoras internacionales.</p>
      <div class="pe-detail-grid">
        <div class="pe-detail-item">
          <span class="pe-detail-label">\U0001f4cd D\u00f3nde</span>
          <span class="pe-detail-value"><strong>onapi.gob.do</strong> \u2014 Sistema E-SERPI en l\u00ednea. F\u00edsicamente en Av. Los Pr\u00f3ceres, Santo Domingo.</span>
        </div>
        <div class="pe-detail-item">
          <span class="pe-detail-label">\U0001f4cb Clases Cr\u00edticas</span>
          <span class="pe-detail-value"><strong>Clase 41</strong> \u2014 Producci\u00f3n musical, edici\u00f3n discogr\u00e1fica, gesti\u00f3n de entretenimiento.<br><strong>Clase 35</strong> \u2014 Gesti\u00f3n de negocios comerciales, administraci\u00f3n de activos intangibles.</span>
        </div>
        <div class="pe-detail-item">
          <span class="pe-detail-label">\U0001f4b0 Costo</span>
          <span class="pe-detail-value">RD$3,500 a RD$6,500 (~$60\u2013$110 USD) seg\u00fan modalidad. Registrar ambas clases cuesta lo mismo que una sola.</span>
        </div>
        <div class="pe-detail-item">
          <span class="pe-detail-label">\u23f1 Tiempo</span>
          <span class="pe-detail-value">5 d\u00edas h\u00e1biles para el certificado. Hasta 10 si hay revisi\u00f3n manual.</span>
        </div>
      </div>
      <div class="pe-tip"><strong>\U0001f4a1 Tip clave:</strong> Antes de pagar, busca en el portal de ONAPI si el nombre que elegiste ya est\u00e1 registrado. Elige un nombre que suene institucional en espa\u00f1ol e ingl\u00e9s: ej. <em>Antilles Music Group</em>, <em>Heritage Catalog Assets</em>, <em>Caribe Legacy Records</em>.</div>
    </div>
  </div>

  <!-- ═══ STEP 2: SAS/SRL ═══ -->
  <div class="pe-step" data-step="2">
    <div class="pe-step-header" onclick="this.parentElement.classList.toggle('open')">
      <div class="pe-step-icon">\U0001f3e2</div>
      <div class="pe-step-info">
        <div class="pe-step-num">PASO 2 \u00b7 Semanas 1\u20133</div>
        <h3 class="pe-step-title">Constituir la SAS (Sociedad por Acciones Simplificada)</h3>
        <div class="pe-step-meta">
          <span class="pe-meta">~RD$28,000</span>
          <span class="pe-meta">15\u201320 d\u00edas</span>
          <span class="pe-meta gold">\u2714 SAS > SRL</span>
        </div>
      </div>
      <div class="pe-step-arrow">\u25bc</div>
    </div>
    <div class="pe-step-body">
      <p>La estructura legal que separa tu patrimonio personal del de la empresa. Es el requisito para que distribuidoras internacionales firmen contratos contigo. <strong>En Rep\u00fablica Dominicana, la SAS (Sociedad por Acciones Simplificada) es superior a la SRL</strong> para proyectos de gesti\u00f3n de cat\u00e1logos musicales.</p>

      <div class="pe-compare-section" style="margin:8px 0;padding:12px">
        <h3>\U0001f48e SAS vs SRL: \u00bfCu\u00e1l elegir?</h3>
        <p>La SAS fue creada por la <strong>Ley 31-11</strong> y est\u00e1 dise\u00f1ada para empresas modernas, tecnol\u00f3gicas y con proyecci\u00f3n internacional. La SRL es un veh\u00edculo del siglo XX. Para un sello independiente que manejar\u00e1 activos digitales, contratos internacionales y tokenizaci\u00f3n, la SAS es la \u00fanica opci\u00f3n correcta.</p>
        <div class="pe-compare-grid">
          <div class="pe-compare-col loser">
            <div class="pe-compare-title">\u274c SRL (Soc. Responsabilidad Limitada)</div>
            <ul>
              <li>Requiere <strong>m\u00ednimo 2 socios</strong> para constituirse</li>
              <li>Transferencia de cuotas requiere asamblea y modificaci\u00f3n de estatutos</li>
              <li>Estructura de gobierno r\u00edgida definida por ley</li>
              <li>Menos atractiva para inversores internacionales</li>
              <li>Marco legal tradicional sin flexibilidad operativa</li>
              <li>No permite emisi\u00f3n de acciones para captar capital</li>
            </ul>
          </div>
          <div class="pe-compare-col winner">
            <div class="pe-compare-title">\u2714 SAS (Soc. por Acciones Simplificada)</div>
            <ul>
              <li><strong>1 solo socio es suficiente</strong> \u2014 control total</li>
              <li>Acciones transferibles libremente sin tr\u00e1mites complejos</li>
              <li>Flexibilidad total: los estatutos definen el gobierno corporativo</li>
              <li>Dise\u00f1ada para inversi\u00f3n extranjera y capital de riesgo</li>
              <li>Marco moderno (Ley 31-11) alineado con est\u00e1ndares internacionales</li>
              <li>Puede emitir acciones para inversionistas y tokenizaci\u00f3n futura</li>
            </ul>
          </div>
        </div>
      </div>

      <div class="pe-detail-grid" style="margin-top:8px">
        <div class="pe-detail-item">
          <span class="pe-detail-label">\U0001f4dd Objeto Social</span>
          <span class="pe-detail-value">Debe decir: <em>Distribuci\u00f3n digital, administraci\u00f3n, licenciamiento y explotaci\u00f3n comercial de fonogramas, cat\u00e1logos musicales y derechos conexos, desarrollo de infraestructura tecnol\u00f3gica</em>. Si es gen\u00e9rico, las distribuidoras cuestionar\u00e1n tu facultad legal.</span>
        </div>
        <div class="pe-detail-item">
          <span class="pe-detail-label">\U0001f3e6 Cuenta Bancaria</span>
          <span class="pe-detail-value"><strong>Abrirla inmediatamente despu\u00e9s del RNC.</strong> Banreservas y BHD Le\u00f3n manejan transferencias internacionales de regal\u00edas. Sin cuenta corporativa, no puedes recibir pagos de SoundExchange ni distribuidoras.</span>
        </div>
      </div>
      <div class="pe-tip"><strong>\U0001f4a1 Tip clave:</strong> El capital social m\u00ednimo legal es RD$100,000. Declara ese monto \u2014 pagas 1% de impuesto de constituci\u00f3n = RD$1,000. No declares m\u00e1s de lo necesario en esta etapa. Busca un abogado que haya constituido SAS antes, no es lo mismo que una SRL.</div>
    </div>
  </div>

  <!-- ═══ STEP 3: ONDA ═══ -->
  <div class="pe-step" data-step="3">
    <div class="pe-step-header" onclick="this.parentElement.classList.toggle('open')">
      <div class="pe-step-icon">\U0001f4dc</div>
      <div class="pe-step-info">
        <div class="pe-step-num">PASO 3 \u00b7 Semanas 2\u20134</div>
        <h3 class="pe-step-title">Registrar la SAS como Productor Fonogr\u00e1fico en ONDA</h3>
        <div class="pe-step-meta">
          <span class="pe-meta">RD$8,000\u2013RD$10,000</span>
          <span class="pe-meta">10\u201315 d\u00edas</span>
          <span class="pe-meta">\u26a0\ufe0f Productor Fonogr\u00e1fico</span>
        </div>
      </div>
      <div class="pe-step-arrow">\u25bc</div>
    </div>
    <div class="pe-step-body">
      <p><strong>Este es el paso que casi todos omiten y es el m\u00e1s poderoso.</strong> La mayor\u00eda sabe que la ONDA protege a los autores. Lo que no saben es que tambi\u00e9n reconoce a los <strong>Productores Fonogr\u00e1ficos</strong> \u2014 los due\u00f1os de las grabaciones (masters). Al registrar tu SAS bajo esta categor\u00eda, el Estado dominicano te reconoce formalmente como una entidad con facultad legal para poseer, distribuir y reclamar masters.</p>
      <p>Cuando YouTube recibe un reclamo de derechos de tu empresa respaldado por una certificaci\u00f3n de la ONDA, lo procesa con <strong>prioridad institucional</strong>.</p>
      <div class="pe-detail-grid">
        <div class="pe-detail-item">
          <span class="pe-detail-label">\U0001f4cd D\u00f3nde</span>
          <span class="pe-detail-value">Oficinas f\u00edsicas de la ONDA en Santo Domingo. Este tr\u00e1mite <strong>no se hace en l\u00ednea</strong>.</span>
        </div>
        <div class="pe-detail-item">
          <span class="pe-detail-label">\U0001f4c4 Documentos</span>
          <span class="pe-detail-value">RNC de la SAS, Registro Mercantil (C\u00e1mara de Comercio), certificado de ONAPI (Paso 1).</span>
        </div>
        <div class="pe-detail-item">
          <span class="pe-detail-label">\U0001f3af Solicitar</span>
          <span class="pe-detail-value"><strong>Productor Fonogr\u00e1fico</strong> \u2014 no como autor individual. Son categor\u00edas diferentes en la ONDA.</span>
        </div>
        <div class="pe-detail-item">
          <span class="pe-detail-label">\U0001f4b0 Costo</span>
          <span class="pe-detail-value">RD$8,000 a RD$10,000 (~$135\u2013$170 USD).</span>
        </div>
      </div>
      <div class="pe-tip"><strong>\U0001f4a1 El truco de la Obra Colectiva:</strong> En la misma visita, pregunta por el registro de <strong>Obra Colectiva</strong>. Registrar las 178 canciones como compilaci\u00f3n en lugar de una por una reduce el costo de <strong>RD$300,000 a menos de RD$10,000</strong>.</div>
    </div>
  </div>

  <!-- ═══ STEP 4: CONTRATO ═══ -->
  <div class="pe-step" data-step="4">
    <div class="pe-step-header" onclick="this.parentElement.classList.toggle('open')">
      <div class="pe-step-icon">\u270d\ufe0f</div>
      <div class="pe-step-info">
        <div class="pe-step-num">PASO 4 \u00b7 Semana 3</div>
        <h3 class="pe-step-title">Contrato Matriz de Administraci\u00f3n (Abogado Especializado)</h3>
        <div class="pe-step-meta">
          <span class="pe-meta">RD$15,000\u2013RD$18,000</span>
          <span class="pe-meta">3\u20135 d\u00edas</span>
          <span class="pe-meta">\u2714 Activo legal</span>
        </div>
      </div>
      <div class="pe-step-arrow">\u25bc</div>
    </div>
    <div class="pe-step-body">
      <p>Lo pagas una vez y lo usas con cada artista que incorpores al sello durante a\u00f1os. Es <strong>tu activo legal m\u00e1s valioso</strong>. Bien redactado, te protege ante cualquier disputa y le da al artista la certeza de que no te quedar\u00e1s con su m\u00fasica.</p>
      <div class="pe-detail-grid">
        <div class="pe-detail-item">
          <span class="pe-detail-label">\U0001f4cb Cl\u00e1usula 1</span>
          <span class="pe-detail-value"><strong>Mandato de Administraci\u00f3n Exclusiva</strong> \u2014 Poder para negociar distribuci\u00f3n, reclamar derechos, registrar ISRCs y administrar plataformas digitales.</span>
        </div>
        <div class="pe-detail-item">
          <span class="pe-detail-label">\U0001f4cb Cl\u00e1usula 2</span>
          <span class="pe-detail-value"><strong>Claim & Monetize</strong> \u2014 No eliminar videos de terceros. Solo reclamar la monetizaci\u00f3n. Protege el tr\u00e1fico org\u00e1nico hist\u00f3rico.</span>
        </div>
        <div class="pe-detail-item">
          <span class="pe-detail-label">\U0001f4cb Cl\u00e1usula 3</span>
          <span class="pe-detail-value"><strong>Split de Regal\u00edas</strong> \u2014 70% artista / 30% sello (fee de administraci\u00f3n). Para cat\u00e1logos muy valiosos, negociar 75/25.</span>
        </div>
        <div class="pe-detail-item">
          <span class="pe-detail-label">\U0001f4cb Cl\u00e1usula 4</span>
          <span class="pe-detail-value"><strong>Duraci\u00f3n 10 a\u00f1os</strong> \u2014 Con renovaci\u00f3n autom\u00e1tica. Protege tu inversi\u00f3n en digitalizaci\u00f3n y gesti\u00f3n del cat\u00e1logo.</span>
        </div>
        <div class="pe-detail-item">
          <span class="pe-detail-label">\U0001f4cb Cl\u00e1usula 5</span>
          <span class="pe-detail-value"><strong>Adelanto Recuperable</strong> \u2014 Cualquier adelanto al artista se recupera de las primeras regal\u00edas antes del split.</span>
        </div>
        <div class="pe-detail-item">
          <span class="pe-detail-label">\U0001f4cb Cl\u00e1usula 6</span>
          <span class="pe-detail-value"><strong>Explotaci\u00f3n Web3</strong> \u2014 Autorizaci\u00f3n expresa para tokenizaci\u00f3n, mercado secundario y activos digitales del cat\u00e1logo.</span>
        </div>
      </div>
      <div class="pe-tip"><strong>\U0001f4a1 Tip clave:</strong> Busca un abogado que haya trabajado con <strong>artistas o sellos discogr\u00e1ficos</strong>, no un corporativo general. La diferencia en calidad del contrato es enorme. La ONDA puede orientarte sobre especialistas en derecho de autor en el pa\u00eds.</div>
    </div>
  </div>

  <!-- ═══ BOTTLENECK ═══ -->
  <div class="pe-bottleneck">
    <div class="pe-bn-icon">\U0001f6a8</div>
    <div class="pe-bn-content">
      <div class="pe-bn-title">EL CUELLO DE BOTELLA \u2014 ORDEN IRROMPIBLE</div>
      <p><strong>ONAPI \u2192 SAS \u2192 RNC \u2192 Cuenta Bancaria \u2192 ONDA \u2192 Contrato \u2192 Pitch.</strong> No puedes ir a la ONDA como empresa sin el RNC. No puedes pedir el RNC sin el Registro Mercantil. No puedes hacer el Registro Mercantil sin un nombre de ONAPI registrado. Cada paso depende del anterior. Saltarse uno es perder semanas en devoluciones.</p>
    </div>
  </div>

  <!-- ═══ COMPARATIVA SAS ═══ -->
  <div class="pe-compare-section">
    <h3>\U0001f48e \u00bfPor qu\u00e9 SAS y no SRL? La explicaci\u00f3n definitiva</h3>
    <p>En Rep\u00fablica Dominicana existen dos figuras jur\u00eddicas para empresas privadas: la SRL (Sociedad de Responsabilidad Limitada, Ley 479-08) y la SAS (Sociedad por Acciones Simplificada, Ley 31-11). Aunque ambas limitan la responsabilidad personal, la SAS fue creada espec\u00edficamente para emprendimientos modernos, tecnol\u00f3gicos y con proyecci\u00f3n internacional.</p>
    <p><strong>Para un sello independiente que manejar\u00e1 activos digitales, contratos internacionales y tokenizaci\u00f3n Web3, la SAS es la \u00fanica opci\u00f3n correcta.</strong> La SRL fue dise\u00f1ada para negocios tradicionales (tiendas, restaurantes, servicios locales) donde no se espera inversi\u00f3n externa ni transferencia de participaciones. La SAS fue dise\u00f1ada para startups, scale-ups y empresas de propiedad intelectual.</p>
    <p>La diferencia decisiva: en una SRL, transferir las cuotas de participaci\u00f3n requiere modificar los estatutos ante la C\u00e1mara de Comercio. En una SAS, las acciones se transfieren con un simple endoso. Cuando llegue el momento de la LLC en Wyoming y la tokenizaci\u00f3n, la estructura de acciones de la SAS facilita la cesi\u00f3n de derechos de explotaci\u00f3n internacional sin fricci\u00f3n legal.</p>
    <div class="pe-compare-grid">
      <div class="pe-compare-col loser">
        <div class="pe-compare-title">\u274c SRL (Tradicional)</div>
        <ul>
          <li>M\u00ednimo <strong>2 socios</strong> requeridos</li>
          <li>Transferencia de cuotas requiere asamblea y modificaci\u00f3n de estatutos</li>
          <li>Estructura de gobierno r\u00edgida (Junta Directiva obligatoria)</li>
          <li>No puede emitir acciones para captar capital</li>
          <li>Marco legal tradicional sin flexibilidad operativa</li>
          <li>Requiere asamblea para cambios de administraci\u00f3n</li>
        </ul>
      </div>
      <div class="pe-compare-col winner">
        <div class="pe-compare-title">\u2714 SAS (Modern \u2014 Recomendada)</div>
        <ul>
          <li><strong>1 solo socio</strong> es suficiente \u2014 control total</li>
          <li>Acciones transferibles libremente sin tr\u00e1mites complejos</li>
          <li>Flexibilidad total: los estatutos definen el gobierno corporativo</li>
          <li>Puede emitir acciones para inversionistas y tokenizaci\u00f3n</li>
          <li>Marco moderno (Ley 31-11) alineado con est\u00e1ndares internacionales</li>
          <li>Cambios de administraci\u00f3n simples seg\u00fan estatutos</li>
        </ul>
      </div>
    </div>
    <div class="pe-sas-cta">\u2714 RECOMENDACI\u00d3N: Constituye una SAS, no una SRL. Tu abogado debe saber la diferencia.</div>
  </div>

  <!-- ═══ INVESTMENT SUMMARY ═══ -->
  <div class="pe-summary-card">
    <div class="pe-summary-header">
      <span class="icon">\U0001f4b0</span>
      <h3>Inversi\u00f3n Total Fase 1</h3>
      <span class="total-badge">~$1,050 USD</span>
    </div>
    <div style="overflow-x:auto">
      <table class="pe-summary-table">
        <thead>
          <tr>
            <th>#</th>
            <th>Paso</th>
            <th>Instituci\u00f3n</th>
            <th>Costo RD$</th>
            <th>Costo USD</th>
            <th>Tiempo</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1</td>
            <td>Nombre Comercial</td>
            <td>ONAPI</td>
            <td>RD$3,500\u20136,500</td>
            <td class="gold">~$100</td>
            <td>5\u201310 d\u00edas</td>
          </tr>
          <tr>
            <td>2</td>
            <td>Constituci\u00f3n SAS</td>
            <td>C\u00e1mara Comercio + DGII</td>
            <td>RD$24,000\u201330,000</td>
            <td class="gold">~$500</td>
            <td>15\u201320 d\u00edas</td>
          </tr>
          <tr>
            <td>3</td>
            <td>Productor Fonogr\u00e1fico</td>
            <td>ONDA</td>
            <td>RD$8,000\u201310,000</td>
            <td class="gold">~$150</td>
            <td>10\u201315 d\u00edas</td>
          </tr>
          <tr>
            <td>4</td>
            <td>Contrato Matriz</td>
            <td>Abogado Especializado</td>
            <td>RD$15,000\u201318,000</td>
            <td class="gold">~$300</td>
            <td>3\u20135 d\u00edas</td>
          </tr>
          <tr class="total">
            <td></td>
            <td><strong>TOTAL</strong></td>
            <td></td>
            <td><strong>~RD$52,000</strong></td>
            <td class="gold"><strong>~$1,050</strong></td>
            <td><strong>~30 d\u00edas</strong></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>

  <!-- ═══ COMPLETION ═══ -->
  <div class="pe-complete">
    <div class="pe-complete-icon">\U0001f3c6</div>
    <div class="pe-complete-content">
      <h4>\u2705 Al completar esta fase tienes</h4>
      <div class="pe-complete-items">
        <div class="pe-complete-item"><strong>1.</strong> Certificado de ONAPI \u2014 Tu nombre comercial protegido en RD</div>
        <div class="pe-complete-item"><strong>2.</strong> RNC y Registro Mercantil \u2014 Tu SAS existe legalmente</div>
        <div class="pe-complete-item"><strong>3.</strong> Certificaci\u00f3n ONDA \u2014 Facultad legal para administrar masters</div>
        <div class="pe-complete-item"><strong>4.</strong> Contrato Matriz firmado \u2014 T\u00e9rminos claros con cada artista</div>
      </div>
    </div>
  </div>

</div>"""

# Replace the entire tab content
new_html = html[:start_idx] + new_content + html[end_idx:]

with open('master-plan.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print(f"SUCCESS: Replaced tab-pasos-estrella content. New file size: {len(new_html)} bytes")
print(f"Old content was {end_idx - start_idx} bytes, new content is {len(new_content)} bytes")
