import streamlit as st
from Ai import get_ai_response

st.title("AI Assistant")

API_KEY = st.secrets["API_KEY"]

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])

# Input (auto clears)
prompt = st.chat_input("Ask something...")

if prompt:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # Get AI response using FULL history
    response = get_ai_response(st.session_state.messages, API_KEY)

    # Add AI message
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
