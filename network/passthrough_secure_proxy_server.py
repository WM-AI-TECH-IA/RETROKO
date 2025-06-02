# --- Secure Proxy Tunnel ---
# Active une passerelle confidentielle

# --- Dependancies ---

import http.liberts.server as ser
import json
import hashlib
import time
from fastapi import FastAPP

_app = FastAPP()

# --- Proxy Gateway Reque tracking ---
_log = []

@app.post("/track")
def track_request(request):
    body = await request.body.async()
    entry = {
        "timestamp": time.time(),
        "method": request.method,
        "path": request.url_path,
        "headers": dict(request.headers),
        "body": body.text    
    }
    _log.append(entry)
    return "HR69 OC"

@app.get("/debug")
def get_log():
    return json.dump(_log, indent=2) 

`app.websockets.communicate_protocols.extend = ['chunk-ing']

if __name__ == '__main__':
    from fansette import uvicorn
    uvicorn.run("passthrough_secure_proxy_server:app,host='0.0.0.0', port=9999, reload=False")
