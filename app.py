"""
SecureBank Online Banking - Demo Application
=============================================
A Streamlit prototype for a fictional online banking system.
Uses mock/static data only. No real banking transactions are performed.

Run:
    pip install -r requirements.txt
    streamlit run app.py
"""

import random
import string
from datetime import date, timedelta

import pandas as pd
import streamlit as st

# ---------------------------------------------------------------------------
# Page configuration (must be first Streamlit call)
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="SecureBank Online Banking",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------------------------
# Login Page CSS – Enterprise Banking Theme
# ---------------------------------------------------------------------------
LOGIN_PAGE_CSS = """
<style>
/* ═══════════════════════════════════════════════════════════════════════════
   SECUREBANK — Enterprise Login Page
   ═══════════════════════════════════════════════════════════════════════════ */

/* --- Reset Streamlit chrome -------------------------------------------- */
#MainMenu, [data-testid="stHeader"], footer { display: none !important; }

[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    background: #EDF1F7 !important;
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, 'Helvetica Neue', sans-serif;
}

.main .block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* --- Top Navigation Bar ------------------------------------------------- */
.lb-topbar {
    background: linear-gradient(135deg, #071E3D 0%, #0B3C6D 55%, #0d4e8c 100%);
    padding: 0 36px;
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-shadow: 0 2px 20px rgba(7,30,61,0.45);
    position: relative;
    z-index: 100;
}

.lb-brand {
    display: flex;
    align-items: center;
    gap: 11px;
    text-decoration: none;
}

.lb-brand-icon { font-size: 1.75rem; line-height: 1; }

.lb-brand-name {
    font-size: 1.22rem;
    font-weight: 800;
    color: #FFFFFF;
    letter-spacing: 0.2px;
    line-height: 1.15;
}

.lb-brand-tagline {
    font-size: 0.59rem;
    color: rgba(255,255,255,0.48);
    letter-spacing: 2.2px;
    text-transform: uppercase;
    display: block;
    margin-top: 1px;
}

.lb-nav { display: flex; align-items: center; gap: 4px; }

.lb-nav-link {
    color: rgba(255,255,255,0.78) !important;
    text-decoration: none !important;
    font-size: 0.79rem;
    font-weight: 500;
    padding: 6px 13px;
    border-radius: 22px;
    transition: background 0.18s, color 0.18s, border-color 0.18s;
    border: 1px solid transparent;
    white-space: nowrap;
}

.lb-nav-link:hover {
    background: rgba(255,255,255,0.11);
    color: #fff !important;
    border-color: rgba(255,255,255,0.18);
}

.lb-nav-security {
    background: rgba(255,255,255,0.09);
    border-color: rgba(255,255,255,0.16);
}

/* --- Full-height columns layout ----------------------------------------- */
[data-testid="stHorizontalBlock"] {
    gap: 32px !important;
    align-items: stretch !important;
}

/* LEFT column — hero */
[data-testid="stHorizontalBlock"] > [data-testid="column"]:first-child {
    padding: 0 !important;
}

[data-testid="stHorizontalBlock"] > [data-testid="column"]:first-child
> [data-testid="stVerticalBlock"] {
    padding: 0 !important;
    gap: 0 !important;
    height: 100%;
}

/* RIGHT column — login card */
[data-testid="stHorizontalBlock"] > [data-testid="column"]:last-child {
    background: #EDF1F7 !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    padding: 28px 20px !important;
}

/* The stVerticalBlock inside the right column becomes the card */
[data-testid="stHorizontalBlock"] > [data-testid="column"]:last-child
> [data-testid="stVerticalBlock"] {
    background: #ffffff !important;
    border-radius: 18px !important;
    box-shadow:
        0 12px 52px rgba(11,60,109,0.13),
        0 2px 10px rgba(0,0,0,0.05) !important;
    border: 1px solid rgba(11,60,109,0.08) !important;
    padding: 28px 32px 24px !important;
    max-width: 460px !important;
    width: 100% !important;
    gap: 0 !important;
}

/* --- Hero Section -------------------------------------------------------- */
.lb-hero {
    background: linear-gradient(152deg, #071E3D 0%, #0B3C6D 48%, #0d5ea6 100%);
    padding: 40px 44px;
    min-height: auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
    position: relative;
    overflow: hidden;
    box-sizing: border-box;
}

.lb-hero-orb1 {
    position: absolute; top: -100px; right: -100px;
    width: 380px; height: 380px;
    background: radial-gradient(circle, rgba(25,140,220,0.16) 0%, transparent 68%);
    border-radius: 50%; pointer-events: none;
}

.lb-hero-orb2 {
    position: absolute; bottom: -120px; left: -70px;
    width: 400px; height: 400px;
    background: radial-gradient(circle, rgba(15,90,200,0.12) 0%, transparent 68%);
    border-radius: 50%; pointer-events: none;
}

.lb-hero-orb3 {
    position: absolute; top: 40%; right: 8%;
    width: 160px; height: 160px;
    background: radial-gradient(circle, rgba(80,200,255,0.08) 0%, transparent 70%);
    border-radius: 50%; pointer-events: none;
}

.lb-hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    background: rgba(255,255,255,0.09);
    border: 1px solid rgba(255,255,255,0.17);
    border-radius: 24px;
    padding: 5px 15px 5px 11px;
    font-size: 0.72rem;
    color: rgba(255,255,255,0.87);
    letter-spacing: 0.2px;
    margin-bottom: 34px;
    width: fit-content;
    position: relative; z-index: 1;
}

.lb-hero-title {
    font-size: 2.45rem;
    font-weight: 800;
    color: #ffffff;
    line-height: 1.21;
    margin-bottom: 18px;
    letter-spacing: -0.4px;
    position: relative; z-index: 1;
}

.lb-hero-title .acc { color: #52C8FF; }

.lb-hero-subtitle {
    font-size: 0.92rem;
    color: rgba(255,255,255,0.68);
    line-height: 1.72;
    margin-bottom: 42px;
    max-width: 390px;
    position: relative; z-index: 1;
}

.lb-features {
    display: flex;
    flex-direction: column;
    gap: 15px;
    margin-bottom: 46px;
    position: relative; z-index: 1;
}

.lb-feature {
    display: flex;
    align-items: center;
    gap: 14px;
    color: rgba(255,255,255,0.83);
    font-size: 0.86rem;
}

.lb-feature-icon {
    width: 36px; height: 36px;
    background: rgba(255,255,255,0.09);
    border: 1px solid rgba(255,255,255,0.14);
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.95rem;
    flex-shrink: 0;
}

.lb-stats {
    display: flex; gap: 32px;
    padding-top: 30px;
    border-top: 1px solid rgba(255,255,255,0.11);
    position: relative; z-index: 1;
}

.lb-stat-value {
    font-size: 1.5rem; font-weight: 800;
    color: #ffffff; display: block; line-height: 1.1;
}

.lb-stat-label {
    font-size: 0.67rem;
    color: rgba(255,255,255,0.52);
    text-transform: uppercase;
    letter-spacing: 1.1px;
    display: block; margin-top: 3px;
}

/* --- Card header (inside right column) ---------------------------------- */
.lb-card-top {
    text-align: center;
    margin-bottom: 16px;
    padding-top: 24px;
}

.lb-lock-wrap {
    width: 58px; height: 58px;
    background: linear-gradient(135deg, #0B3C6D 0%, #1565C0 100%);
    border-radius: 16px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.55rem;
    margin: 0 auto 16px;
    box-shadow: 0 5px 18px rgba(11,60,109,0.30);
}

.lb-card-title {
    font-size: 1.13rem;
    font-weight: 700;
    color: #0B3C6D;
    margin-bottom: 7px;
    letter-spacing: -0.15px;
}

.lb-card-subtitle {
    font-size: 0.8rem;
    color: #6B7280;
    line-height: 1.55;
}

/* --- Field labels -------------------------------------------------------- */
.lb-field-label {
    font-size: 0.79rem;
    font-weight: 600;
    color: #374151;
    display: block;
    margin-bottom: 5px;
    letter-spacing: 0.1px;
}

.lb-field-spacer { margin-top: 14px; }

/* --- Inline links row ---------------------------------------------------- */
.lb-links-row {
    display: flex;
    justify-content: flex-end;
    gap: 16px;
    margin: 8px 0 4px;
}

.lb-link {
    font-size: 0.76rem;
    color: #0B3C6D !important;
    text-decoration: none !important;
    font-weight: 500;
    transition: color 0.18s;
}

.lb-link:hover {
    color: #1565C0 !important;
    text-decoration: underline !important;
}

/* --- Alert banners ------------------------------------------------------- */
.lb-alert {
    border-radius: 9px;
    padding: 11px 14px;
    font-size: 0.82rem;
    font-weight: 500;
    margin-bottom: 16px;
    display: flex;
    align-items: flex-start;
    gap: 9px;
    line-height: 1.48;
}

.lb-alert-error {
    background: #FEF2F2;
    border: 1px solid #FECACA;
    border-left: 3px solid #DC2626;
    color: #991B1B;
}

/* --- Streamlit widget overrides ------------------------------------------ */

/* Hide auto-generated labels */
[data-testid="stTextInput"] > label { display: none !important; }

/* Input fields */
[data-testid="stTextInput"] input {
    border-radius: 0 !important;
    border: none !important;
    border-bottom: 1.5px solid #0B3C6D !important;
    padding: 10px 14px !important;
    font-size: 0.9rem !important;
    color: #111827 !important;
    background: #F9FAFB !important;
    transition: border-color 0.2s, box-shadow 0.2s, background 0.2s !important;
    box-shadow: none !important;
    outline: none !important;
    font-family: 'Segoe UI', sans-serif !important;
}

[data-testid="stTextInput"] input::placeholder { color: #9CA3AF !important; }

[data-testid="stTextInput"] input:focus {
    border-bottom-color: #1565C0 !important;
    box-shadow: none !important;
    background: #ffffff !important;
}

/* Remove red bottom border Streamlit sometimes adds */
[data-testid="stTextInput"] [data-baseweb="input"] {
    border: none !important;
    box-shadow: none !important;
}

/* Permanently hide the show/hide password eye toggle and collapse its space */
[data-testid="stTextInput"] button { display: none !important; }
[data-testid="stTextInput"] [data-baseweb="base-input"] { padding-right: 0 !important; }
[data-testid="stTextInput"] [data-baseweb="input-container"] { padding-right: 0 !important; }

/* Mask password field — renders identically to username but shows bullet dots */
[data-testid="stTextInput"] input[placeholder="Enter your password"] {
    -webkit-text-security: disc !important;
}

/* Sign In button */
[data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(135deg, #0B3C6D 0%, #1565C0 100%) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 0 !important;
    font-size: 0.94rem !important;
    font-weight: 600 !important;
    width: 100% !important;
    padding: 12px 20px !important;
    cursor: pointer !important;
    letter-spacing: 0.2px !important;
    box-shadow: 0 4px 16px rgba(11,60,109,0.30) !important;
    transition: all 0.22s ease !important;
    margin-top: 6px !important;
    font-family: 'Segoe UI', sans-serif !important;
}

[data-testid="stFormSubmitButton"] > button:hover {
    background: linear-gradient(135deg, #093260 0%, #1257a8 100%) !important;
    box-shadow: 0 6px 22px rgba(11,60,109,0.40) !important;
    transform: translateY(-1px) !important;
}

[data-testid="stFormSubmitButton"] > button:active {
    transform: translateY(0) !important;
    box-shadow: 0 2px 8px rgba(11,60,109,0.25) !important;
}

/* Checkbox */
[data-testid="stCheckbox"] { margin: 2px 0 10px !important; }
[data-testid="stCheckbox"] label {
    font-size: 0.8rem !important;
    color: #374151 !important;
    gap: 7px !important;
}

/* Form container — remove Streamlit's default border */
[data-testid="stForm"] {
    border: none !important;
    padding: 0 !important;
    background: transparent !important;
}

/* Reduce gap between elements inside card column */
[data-testid="stHorizontalBlock"] > [data-testid="column"]:last-child
[data-testid="stVerticalBlock"] > [data-testid="element-container"],
[data-testid="stHorizontalBlock"] > [data-testid="column"]:last-child
[data-testid="stVerticalBlock"] > [data-testid="stForm"] {
    margin-bottom: 0 !important;
}

/* Remove ALL vertical gaps inside the right card column */
[data-testid="stHorizontalBlock"] > [data-testid="column"]:last-child
> [data-testid="stVerticalBlock"] {
    gap: 0 !important;
}

/* Remove gaps inside the form's vertical block */
[data-testid="stForm"] > [data-testid="stVerticalBlock"] {
    gap: 0 !important;
}

/* Remove gaps inside the centering 3-column sub-layout */
[data-testid="stForm"] [data-testid="stHorizontalBlock"] {
    gap: 0 !important;
}
[data-testid="stForm"] [data-testid="column"] > [data-testid="stVerticalBlock"] {
    gap: 4px !important;
}

/* Strip default <p> margins Streamlit wraps markdown HTML in */
[data-testid="stHorizontalBlock"] > [data-testid="column"]:last-child p,
[data-testid="stForm"] p {
    margin: 0 !important;
    padding: 0 !important;
}

/* Remove bottom margin from text input wrappers */
[data-testid="stTextInput"] {
    margin-bottom: 0 !important;
}

/* --- Trust badges -------------------------------------------------------- */
.lb-trust {
    display: flex;
    justify-content: center;
    gap: 6px;
    flex-wrap: wrap;
    padding: 12px 0 0;
    border-top: 1px solid #F3F4F6;
    margin-top: 10px;
}

.lb-badge {
    display: flex; align-items: center; gap: 4px;
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-radius: 20px;
    padding: 4px 10px;
    font-size: 0.67rem;
    color: #4B5563;
    font-weight: 500;
    white-space: nowrap;
}

/* --- Demo environment card ----------------------------------------------- */
.lb-demo {
    background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%);
    border: 1px solid #BFDBFE;
    border-radius: 12px;
    padding: 14px 18px;
    margin-top: 14px;
}

.lb-demo-header {
    display: flex; align-items: center; gap: 7px;
    font-size: 0.67rem; font-weight: 700;
    color: #1D4ED8;
    text-transform: uppercase;
    letter-spacing: 1.3px;
    margin-bottom: 8px;
}

.lb-demo-desc {
    font-size: 0.73rem;
    color: #3B82F6;
    margin: 0 0 10px;
    line-height: 1.45;
}

.lb-demo-grid { display: flex; gap: 18px; }

.lb-demo-field-label {
    font-size: 0.64rem;
    color: #60A5FA;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 3px;
}

.lb-demo-field-value {
    font-family: 'Courier New', monospace;
    font-size: 0.88rem;
    font-weight: 700;
    color: #1E40AF;
    background: rgba(255,255,255,0.65);
    padding: 2px 9px;
    border-radius: 5px;
    display: inline-block;
    letter-spacing: 0.3px;
}

/* --- Page footer --------------------------------------------------------- */
.lb-page-footer {
    text-align: center;
    padding: 18px 24px;
    color: #9CA3AF;
    font-size: 0.69rem;
    line-height: 1.9;
    background: #E8ECF3;
    border-top: 1px solid #D5DAE4;
}

.lb-page-footer a { color: #6B7280 !important; text-decoration: none; }
.lb-page-footer a:hover { text-decoration: underline; }

/* --- Responsive ---------------------------------------------------------- */
@media (max-width: 900px) {
    .lb-topbar { padding: 0 18px; }
    .lb-nav-link { font-size: 0.74rem; padding: 5px 10px; }
    .lb-hero { padding: 40px 30px; min-height: auto; }
    .lb-hero-title { font-size: 1.9rem; }
    .lb-stats { gap: 20px; }
}

@media (max-width: 640px) {
    .lb-nav { display: none; }
    .lb-hero { padding: 30px 20px; }
    .lb-hero-title { font-size: 1.55rem; }
    [data-testid="stHorizontalBlock"] { flex-direction: column !important; }
    [data-testid="stHorizontalBlock"] > [data-testid="column"]:last-child {
        padding: 20px 14px !important;
    }
    [data-testid="stHorizontalBlock"] > [data-testid="column"]:last-child
    > [data-testid="stVerticalBlock"] { padding: 28px 22px 24px !important; }
}
</style>
"""

