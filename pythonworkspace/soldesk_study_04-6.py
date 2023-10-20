# 크롤링
from bs4 import BeautifulSoup
# cmd 창에서 먼저 pip install bs4 를 해야함 다운 및 업그레이드 후 실행 시 정상 동작 됨


html = """
<html><body>
  <h1> 스크레이핑이란?</h1>
  <p> 웹 페이지를 분석하는 것 </p>
  <p> 원하는 부분을 추출하는 것 </p>
</body></html>"""
soup = BeautifulSoup(html, 'html.parser')
h1 = soup.html.h1
print(h1)
print(h1.string)
p1 = soup.html.p
print(p1)
print(p1.string)
p2 = soup.html.p.next_sibling.next_sibling
print(p2)
print(p2.string)
