import streamlit as st
from Ai import get_ai_response

st.title("AI Assistant")

API_KEY = ""

user_input = st.text_input("Ask something")

if st.button("Send"):
    response = get_ai_response(user_input, API_KEY)
    st.write(response)