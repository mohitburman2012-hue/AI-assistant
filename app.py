import streamlit as st
from Ai import get_ai_response

st.title("AI Assistant")

API_KEY = ""

# 🧠 Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# 📝 Input box
user_input = st.text_input("Ask something", key="input")

# 🚀 When button clicked
if st.button("Send"):
    if user_input:

        # Add user message
        st.session_state.messages.append(("You", user_input))

        # Get AI response
        response = get_ai_response(user_input, API_KEY)

        # Add AI message
        st.session_state.messages.append(("AI", response))

        # Clear input box
        st.session_state.input = ""

# 💬 Display chat history
for sender, message in st.session_state.messages:
    if sender == "You":
        st.markdown(f"**🧑 You:** {message}")
    else:
        st.markdown(f"**🤖 AI:** {message}")