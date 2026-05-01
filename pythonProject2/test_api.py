import requests

url = "http://127.0.0.1:5000/analyze"

data = {
    "text": "人工智能正在快速发展"
}

res = requests.post(url, json=data)

print(res.json())