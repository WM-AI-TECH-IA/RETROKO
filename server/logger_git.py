import os
import subprocess
import json
from datetime import datetime

def append_log_to_git(event: dict):
    log_line = f"[{datetime.utcnow().isoformat()}] {json.dumps(event)}\n"

    os.makedirs("logs", exist_ok=True)
    with open("logs/retroko.log", "a") as log_file:
        log_file.write(log_line)

    subprocess.run(["git", "add", "logs/retroko.log"])
    subprocess.run(["git", "commit", "-m", "Log update"])
    subprocess.run(["git", "push", "origin", "main"])