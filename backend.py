# setp 1: Setup pydantic model (Schema validation)
from pydantic import BaseModel

class RequestTest(BaseModel):
    query: str

# Setp 2: Setup AI agent from frontend requests

# Step 3: Run app and explore Swagger UI docs