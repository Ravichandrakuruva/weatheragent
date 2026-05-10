from google.adk.agents import LlmAgent
from google.adk.runners import Runner
from fastapi import FastAPI
import uvicorn

def get_capital_city(country: str) -> str:
    capitals = {
        "france": "Paris",
        "japan": "Tokyo",
        "india": "New Delhi",
        "usa": "Washington, D.C.",
        "germany": "Berlin",
        "canada": "Ottawa",
        "australia": "Canberra"
    }
    return capitals.get(country.lower(), f"Unknown capital for {country}")

root_agent = LlmAgent(
    name="capital_agent",
    model="gemini-2.5-flash",
    description="Agent that answers questions about capital cities of countries",
    instruction="""
You are a geography assistant.

Your job:
- Identify the country from the user query
- Always use the tool get_capital_city
- Respond like:
  "The capital of France is Paris."
""",
    tools=[get_capital_city],
)

runner = Runner(agent=root_agent)

app = FastAPI()

@app.post("/run")
async def run_agent(request: dict):
    return await runner.run(request)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)