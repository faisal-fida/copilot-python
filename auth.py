import asyncio
import httpx
from dotenv import load_dotenv
import os, json

load_dotenv()

class GitHubAuth:
    def __init__(self):
        self.access_token = None
        self.device_code = None

    async def authenticate(self):
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://github.com/login/device/code",
                headers=json.loads(os.getenv("GITHUB_HEADERS")),
                data=json.loads(os.getenv("GITHUB_DATA"))
            )
            response.raise_for_status()
            data = response.json()
            self.device_code = data.get("device_code")
            user_code = data.get("user_code")
            verification_uri = data.get("verification_uri")

            print(f"Please visit {verification_uri} and enter code {user_code} to authenticate.")

        while True:
            await asyncio.sleep(5)
            response = await client.post(
                "https://github.com/login/oauth/access_token",
                headers={
                    "accept": "application/json",
                    "editor-version": "Neovim/0.6.1",
                    "editor-plugin-version": "copilot.vim/1.16.0",
                    "content-type": "application/json",
                    "user-agent": "GithubCopilot/1.155.0",
                    "accept-encoding": "gzip,deflate,br"
                },
                data={"client_id": os.getenv("GITHUB_CLIENT_ID"), "device_code": self.device_code, "grant_type": "urn:ietf:params:oauth:grant-type:device_code"}
            )

            response.raise_for_status()
            token_data = response.json()
            self.access_token = token_data.get("access_token")

            if self.access_token:
                break
