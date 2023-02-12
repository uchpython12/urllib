import urllib.parse
from urllib import request

name = urllib.parse.quote("中文")
data = {
    "name": "名字",
    "location": "python"
}
new_data = urllib.parse.urlencode(data)  #中文後綴
url = '' #網址
url =url+new_data #網址 +中文後綴

# 解決反爬一種手段 User-Agent
headers = {
    "User-Agent": ""
}
request_head = request.Request(url=url, headers=headers)

response = request.urlopen(request_head)

# 獲取響應內容

content = response.read().decode("utf-8")
print(content)

#獲取網址
content = response.geturl()
print(content)