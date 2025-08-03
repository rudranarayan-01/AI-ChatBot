from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List
from ai_agent import get_response_from_AI_agent

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool

    model_config = {
        "protected_namespaces": ()
    }

ALLOWED_MODELS = {
    "Groq": ["llama3-70b-8192", "mixtral-8x7b-32768", "llama-3.3-70b-versatile"],
    "OpenAI": ["gpt-4o-mini", "gemma-7b-it"]
}

app = FastAPI(
    title="AI Agent API",
    description="API for AI Agent using LangChain and Groq/OpenAI",
    version="1.0.0"
)

@app.post("/chat")
def chat(request: RequestState):
    try:
        if request.model_name not in ALLOWED_MODELS.get(request.model_provider, []):
            return JSONResponse(status_code=400, content={"error": f"Model '{request.model_name}' not allowed for provider '{request.model_provider}'."})

        response = get_response_from_AI_agent(
            llm_id=request.model_name,
            query=request.messages,
            allow_search=request.allow_search,
            system_prompt=request.system_prompt,
            provider=request.model_provider
        )

        return JSONResponse(content={"response": response})

    except Exception as e:
        import traceback
        traceback.print_exc()
        return JSONResponse(status_code=500, content={
            "error": "Internal server error",
            "details": str(e)
        })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
