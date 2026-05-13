"""Login page – Enterprise Banking UI."""

import streamlit as st

from data.mock_data import MOCK_CREDENTIALS
from styles.login_css import LOGIN_PAGE_CSS
from utils.helpers import navigate


def login_page():
    st.markdown(LOGIN_PAGE_CSS, unsafe_allow_html=True)

    # ── Top Navigation Bar ────────────────────────────────────────────────────
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

        st.markdown("""
<div class="lb-card-top">
    <div class="lb-lock-wrap">🔒</div>
    <div class="lb-card-title">Secure Online Banking Sign In</div>
    <div class="lb-card-subtitle">
        Enter your credentials to securely access your account.
    </div>
</div>
""".strip(), unsafe_allow_html=True)

        if st.session_state.get("login_error"):
            st.markdown("""
<div class="lb-alert lb-alert-error">
    <span>⚠️</span>
    <span>Invalid username or password. Please verify your credentials and try again.</span>
</div>
""".strip(), unsafe_allow_html=True)

        with st.form("login_form", clear_on_submit=False):
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

                st.markdown("""
<div class="lb-links-row">
    <a href="#" class="lb-link">Forgot Username?</a>
    <a href="#" class="lb-link">Forgot Password?</a>
</div>
""".strip(), unsafe_allow_html=True)

                submitted = st.form_submit_button(
                    "🔑  Sign In to Your Account", use_container_width=True
                )

        if submitted:
            if MOCK_CREDENTIALS.get(username) == password:
                st.session_state["login_error"] = False
                st.session_state["authenticated"] = True
                navigate("dashboard")
            else:
                st.session_state["login_error"] = True
                st.rerun()

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

