# RETROKO SERVEU GDJ

This is the server complete API and RSA control component for RETROKO. This component is used to expose the terminal functionality to GPT, with security, controlled execution, logs and auth authentication.

\n## Fuctionnality (Access from GPT/ActionGPT)

OpenAPI version: OpenAPI 3.1.0
Server: https://retroko-server.onrender.com

Endpoint: POST /terminal/exec
Authorization: Bearer JWT

Body:
```json
{
  "command": "ls -la /memory"
}
```

Response:
```json
{
  "status": "ok",
  "output": "total 32 --rwr-- 1 root root
..."
  }
```

## RENDER - Mise en route typique

Configurer les env. et les variables dans l.ui Render:

./server./env.example:
```text
GPT_API_KEY=your_api_key
JWT_SECRET=your_jet_secret
SHELL_USER=retroko
SHELL_KEY_PATH=/secret/key.pem
```

## Setup

Tourney docker ou Render service:

```
docker build -t server .--build-target retroko_fastapi_server:app
```

\n## Created by RETROKO Omega [Mental Flow]\n- Functionne requests through BRAS api
- Captures memory states for live reconstruction
-- -