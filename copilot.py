import json
import httpx

class GitHubCopilot:
    def __init__(self, access_token):
        self.access_token = access_token

    async def get_completion(self, prompt, language="python"):
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    "https://copilot-proxy.githubusercontent.com/v1/engines/copilot-codex/completions",
                    headers={"authorization": f"Bearer {self.access_token}"},
                    json={
                        "prompt": prompt,
                        "suffix": "",
                        "max_tokens": 1000,
                        "temperature": 0,
                        "top_p": 1,
                        "n": 1,
                        "stop": ["\n"],
                        "nwo": "github/copilot.vim",
                        "stream": True,
                        "extra": {"language": language}
                    }
                )
                response.raise_for_status()
            except httpx.RequestError:
                return ""

            result = ""
            async for chunk in response.aiter_text():
                if chunk.startswith("data: {"):
                    json_completion = json.loads(chunk[6:])
                    completion = json_completion.get("choices")[0].get("text")
                    result += completion if completion else "\n"
            return result
