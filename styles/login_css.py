# Login page CSS - Enterprise Banking Theme
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
