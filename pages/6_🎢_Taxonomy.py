"""This page for Taxonomy"""
import streamlit as st
from work import API
api = API()
st.markdown("# 🎢 Taxonomy")

if "api_key" not in st.session_state:
    st.session_state['api_key'] = None

if st.session_state['api_key'] != None:
    box = st.text_area("Enter your text")
    if st.button("Taxonomy Analysis") and box:
        api.taxonomy_analysis(box)
else:
    st.error("Sign up or login first")
    st.error("Please enter your API key")