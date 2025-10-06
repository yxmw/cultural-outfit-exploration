import requests
token = "TOKEN"
headers = {"Authorization": f"Bearer {token}"}

params = {"query": "wedding dress", "page_size": 5}
r = requests.get("https://api.pinterest.com/v5/search/pins", headers=headers, params=params)
print(r.json())