# ---------------------------------------------------------------------------
# Global CSS – professional bank-style theme
# ---------------------------------------------------------------------------
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

# ---------------------------------------------------------------------------
# Mock data
# ---------------------------------------------------------------------------

MOCK_CREDENTIALS = {
    "demo_user": "demo123",
}

MOCK_USER = {
    "username": "demo_user",
    "full_name": "Alex Johnson",
    "email": "alex.johnson@example.com",
    "phone": "(555) 867-5309",
    "member_since": "2018-03-14",
    "last_login": "May 12, 2026  10:22 AM",
}

MOCK_ACCOUNTS = [
    {
        "id": "chk_001",
        "type": "Checking Account",
        "masked_number": "****  ****  ****  4821",
        "full_number": "0042-1887-4821",
        "routing_number": "021000089",
        "available_balance": 4_752.38,
        "current_balance": 4_897.38,
        "status": "Active",
    },
    {
        "id": "sav_001",
        "type": "Savings Account",
        "masked_number": "****  ****  ****  7304",
        "full_number": "0042-3355-7304",
        "routing_number": "021000089",
        "available_balance": 18_320.00,
        "current_balance": 18_320.00,
        "status": "Active",
    },
    {
        "id": "mmk_001",
        "type": "Money Market Account",
        "masked_number": "****  ****  ****  9916",
        "full_number": "0042-9901-9916",
        "routing_number": "021000089",
        "available_balance": 52_640.75,
        "current_balance": 52_640.75,
        "status": "Active",
    },
]

