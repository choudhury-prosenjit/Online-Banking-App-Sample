"""Mock data for SecureBank – no real banking data."""

import random
import string
from datetime import date, timedelta

# ---------------------------------------------------------------------------
# Credentials
# ---------------------------------------------------------------------------

MOCK_CREDENTIALS = {
    "demo_user": "demo123",
}

# ---------------------------------------------------------------------------
# User profile
# ---------------------------------------------------------------------------

MOCK_USER = {
    "username": "demo_user",
    "full_name": "Alex Johnson",
    "email": "alex.johnson@example.com",
    "phone": "(555) 867-5309",
    "member_since": "2018-03-14",
    "last_login": "May 12, 2026  10:22 AM",
}

# ---------------------------------------------------------------------------
# Bank accounts
# ---------------------------------------------------------------------------

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

# ---------------------------------------------------------------------------
# Credit cards
# ---------------------------------------------------------------------------

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

# ---------------------------------------------------------------------------
# Transaction builders
# ---------------------------------------------------------------------------

def _build_account_transactions(start_balance: float, count: int = 20) -> list[dict]:
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
        transactions.append({
            "Date": txn_date.strftime("%b %d, %Y"),
            "Description": desc,
            "Type": txn_type,
            "Amount": f"{'−' if txn_type == 'Debit' else '+'}${abs(amount):,.2f}",
            "Balance": f"${balance:,.2f}",
        })
    return transactions


def _build_cc_transactions(count: int = 20) -> list[dict]:
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
        transactions.append({
            "Date": txn_date.strftime("%b %d, %Y"),
            "Merchant": merchant,
            "Category": category,
            "Amount": f"${amount:,.2f}",
            "Status": status,
        })
    return transactions


# Pre-built transaction maps
MOCK_ACCOUNT_TRANSACTIONS: dict[str, list[dict]] = {
    acc["id"]: _build_account_transactions(acc["current_balance"])
    for acc in MOCK_ACCOUNTS
}

MOCK_CC_TRANSACTIONS: dict[str, list[dict]] = {
    card["id"]: _build_cc_transactions() for card in MOCK_CREDIT_CARDS
}

# ---------------------------------------------------------------------------
# Zelle recipients
# ---------------------------------------------------------------------------

INITIAL_ZELLE_RECIPIENTS = [
    {"name": "Maria Garcia", "contact": "maria.garcia@example.com", "nickname": "Maria"},
    {"name": "David Kim",    "contact": "(555) 321-7654",           "nickname": "David"},
    {"name": "Sarah Chen",   "contact": "sarah.chen@example.com",   "nickname": "Sarah"},
]

