import requests, json

url = "https://retroko-daemon.onrender.com/webhook"
data = {"test": "webhook_check", "timestamp": "alpha"}

res = requests.post(url, json=data)
print("[RESPUNIVE] Status:", res.status_code)
print("[RESPUNIVE] Body:", res.text)
