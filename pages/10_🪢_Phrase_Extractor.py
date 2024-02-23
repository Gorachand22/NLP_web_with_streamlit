"""This page for Phrase Extractor"""
import streamlit as st
from work import API
api = API()
st.markdown("# 🪢 Phrase Extractor")

if "api_key" not in st.session_state:
    st.session_state['api_key'] = None

if st.session_state['api_key'] != None:
    box = st.text_area("Enter your text")
    if st.button("Phrase Extractor") and box:
        api.phrase_extractor(box)
else:
    st.error("Sign up or login first")
    st.error("Please enter your API key")