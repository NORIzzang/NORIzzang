import urllib.request as req
from bs4 import BeautifulSoup
url = "https://finance.naver.com/marketindex/"
res = req.urlopen(url)

soup = BeautifulSoup(res, 'html.parser')
# 특정한부분 가져오려고 함
# pri = soup.select_one 하면 print(pri[0].string) 안해도 됨 / print(pri.string)
pri = soup.select('#exchangeList > li.on > a.head.usd > div > span.value')
# print(pri) 하면 [<span class="value">1,336.50</span>] 이렇게 가져옴
print(pri[0].string)


'exchangeList > li.on > a.head.usd > div > span.value'
'#exchangeList > li.on > a.head.jpy > div > span.value'
'#exchangeList > li.on > a.head.eur > div > span.value'
