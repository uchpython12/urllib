from urllib import request

# 使用urlib獲取url代碼

# 定義一個url 訪問的地址
url = ''

# 模擬瀏覽器向服務器發送請求 response 響應
response = request.urlopen(url)

# # 獲取響應頁面的原碼 一個字節的去讀
# content = response.read().decode('utf-8')
# print(content)

# # 返回多少字節
# content = response.read(5).decode('utf-8')
# print(content)

# # 讀取一行
# content = response.readline().decode('utf-8')
# print(content)

# # 一行一行讀 直到讀完
# content = response.readlines()
# print(content)

# # 顯示狀態碼
# content = response.getcode()
# print(content)

# # 顯示url地址
# content = response.geturl()
# print(content)

# 顯示響應頭
content = response.getheaders()
print(content)

# 一個類型 HTTPResponse
# 六個方法 read readline readlines getcode geturl getheaders