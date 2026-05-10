from google.adk.agents import LlmAgent

def get_capital_city(country: str) -> str:
    """Returns the capital city of a given country."""
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
- Always use the tool get_capital_city to find the capital
- Respond in a clear sentence like:
  "The capital of France is Paris."

Rules:
- Do NOT guess answers
- Always use the tool for accuracy
""",
    tools=[get_capital_city],
)