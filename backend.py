# setp 1: Setup pydantic model (Schema validation)
from pydantic import BaseModel
from typing import List

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_provider:str
    messages: List[str]
    allow_search: bool
    
    

# Setp 2: Setup AI agent from frontend requests
from fastapi import FastAPI

ALLOWED_MODEL_NAMES = ["gpt-4o-mini", "llama3-70b-8192","mixtral-8x7b-32768", "lamma3.3-70b-versatile"]

app = FastAPI(title="AI Agent API", description="API for AI Agent using LangChain and Groq", version="1.0.0")
@app.post("/chat")

def chat(request: RequestState):
    """API endpoint to interact with chatbot using langgraph and search tools.
    It dinamically selects the model based on the request.
    """

# Step 3: Run app and explore Swagger UI docs