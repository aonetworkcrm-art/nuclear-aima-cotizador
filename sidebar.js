// ── Sidebar Global Nuclear AIMA ──
// Inyecta sidebar + header dinámico en cualquier página que incluya este script

(function() {
  // ── CONFIG ──
  const SIDEBAR_WIDTH = 260;
  const SIDEBAR_COLLAPSED = 60;

  const navItems = [
    { section: 'Panel Principal', items: [
      { icon: '☢️', label: 'Dashboard', href: 'index.html', keywords: 'inicio dashboard principal centro comando' }
    ]},
    { section: 'Apps & Herramientas', items: [
      { icon: '📊', label: 'Cotizador', href: 'cotizador.html', keywords: 'cotizador presupuesto multi-key admin' },
      { icon: '🔍', label: 'Live Search Nodos', href: 'live-search.html', keywords: 'live search nodos virales fugas youtube' },
      { icon: '🕵️', label: 'OSINT Command Center', href: 'osint-center.html', keywords: 'osint dorking google keyword planner cpc domain traffic news discovery' },
      { icon: '🎬', label: 'Short Tracker', href: 'short-tracker.html', keywords: 'shorts tracker replicas virales youtube fan videos' },
      { icon: '💰', label: 'Adelantos', href: 'adelantos.html', keywords: 'adelantos financiamiento beatbread believe orchard sonosuite soundexchange' },
      { icon: '⭐', label: 'Master Plan', href: 'master-plan.html', keywords: 'master plan fases hoja ruta estrategia checklists' },
      { icon: '🔮', label: 'Oráculo en Vivo', href: 'oraculo.html', keywords: 'oráculo oracle yield canciones tiempo real top 12' },
      { icon: '📡', label: 'Streaming', href: 'streaming.html', keywords: 'streaming 24/7 youtube twitch facebook' },
      { icon: '🌐', label: 'Landing Page', href: 'landing-page.html', keywords: 'landing page aterrizaje leads' },
      { icon: '🧲', label: 'Lead Magnet', href: 'lead-magnet.html', keywords: 'lead magnet captación leads' }
    ]},
    { section: '🎵 Ramón Orlando', items: [
      { icon: '🏟️', label: '50 Aniversario', href: 'ramon-orlando/evento-50/ramon-orlando-50.html', keywords: '50 aniversario estadio olímpico evento' },
      { icon: '💿', label: 'Catálogo Completo', href: 'data/catalogo-completo-ramon-orlando.csv', keywords: 'catálogo albums canciones 190' },
      { icon: '📜', label: 'Contrato', href: 'ramon-orlando/CONTRATO%20DE%20ASESORAMIENTO%20ESTRAT%C3%89GI.txt', keywords: 'contrato asesoramiento legal' },
      { icon: '⭐', label: 'Pasos Estrella', href: 'ramon-orlando/PASOS%20ESTRELLA%20PARA%20SELLO%20INDEPENDIENTE%20DIRECTOR%20Y%20AGREGADOR%20DE%20CATALOGOS%20HISTORICOS/start.txt', keywords: 'pasos estrella sello independiente guía' },
      { icon: '🛡️', label: 'La Clave Registrar', href: 'ramon-orlando/PASOS%20ESTRELLA%20PARA%20SELLO%20INDEPENDIENTE%20DIRECTOR%20Y%20AGREGADOR%20DE%20CATALOGOS%20HISTORICOS/LA%20CLAVE%20PARA%20REGISTRAR%20Y%20SER%20INMUN.txt', keywords: 'clave registrar inmune protección' },
      { icon: '💰', label: 'Financiadoras', href: 'ramon-orlando/boveda%20de%20seguridad/financiadoras%20principales/financiadoras%20principales.txt', keywords: 'financiadoras beatbread adelantos' }
    ]},
    { section: '🏛️ Legal', items: [
      { icon: '🏛️', label: 'ONAPI · ONDA · SRL', href: 'onapi-onda.html', keywords: 'onapi onda srl registro legal fundación' }
    ]},
    { section: '📄 Biblioteca', items: [
      { icon: '📋', label: 'Propuesta Maestra', href: 'pdf/PROPUESTA-MAESTRA-NUCLEAR-AIMAtm.pdf', keywords: 'propuesta maestra nuclear aima' },
      { icon: '📘', label: 'Proyecto Ramón Orlando', href: 'pdf/Proyecto%20Ram%C3%B3n%20Orlando.pdf', keywords: 'proyecto ramón orlando plan' },
      { icon: '🚀', label: 'Hyperion Plan Maestro', href: 'pdf/Hyperion%20Systems%20-%20El%20Plan%20Maestro.pdf', keywords: 'hyperion plan maestro' },
      { icon: '🏛️', label: 'Plan Libertad y Legado', href: 'pdf/Plan%20Maestro%20Libertad%20y%20Legado.pdf', keywords: 'libertad legado plan maestro' },
      { icon: '💵', label: 'Estrategia Repago', href: 'pdf/Estrategia%20de%20Repago%20y%20Colateral%20-%20Ram%C3%B3n%20Orlando.pdf', keywords: 'repago colateral estrategia' },
      { icon: '🔥', label: 'Fórmula Viral 21', href: 'pdf/F%C3%B3rmula%20Viral%2021.pdf', keywords: 'fórmula viral 21 metodología' }
    ]},
    { section: '⚙️ Sistema', items: [
      { icon: '🔗', label: 'GitHub Repo', href: 'https://github.com/aonetworkcrm-art/nuclear-aima-cotizador', keywords: 'github repositorio código', external: true },
      { icon: '🗄️', label: 'Backend', href: '#', keywords: 'backend servidor' }
    ]}
  ];

  // ── BUILD SIDEBAR ──
  function buildSidebar() {
    // Sidebar container
    const sidebar = document.createElement('div');
    sidebar.id = 'nuclear-sidebar';
    sidebar.innerHTML = `
      <div class="ns-sidebar">
        <div class="ns-header">
          <div class="ns-logo">
            <span class="ns-logo-icon">☢️</span>
            <span class="ns-logo-text">Nuclear AIMA</span>
          </div>
          <button class="ns-toggle" id="nsToggle" title="Toggle sidebar">☰</button>
        </div>
        <div class="ns-search">
          <input type="text" id="nsSearch" placeholder="Buscar páginas..." autocomplete="off">
          <span class="ns-search-icon">🔍</span>
        </div>
        <div class="ns-results" id="nsResults"></div>
        <nav class="ns-nav" id="nsNav"></nav>
        <div class="ns-footer">
          <div class="ns-version">v2.0</div>
          <div class="ns-status online">● Online</div>
        </div>
      </div>
      <div class="ns-overlay" id="nsOverlay"></div>
    `;
    document.body.prepend(sidebar);

    // Build navigation
    const nav = document.getElementById('nsNav');
    navItems.forEach(group => {
      const section = document.createElement('div');
      section.className = 'ns-section';
      section.innerHTML = `<div class="ns-section-title">${group.section}</div>`;
      const list = document.createElement('div');
      list.className = 'ns-items';
      group.items.forEach(item => {
        const link = document.createElement('a');
        link.className = 'ns-item';
        link.href = item.href;
        if (item.external) link.target = '_blank';
        link.dataset.keywords = (item.keywords || '') + ' ' + item.label.toLowerCase();
        link.innerHTML = `
          <span class="ns-item-icon">${item.icon}</span>
          <span class="ns-item-label">${item.label}</span>
        `;
        // Highlight current page
        if (item.href === window.location.pathname.split('/').pop() || 
            (item.href === 'index.html' && window.location.pathname.endsWith('/'))) {
          link.classList.add('active');
        }
        list.appendChild(link);
      });
      section.appendChild(list);
      nav.appendChild(section);
    });

    // Toggle sidebar
    const toggle = document.getElementById('nsToggle');
    const overlay = document.getElementById('nsOverlay');
    toggle.addEventListener('click', () => {
      document.body.classList.toggle('ns-collapsed');
    });
    overlay.addEventListener('click', () => {
      document.body.classList.remove('ns-mobile-open');
    });

    // Search functionality
    const search = document.getElementById('nsSearch');
    const results = document.getElementById('nsResults');
    const allItems = nav.querySelectorAll('.ns-item');

    search.addEventListener('input', function() {
      const q = this.value.toLowerCase().trim();
      if (q.length < 2) {
        results.classList.remove('active');
        allItems.forEach(item => item.style.display = '');
        document.querySelectorAll('.ns-section').forEach(s => s.style.display = '');
        document.getElementById('nsNav').scrollTop = 0;
        return;
      }

      const matches = [];
      allItems.forEach(item => {
        const keywords = item.dataset.keywords || '';
        const label = item.querySelector('.ns-item-label').textContent.toLowerCase();
        if (keywords.includes(q) || label.includes(q)) {
          matches.push(item);
          item.style.display = '';
        } else {
          item.style.display = 'none';
        }
      });

      // Hide empty sections
      document.querySelectorAll('.ns-section').forEach(s => {
        const hasVisible = Array.from(s.querySelectorAll('.ns-item')).some(item => item.style.display !== 'none');
        if (hasVisible && q.length >= 2) {
          s.style.display = '';
        } else if (q.length >= 2) {
          s.style.display = 'none';
        } else {
          s.style.display = '';
        }
      });

      // Show search results popup
      if (matches.length > 0 && q.length >= 2) {
        results.innerHTML = matches.slice(0, 8).map(item => {
          const label = item.querySelector('.ns-item-label').textContent;
          const icon = item.querySelector('.ns-item-icon').textContent;
          const href = item.getAttribute('href');
          return `<a href="${href}" class="ns-result-item"><span class="ns-result-icon">${icon}</span>${label}</a>`;
        }).join('');
        results.classList.add('active');
      } else if (q.length >= 2) {
        results.innerHTML = '<div class="ns-result-empty">Sin resultados</div>';
        results.classList.add('active');
      } else {
        results.classList.remove('active');
      }
    });

    // Close search on click outside
    document.addEventListener('click', function(e) {
      if (!e.target.closest('.ns-search')) {
        results.classList.remove('active');
      }
    });

    // Add main content shift
    document.body.classList.add('ns-sidebar-ready');
  }

  // ── INJECT STYLES ──
  function injectStyles() {
    const styles = document.createElement('style');
    styles.textContent = `
      :root {
        --ns-width: ${SIDEBAR_WIDTH}px;
        --ns-collapsed-width: ${SIDEBAR_COLLAPSED}px;
        --ns-bg: #0f0f12;
        --ns-bg2: #16161a;
        --ns-bg3: #1e1e24;
        --ns-border: rgba(255,255,255,0.06);
        --ns-text: #e8e6e2;
        --ns-muted: #6b6966;
        --ns-accent: #c9a96e;
        --ns-hover: rgba(201,169,110,0.08);
        --ns-active: rgba(201,169,110,0.14);
        --ns-font: 'Inter', system-ui, sans-serif;
        --ns-mono: 'JetBrains Mono', 'Fira Code', monospace;
      }

      /* Main content shift */
      body.ns-sidebar-ready {
        margin-left: var(--ns-width);
        transition: margin-left 0.3s cubic-bezier(0.4, 0, 0.2, 1);
      }
      body.ns-collapsed {
        margin-left: var(--ns-collapsed-width);
      }

      /* Sidebar base */
      .ns-sidebar {
        position: fixed;
        top: 0;
        left: 0;
        width: var(--ns-width);
        height: 100vh;
        background: var(--ns-bg);
        border-right: 0.5px solid var(--ns-border);
        z-index: 1000;
        display: flex;
        flex-direction: column;
        transition: width 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        overflow: hidden;
      }
      body.ns-collapsed .ns-sidebar {
        width: var(--ns-collapsed-width);
      }

      /* Header / Logo */
      .ns-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 16px;
        border-bottom: 0.5px solid var(--ns-border);
        flex-shrink: 0;
      }
      .ns-logo {
        display: flex;
        align-items: center;
        gap: 10px;
        overflow: hidden;
        white-space: nowrap;
      }
      .ns-logo-icon {
        font-size: 22px;
        width: 32px;
        height: 32px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: linear-gradient(135deg, #c9a96e, #8b6c3a);
        border-radius: 8px;
        flex-shrink: 0;
      }
      .ns-logo-text {
        font-size: 14px;
        font-weight: 600;
        color: var(--ns-text);
        letter-spacing: -0.3px;
      }
      .ns-toggle {
        background: none;
        border: none;
        color: var(--ns-muted);
        font-size: 18px;
        cursor: pointer;
        padding: 4px;
        border-radius: 6px;
        transition: all 0.15s;
        flex-shrink: 0;
      }
      .ns-toggle:hover {
        background: var(--ns-hover);
        color: var(--ns-text);
      }
      body.ns-collapsed .ns-logo-text,
      body.ns-collapsed .ns-toggle { display: none; }

      /* Search */
      .ns-search {
        position: relative;
        padding: 12px 16px;
        flex-shrink: 0;
      }
      .ns-search input {
        width: 100%;
        background: var(--ns-bg2);
        border: 0.5px solid var(--ns-border);
        border-radius: 8px;
        padding: 9px 12px 9px 32px;
        color: var(--ns-text);
        font-size: 12px;
        font-family: var(--ns-font);
        outline: none;
        transition: border 0.15s;
      }
      .ns-search input:focus {
        border-color: var(--ns-accent);
      }
      .ns-search input::placeholder {
        color: var(--ns-muted);
      }
      .ns-search-icon {
        position: absolute;
        left: 24px;
        top: 50%;
        transform: translateY(-50%);
        font-size: 12px;
        pointer-events: none;
      }
      body.ns-collapsed .ns-search { display: none; }

      /* Search results popup */
      .ns-results {
        display: none;
        position: absolute;
        top: 100%;
        left: 12px;
        right: 12px;
        background: var(--ns-bg2);
        border: 0.5px solid var(--ns-border);
        border-radius: 8px;
        z-index: 100;
        max-height: 280px;
        overflow-y: auto;
        box-shadow: 0 8px 30px rgba(0,0,0,0.4);
      }
      .ns-results.active { display: block; }
      .ns-result-item {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 10px 14px;
        color: var(--ns-text);
        text-decoration: none;
        font-size: 12px;
        transition: background 0.1s;
        border-bottom: 0.5px solid rgba(255,255,255,0.03);
      }
      .ns-result-item:hover { background: var(--ns-hover); }
      .ns-result-item:last-child { border-bottom: none; }
      .ns-result-icon { font-size: 16px; }
      .ns-result-empty {
        padding: 20px;
        text-align: center;
        color: var(--ns-muted);
        font-size: 12px;
      }

      /* Navigation */
      .ns-nav {
        flex: 1;
        overflow-y: auto;
        overflow-x: hidden;
        padding: 8px 0;
      }
      .ns-nav::-webkit-scrollbar { width: 3px; }
      .ns-nav::-webkit-scrollbar-thumb { background: var(--ns-border); border-radius: 2px; }

      .ns-section { margin-bottom: 4px; }
      .ns-section-title {
        padding: 6px 16px;
        font-size: 9px;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: var(--ns-muted);
        font-weight: 500;
      }
      body.ns-collapsed .ns-section-title { display: none; }

      .ns-items { display: flex; flex-direction: column; }

      .ns-item {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 8px 16px;
        color: var(--ns-muted);
        text-decoration: none;
        font-size: 12px;
        transition: all 0.12s;
        border-left: 2px solid transparent;
        white-space: nowrap;
        overflow: hidden;
      }
      .ns-item:hover {
        background: var(--ns-hover);
        color: var(--ns-text);
      }
      .ns-item.active {
        background: var(--ns-active);
        color: var(--ns-accent);
        border-left-color: var(--ns-accent);
      }
      .ns-item-icon {
        font-size: 16px;
        width: 24px;
        text-align: center;
        flex-shrink: 0;
      }
      .ns-item-label {
        overflow: hidden;
        text-overflow: ellipsis;
      }
      body.ns-collapsed .ns-item-label { display: none; }
      body.ns-collapsed .ns-item { justify-content: center; padding: 10px 0; }

      /* Footer */
      .ns-footer {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 10px 16px;
        border-top: 0.5px solid var(--ns-border);
        flex-shrink: 0;
      }
      .ns-version {
        font-size: 10px;
        font-family: var(--ns-mono);
        color: var(--ns-muted);
      }
      .ns-status {
        font-size: 9px;
        display: flex;
        align-items: center;
        gap: 4px;
      }
      .ns-status.online { color: #4cad7c; }
      .ns-status::before {
        content: '';
        width: 6px;
        height: 6px;
        border-radius: 50%;
        display: inline-block;
      }
      .ns-status.online::before { background: #4cad7c; }
      body.ns-collapsed .ns-footer { flex-direction: column; gap: 4px; padding: 8px; }
      body.ns-collapsed .ns-version { font-size: 8px; }

      /* Overlay for mobile */
      .ns-overlay { display: none; }

      /* Responsive */
      @media (max-width: 768px) {
        body.ns-sidebar-ready {
          margin-left: 0 !important;
        }
        .ns-sidebar {
          transform: translateX(-100%);
          width: 280px !important;
        }
        body.ns-mobile-open .ns-sidebar {
          transform: translateX(0);
        }
        .ns-overlay {
          display: none;
          position: fixed;
          top: 0; left: 0; right: 0; bottom: 0;
          background: rgba(0,0,0,0.5);
          z-index: 999;
        }
        body.ns-mobile-open .ns-overlay {
          display: block;
        }
        /* Mobile hamburger button */
        .ns-mobile-hamburger {
          display: flex !important;
        }
      }

      /* Mobile hamburger (visible outside sidebar) */
      .ns-mobile-hamburger {
        display: none;
        position: fixed;
        top: 12px;
        left: 12px;
        z-index: 1001;
        width: 36px;
        height: 36px;
        align-items: center;
        justify-content: center;
        background: var(--ns-bg2);
        border: 0.5px solid var(--ns-border);
        border-radius: 8px;
        color: var(--ns-text);
        font-size: 18px;
        cursor: pointer;
        transition: all 0.15s;
      }
      .ns-mobile-hamburger:hover {
        background: var(--ns-bg3);
      }

      @media (min-width: 769px) {
        body.ns-collapsed .ns-item-icon { font-size: 18px; }
        body.ns-collapsed .ns-section-title { display: none; }
      }
    `;
    document.head.appendChild(styles);
  }

  // ── MOBILE HAMBURGER ──
  function addMobileHamburger() {
    const btn = document.createElement('button');
    btn.className = 'ns-mobile-hamburger';
    btn.id = 'nsMobileHamburger';
    btn.innerHTML = '☰';
    btn.addEventListener('click', () => {
      document.body.classList.toggle('ns-mobile-open');
    });
    document.body.prepend(btn);
  }

  // ── INIT ──
  injectStyles();
  buildSidebar();
  addMobileHamburger();
})();
