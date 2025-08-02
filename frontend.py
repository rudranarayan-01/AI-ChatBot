# Step 1: Setup UI with streamlit(model provider, model, websearch, system prompt, query)
import streamlit as st

st.set_page_config(page_title="AI Agent", page_icon=":robot_face:", layout="wide")
st.title("AI Agent")
st.write("Create and interact with AI agents.")
# st.sidebar.header("Settings")

system_prompt = st.text_area("Define your AI agent", height=70,placeholder= "You are a helpful AI assistant.")

MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile","mixtral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider = st.radio("Select model provider", ("Groq", "OpenAI"), horizontal=True)

if provider == "Groq":
    selected_model = st.selectbox("Select model", MODEL_NAMES_GROQ)
elif provider == "OpenAI":
    selected_model = st.selectbox("Select model", MODEL_NAMES_OPENAI, index=0)


alow_web_search = st.checkbox("Allow web search", value=True)

user_query = st.text_area("Enter your query", placeholder="What is the capital of France?")

if st.button("Ask Agent!"):
    # get response from backend and show
    if user_query.strip():
        response = "This is a placeholder response from the backend."
        st.subheader("Response")
        st.markdown(f'**Final Response:** {response}')

# Step 2: Connect backend with URL