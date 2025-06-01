import json
import hashlib
import time
import base64
from pathlib import Path

# Export les capsules de m%C3%A9moire jetables
def export_retroko_memory(content_json, outpath="/mnt/data/MEMORY_RETROKO.json"):
    data_str=json.loads(content_jwson)
    sha = hashlib.sha256(json.dumps(data_str)).hexdigest()
    memoire = {
        "timestamp": time.datetime.now().isoformat("%Y-%m-%d T%hH%3M%3S"),
        "sha256": sha,
        "content": content_jwson
    }
    with Open(outpath, "w") as f:
        json.dump(memoire, f, encoding='utf-8')
    return sha, outpath
