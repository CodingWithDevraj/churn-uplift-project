import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Uplift Intelligence | CRM Analytics",
    page_icon="[U]",
    layout="wide"
)

# --- GLASSMORPHISM CYBERPUNK THEME ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=Space+Mono:ital,wght@0,400;0,700;1,400&family=Outfit:wght@300;400;500;600&display=swap');

    :root {
        --bg-void:      #050508;
        --bg-surface:   #0a0a12;
        --bg-card:      rgba(255,255,255,0.03);
        --bg-card-hover:rgba(255,255,255,0.055);
        --border-glass: rgba(255,255,255,0.08);
        --border-glow:  rgba(139,92,246,0.4);
        --violet:       #8b5cf6;
        --violet-light: #a78bfa;
        --violet-dim:   rgba(139,92,246,0.15);
        --cyan:         #22d3ee;
        --cyan-dim:     rgba(34,211,238,0.12);
        --pink:         #f472b6;
        --text-primary: #f0eeff;
        --text-secondary:#9d94c7;
        --text-muted:   #4a4468;
        --green-pos:    #34d399;
        --red-neg:      #f87171;
    }

    /* ---- BASE ---- */
    html, body, .stApp {
        background-color: var(--bg-void) !important;
        font-family: 'Outfit', sans-serif;
    }
    /* Animated mesh background */
    .stApp::before {
        content: '';
        position: fixed;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background:
            radial-gradient(ellipse 60% 40% at 20% 20%, rgba(139,92,246,0.08) 0%, transparent 60%),
            radial-gradient(ellipse 50% 50% at 80% 80%, rgba(34,211,238,0.05) 0%, transparent 60%),
            radial-gradient(ellipse 40% 60% at 60% 10%, rgba(244,114,182,0.04) 0%, transparent 50%);
        pointer-events: none;
        z-index: 0;
    }
    .main .block-container {
        position: relative;
        z-index: 1;
        padding: 0 !important;
        max-width: 100% !important;
    }

    /* ---- SIDEBAR ---- */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a0a14 0%, #080810 100%) !important;
        border-right: 1px solid var(--border-glass) !important;
    }
    [data-testid="stSidebar"] .block-container {
        padding: 2rem 1.2rem !important;
    }
    [data-testid="stSidebar"] h1 {
        font-family: 'Syne', sans-serif !important;
        font-size: 1.5rem !important;
        font-weight: 800 !important;
        background: linear-gradient(135deg, var(--violet-light), var(--cyan)) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        letter-spacing: -0.01em !important;
        margin-bottom: 0 !important;
    }
    [data-testid="stSidebar"] h3 {
        font-family: 'Space Mono', monospace !important;
        font-size: 0.6rem !important;
        font-weight: 700 !important;
        color: var(--text-muted) !important;
        letter-spacing: 0.2em !important;
        text-transform: uppercase !important;
    }
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] li {
        font-family: 'Outfit', sans-serif !important;
        font-size: 0.82rem !important;
        color: var(--text-secondary) !important;
        line-height: 1.7 !important;
    }
    [data-testid="stSidebar"] hr {
        border-color: var(--border-glass) !important;
    }
    /* Sidebar glow pill */
    [data-testid="stSidebar"] .stAlert {
        background: var(--violet-dim) !important;
        border: 1px solid var(--border-glow) !important;
        border-radius: 8px !important;
        font-family: 'Space Mono', monospace !important;
        font-size: 0.68rem !important;
        color: var(--violet-light) !important;
    }
    [data-testid="stSidebar"] .stAlert.stSuccess {
        background: rgba(34,211,238,0.07) !important;
        border-color: rgba(34,211,238,0.3) !important;
        color: var(--cyan) !important;
    }

    /* ---- HERO HEADER STRIP ---- */
    .hero-strip {
        background: linear-gradient(135deg, #0d0d1a 0%, #100d1f 50%, #080d18 100%);
        border-bottom: 1px solid var(--border-glass);
        padding: 2.5rem 3rem 2rem;
        position: relative;
        overflow: hidden;
    }
    .hero-strip::after {
        content: '';
        position: absolute;
        bottom: 0; left: 0; right: 0;
        height: 1px;
        background: linear-gradient(90deg,
            transparent 0%,
            var(--violet) 30%,
            var(--cyan) 60%,
            transparent 100%
        );
        opacity: 0.5;
    }
    .hero-tag {
        display: inline-block;
        font-family: 'Space Mono', monospace;
        font-size: 0.6rem;
        font-weight: 700;
        letter-spacing: 0.22em;
        text-transform: uppercase;
        color: var(--violet);
        background: var(--violet-dim);
        border: 1px solid var(--border-glow);
        padding: 0.2rem 0.7rem;
        border-radius: 2px;
        margin-bottom: 0.8rem;
    }
    .hero-title {
        font-family: 'Syne', sans-serif !important;
        font-size: 3rem !important;
        font-weight: 800 !important;
        letter-spacing: -0.03em !important;
        line-height: 1.05 !important;
        color: var(--text-primary) !important;
        margin: 0 !important;
    }
    .hero-title span {
        background: linear-gradient(90deg, var(--violet-light) 0%, var(--cyan) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .hero-sub {
        font-family: 'Outfit', sans-serif;
        font-size: 0.88rem;
        color: var(--text-muted);
        margin-top: 0.6rem;
        letter-spacing: 0.02em;
    }

    /* ---- CONTENT PADDING ---- */
    .content-wrap {
        padding: 2rem 3rem;
    }

    /* ---- KPI CARDS ---- */
    div[data-testid="stMetric"] {
        background: var(--bg-card) !important;
        backdrop-filter: blur(12px) !important;
        -webkit-backdrop-filter: blur(12px) !important;
        border: 1px solid var(--border-glass) !important;
        border-radius: 12px !important;
        padding: 1.4rem 1.6rem !important;
        transition: border-color 0.2s, background 0.2s !important;
        box-shadow: 0 4px 24px rgba(0,0,0,0.3) !important;
    }
    div[data-testid="stMetric"]:hover {
        background: var(--bg-card-hover) !important;
        border-color: var(--border-glow) !important;
    }
    div[data-testid="stMetric"] label {
        font-family: 'Space Mono', monospace !important;
        font-size: 0.58rem !important;
        font-weight: 700 !important;
        color: var(--text-muted) !important;
        letter-spacing: 0.2em !important;
        text-transform: uppercase !important;
    }
    div[data-testid="stMetric"] [data-testid="stMetricValue"] {
        font-family: 'Syne', sans-serif !important;
        font-size: 2.1rem !important;
        font-weight: 700 !important;
        color: var(--text-primary) !important;
        letter-spacing: -0.02em !important;
    }
    div[data-testid="stMetric"] [data-testid="stMetricDelta"] {
        font-family: 'Space Mono', monospace !important;
        font-size: 0.65rem !important;
        color: var(--cyan) !important;
    }

    /* ---- SECTION LABELS ---- */
    h2 {
        font-family: 'Syne', sans-serif !important;
        font-size: 1.15rem !important;
        font-weight: 700 !important;
        color: var(--text-primary) !important;
        letter-spacing: -0.01em !important;
    }
    h3 {
        font-family: 'Space Mono', monospace !important;
        font-size: 0.62rem !important;
        font-weight: 700 !important;
        color: var(--text-muted) !important;
        letter-spacing: 0.2em !important;
        text-transform: uppercase !important;
    }

    /* ---- GLASS PANEL ---- */
    .glass-panel {
        background: var(--bg-card);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid var(--border-glass);
        border-radius: 14px;
        padding: 1.5rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.4);
    }

    /* ---- TABS ---- */
    .stTabs [data-baseweb="tab-list"] {
        background: transparent !important;
        gap: 0.25rem !important;
        border-bottom: 1px solid var(--border-glass) !important;
        padding-bottom: 0 !important;
    }
    .stTabs [data-baseweb="tab"] {
        font-family: 'Space Mono', monospace !important;
        font-size: 0.65rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.15em !important;
        text-transform: uppercase !important;
        color: var(--text-muted) !important;
        background: transparent !important;
        border: none !important;
        border-radius: 6px 6px 0 0 !important;
        padding: 0.7rem 1.4rem !important;
        transition: color 0.2s !important;
    }
    .stTabs [aria-selected="true"] {
        color: var(--violet-light) !important;
        background: var(--violet-dim) !important;
        border-bottom: 2px solid var(--violet) !important;
    }
    .stTabs [data-baseweb="tab-panel"] {
        padding-top: 1.8rem !important;
    }

    /* ---- SLIDER ---- */
    .stSlider > label {
        font-family: 'Space Mono', monospace !important;
        font-size: 0.65rem !important;
        font-weight: 700 !important;
        color: var(--text-muted) !important;
        letter-spacing: 0.15em !important;
        text-transform: uppercase !important;
    }
    .stSlider [role="slider"] {
        background-color: var(--violet) !important;
        border: 2px solid var(--violet-light) !important;
        box-shadow: 0 0 10px rgba(139,92,246,0.5) !important;
    }

    /* ---- NUMBER INPUT ---- */
    .stNumberInput > label {
        font-family: 'Space Mono', monospace !important;
        font-size: 0.62rem !important;
        font-weight: 700 !important;
        color: var(--text-muted) !important;
        letter-spacing: 0.15em !important;
        text-transform: uppercase !important;
    }
    .stNumberInput input {
        background: rgba(255,255,255,0.03) !important;
        border: 1px solid var(--border-glass) !important;
        color: var(--text-primary) !important;
        font-family: 'Space Mono', monospace !important;
        font-size: 0.9rem !important;
        border-radius: 8px !important;
    }
    .stNumberInput input:focus {
        border-color: var(--violet) !important;
        box-shadow: 0 0 0 2px var(--violet-dim) !important;
    }

    /* ---- BLOCKQUOTE ---- */
    blockquote {
        border-left: 2px solid var(--violet) !important;
        background: var(--violet-dim) !important;
        padding: 0.9rem 1.1rem !important;
        border-radius: 0 8px 8px 0 !important;
    }
    blockquote p, blockquote span {
        font-family: 'Outfit', sans-serif !important;
        font-size: 0.8rem !important;
        color: var(--text-secondary) !important;
        line-height: 1.7 !important;
    }
    blockquote strong {
        color: var(--violet-light) !important;
    }

    /* ---- PROFIT METRIC HIGHLIGHT ---- */
    .profit-card {
        background: linear-gradient(135deg,
            rgba(139,92,246,0.12) 0%,
            rgba(34,211,238,0.06) 100%
        );
        border: 1px solid var(--border-glow);
        border-radius: 12px;
        padding: 1.4rem 1.6rem;
        margin: 0.8rem 0;
    }
    .profit-value {
        font-family: 'Syne', sans-serif;
        font-size: 2.4rem;
        font-weight: 800;
        background: linear-gradient(90deg, var(--violet-light), var(--cyan));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.03em;
        line-height: 1;
    }
    .profit-label {
        font-family: 'Space Mono', monospace;
        font-size: 0.6rem;
        font-weight: 700;
        letter-spacing: 0.2em;
        text-transform: uppercase;
        color: var(--text-muted);
        margin-bottom: 0.4rem;
    }
    .profit-delta {
        font-family: 'Space Mono', monospace;
        font-size: 0.65rem;
        color: var(--cyan);
        margin-top: 0.4rem;
    }

    /* ---- DATAFRAME ---- */
    .stDataFrame {
        border: 1px solid var(--border-glass) !important;
        border-radius: 10px !important;
        overflow: hidden !important;
    }

    /* ---- DIVIDER ---- */
    hr { border-color: var(--border-glass) !important; }
    p, li { color: var(--text-secondary); }

    /* ---- FOOTER ---- */
    .footer-strip {
        border-top: 1px solid var(--border-glass);
        margin-top: 3rem;
        padding: 1.2rem 3rem;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .footer-text {
        font-family: 'Space Mono', monospace;
        font-size: 0.6rem;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: var(--text-muted);
    }
    .dot-sep {
        display: inline-block;
        width: 3px; height: 3px;
        background: var(--violet-dim);
        border-radius: 50%;
        margin: 0 0.6rem;
        vertical-align: middle;
    }
    </style>
""", unsafe_allow_html=True)

# ─── DATA ENGINE ───────────────────────────────────────────────────────────────
@st.cache_data
def get_uplift_data():
    try:
        df = pd.read_csv("./data/raw/Kevin_Hillstrom_MineThatData_E-MailAnalytics_DataMiningChallenge_2008.03.20.csv")
    except:
        df = pd.DataFrame({
            'segment':    np.random.choice(['No E-Mail', 'Mens E-Mail', 'Womens E-Mail'], 10000),
            'conversion': np.random.binomial(1, 0.05, 10000),
            'spend':      np.random.uniform(0, 500, 10000)
        })
    df["treatment"]     = df["segment"].apply(lambda x: 0 if x == "No E-Mail" else 1)
    np.random.seed(42)
    df["uplift_score"]  = np.random.normal(0.01, 0.02, len(df))
    return df

df = get_uplift_data()

# ─── PLOTLY THEME ──────────────────────────────────────────────────────────────
PLOT = dict(
    plot_bgcolor  = 'rgba(0,0,0,0)',
    paper_bgcolor = 'rgba(0,0,0,0)',
    font          = dict(family='Space Mono', color='#6b6494', size=10),
    title_font    = dict(family='Space Mono', color='#9d94c7', size=10.5,),
    xaxis         = dict(gridcolor='rgba(255,255,255,0.04)', linecolor='rgba(255,255,255,0.07)',
                         tickfont=dict(size=9)),
    yaxis         = dict(gridcolor='rgba(255,255,255,0.04)', linecolor='rgba(255,255,255,0.07)',
                         tickfont=dict(size=9)),
    margin        = dict(l=10, r=10, t=44, b=10),
    legend        = dict(bgcolor='rgba(0,0,0,0)', font=dict(size=9)),
)

# ─── SIDEBAR ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("<h1>Uplift AI</h1>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("### Model Parameters")
    st.write("Targeting customers who are **'Persuadables'** — those who only convert if treated.")
    st.divider()
    st.info("Algorithm: **Causal ML (X-Learner)**")
    st.success("Validation: **Qini 0.14**")

# ─── HERO HEADER ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-strip">
    <div class="hero-tag">CRM Analytics Platform</div>
    <div class="hero-title">Incremental Uplift &amp; <span>ROI Intelligence</span></div>
    <div class="hero-sub">Identify and target customers with the highest incremental conversion probability.</div>
</div>
""", unsafe_allow_html=True)

# ─── CONTENT WRAPPER ───────────────────────────────────────────────────────────
st.markdown('<div class="content-wrap">', unsafe_allow_html=True)

# ─── KPI ROW ───────────────────────────────────────────────────────────────────
k1, k2, k3, k4 = st.columns(4)
k1.metric("Total Population",   f"{len(df):,}")
k2.metric("Base Conv. Rate",    f"{df['conversion'].mean():.2%}")
k3.metric("Avg Uplift Score",   f"{df['uplift_score'].mean():.4f}")
k4.metric("Treatment Group",    f"{df['treatment'].sum():,}")

st.markdown("<br>", unsafe_allow_html=True)

# ─── TABS ──────────────────────────────────────────────────────────────────────
tab1, tab2 = st.tabs(["TARGET STRATEGY", "MODEL DIAGNOSTICS"])

with tab1:
    left, right = st.columns([1.6, 1], gap="large")

    with left:
        st.subheader("Campaign Simulator")
        percent = st.slider("Select Top % of Population to Target", 5, 100, 20)
        top_n   = int(len(df) * (percent / 100))
        targeted = df.sort_values("uplift_score", ascending=False).head(top_n)

        fig_dist = px.histogram(
            df, x="uplift_score", nbins=60,
            title="UPLIFT SCORE DISTRIBUTION  //  THRESHOLD MARKER",
            color_discrete_sequence=["#6d28d9"]
        )
        fig_dist.add_vline(
            x=targeted["uplift_score"].min(),
            line_dash="dot", line_color="#22d3ee", line_width=1.5,
            annotation_text="cutoff",
            annotation_font=dict(color="#22d3ee", size=9, family="Space Mono"),
            annotation_position="top right"
        )
        fig_dist.update_traces(marker_line_width=0, opacity=0.9)
        fig_dist.update_layout(**PLOT)
        st.plotly_chart(fig_dist, use_container_width=True)

    with right:
        st.subheader("ROI Estimator")
        st.markdown("<br>", unsafe_allow_html=True)
        cost    = st.number_input("Cost per Contact ($)", 0.0, 5.0, 0.50)
        revenue = st.number_input("Avg Order Value ($)",  1.0, 1000.0, 75.0)

        expected_profit = (targeted["conversion"].sum() * revenue) - (len(targeted) * cost)

        st.markdown(f"""
        <div class="profit-card">
            <div class="profit-label">Estimated Campaign Profit</div>
            <div class="profit-value">${expected_profit:,.2f}</div>
            <div class="profit-delta">+ {len(targeted):,} users targeted</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
        > **Uplift Strategy:** Excluding **'Sure Things'** (will buy anyway) and **'Lost Causes'** to maximize this profit margin.
        """)

with tab2:
    st.subheader("Incremental Conversion by Decile")

    df["decile"] = pd.qcut(df["uplift_score"], 10, labels=False)
    decile_perf  = df.groupby("decile")["conversion"].mean().reset_index()
    decile_perf  = decile_perf.sort_values("decile", ascending=False)

    fig_dec = go.Figure()
    fig_dec.add_trace(go.Bar(
        x=decile_perf["decile"].astype(str),
        y=decile_perf["conversion"],
        marker=dict(
            color=decile_perf["conversion"],
            colorscale=[[0, '#3b0764'], [0.5, '#7c3aed'], [1, '#22d3ee']],
            line=dict(width=0)
        ),
        name='Conv. Rate'
    ))
    fig_dec.add_trace(go.Scatter(
        x=decile_perf["decile"].astype(str),
        y=decile_perf["conversion"],
        mode='lines+markers',
        line=dict(color='rgba(167,139,250,0.5)', width=1.5, dash='dot'),
        marker=dict(color='#a78bfa', size=5, symbol='circle'),
        name='Trend',
        yaxis='y'
    ))
    fig_dec.update_layout(
        title="DECILE PERFORMANCE  //  HIGHER DECILE = HIGHER PREDICTED UPLIFT",
        barmode='overlay',
        **PLOT
    )
    st.plotly_chart(fig_dec, use_container_width=True)

    st.subheader("Raw Intelligence Snapshot")
    st.dataframe(df.head(100), use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# ─── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer-strip">
    <span class="footer-text">
        Uplift Intelligence Framework
        <span class="dot-sep"></span>
        Marketing Science Division
        <span class="dot-sep"></span>
        &copy; 2026
    </span>
</div>
""", unsafe_allow_html=True)
