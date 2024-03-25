from fastapi import FastAPI
from auth import GitHubAuth
from copilot import GitHubCopilot
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
github_auth = GitHubAuth()
github_copilot = None

@app.on_event("startup")
async def startup_event():
    await github_auth.authenticate()
    global github_copilot
    github_copilot = GitHubCopilot(github_auth.access_token)

@app.post("/copilot/completion/")
async def copilot_completion(prompt: str, language: str = "python"):
    if not github_auth.access_token:
        return {"message": "Token not available. Please try again later."}
    return await github_copilot.get_completion(prompt, language)
