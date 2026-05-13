"""Credit Card Details page."""
import pandas as pd
import streamlit as st
from data.mock_data import MOCK_CC_TRANSACTIONS, MOCK_CREDIT_CARDS
from utils.helpers import fmt_currency, navigate, render_footer, render_header, styled_table
def credit_card_details_page():
    card_id = st.session_state.get("selected_card_id")
    card = next((c for c in MOCK_CREDIT_CARDS if c["id"] == card_id), None)
    render_header(subtitle="Credit Card Details")
    if card is None:
        st.error("Credit card not found.")
        if st.button("← Back to Dashboard"):
            navigate("dashboard")
        return
    if st.button("← Back to Dashboard"):
        navigate("dashboard")
    st.markdown(f'<div class="section-title">{card["type"]}</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<div class="card"><div class="card-header">Card Number</div><div class="account-number" style="font-size:1.1rem;font-weight:700;">{card["masked_number"]}</div><div class="label-small" style="margin-top:12px;">Credit Limit</div><div class="value-medium">{fmt_currency(card["credit_limit"])}</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="card"><div class="card-header">Current Balance</div><div class="balance-negative">{fmt_currency(card["current_balance"])}</div><div class="label-small" style="margin-top:12px;">Available Credit</div><div class="balance-positive">{fmt_currency(card["available_credit"])}</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="card"><div class="card-header">Minimum Payment Due</div><div class="balance-negative">{fmt_currency(card["minimum_payment"])}</div><div class="label-small" style="margin-top:12px;">Payment Due Date</div><div class="value-medium">{card["payment_due_date"]}</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Recent Transactions (Last 20)</div>', unsafe_allow_html=True)
    txns = MOCK_CC_TRANSACTIONS.get(card_id, [])
    if txns:
        st.dataframe(styled_table(pd.DataFrame(txns)), use_container_width=True, hide_index=True)
    else:
        st.info("No transactions to display.")
    render_footer()