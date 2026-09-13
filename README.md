# oslogapp

oslogapp

Build
docker build -t oslogapp .

Run
docker run -d \
  --name oslogapp \
  -e APP_NAME="appname" \
  -e FOOTER_NAME="oslogcu" \
  -e INTERVAL_SECONDS=3600 \
  -e SLACK_API_URL="https://hooks.slack.com/services/XXXXX/XXXXX/XXXXX" \
  --restart unless-stopped \
  oslogapp
