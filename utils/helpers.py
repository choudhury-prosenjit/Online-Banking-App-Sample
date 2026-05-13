"""Shared UI helpers, navigation, formatting, and table styling."""
import pandas as pd
import streamlit as st
from data.mock_data import INITIAL_ZELLE_RECIPIENTS
from styles.theme_css import THEME_CSS
_TABLE_STYLES = [
    {"selector": "thead th", "props": [
        ("background-color", "#0B3C6D"), ("color", "#FFFFFF"), ("font-weight", "700"),
        ("font-size", "0.76rem"), ("text-transform", "uppercase"), ("letter-spacing", "0.7px"),
        ("padding", "12px 16px"), ("border-bottom", "3px solid #1565C0"), ("white-space", "nowrap"),
    ]},
    {"selector": "tbody tr:nth-child(odd) td", "props": [("background-color", "#FFFFFF"), ("color", "#1F2937")]},
    {"selector": "tbody tr:nth-child(even) td", "props": [("background-color", "#E8F0FE"), ("color", "#1F2937")]},
    {"selector": "tbody td", "props": [("font-size", "0.875rem"), ("padding", "10px 16px"), ("border-bottom", "1px solid #C7D7F0")]},
    {"selector": "tbody tr:hover td", "props": [("background-color", "#BFDBFE"), ("color", "#0B3C6D")]},
    {"selector": "table", "props": [("border-collapse", "collapse"), ("width", "100%")]},
]
def styled_table(df: pd.DataFrame):
    """Return a pandas Styler with banking-themed header and alternating rows."""
    return df.style.set_table_styles(_TABLE_STYLES).hide(axis="index")
def init_session_state():
    defaults = {
        "authenticated": False, "current_page": "login",
        "selected_account_id": None, "selected_card_id": None,
        "zelle_recipients": INITIAL_ZELLE_RECIPIENTS.copy(), "transfer_confirmation": None,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
def navigate(page: str, **kwargs):
    st.session_state["current_page"] = page
    for k, v in kwargs.items():
        st.session_state[k] = v
    st.rerun()
def fmt_currency(amount: float) -> str:
    return f"${amount:,.2f}"
def render_header(subtitle: str = ""):
    st.markdown(THEME_CSS, unsafe_allow_html=True)
    sub_html = f"<p>{subtitle}</p>" if subtitle else ""
    st.markdown(f'<div class="bank-header"><div>🏦</div><div><h1>SecureBank</h1>{sub_html}</div></div>', unsafe_allow_html=True)
def render_footer():
    st.markdown('<div class="demo-footer">🔒 This is a demo banking application using mock data only. No real banking transactions are performed.</div>', unsafe_allow_html=True)