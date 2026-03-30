import streamlit as st
from Ai import get_ai_response

st.title("AI Assistant")

API_KEY = st.secrets["API_KEY"]

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for role, message in st.session_state.messages:
    if role == "user":
        st.chat_message("user").write(message)
    else:
        st.chat_message("assistant").write(message)

# Chat input (auto clears)
prompt = st.chat_input("Ask something...")

if prompt:
    # Show user message
    st.chat_message("user").write(prompt)
    st.session_state.messages.append(("user", prompt))

    # Get AI response
    response = get_ai_response(prompt, API_KEY)

    # Show AI response
    st.chat_message("assistant").write(response)
    st.session_state.messages.append(("assistant", response))
