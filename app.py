import streamlit as st
from main import chatbot
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="AI Chatbot")
st.title("AI Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for role, msg in st.session_state["messages"]:
    st.chat_message(role).write(msg)

if prompt := st.chat_input("Type your message..."):
    st.session_state["messages"].append(("user", prompt))
    st.chat_message("user").write(prompt)

    reply = chatbot(prompt)
    st.session_state["messages"].append(("assistant", reply))
    st.chat_message("assistant").write(reply)
