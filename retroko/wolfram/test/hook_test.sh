#!/usr/bin/bash
# RETRKO SANDBOX TEST SERVICE

export URL=http://localhost:8080/hook

curl -X POST $URL \
  -H "Content-Type: application/json" \
  -d '{
  "event": "custom-test",
  "data": {
    "query": "voir temps",
    "source": "httpbin.io"
  }
}'

echo "Hook test sent. Validez sur via /memory/ avec SHA stockee."
