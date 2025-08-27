gcloud run deploy weather-agent-real --source . --region us-central1 --platform managed --allow-unauthenticated --set-env-vars OPENWEATHER_API_KEY="3c14c46b220142c08572303eb2d1b003"s
--how to publish versions using tags to repo---
git checkout main
git pull -p
git tag -am "weather agent" v1.0 origin/main
git push origin v1.o