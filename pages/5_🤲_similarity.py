"""This page for Similarity Analysis"""
import streamlit as st
from work import API
api = API()
st.markdown("# 🤲 Similarity")

if "api_key" not in st.session_state:
    st.session_state['api_key'] = None

if st.session_state['api_key'] != None:
    box1 = st.text_area("Enter 1st text")
    box2 = st.text_area("Enter 2nd text")
    if st.button("Check Similarity%") and box1 and box2:
        api.similarity_analysis(box1, box2)
else:
    st.error("Sign up or login first")
    st.error("Please enter your API key")