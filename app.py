"""
SecureBank Online Banking - Demo Application
Run: streamlit run app.py
Structure:
  app.py                     <- entry point & router
  styles/login_css.py        <- login page CSS
  styles/theme_css.py        <- inner-pages CSS
  data/mock_data.py          <- mock data
  utils/helpers.py           <- shared helpers
  views/login.py             <- login page
  views/dashboard.py         <- dashboard
  views/account_details.py   <- account details
  views/credit_card_details.py <- credit card details
  views/zelle_transfer.py    <- Zelle transfer
"""
import streamlit as st
st.set_page_config(
    page_title="SecureBank Online Banking",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="collapsed",
)
from utils.helpers import init_session_state
from views.login import login_page
from views.dashboard import dashboard_page
from views.account_details import account_details_page
from views.credit_card_details import credit_card_details_page
from views.zelle_transfer import zelle_transfer_page
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