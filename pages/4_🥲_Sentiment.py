"""This page for Sentiment Analysis"""
import streamlit as st
from work import API
api = API()
st.markdown("# 🥲 Sentiment")

if "api_key" not in st.session_state:
    st.session_state['api_key'] = None

if st.session_state['api_key'] != None:
    box = st.text_area("Enter your text")
    if st.button("Check Sentiment") and box:
        api.sentiment_analysis(box)
else:
    st.error("Sign up or login first")
    st.error("Please enter your API key")