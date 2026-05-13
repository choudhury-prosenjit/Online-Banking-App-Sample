"""Account Details page."""
import pandas as pd
import streamlit as st
from data.mock_data import MOCK_ACCOUNT_TRANSACTIONS, MOCK_ACCOUNTS
from utils.helpers import fmt_currency, navigate, render_footer, render_header, styled_table
def account_details_page():
    acc_id = st.session_state.get("selected_account_id")
    acc = next((a for a in MOCK_ACCOUNTS if a["id"] == acc_id), None)
    render_header(subtitle="Account Details")
    if acc is None:
        st.error("Account not found.")
        if st.button("← Back to Dashboard"):
            navigate("dashboard")
        return
    if st.button("← Back to Dashboard"):
        navigate("dashboard")
    st.markdown(f'<div class="section-title">{acc["type"]}</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<div class="card"><div class="card-header">Account Number</div><div class="account-number" style="font-size:1.1rem;font-weight:700;">{acc["full_number"]}</div><div class="label-small" style="margin-top:12px;">Routing Number</div><div class="value-medium">{acc["routing_number"]}</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown(f'<div class="card"><div class="card-header">Available Balance</div><div class="balance-positive">{fmt_currency(acc["available_balance"])}</div><div class="label-small" style="margin-top:12px;">Current Balance</div><div class="value-medium">{fmt_currency(acc["current_balance"])}</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown(f'<div class="card"><div class="card-header">Account Status</div><div><span class="badge-green">{acc["status"]}</span></div><div class="label-small" style="margin-top:12px;">Account Type</div><div class="value-medium">{acc["type"]}</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Recent Transactions (Last 20)</div>', unsafe_allow_html=True)
    txns = MOCK_ACCOUNT_TRANSACTIONS.get(acc_id, [])
    if txns:
        st.dataframe(styled_table(pd.DataFrame(txns)), use_container_width=True, hide_index=True)
    else:
        st.info("No transactions to display.")
    render_footer()