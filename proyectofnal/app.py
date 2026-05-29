import streamlit as st
import pandas as pd



# ── Configuración de página ──────────────────────────────────────────────────
st.set_page_config(
    page_title="Minería – Dashboard de Análisis",
    page_icon="⛏️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── CSS personalizado ────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
    /* ── Fuentes ── */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    /* ── Fondo general y sidebar ── */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #0d0d1a;
        font-family: 'Inter', sans-serif;
        color: #e0e0e0;
    }
    [data-testid="stSidebar"] {
        background-color: #12122a !important;
        border-right: 1px solid #1e1e3a;
        min-width: 220px !important;
        max-width: 220px !important;
    }
    [data-testid="stSidebar"] > div:first-child {
        padding: 1.5rem 1rem 1rem 1rem;
    }

    /* ── Logo / Título sidebar ── */
    .sidebar-logo {
        display: flex;
        align-items: center;
        gap: 8px;
        margin-bottom: 4px;
    }
    .sidebar-logo span.logo-icon {
        font-size: 1.4rem;
    }
    .sidebar-logo span.logo-text {
        font-size: 1.25rem;
        font-weight: 700;
        color: #f0397a;
        letter-spacing: 0.5px;
    }
    .sidebar-subtitle {
        font-size: 0.72rem;
        color: #7a7a9a;
        margin-bottom: 1.4rem;
        padding-left: 2px;
    }

    /* ── Sección NAVEGACIÓN ── */
    .nav-section-title {
        font-size: 0.65rem;
        font-weight: 600;
        letter-spacing: 1.5px;
        color: #555575;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
        padding-left: 4px;
    }

    /* ── Botones de navegación ── */
    div[data-testid="stSidebar"] .stButton > button {
        width: 100%;
        text-align: left;
        background: transparent;
        border: none;
        border-radius: 8px;
        color: #b0b0cc;
        font-size: 0.85rem;
        font-weight: 400;
        padding: 0.45rem 0.75rem;
        margin-bottom: 2px;
        cursor: pointer;
        transition: background 0.2s, color 0.2s;
    }
    div[data-testid="stSidebar"] .stButton > button:hover {
        background: #1e1e3a;
        color: #ffffff;
    }

    /* ── Botón activo (inyectado por clase) ── */
    .nav-active button {
        background: #f0397a !important;
        color: #ffffff !important;
        font-weight: 600 !important;
    }

    /* ── Sección FILTROS ── */
    .filter-section-title {
        font-size: 0.65rem;
        font-weight: 600;
        letter-spacing: 1.5px;
        color: #555575;
        text-transform: uppercase;
        margin-top: 1.4rem;
        margin-bottom: 0.5rem;
        padding-left: 4px;
    }
    .filter-label {
        font-size: 0.78rem;
        color: #9090b0;
        margin-bottom: 3px;
        padding-left: 2px;
    }

    /* ── Sliders y selectboxes ── */
    div[data-testid="stSidebar"] .stSlider > div { padding: 0; }
    div[data-testid="stSidebar"] .stSelectbox > div > div {
        background-color: #1a1a32 !important;
        border: 1px solid #2a2a48 !important;
        border-radius: 8px !important;
        color: #c0c0dc !important;
        font-size: 0.82rem !important;
    }
    div[data-testid="stSidebar"] [data-baseweb="select"] {
        background-color: #1a1a32 !important;
    }
    div[data-testid="stSidebar"] [data-baseweb="select"] * {
        background-color: #1a1a32 !important;
        color: #c0c0dc !important;
        font-size: 0.82rem !important;
    }

    /* ── Slider track & thumb ── */
    div[data-testid="stSidebar"] [data-testid="stSlider"] [role="slider"] {
        background-color: #f0397a !important;
    }
    div[data-testid="stSidebar"] [data-testid="stSlider"] div[data-testid="stTickBar"] {
        color: #7a7a9a;
        font-size: 0.7rem;
    }

    /* ── Cuadro "Acerca de" ── */
    .about-box {
        background: #1a1a32;
        border: 1px solid #2a2a48;
        border-radius: 10px;
        padding: 0.85rem 0.9rem;
        margin-top: 1.6rem;
        font-size: 0.75rem;
        color: #9090b0;
        line-height: 1.55;
    }
    .about-box .about-title {
        font-size: 0.8rem;
        font-weight: 600;
        color: #c0c0dc;
        margin-bottom: 0.45rem;
        display: flex;
        align-items: center;
        gap: 5px;
    }
    .about-box .about-source {
        margin-top: 0.7rem;
        font-size: 0.7rem;
        color: #666688;
    }
    .about-box .about-source span {
        color: #9090b0;
    }

    /* ── Ocultar elementos de Streamlit que no necesitamos ── */
    #MainMenu, footer, header { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Estado de navegación ─────────────────────────────────────────────────────
