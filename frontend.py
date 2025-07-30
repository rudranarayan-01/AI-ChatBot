# Step 1: Setup UI with streamlit(model provider, model, system prompt, query)
import streamlit as st

st.set_page_config(page_title="AI Agent", page_icon=":robot_face:", layout="wide")
st.title("AI Agent")
st.write("Create and interact with AI agents.")
st.sidebar.header("Settings")

# Step 2: Connect backend with URL