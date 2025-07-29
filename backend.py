# setp 1: Setup pydantic model (Schema validation)
from pydantic import BaseModel
from typing import List
from ai_agent import get_response_from_AI_agent 

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt:str
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
    
    if request.model_name not in ALLOWED_MODEL_NAMES:
        raise ValueError(f"Model {request.model_name} is not allowed. Allowed models are: {ALLOWED_MODEL_NAMES}")
    
    llm_id = request.model_name
    query = request.messages
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider
    
    # Create AI agnet for the request
    response = get_response_from_AI_agent(llm_id, query, allow_search, system_prompt, provider)
    return response

# Step 3: Run app and explore Swagger UI docs

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.1", port=8000)
    # Visit http://