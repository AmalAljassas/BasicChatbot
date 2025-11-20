import os
import streamlit as st
from openai import AzureOpenAI
from streamlit_chat import message

# Environment variables
endpoint = os.getenv("ENDPOINT_URL", "https://<your-foundry-endpoint>.openai.azure.com/")
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "<your-api-key>")

# Initialize Azure OpenAI client
if "client" not in st.session_state:
    st.session_state.client = AzureOpenAI(
        azure_endpoint=endpoint,
        api_key=subscription_key,
        api_version="2025-01-01-preview",
    )
client = st.session_state.client

# Streamlit page setup
st.set_page_config(page_title="BasicChatbot", page_icon="✨")
st.title("✨ Basic Chatbot")
st.write("Welcome! This is a simple chatbot using Azure OpenAI. Type your message below to start chatting.")
st.markdown("---")

# Session state for chat
st.session_state.setdefault("past", [])
st.session_state.setdefault("generated", [])

# Function to get bot response
def get_response(user_input):
    """Call Azure OpenAI API and append response to session state."""
    
    # Store user input
    st.session_state.past.append(user_input)
    
    # Prepare chat messages
    chat_prompt = [
        {
            "role": "system",
            "content": [{"type": "text", "text": "You are a helpful assistant."}]
        }
    ]
    for text in st.session_state.past:
        chat_prompt.append({"role": "user", "content": [{"type": "text", "text": text}]})
    
    # Generate completion
    try:
        completion = client.chat.completions.create(
            model=deployment,
            messages=chat_prompt,
            max_tokens=800,
            temperature=0.7
        )
        bot_text = completion.choices[0].message.content
    except Exception as e:
        bot_text = f"[Error] {e}"
    
    # Store bot response
    st.session_state.generated.append(bot_text)

# Chat input
if prompt := st.chat_input("Say something..."):
    get_response(prompt)

# Display chat
for i in range(len(st.session_state.past)):
    st.markdown(f"{st.session_state.past[i]}")
    with st.chat_message("✨"):
        st.write(st.session_state.generated[i])
