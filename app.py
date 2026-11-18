
import streamlit as st
from chatbot import get_response

# Page configuration
st.set_page_config(
    page_title="FitBot AI",
    page_icon="💪"
)

# Application heading
st.title("💪 FitBot AI")
st.caption("Your personal AI fitness assistant")

# Initialize conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Get user input
if prompt := st.chat_input("Ask me anything about fitness..."):

    # Store user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    with st.chat_message("assistant"):

        with st.spinner("FitBot is thinking..."):

            try:
                answer = get_response(
                    st.session_state.messages
                )

                st.markdown(answer)

                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )

            except Exception as e:
                st.error(f"Something went wrong: {e}")
