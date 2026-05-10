adk deploy cloud_run \
  --project=prj-bootstrap-491917 \
  --region=us-central1 \
  --service_name=capital-agent \
  --app_name=capital_agent \
  --with_ui \
  ./capital_agent


  Create a Session
  curl -X POST \
"https://capital-agent-76106446332.us-central1.run.app/apps/capital_agent/users/user_123/sessions/session_abc" \
-H "Authorization: Bearer $(gcloud auth print-identity-token)" \
-H "Content-Type: application/json" \
-d '{}'


Run a Agent
curl -X POST \
"https://capital-agent-76106446332.us-central1.run.app/run_sse" \
-H "Authorization: Bearer $(gcloud auth print-identity-token)" \
-H "Content-Type: application/json" \
-d '{
  "app_name": "capital_agent",
  "user_id": "user_123",
  "session_id": "session_abc",
  "new_message": {
    "role": "user",
    "parts": [
      { "text": "What is the capital of France?" }
    ]
  },
  "streaming": false
}'