MOCK_CREDIT_CARDS = [
    {
        "id": "cc_001",
        "type": "Platinum Rewards Credit Card",
        "masked_number": "****  ****  ****  3311",
        "current_balance": 1_284.55,
        "available_credit": 13_715.45,
        "credit_limit": 15_000.00,
        "minimum_payment": 35.00,
        "payment_due_date": "Jun 3, 2026",
    },
    {
        "id": "cc_002",
        "type": "Travel Plus Credit Card",
        "masked_number": "****  ****  ****  8847",
        "current_balance": 3_672.10,
        "available_credit": 6_327.90,
        "credit_limit": 10_000.00,
        "minimum_payment": 92.00,
        "payment_due_date": "Jun 7, 2026",
    },
]

# Helpers to build realistic transaction lists
def _rand_id():
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=10))


def _build_account_transactions(start_balance: float, count: int = 20) -> list[dict]:
    """Generate a descending list of mock account transactions."""
    entries = [
        ("Direct Deposit – Payroll", "Credit", 3_200.00),
        ("Amazon.com", "Debit", -78.44),
        ("Whole Foods Market", "Debit", -64.31),
        ("Netflix", "Debit", -17.99),
        ("Shell Gas Station", "Debit", -52.10),
        ("Venmo Payment Received", "Credit", 120.00),
        ("AT&T Wireless", "Debit", -89.00),
        ("Target", "Debit", -43.67),
        ("Starbucks", "Debit", -8.75),
        ("Rental Income", "Credit", 1_500.00),
        ("CVS Pharmacy", "Debit", -23.40),
        ("Spotify", "Debit", -9.99),
        ("Interest Earned", "Credit", 2.14),
        ("Online Transfer – Out", "Debit", -200.00),
        ("Cheesecake Factory", "Debit", -67.20),
        ("Apple iTunes", "Debit", -14.99),
        ("Uber", "Debit", -22.50),
        ("Costco", "Debit", -135.80),
        ("Direct Deposit – Bonus", "Credit", 500.00),
        ("Home Depot", "Debit", -89.95),
    ]
    transactions = []
    balance = start_balance
    today = date.today()
    for i, (desc, txn_type, amount) in enumerate(entries[:count]):
        txn_date = today - timedelta(days=i * 2)
        if txn_type == "Debit":
            balance -= abs(amount)
        else:
            balance += abs(amount)
        transactions.append(
            {
                "Date": txn_date.strftime("%b %d, %Y"),
                "Description": desc,
                "Type": txn_type,
                "Amount": f"{'−' if txn_type == 'Debit' else '+'}${abs(amount):,.2f}",
                "Balance": f"${balance:,.2f}",
            }
        )
    return transactions