if "pagina_activa" not in st.session_state:
    st.session_state.pagina_activa = "Resumen"

# ── SIDEBAR ──────────────────────────────────────────────────────────────────
with st.sidebar:

    # Logo
    st.markdown(
        """
        <div class="sidebar-logo">
            <span class="logo-icon">⛏️</span>
            <span class="logo-text">Minería</span>
        </div>
        <div class="sidebar-subtitle">Dashboard de Análisis</div>
        """,
        unsafe_allow_html=True,
    )

    # ── NAVEGACIÓN ──────────────────────────────────────────────────────────
    st.markdown('<div class="nav-section-title">Navegación</div>', unsafe_allow_html=True)

    nav_items = [
        ("🏠", "Resumen"),
        ("⛏️", "Minería"),
        ("☰", "Categorías"),
        ("🛡️", "Formalización"),
        ("📍", "Puntos de Concentración"),
        ("📈", "Análisis"),
    ]

    for icono, nombre in nav_items:
        activo = st.session_state.pagina_activa == nombre
        clase = "nav-active" if activo else ""
        st.markdown(f'<div class="{clase}">', unsafe_allow_html=True)
        if st.button(f"{icono}  {nombre}", key=f"nav_{nombre}"):
            st.session_state.pagina_activa = nombre
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    # ── FILTROS ─────────────────────────────────────────────────────────────
    st.markdown('<div class="filter-section-title">Filtros</div>', unsafe_allow_html=True)

    # Rango de años
    st.markdown('<div class="filter-label">Rango de años</div>', unsafe_allow_html=True)
    anio_inicio, anio_fin = st.select_slider(
        label="rango_años",
        options=list(range(2010, 2025)),
        value=(2010, 2024),
        label_visibility="collapsed",
    )
    st.markdown(
        f'<div style="font-size:0.78rem;color:#c0c0dc;margin-bottom:10px;">'
        f'📅 {anio_inicio} – {anio_fin}</div>',
        unsafe_allow_html=True,
    )

    # Departamento
    st.markdown('<div class="filter-label">Departamento</div>', unsafe_allow_html=True)
    departamentos = [
        "Todos", "Antioquia", "Bolívar", "Boyacá", "Caldas", "Cauca",
        "Chocó", "Córdoba", "Cundinamarca", "Nariño", "Santander", "Tolima", "Vichada",
    ]
    departamento = st.selectbox(
        label="departamento",
        options=departamentos,
        index=0,
        label_visibility="collapsed",
    )

    # Categoría minera
    st.markdown('<div class="filter-label" style="margin-top:8px;">Categoría minera</div>', unsafe_allow_html=True)
    categorias = [
        "Todas",
        "Materiales de Construcción",
        "Energéticos",
        "Metales Preciosos",
        "Metales No Preciosos",
        "Otros Minerales",
    ]
    categoria = st.selectbox(
        label="categoria",
        options=categorias,
        index=0,
        label_visibility="collapsed",
    )

    # ── ACERCA DE ────────────────────────────────────────────────────────────
    st.markdown(
        """
        <div class="about-box">
            <div class="about-title">ℹ️ Acerca de</div>
            Análisis de la relación entre la actividad minera y los procesos
            de formalización en Colombia a nivel territorial.
            <div class="about-source">
                Fuente: <span>ANM, UPME, DANE</span><br>
                Última actualización: <span>Mayo 2024</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ── ÁREA PRINCIPAL (placeholder hasta siguientes pasos) ──────────────────────
st.markdown(
    f"""
    <div style="padding: 2rem; color: #7a7a9a; font-size: 0.9rem;">
        Página activa: <strong style="color:#f0397a;">{st.session_state.pagina_activa}</strong><br>
        Filtros: {anio_inicio}–{anio_fin} | {departamento} | {categoria}
    </div>
    """,
    unsafe_allow_html=True,
)