import requests
import json


# 执行API调用并存储响应
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
r = requests.get(url, headers=headers, timeout=10)
print(f"Status code: {r.status_code}")

# 探索数据的结构
response_dict = r.json()
readable_file = 'data/readable_hn_data.json'
with open (readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)