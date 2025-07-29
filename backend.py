# main.py

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
from ai_agent import get_response_from_AI_agent

# Step 1: Request schema
class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool

    model_config = {
        "protected_namespaces": ()
    }

# Step 2: Allowed models
ALLOWED_MODEL_NAMES = [
    "llama3-70b-8192",
    "mixtral-8x7b-32768",
    "gemma-7b-it"
]


# Step 3: FastAPI App
app = FastAPI(
    title="AI Agent API",
    description="API for AI Agent using LangChain and Groq",
    version="1.0.0"
)

@app.post("/chat")
def chat(request: RequestState):
    try:
        if request.model_name not in ALLOWED_MODEL_NAMES:
            return JSONResponse(status_code=400, content={"error": "Model not allowed."})

        llm_id = request.model_name
        provider = request.model_provider
        system_prompt = request.system_prompt
        query = request.messages
        allow_search = request.allow_search

        response = get_response_from_AI_agent(
            llm_id, query, allow_search, system_prompt, provider
        )

        return JSONResponse(content={"response": response})
    
    except Exception as e:
        import traceback
        traceback.print_exc()
        return JSONResponse(status_code=500, content={
            "error": "Internal server error",
            "details": str(e)
        })

# Step 4: Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
