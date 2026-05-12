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
# Global CSS – professional bank-style theme
# ---------------------------------------------------------------------------
THEME_CSS = """
<style>
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
# 1. Login Page
# ---------------------------------------------------------------------------

def login_page():
    render_header()
    st.markdown(THEME_CSS, unsafe_allow_html=True)

    # Center the login card using columns
    _, center, _ = st.columns([1, 1.2, 1])
    with center:
        st.markdown("### 🔐 Online Banking Sign In")
        st.markdown("Welcome back! Please enter your credentials to access your account.")
        st.markdown("---")

        with st.form("login_form", clear_on_submit=False):
            username = st.text_input("Username", placeholder="Enter username")
            password = st.text_input("Password", placeholder="Enter password", type="password")
            submitted = st.form_submit_button("Sign In →", use_container_width=True)

        if submitted:
            if MOCK_CREDENTIALS.get(username) == password:
                st.session_state["authenticated"] = True
                navigate("dashboard")
            else:
                st.error("❌ Invalid username or password. Please try again.")

        st.markdown("---")
        st.caption("Demo credentials → Username: `demo_user`  |  Password: `demo123`")

    render_footer()


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
            df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Date": st.column_config.TextColumn("Date", width="small"),
                "Description": st.column_config.TextColumn("Description", width="large"),
                "Type": st.column_config.TextColumn("Type", width="small"),
                "Amount": st.column_config.TextColumn("Amount", width="small"),
                "Balance": st.column_config.TextColumn("Balance After", width="small"),
            },
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
            df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Date": st.column_config.TextColumn("Date", width="small"),
                "Merchant": st.column_config.TextColumn("Merchant", width="large"),
                "Category": st.column_config.TextColumn("Category", width="small"),
                "Amount": st.column_config.TextColumn("Amount", width="small"),
                "Status": st.column_config.TextColumn("Status", width="small"),
            },
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