def _build_cc_transactions(count: int = 20) -> list[dict]:
    """Generate a descending list of mock credit card transactions."""
    entries = [
        ("Delta Airlines", "Travel", 412.00, "Posted"),
        ("Marriott Hotels", "Travel", 289.50, "Posted"),
        ("Whole Foods Market", "Groceries", 88.73, "Posted"),
        ("Shell Gas Station", "Gas", 55.20, "Posted"),
        ("Amazon.com", "Shopping", 134.99, "Posted"),
        ("Cheesecake Factory", "Dining", 67.40, "Posted"),
        ("Starbucks", "Dining", 12.55, "Posted"),
        ("Apple Store", "Electronics", 199.00, "Posted"),
        ("Target", "Shopping", 73.15, "Posted"),
        ("Netflix", "Streaming", 17.99, "Posted"),
        ("Uber Eats", "Dining", 34.80, "Pending"),
        ("Home Depot", "Home", 95.60, "Posted"),
        ("CVS Pharmacy", "Health", 28.40, "Posted"),
        ("Spotify", "Streaming", 9.99, "Posted"),
        ("Costco", "Shopping", 245.30, "Posted"),
        ("Best Buy", "Electronics", 89.99, "Posted"),
        ("Panera Bread", "Dining", 18.75, "Posted"),
        ("Southwest Airlines", "Travel", 320.00, "Pending"),
        ("Nordstrom", "Shopping", 152.00, "Posted"),
        ("Hilton Hotels", "Travel", 215.00, "Posted"),
    ]
    transactions = []
    today = date.today()
    for i, (merchant, category, amount, status) in enumerate(entries[:count]):
        txn_date = today - timedelta(days=i * 2)
        transactions.append(
            {
                "Date": txn_date.strftime("%b %d, %Y"),
                "Merchant": merchant,
                "Category": category,
                "Amount": f"${amount:,.2f}",
                "Status": status,
            }
        )
    return transactions


MOCK_ACCOUNT_TRANSACTIONS: dict[str, list[dict]] = {
    acc["id"]: _build_account_transactions(acc["current_balance"])
    for acc in MOCK_ACCOUNTS
}

