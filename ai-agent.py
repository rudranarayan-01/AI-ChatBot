import dotenv

# Step 1: Load environment variables from .env file

GROQ_API_KEY = dotenv.get_key(".env", "GROQ_API_KEY")
TAVILY_API_KEY = dotenv.get_key(".env", "TAVILY_API_KEY")
OPENAI_API_KEY = dotenv.get_key(".env", "OPENAI_API_KEY")

# Check if the API keys are set
if not GROQ_API_KEY or not TAVILY_API_KEY or not OPENAI_API_KEY:
    raise ValueError("API keys are not set in the .env file. Please set GROQ_API_KEY, TAVILY_API_KEY, and OPENAI_API_KEY.")

# Step 2: Setting up LLMS
