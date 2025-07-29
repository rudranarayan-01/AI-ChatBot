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

openai_llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)
groq_llm = ChatGroq(model="llama3-70b-8192", api_key=GROQ_API_KEY)
search_tools = TavilySearch(max_results=2)

system_prompt = "Act as an AI chatbot who is smart and friendly"

def get_response_from_AI_agent(llm_id, query, allow_search, system_prompt, provider):  
    if provider == "Groq":
        llm = ChatGroq(model=llm_id, api_key=GROQ_API_KEY)
    elif provider == "OpenAI":
        llm = ChatOpenAI(model=llm_id, api_key=OPENAI_API_KEY)
    else:
        raise ValueError(f"Unsupported provider: {provider}")
        
    tools = [TavilySearch(max_results=2)] if allow_search else []
    
    agent = create_react_agent(
        model=llm,
        tools=tools,   
    )

    state = {
        "messages": [
            {"role": "system", "content": system_prompt},
            *[{"role": "user", "content": msg} for msg in query]
        ]
    }

    response = agent.invoke(state)
    messages = response.get("messages")
    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]
    return ai_messages[-1] if ai_messages else "No AI response received."

