# Step 1: Setup UI with streamlit(model provider, model, websearch, system prompt, query)
import streamlit as st

st.set_page_config(page_title="AI Agent", page_icon=":robot_face:", layout="centered")
st.title("AI Agent")
st.write("Create and interact with AI agents.")
# st.sidebar.header("Settings")

system_prompt = st.text_area("Define your AI agent", height=70,placeholder= "You are a helpful AI assistant.")

MODEL_NAMES_GROQ = ["llama3-70b-8192","llama-3.3-70b-versatile","mixtral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini","gemma-7b-it"]

provider = st.radio("Select model provider", ("Groq", "OpenAI"), horizontal=True)

if provider == "Groq":
    selected_model = st.selectbox("Select model", MODEL_NAMES_GROQ)
elif provider == "OpenAI":
    selected_model = st.selectbox("Select model", MODEL_NAMES_OPENAI, index=0)


alow_web_search = st.checkbox("Allow web search", value=True)

user_query = st.text_area("Enter your query", placeholder="What is the capital of France?")

API_URL = "http://127.0.0.1:8000/chat"

if st.button("Ask Agent!"):
    # Step 2: Connect backend with URL
    import requests
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
            st.error("No response received from the agent. Try the same with this model: llama3-70b-8192")
    else:
        st.error(f"Error: {response.status_code} - {response.json().get('error', 'Unknown error')}")


