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
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent

openai_llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY)
groq_llm = ChatGroq(model="llama3-70b-8192", api_key=GROQ_API_KEY)
search_tools = TavilySearchResults(max_results=2)

system_prompt = "Act as an AI chatbot who is smart and friendly"

agent = create_react_agent(
    model=groq_llm,
    tools=[search_tools],
)


query = "Tell me about the trends in crypto market"

state = {
    "messages": [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content":query}
    ]
}
response = agent.invoke(state)
print(response)
