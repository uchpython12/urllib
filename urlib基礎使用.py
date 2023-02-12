from urllib import request

# 使用urlib獲取url代碼

# 定義一個url 訪問的地址
url = ''

# 模擬瀏覽器向服務器發送請求 response 響應
response = request.urlopen(url)

# 獲取響應頁面的原碼

content = response.read().decode('utf-8')

print(content)