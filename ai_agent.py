# ai_agent.py

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv(".env")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not GROQ_API_KEY or not TAVILY_API_KEY or not OPENAI_API_KEY:
    raise ValueError("API keys are not set properly.")

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

def get_response_from_AI_agent(llm_id, query, allow_search, system_prompt, provider):  
    # Select model
    if provider == "Groq":
        llm = ChatGroq(model=llm_id, api_key=GROQ_API_KEY)
    elif provider == "OpenAI":
        llm = ChatOpenAI(model=llm_id, api_key=OPENAI_API_KEY)
    else:
        raise ValueError(f"Unsupported provider: {provider}")
        
    tools = [TavilySearch(api_key=TAVILY_API_KEY, max_results=2)] if allow_search else []

    # Create LangGraph agent
    agent = create_react_agent(model=llm, tools=tools)

    # Convert input messages to LangChain format
    state = {
        "messages": [
            SystemMessage(content=system_prompt),
            *[HumanMessage(content=msg) for msg in query]
        ]
    }

    try:
        response = agent.invoke(state)
        messages = response.get("messages", [])
        ai_messages = [msg.content for msg in messages if isinstance(msg, AIMessage)]
        return ai_messages[-1] if ai_messages else "No AI response received."
    except Exception as e:
        print("❌ Agent failed:", e)
        return f"Error: {str(e)}"
