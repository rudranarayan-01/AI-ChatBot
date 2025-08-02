# Step 1: Setup UI with streamlit(model provider, model, system prompt, query)
import streamlit as st

st.set_page_config(page_title="AI Agent", page_icon=":robot_face:", layout="wide")
st.title("AI Agent")
st.write("Create and interact with AI agents.")
# st.sidebar.header("Settings")

system_prompt = st.text_area("Define your AI agent", height=70,placeholder= "You are a helpful AI assistant.")

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile","mixtral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

# Step 2: Connect backend with URL