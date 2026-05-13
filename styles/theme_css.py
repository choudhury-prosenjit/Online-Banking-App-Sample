# Global theme CSS for inner pages
THEME_CSS = """
<style>
/* ---- Hide Streamlit chrome ---- */
#MainMenu, [data-testid="stHeader"], [data-testid="stToolbar"], footer {
    display: none !important;
}

/* ---- Base ---- */
html, body, [data-testid="stAppViewContainer"] {
    background-color: #f0f2f6;
    font-family: 'Segoe UI', sans-serif;
}

/* ---- Header bar ---- */
.bank-header {
    background: linear-gradient(90deg, #0a2342 0%, #1a3a6b 100%);
    color: #ffffff;
    padding: 18px 32px;
    border-radius: 0 0 8px 8px;
    margin-bottom: 24px;
    display: flex;
    align-items: center;
    gap: 16px;
}
.bank-header h1 {
    margin: 0;
    font-size: 1.8rem;
    font-weight: 700;
    letter-spacing: 1px;
}
.bank-header p {
    margin: 0;
    font-size: 0.9rem;
    opacity: 0.85;
}

/* ---- Cards ---- */
.card {
    background: #ffffff;
    border-radius: 10px;
    padding: 20px 24px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    margin-bottom: 16px;
}
.card-header {
    font-size: 0.78rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.8px;
    color: #6b7280;
    margin-bottom: 4px;
}
.card-title {
    font-size: 1.15rem;
    font-weight: 700;
    color: #0a2342;
    margin-bottom: 8px;
}
.account-number {
    font-family: 'Courier New', monospace;
    color: #374151;
    font-size: 0.95rem;
}
.balance-positive {
    color: #16a34a;
    font-size: 1.6rem;
    font-weight: 700;
}
.balance-negative {
    color: #dc2626;
    font-size: 1.6rem;
    font-weight: 700;
}
.label-small {
    font-size: 0.78rem;
    color: #6b7280;
    margin-bottom: 2px;
}
.value-medium {
    font-size: 1.05rem;
    font-weight: 600;
    color: #111827;
}

/* ---- Section titles ---- */
.section-title {
    font-size: 1.1rem;
    font-weight: 700;
    color: #0a2342;
    border-left: 4px solid #1a3a6b;
    padding-left: 10px;
    margin: 24px 0 12px 0;
}

/* ---- Status badges ---- */
.badge-green {
    background: #dcfce7;
    color: #16a34a;
    border-radius: 20px;
    padding: 2px 10px;
    font-size: 0.8rem;
    font-weight: 600;
}
.badge-blue {
    background: #dbeafe;
    color: #1d4ed8;
    border-radius: 20px;
    padding: 2px 10px;
    font-size: 0.8rem;
    font-weight: 600;
}

/* ---- Footer ---- */
.demo-footer {
    margin-top: 40px;
    padding: 14px 20px;
    background: #1e293b;
    color: #94a3b8;
    border-radius: 8px;
    font-size: 0.82rem;
    text-align: center;
}

/* ---- Login box ---- */
.login-box {
    max-width: 420px;
    margin: 40px auto;
    background: #ffffff;
    border-radius: 12px;
    padding: 40px 36px;
    box-shadow: 0 4px 24px rgba(0,0,0,0.12);
}

/* ---- Success / Error banners ---- */
.success-banner {
    background: #f0fdf4;
    border: 1px solid #86efac;
    border-radius: 8px;
    padding: 16px 20px;
    color: #16a34a;
    margin-bottom: 16px;
}
.error-banner {
    background: #fef2f2;
    border: 1px solid #fca5a5;
    border-radius: 8px;
    padding: 16px 20px;
    color: #dc2626;
    margin-bottom: 16px;
}

/* ---- Dataframe overrides ---- */
[data-testid="stDataFrame"] table {
    font-size: 0.88rem;
}

/* ---- Button hover contrast fix ---- */
/* Default (secondary) buttons — e.g. "View Details →" */
[data-testid="stButton"] > button {
    color: #0a2342 !important;
    background-color: #ffffff !important;
    border: 1px solid #d1d5db !important;
    font-weight: 500;
    transition: background-color 0.18s, color 0.18s, border-color 0.18s;
}

[data-testid="stButton"] > button:hover {
    background-color: #0a2342 !important;
    color: #ffffff !important;
    border-color: #0a2342 !important;
}

/* Primary buttons — e.g. "💸 Transfer Money with Zelle®" */
[data-testid="stButton"] > button[kind="primary"] {
    background-color: #0a2342 !important;
    color: #ffffff !important;
    border-color: #0a2342 !important;
}

[data-testid="stButton"] > button[kind="primary"]:hover {
    background-color: #1a3a6b !important;
    color: #ffffff !important;
    border-color: #1a3a6b !important;
}

/* ---- Form widget contrast fixes (Zelle & all inner pages) ---- */

/* Widget labels */
[data-testid="stWidgetLabel"] label,
[data-testid="stWidgetLabel"] p,
label[data-baseweb="label"] {
    color: #111827 !important;
    font-weight: 600 !important;
    font-size: 0.875rem !important;
}

/* ---- Selectbox — comprehensive selected-value contrast fix ---- */

/* The outer control box */
[data-testid="stSelectbox"] [data-baseweb="select"] > div:first-child {
    background-color: #ffffff !important;
    border: 1.5px solid #0B3C6D !important;
    border-radius: 6px !important;
}

/* Every text node inside the select control (covers singleValue, placeholder, input) */
[data-testid="stSelectbox"] [data-baseweb="select"] span,
[data-testid="stSelectbox"] [data-baseweb="select"] div,
[data-testid="stSelectbox"] [data-baseweb="select"] p,
[data-testid="stSelectbox"] [data-baseweb="select"] input,
[data-testid="stSelectbox"] [data-baseweb="select"] [class*="singleValue"],
[data-testid="stSelectbox"] [data-baseweb="select"] [class*="placeholder"],
[data-testid="stSelectbox"] [data-baseweb="select"] [class*="Input"],
[data-testid="stSelectbox"] [data-baseweb="select"] [data-testid="stMarkdownContainer"] p {
    color: #111827 !important;
    background-color: transparent !important;
}

/* Dropdown arrow icon — keep it dark */
[data-testid="stSelectbox"] [data-baseweb="select"] svg {
    fill: #374151 !important;
}

/* Dropdown menu container */
[data-baseweb="popover"],
[data-baseweb="menu"] {
    background-color: #ffffff !important;
    border: 1px solid #0B3C6D !important;
    border-radius: 6px !important;
    box-shadow: 0 4px 16px rgba(11,60,109,0.15) !important;
}

/* Each option in the dropdown */
[data-baseweb="popover"] [role="option"],
[data-baseweb="menu"] li,
[data-baseweb="menu"] [role="option"] {
    color: #111827 !important;
    background-color: #ffffff !important;
    font-size: 0.88rem !important;
}

/* Hovered option */
[data-baseweb="popover"] [role="option"]:hover,
[data-baseweb="menu"] li:hover,
[data-baseweb="menu"] [role="option"]:hover,
[data-baseweb="popover"] [aria-selected="true"],
[data-baseweb="menu"] [aria-selected="true"] {
    background-color: #DBEAFE !important;
    color: #0B3C6D !important;
    font-weight: 600 !important;
}

/* Number input */
[data-testid="stNumberInput"] input {
    color: #111827 !important;
    background-color: #ffffff !important;
    border: 1.5px solid #0B3C6D !important;
    border-radius: 6px !important;
    font-size: 0.9rem !important;
}
[data-testid="stNumberInput"] input:focus {
    border-color: #1565C0 !important;
    box-shadow: 0 0 0 3px rgba(11,60,109,0.10) !important;
}

/* Text input (non-login pages) — ensure dark typed text */
[data-testid="stTextInput"] input {
    color: #111827 !important;
    background-color: #ffffff !important;
    -webkit-text-fill-color: #111827 !important;
}
[data-testid="stTextInput"] input::placeholder {
    color: #6B7280 !important;
    -webkit-text-fill-color: #6B7280 !important;
    opacity: 1 !important;
}

/* Caption / helper text */
[data-testid="stCaptionContainer"] p {
    color: #374151 !important;
    font-size: 0.82rem !important;
}

/* Markdown headings on inner pages */
[data-testid="stMarkdownContainer"] h4 {
    color: #0a2342 !important;
    font-weight: 700 !important;
}

/* st.info / st.warning / st.error message text */
[data-testid="stAlert"] p {
    color: #1F2937 !important;
    font-weight: 500 !important;
}
</style>
"""
