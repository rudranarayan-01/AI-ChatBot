import streamlit as st
import requests

st.set_page_config(page_title="AI Agent", page_icon=":robot_face:", layout="centered")
st.title("AI Agent")
st.write("Create and interact with AI agents.")

system_prompt = st.text_area("Define your AI agent", height=70, placeholder="You are a helpful AI assistant.")

MODEL_NAMES = {
    "Groq": ["llama3-70b-8192", "llama-3.3-70b-versatile", "mixtral-8x7b-32768"],
    "OpenAI": ["gpt-4o-mini", "gemma-7b-it"]
}

provider = st.radio("Select model provider", list(MODEL_NAMES.keys()), horizontal=True)
selected_model = st.selectbox("Select model", MODEL_NAMES[provider])

alow_web_search = st.checkbox("Allow web search", value=True)
user_query = st.text_area("Enter your query", placeholder="What is the capital of France?")

API_URL = "http://127.0.0.1:8000/chat"

if st.button("Ask Agent!"):
    payload = {
        "model_name": selected_model,
        "model_provider": provider,
        "system_prompt": system_prompt,
        "messages": [user_query],
        "allow_search": alow_web_search
    }

    response = requests.post(API_URL, json=payload)
    if response.status_code == 200:
        data = response.json()
        if "response" in data:
            st.subheader("Response")
            st.markdown(f'**Final Response:** {data["response"]}')
        else:
            st.warning("No valid response received. Try again with a different model.")
    else:
        st.error(f"Error: {response.status_code} - {response.json().get('error', 'Unknown error')}")
