import urllib.request
url = "http://uta.pw/shodou/img/28/214.png"
saveFile = "test.png"
# C:\Users\Core\Norizzang\NORIzzang 이 경로에 이미지 불러옴
urllib.request.urlretrieve(url, "test.png")

url = "http://uta.pw/shodou/img/28.214.png"
mem = urllib.request.urlopen(url).read()
with open("test1 png", "wb") as f:
    f.write(mem)
