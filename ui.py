import os
import streamlit as st
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_host = os.environ.get("HOST", "api")
api_port = int(os.environ.get("PORT", 8080))

with st.sidebar:
    st.markdown("## AI chat assistant bot for Discord communities.\n")
    st.markdown("This bot can answer to your questions regarding the discord community and help you to learn more about it.")
    st.markdown(
        """ Just enter your question in the chat area.\n"""
    )
    st.markdown(
        "Example: 'what is this community?'",
    )
    st.markdown(
        """[View the source code on GitHub](https://github.com/Asinsayedali/AI-ChatAssistant)""")
    


  

 #UI elements
st.title("AI Chat assistant for Discord Communities")
prompt = st.chat_input("How can I help you?")
# prompt = st.chat_input("How can I help you today?")
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# React to user input
if prompt:
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    

    url = f"http://{api_host}:{api_port}/"
    data = {"query": prompt, "user": "user"}

    response = requests.post(url, json=data)

    if response.status_code == 200:
        response = response.json()
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
    else:
        st.error(
            f"Failed to send data to Discounts API. Status code: {response.status_code}"
        )
