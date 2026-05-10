Invoking weather app (cloud Run) through Cloud Functions using Conversational Agent
Deploy a weather app on cloud Run (external)
curl https://weather-agent-real-76106446332.us-central1.run.app/weather?city=Dallas
Deploy this cloud run on cloud function 
https://us-central1-prj-bootstrap-491917.cloudfunctions.net/weather-proxy?city=Charlotte
Create app in conversational agent
create tool and create openapi.yaml
add instructions as below:
## Weather Query Handling Instructions

- When the user asks for current weather, temperature, or weather conditions for any city:
  - Extract the city name from the user query.
  - Use the tool `${TOOL:cf-weather-tool}` to fetch real-time weather data.

- Execution steps:
  - Identify the city from the user request (e.g., "What is the weather in Dallas?" → city = Dallas)
  - Call `${TOOL:cf-weather-tool}` with:
    - city = extracted city name

- After receiving tool response:
  - Extract the following fields:
    - city
    - temperature
    - condition
  - Format the response in a user-friendly sentence:
    - Example: "The weather in Dallas is 26.8°C with clear sky."

- If the city is missing or unclear:
  - Ask a clarifying question:
    - "Which city would you like the weather for?"
