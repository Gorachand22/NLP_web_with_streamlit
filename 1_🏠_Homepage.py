"""This the landing page of the website."""

import streamlit as st
from work import Database
db= Database()
st.markdown("# 🏠 Homepage")

if 'forget_pass' not in st.session_state:
            st.session_state['forget_pass'] = False

if "api_key" not in st.session_state:
    st.session_state['api_key'] = None

if "is_api" not in st.session_state:
    st.session_state['is_api'] = False

option = st.selectbox("Select a section", ["Sign Up", "Log in"])

if option == "Sign Up":
    st.write("Sign Up")
    db.signup()


elif option == "Log in":
    st.write("Log in")
    db.check_login()
    if st.session_state['is_api']:
        db.API()
    if st.session_state['forget_pass']:
        db.forget_password()