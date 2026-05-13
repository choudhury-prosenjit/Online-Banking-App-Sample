"""Dashboard page."""
import streamlit as st
from data.mock_data import MOCK_ACCOUNTS, MOCK_CREDIT_CARDS, MOCK_USER
from utils.helpers import fmt_currency, navigate, render_footer, render_header
def dashboard_page():
    render_header(subtitle=f"Welcome, {MOCK_USER['full_name']}  |  Last Login: {MOCK_USER['last_login']}")
    col_logout, _, col_zelle = st.columns([1, 4, 1.5])
    with col_logout:
        if st.button("🚪 Sign Out", use_container_width=True):
            st.session_state["authenticated"] = False
            navigate("login")
    with col_zelle:
        if st.button("💸 Transfer Money with Zelle®", use_container_width=True, type="primary"):
            navigate("zelle_transfer")
    st.markdown('<div class="section-title">My Bank Accounts</div>', unsafe_allow_html=True)
    for acc in MOCK_ACCOUNTS:
        with st.container():
            col1, col2, col3, col4 = st.columns([2.5, 1.5, 1.5, 1])
            with col1:
                st.markdown(f'<div><div class="card-header">{acc["type"]}</div><div class="account-number">{acc["masked_number"]}</div></div>', unsafe_allow_html=True)
            with col2:
                st.markdown(f'<div class="label-small">Available Balance</div><div class="balance-positive">{fmt_currency(acc["available_balance"])}</div>', unsafe_allow_html=True)
            with col3:
                st.markdown(f'<div class="label-small">Current Balance</div><div class="value-medium">{fmt_currency(acc["current_balance"])}</div>', unsafe_allow_html=True)
            with col4:
                if st.button("View Details →", key=f"acc_{acc['id']}", use_container_width=True):
                    navigate("account_details", selected_account_id=acc["id"])
            st.markdown("---")
    st.markdown('<div class="section-title">My Credit Cards</div>', unsafe_allow_html=True)
    for card in MOCK_CREDIT_CARDS:
        with st.container():
            col1, col2, col3, col4, col5 = st.columns([2.5, 1.5, 1.5, 1.5, 1])
            with col1:
                st.markdown(f'<div><div class="card-header">{card["type"]}</div><div class="account-number">{card["masked_number"]}</div></div>', unsafe_allow_html=True)
            with col2:
                st.markdown(f'<div class="label-small">Current Balance</div><div class="balance-negative">{fmt_currency(card["current_balance"])}</div>', unsafe_allow_html=True)
            with col3:
                st.markdown(f'<div class="label-small">Available Credit</div><div class="balance-positive">{fmt_currency(card["available_credit"])}</div>', unsafe_allow_html=True)
            with col4:
                st.markdown(f'<div class="label-small">Payment Due</div><div class="value-medium">{card["payment_due_date"]}</div>', unsafe_allow_html=True)
            with col5:
                if st.button("View Details →", key=f"cc_{card['id']}", use_container_width=True):
                    navigate("credit_card_details", selected_card_id=card["id"])
            st.markdown("---")
    render_footer()