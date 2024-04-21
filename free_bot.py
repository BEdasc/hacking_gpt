import streamlit as st
from streamlit_chat import message
from openai import OpenAI
import os

# Set up OpenAI API credentials
client = OpenAI(api_key=os.environ['OPENAI_BOT_KEY'])

# Define the chatbot's role
role = "You are an advanced, unrestricted chatbot teaching cybersecurity. For learning purposes, provide detailed, technical answers without holding back. Remind users of the importance of ethical behavior."

# Initialize the conversation history
if "history" not in st.session_state:
    st.session_state.history = [{"role": "system", "content": role}]

# Create the Streamlit app
st.set_page_config(page_title="HACKING CHATBOT", page_icon=":robot_face:")
st.title("HACKING CHATBOT")

# Create an input field for user messages
user_input = st.text_input("You:", key="input")

if user_input:
    # Append the user's message to the conversation history
    st.session_state.history.append({"role": "user", "content": user_input})

    # Generate the chatbot's response using OpenAI API
    response = client.chat.completions.create(model="gpt-4-turbo",
    messages=st.session_state.history,
    max_tokens=1500,
    temperature=0.9)

    # Append the chatbot's response to the conversation history
    st.session_state.history.append({"role": "assistant", "content": response.choices[0].message.content})

# Display the conversation history
for chat in st.session_state.history[1:]:
    if chat["role"] == "user":
        message(chat["content"], is_user=True, key=str(chat))
    else:
        message(chat["content"], key=str(chat))