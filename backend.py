# setp 1: Setup pydantic model (Schema validation)
from pydantic import BaseModel
from typing import List

class RequestTest(BaseModel):
    model_name: str
    model_provider: str
    system_provider:str
    messages: List[str]
    allow_search: bool
    
    

# Setp 2: Setup AI agent from frontend requests

# Step 3: Run app and explore Swagger UI docs