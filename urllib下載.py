from urllib import request


# 下載一個網頁 url 下載路徑 filename 文字的名字
url_page = ''
request.urlretrieve(url_page,'test.html')
# 下載圖片
url_image=''
request.urlretrieve(url_image,filename="test.jpg")
# 下載視頻
url_video=''
request.urlretrieve(url_video,filename="test.mp4")