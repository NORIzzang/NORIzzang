# 스크래핑

import urllib.request
import urllib.parse
regionNumber = int(input("지역번호를 입력하세요. "))
API = "https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
value = {"stnId": regionNumber}
params = urllib.parse.urlencode(value)
print(params)
url = API + "?" + params
print(url)

mem = urllib.request.urlopen(url).read()
text = mem.decode("utf-8")
print(text)
