import streamlit as st
from Ai import get_ai_response

st.title("AI Assistant")

API_KEY = st.secrets["API_KEY"]

# Create chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Input box
user_input = st.text_input("Ask something")

# Send button
if st.button("Send"):
    if user_input:

        # Save user message
        st.session_state.messages.append(("You", user_input))

        # Get AI response
        response = get_ai_response(user_input, API_KEY)

        # Save AI message
        st.session_state.messages.append(("AI", response))

# Show chat history
for sender, message in st.session_state.messages:
    if sender == "You":
        st.markdown(f"**🧑 You:** {message}")
    else:
        st.markdown(f"**🤖 AI:** {message}")
