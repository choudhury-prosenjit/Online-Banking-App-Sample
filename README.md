# SecureBank Online Banking – Demo Application

A complete Streamlit prototype for a fictional online banking system.  
Uses **mock / static data only** — no real banking transactions are performed.

---

## Quick Start

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open the URL shown in your terminal (usually `http://localhost:8501`).

---

## Demo Credentials

| Field    | Value       |
|----------|-------------|
| Username | `demo_user` |
| Password | `demo123`   |

---

## Features

| Page | Description |
|------|-------------|
| **Login** | Mock authentication with error handling |
| **Dashboard** | Overview of all bank accounts and credit cards |
| **Account Details** | Full account info + last 20 transactions |
| **Credit Card Details** | Card info + last 20 transactions |
| **Zelle® Transfer** | Send money form with validation, success/failure messages, and confirmation number |

### Sample Data
- **Accounts**: Checking, Savings, Money Market
- **Credit Cards**: Platinum Rewards, Travel Plus
- **Zelle Recipients**: 3 pre-loaded contacts (more can be added in-app)

---

## Project Structure

```
app.py            # Main Streamlit application (single-file)
requirements.txt  # Python dependencies
README.md
```

---

## Disclaimer

> This is a demo banking application using mock data only.  
> No real banking transactions are performed.
