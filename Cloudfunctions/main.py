import functions_framework
import requests
from flask import jsonify, request

CLOUD_RUN_URL = "https://weather-agent-real-76106446332.us-central1.run.app"

@functions_framework.http
def weather_proxy(request):

    city = request.args.get("city")

    if not city:
        return jsonify({
            "error": "city parameter required"
        }), 400

    response = requests.get(
        f"{CLOUD_RUN_URL}/weather",
        params={"city": city}
    )

    data = response.json()

    return jsonify({
        "city": city,
        "temperature": data["main"]["temp"],
        "condition": data["weather"][0]["description"]
    })