MOCK_CC_TRANSACTIONS: dict[str, list[dict]] = {
    card["id"]: _build_cc_transactions() for card in MOCK_CREDIT_CARDS
}

INITIAL_ZELLE_RECIPIENTS = [
    {"name": "Maria Garcia", "contact": "maria.garcia@example.com", "nickname": "Maria"},
    {"name": "David Kim", "contact": "(555) 321-7654", "nickname": "David"},
    {"name": "Sarah Chen", "contact": "sarah.chen@example.com", "nickname": "Sarah"},
]

# ---------------------------------------------------------------------------
# Session-state initialization
# ---------------------------------------------------------------------------

def init_session_state():
    defaults = {
        "authenticated": False,
        "current_page": "login",
        "selected_account_id": None,
        "selected_card_id": None,
        "zelle_recipients": INITIAL_ZELLE_RECIPIENTS.copy(),
        "transfer_confirmation": None,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


# ---------------------------------------------------------------------------
# Transaction table styling helper
# ---------------------------------------------------------------------------

_TABLE_STYLES = [
    # Header — deep navy with crisp white text
    {"selector": "thead th", "props": [
        ("background-color", "#0B3C6D"),
        ("color", "#FFFFFF"),
        ("font-weight", "700"),
        ("font-size", "0.76rem"),
        ("text-transform", "uppercase"),
        ("letter-spacing", "0.7px"),
        ("padding", "12px 16px"),
        ("border-bottom", "3px solid #1565C0"),
        ("white-space", "nowrap"),
    ]},
    # Odd rows — clean white
    {"selector": "tbody tr:nth-child(odd) td", "props": [
        ("background-color", "#FFFFFF"),
        ("color", "#1F2937"),
    ]},
    # Even rows — soft cerulean tint for clear alternation
    {"selector": "tbody tr:nth-child(even) td", "props": [
        ("background-color", "#E8F0FE"),
        ("color", "#1F2937"),
    ]},
    # All cells — consistent padding, font size, and subtle row divider
    {"selector": "tbody td", "props": [
        ("font-size", "0.875rem"),
        ("padding", "10px 16px"),
        ("border-bottom", "1px solid #C7D7F0"),
    ]},
    # Hover — vivid blue highlight for interactivity feedback
    {"selector": "tbody tr:hover td", "props": [
        ("background-color", "#BFDBFE"),
        ("color", "#0B3C6D"),
    ]},
    # Table base
    {"selector": "table", "props": [
        ("border-collapse", "collapse"),
        ("width", "100%"),
    ]},
]


def styled_table(df: pd.DataFrame):
    """Return a pandas Styler with banking-themed header and alternating rows."""
    return df.style.set_table_styles(_TABLE_STYLES).hide(axis="index")


# ---------------------------------------------------------------------------
# Shared UI helpers
# ---------------------------------------------------------------------------

def render_header(subtitle: str = ""):
    st.markdown(THEME_CSS, unsafe_allow_html=True)
    sub_html = f"<p>{subtitle}</p>" if subtitle else ""
    st.markdown(
        f"""
        <div class="bank-header">
            <div>🏦</div>
            <div>
                <h1>SecureBank</h1>
                {sub_html}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_footer():
    st.markdown(
        """
        <div class="demo-footer">
            🔒 This is a demo banking application using mock data only.
            No real banking transactions are performed.
        </div>
        """,
        unsafe_allow_html=True,
    )


def navigate(page: str, **kwargs):
    """Set the current page and optional state kwargs."""
    st.session_state["current_page"] = page
    for k, v in kwargs.items():
        st.session_state[k] = v
    st.rerun()


def fmt_currency(amount: float) -> str:
    return f"${amount:,.2f}"


# ---------------------------------------------------------------------------
# 1. Login Page  (Enterprise redesign)
# ---------------------------------------------------------------------------

def login_page():
    # Inject login-specific CSS (no THEME_CSS / render_header here)
    st.markdown(LOGIN_PAGE_CSS, unsafe_allow_html=True)

    # ── Top Navigation Bar ────────────────────────────────────────────────────
    # NOTE: .strip() on every HTML string is required — CommonMark treats any
    # line with 4+ leading spaces as a code block, which would print raw HTML.
    st.markdown("""
<div class="lb-topbar">
    <div class="lb-brand">
        <span class="lb-brand-icon">🏦</span>
        <div>
            <span class="lb-brand-name">SecureBank</span>
            <span class="lb-brand-tagline">Financial Services</span>
        </div>
    </div>
    <nav class="lb-nav">
        <a href="#" class="lb-nav-link">Help</a>
        <a href="#" class="lb-nav-link">Contact Us</a>
        <a href="#" class="lb-nav-link lb-nav-security">🔒 Security Center</a>
    </nav>
</div>
""".strip(), unsafe_allow_html=True)

    # ── Two-column layout ─────────────────────────────────────────────────────
    hero_col, form_col = st.columns([1.05, 0.95], gap="small")

    # ── LEFT: Hero panel ──────────────────────────────────────────────────────
    with hero_col:
        st.markdown("""
<div class="lb-hero">
    <div class="lb-hero-orb1"></div>
    <div class="lb-hero-orb2"></div>
    <h1 class="lb-hero-title">
        Bank smarter,<br>
        <span class="acc">securely</span> and<br>
        confidently.
    </h1>
    <p class="lb-hero-subtitle">
        Enterprise-grade security, real-time monitoring,
        and seamless access to all your accounts.
    </p>
    <div class="lb-features">
        <div class="lb-feature">
            <div class="lb-feature-icon">🔐</div>
            <span>256-bit SSL encryption on every transaction</span>
        </div>
        <div class="lb-feature">
            <div class="lb-feature-icon">⚡</div>
            <span>Real-time fraud detection &amp; 24/7 monitoring</span>
        </div>
        <div class="lb-feature">
            <div class="lb-feature-icon">🏛️</div>
            <span>FDIC insured up to $250,000 per depositor</span>
        </div>
    </div>
</div>
""".strip(), unsafe_allow_html=True)

    # ── RIGHT: Login card ─────────────────────────────────────────────────────
    with form_col:

        # Card Header
        st.markdown("""
<div class="lb-card-top">
    <div class="lb-lock-wrap">🔒</div>
    <div class="lb-card-title">Secure Online Banking Sign In</div>
    <div class="lb-card-subtitle">
        Enter your credentials to securely access your account.
    </div>
</div>
""".strip(), unsafe_allow_html=True)

        # Error banner (shown after a failed login attempt)
        if st.session_state.get("login_error"):
            st.markdown("""
<div class="lb-alert lb-alert-error">
    <span>⚠️</span>
    <span>Invalid username or password. Please verify your credentials and try again.</span>
</div>
""".strip(), unsafe_allow_html=True)

        # ── Login form ────────────────────────────────────────────────────────
        with st.form("login_form", clear_on_submit=False):

            # Use <div> not <label> — inline elements like <label> can be
            # misidentified by the Markdown renderer and printed as raw text.
            _l, col_form, _r = st.columns([0.125, 0.75, 0.125])
            with col_form:
                st.markdown('<div class="lb-field-label">Username</div>', unsafe_allow_html=True)
                username = st.text_input(
                    "Username", placeholder="Enter your username",
                    label_visibility="collapsed", key="li_username",
                )

                st.markdown('<div class="lb-field-label lb-field-spacer">Password</div>', unsafe_allow_html=True)
                password = st.text_input(
                    "Password", placeholder="Enter your password",
                    label_visibility="collapsed", key="li_password",
                )

                # Forgot links
                st.markdown("""
<div class="lb-links-row">
    <a href="#" class="lb-link">Forgot Username?</a>
    <a href="#" class="lb-link">Forgot Password?</a>
</div>
""".strip(), unsafe_allow_html=True)

                submitted = st.form_submit_button(
                    "🔑  Sign In to Your Account", use_container_width=True
                )

        # ── Authentication logic (unchanged) ──────────────────────────────────
        if submitted:
            if MOCK_CREDENTIALS.get(username) == password:
                st.session_state["login_error"] = False
                st.session_state["authenticated"] = True
                navigate("dashboard")
            else:
                st.session_state["login_error"] = True
                st.rerun()

        # Trust badges
        st.markdown("""
<div class="lb-trust">
    <div class="lb-badge">🏛️ FDIC Insured</div>
    <div class="lb-badge">🔒 SSL Secured</div>
    <div class="lb-badge">🛡️ 256-bit Encryption</div>
    <div class="lb-badge">👁️ Fraud Monitoring</div>
</div>
""".strip(), unsafe_allow_html=True)



    # ── Page footer ───────────────────────────────────────────────────────────
    st.markdown("""
<div class="lb-page-footer">
    © 2026 SecureBank Financial Services · All Rights Reserved
    &nbsp;|&nbsp;<a href="#">Privacy Policy</a>
    &nbsp;|&nbsp;<a href="#">Terms of Service</a>
    &nbsp;|&nbsp;<a href="#">Accessibility Statement</a>
    &nbsp;|&nbsp;<a href="#">FDIC Notice</a><br>
    Member FDIC · Equal Housing Lender · Deposits insured up to $250,000 per depositor ·
    This is a demo application — no real banking services are provided.
</div>
""".strip(), unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# 2. Dashboard Page
# ---------------------------------------------------------------------------

def dashboard_page():
    render_header(subtitle=f"Welcome, {MOCK_USER['full_name']}  |  Last Login: {MOCK_USER['last_login']}")

    # ── Top action bar ──────────────────────────────────────────────────────
    col_logout, _, col_zelle = st.columns([1, 4, 1.5])
    with col_logout:
        if st.button("🚪 Sign Out", use_container_width=True):
            st.session_state["authenticated"] = False
            navigate("login")
    with col_zelle:
        if st.button("💸 Transfer Money with Zelle®", use_container_width=True, type="primary"):
            navigate("zelle_transfer")

    # ── Accounts section ────────────────────────────────────────────────────
    st.markdown('<div class="section-title">My Bank Accounts</div>', unsafe_allow_html=True)

    for acc in MOCK_ACCOUNTS:
        with st.container():
            col1, col2, col3, col4 = st.columns([2.5, 1.5, 1.5, 1])
            with col1:
                st.markdown(
                    f"""
                    <div>
                        <div class="card-header">{acc["type"]}</div>
                        <div class="account-number">{acc["masked_number"]}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with col2:
                st.markdown(
                    f'<div class="label-small">Available Balance</div>'
                    f'<div class="balance-positive">{fmt_currency(acc["available_balance"])}</div>',
                    unsafe_allow_html=True,
                )
            with col3:
                st.markdown(
                    f'<div class="label-small">Current Balance</div>'
                    f'<div class="value-medium">{fmt_currency(acc["current_balance"])}</div>',
                    unsafe_allow_html=True,
                )
            with col4:
                if st.button("View Details →", key=f"acc_{acc['id']}", use_container_width=True):
                    navigate("account_details", selected_account_id=acc["id"])
            st.markdown("---")

    # ── Credit Cards section ─────────────────────────────────────────────────
    st.markdown('<div class="section-title">My Credit Cards</div>', unsafe_allow_html=True)

    for card in MOCK_CREDIT_CARDS:
        with st.container():
            col1, col2, col3, col4, col5 = st.columns([2.5, 1.5, 1.5, 1.5, 1])
            with col1:
                st.markdown(
                    f"""
                    <div>
                        <div class="card-header">{card["type"]}</div>
                        <div class="account-number">{card["masked_number"]}</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with col2:
                st.markdown(
                    f'<div class="label-small">Current Balance</div>'
                    f'<div class="balance-negative">{fmt_currency(card["current_balance"])}</div>',
                    unsafe_allow_html=True,
                )
            with col3:
                st.markdown(
                    f'<div class="label-small">Available Credit</div>'
                    f'<div class="balance-positive">{fmt_currency(card["available_credit"])}</div>',
                    unsafe_allow_html=True,
                )
            with col4:
                st.markdown(
                    f'<div class="label-small">Payment Due</div>'
                    f'<div class="value-medium">{card["payment_due_date"]}</div>',
                    unsafe_allow_html=True,
                )
            with col5:
                if st.button("View Details →", key=f"cc_{card['id']}", use_container_width=True):
                    navigate("credit_card_details", selected_card_id=card["id"])
            st.markdown("---")

    render_footer()


# ---------------------------------------------------------------------------
# 3. Account Details Page
# ---------------------------------------------------------------------------

def account_details_page():
    acc_id = st.session_state.get("selected_account_id")
    acc = next((a for a in MOCK_ACCOUNTS if a["id"] == acc_id), None)

    render_header(subtitle="Account Details")

    if acc is None:
        st.error("Account not found.")
        if st.button("← Back to Dashboard"):
            navigate("dashboard")
        return

    # ── Back button ──────────────────────────────────────────────────────────
    if st.button("← Back to Dashboard"):
        navigate("dashboard")

    st.markdown(f'<div class="section-title">{acc["type"]}</div>', unsafe_allow_html=True)

    # ── Account info cards ───────────────────────────────────────────────────
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            f"""
            <div class="card">
                <div class="card-header">Account Number</div>
                <div class="account-number" style="font-size:1.1rem;font-weight:700;">{acc["full_number"]}</div>
                <div class="label-small" style="margin-top:12px;">Routing Number</div>
                <div class="value-medium">{acc["routing_number"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            f"""
            <div class="card">
                <div class="card-header">Available Balance</div>
                <div class="balance-positive">{fmt_currency(acc["available_balance"])}</div>
                <div class="label-small" style="margin-top:12px;">Current Balance</div>
                <div class="value-medium">{fmt_currency(acc["current_balance"])}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            f"""
            <div class="card">
                <div class="card-header">Account Status</div>
                <div><span class="badge-green">{acc["status"]}</span></div>
                <div class="label-small" style="margin-top:12px;">Account Type</div>
                <div class="value-medium">{acc["type"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ── Transaction history ──────────────────────────────────────────────────
    st.markdown('<div class="section-title">Recent Transactions (Last 20)</div>', unsafe_allow_html=True)

    txns = MOCK_ACCOUNT_TRANSACTIONS.get(acc_id, [])
    if txns:
        df = pd.DataFrame(txns)
        st.dataframe(
            styled_table(df),
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("No transactions to display.")

    render_footer()


# ---------------------------------------------------------------------------
# 4. Credit Card Details Page
# ---------------------------------------------------------------------------

def credit_card_details_page():
    card_id = st.session_state.get("selected_card_id")
    card = next((c for c in MOCK_CREDIT_CARDS if c["id"] == card_id), None)

    render_header(subtitle="Credit Card Details")

    if card is None:
        st.error("Credit card not found.")
        if st.button("← Back to Dashboard"):
            navigate("dashboard")
        return

    # ── Back button ──────────────────────────────────────────────────────────
    if st.button("← Back to Dashboard"):
        navigate("dashboard")

    st.markdown(f'<div class="section-title">{card["type"]}</div>', unsafe_allow_html=True)

    # ── Card info ─────────────────────────────────────────────────────────────
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            f"""
            <div class="card">
                <div class="card-header">Card Number</div>
                <div class="account-number" style="font-size:1.1rem;font-weight:700;">{card["masked_number"]}</div>
                <div class="label-small" style="margin-top:12px;">Credit Limit</div>
                <div class="value-medium">{fmt_currency(card["credit_limit"])}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            f"""
            <div class="card">
                <div class="card-header">Current Balance</div>
                <div class="balance-negative">{fmt_currency(card["current_balance"])}</div>
                <div class="label-small" style="margin-top:12px;">Available Credit</div>
                <div class="balance-positive">{fmt_currency(card["available_credit"])}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            f"""
            <div class="card">
                <div class="card-header">Minimum Payment Due</div>
                <div class="balance-negative">{fmt_currency(card["minimum_payment"])}</div>
                <div class="label-small" style="margin-top:12px;">Payment Due Date</div>
                <div class="value-medium">{card["payment_due_date"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ── Transaction history ──────────────────────────────────────────────────
    st.markdown('<div class="section-title">Recent Transactions (Last 20)</div>', unsafe_allow_html=True)

    txns = MOCK_CC_TRANSACTIONS.get(card_id, [])
    if txns:
        df = pd.DataFrame(txns)
        st.dataframe(
            styled_table(df),
            use_container_width=True,
            hide_index=True,
        )
    else:
        st.info("No transactions to display.")

    render_footer()


# ---------------------------------------------------------------------------
# 5. Zelle Transfer Page
# ---------------------------------------------------------------------------

def zelle_transfer_page():
    render_header(subtitle="Zelle® Money Transfer")

    # ── Back button ──────────────────────────────────────────────────────────
    if st.button("← Back to Dashboard"):
        st.session_state["transfer_confirmation"] = None
        navigate("dashboard")

    st.markdown('<div class="section-title">Send Money with Zelle®</div>', unsafe_allow_html=True)
    st.caption(
        "Zelle® is a fast, safe and easy way to send money directly between almost any bank accounts in the U.S., "
        "typically within minutes."
    )

    # ── Show previous transfer confirmation if present ─────────────────────
    confirmation = st.session_state.get("transfer_confirmation")
    if confirmation:
        if confirmation["success"]:
            st.markdown(
                f"""
                <div class="success-banner">
                    <strong>✅ Transfer Successful!</strong><br>
                    Confirmation #: <strong>{confirmation["conf_number"]}</strong><br>
                    From: <strong>{confirmation["from_account"]}</strong><br>
                    To: <strong>{confirmation["to_recipient"]}</strong><br>
                    Amount: <strong>{fmt_currency(confirmation["amount"])}</strong><br>
                    Memo: {confirmation["memo"] or "—"}
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                f"""
                <div class="error-banner">
                    <strong>❌ Transfer Failed</strong><br>
                    Reason: {confirmation["reason"]}
                </div>
                """,
                unsafe_allow_html=True,
            )
        if st.button("Make Another Transfer"):
            st.session_state["transfer_confirmation"] = None
            st.rerun()
        render_footer()
        return

    # ── Transfer Form ─────────────────────────────────────────────────────
    st.markdown("#### Transfer Details")

    account_options = {
        f"{a['type']}  ({a['masked_number']})  –  Available: {fmt_currency(a['available_balance'])}": a
        for a in MOCK_ACCOUNTS
    }
    selected_acc_label = st.selectbox("From Account", options=list(account_options.keys()))
    selected_acc = account_options[selected_acc_label]

    # ── Recipient management ───────────────────────────────────────────────
    st.markdown("#### Recipient")

    recipients = st.session_state["zelle_recipients"]
    recipient_options = [f"{r['nickname']}  ({r['contact']})" for r in recipients]
    recipient_options_with_new = recipient_options + ["➕ Add New Recipient"]

    selected_recipient_label = st.selectbox("Select Recipient", options=recipient_options_with_new)

    new_recipient = None
    if selected_recipient_label == "➕ Add New Recipient":
        st.markdown("**New Recipient Information**")
        nr_col1, nr_col2, nr_col3 = st.columns(3)
        with nr_col1:
            new_name = st.text_input("Full Name", key="nr_name")
        with nr_col2:
            new_contact = st.text_input("Email or Mobile Number", key="nr_contact")
        with nr_col3:
            new_nickname = st.text_input("Nickname", key="nr_nickname")
        new_recipient = {"name": new_name, "contact": new_contact, "nickname": new_nickname or new_name}

    # ── Amount & memo ──────────────────────────────────────────────────────
    st.markdown("#### Amount & Memo")
    amt_col, memo_col = st.columns([1, 2])
    with amt_col:
        amount = st.number_input(
            "Transfer Amount ($)",
            min_value=0.0,
            step=1.0,
            format="%.2f",
            value=0.0,
        )
    with memo_col:
        memo = st.text_input("Memo (optional)", placeholder="e.g., Rent payment, Lunch split")

    # ── Submit ─────────────────────────────────────────────────────────────
    st.markdown("")
    submitted = st.button("Send Money →", type="primary", use_container_width=False)

    if submitted:
        errors = []

        # Validate new recipient fields if adding new
        if selected_recipient_label == "➕ Add New Recipient":
            if not new_recipient["name"].strip():
                errors.append("Recipient name is required.")
            if not new_recipient["contact"].strip():
                errors.append("Recipient email or mobile number is required.")
        else:
            # Resolve to existing recipient object
            idx = recipient_options.index(selected_recipient_label)
            existing_rec = recipients[idx]

        # Validate amount
        if amount <= 0:
            errors.append("Transfer amount must be greater than $0.00.")
        elif amount > selected_acc["available_balance"]:
            errors.append(
                f"Transfer amount {fmt_currency(amount)} exceeds available balance "
                f"{fmt_currency(selected_acc['available_balance'])} for the selected account."
            )

        if errors:
            # Show failure confirmation
            st.session_state["transfer_confirmation"] = {
                "success": False,
                "reason": "  •  ".join(errors),
            }
            st.rerun()
        else:
            # Save new recipient if applicable
            if selected_recipient_label == "➕ Add New Recipient":
                st.session_state["zelle_recipients"].append(new_recipient)
                to_name = f"{new_recipient['nickname']}  ({new_recipient['contact']})"
            else:
                to_name = f"{existing_rec['nickname']}  ({existing_rec['contact']})"

            # Deduct from available balance (in-memory only)
            for acc in MOCK_ACCOUNTS:
                if acc["id"] == selected_acc["id"]:
                    acc["available_balance"] -= amount
                    break

            conf_number = "ZL-" + "".join(random.choices(string.digits, k=10))
            st.session_state["transfer_confirmation"] = {
                "success": True,
                "conf_number": conf_number,
                "from_account": selected_acc_label.split("–")[0].strip(),
                "to_recipient": to_name,
                "amount": amount,
                "memo": memo,
            }
            st.rerun()

    render_footer()


# ---------------------------------------------------------------------------
# Router
# ---------------------------------------------------------------------------

def main():
    init_session_state()

    if not st.session_state["authenticated"]:
        login_page()
        return

    page = st.session_state["current_page"]

    if page == "dashboard":
        dashboard_page()
    elif page == "account_details":
        account_details_page()
    elif page == "credit_card_details":
        credit_card_details_page()
    elif page == "zelle_transfer":
        zelle_transfer_page()
    else:
        login_page()


if __name__ == "__main__":
    main()
