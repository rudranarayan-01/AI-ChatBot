import dotenv

GROQ_API_KEY = dotenv.get_key(".env", "GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

