"""Zelle Transfer page."""

import random
import string

import streamlit as st

from data.mock_data import MOCK_ACCOUNTS
from utils.helpers import fmt_currency, navigate, render_footer, render_header


def zelle_transfer_page():
    render_header(subtitle="Zelle® Money Transfer")

    if st.button("← Back to Dashboard"):
        st.session_state["transfer_confirmation"] = None
        navigate("dashboard")

    st.markdown('<div class="section-title">Send Money with Zelle®</div>', unsafe_allow_html=True)
    st.caption(
        "Zelle® is a fast, safe and easy way to send money directly between almost any "
        "bank accounts in the U.S., typically within minutes."
    )

    # ── Show previous transfer confirmation ────────────────────────────────────
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

    # ── Transfer Form ──────────────────────────────────────────────────────────
    st.markdown("#### Transfer Details")

    account_options = {
        f"{a['type']}  ({a['masked_number']})  –  Available: {fmt_currency(a['available_balance'])}": a
        for a in MOCK_ACCOUNTS
    }
    selected_acc_label = st.selectbox("From Account", options=list(account_options.keys()))
    selected_acc = account_options[selected_acc_label]

    # ── Recipient management ───────────────────────────────────────────────────
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

    # ── Amount & memo ──────────────────────────────────────────────────────────
    st.markdown("#### Amount & Memo")
    amt_col, memo_col = st.columns([1, 2])
    with amt_col:
        amount = st.number_input("Transfer Amount ($)", min_value=0.0, step=1.0, format="%.2f", value=0.0)
    with memo_col:
        memo = st.text_input("Memo (optional)", placeholder="e.g., Rent payment, Lunch split")

    st.markdown("")
    submitted = st.button("Send Money →", type="primary", use_container_width=False)

    if submitted:
        errors = []
        if selected_recipient_label == "➕ Add New Recipient":
            if not new_recipient["name"].strip():
                errors.append("Recipient name is required.")
            if not new_recipient["contact"].strip():
                errors.append("Recipient email or mobile number is required.")
        else:
            idx = recipient_options.index(selected_recipient_label)
            existing_rec = recipients[idx]

        if amount <= 0:
            errors.append("Transfer amount must be greater than $0.00.")
        elif amount > selected_acc["available_balance"]:
            errors.append(
                f"Transfer amount {fmt_currency(amount)} exceeds available balance "
                f"{fmt_currency(selected_acc['available_balance'])} for the selected account."
            )

        if errors:
            st.session_state["transfer_confirmation"] = {
                "success": False,
                "reason": "  •  ".join(errors),
            }
            st.rerun()
        else:
            if selected_recipient_label == "➕ Add New Recipient":
                st.session_state["zelle_recipients"].append(new_recipient)
                to_name = f"{new_recipient['nickname']}  ({new_recipient['contact']})"
            else:
                to_name = f"{existing_rec['nickname']}  ({existing_rec['contact']})"

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

