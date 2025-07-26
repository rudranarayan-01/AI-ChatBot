import dotenv

# Step 1: Load environment variables from .env file

GROQ_API_KEY = dotenv.get_key(".env", "GROQ_API_KEY")
TAVILY_API_KEY = dotenv.get_key(".env", "TAVILY_API_KEY")
OPENAI_API_KEY = dotenv.get_key(".env", "OPENAI_API_KEY")

# Check if the API keys are set
if not GROQ_API_KEY or not TAVILY_API_KEY or not OPENAI_API_KEY:
    raise ValueError("API keys are not set in the .env file. Please set GROQ_API_KEY, TAVILY_API_KEY, and OPENAI_API_KEY.")

# Step 2: Setting up LLMS
from langchain_groq import Groq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

openai_llm = ChatOpenAI(model="gpt-4o-mini") 
groq_llm = Groq(model="llama-3.3-70b-versatile")
search_tools = TavilySearchResults(max_results=2)

# Step 3: Setting up AI Agnet with search tools functionality
from langgraph.prebuilt import create_react_agent

system_prompt = "Act as a helpful AI smart and friendly Chatbot that can search the web for information. You can use the Tavily search tool to find answers to questions that you don't know."

agent = create_react_agent(
    model=groq_llm,
    tools=[search_tools],
    state_modifier = system_prompt,
)

query = "Tell me about the trends in crypto market"
state = {"message": query}
respose = agent.invoke(state)
print(respose)