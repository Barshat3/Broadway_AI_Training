import os
import streamlit as st
from groq import Groq

# Setup the Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.title("Groq Assistant with Chat Memory")

# Initial system context
base_prompt = "You are a helpful assistant that supports user queries efficiently."

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [{"role": "system", "content": base_prompt}]

# Display previous messages except system prompt
for chat in st.session_state.chat_history[1:]:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])

prompt = st.chat_input("Type your question...")

if prompt:
    # Add user's message to history
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get assistant's response
    with st.chat_message("assistant"):
        with st.spinner("Generating reply..."):
            result = client.chat.completions.create(
                model="gemma2-9b-it",
                messages=st.session_state.chat_history,
                max_tokens=500,
                temperature=1,
            )
            reply = result.choices[0].message.content
            st.markdown(reply)

    # Save assistant reply to chat history
    st.session_state.chat_history.append({"role": "assistant", "content": reply})
