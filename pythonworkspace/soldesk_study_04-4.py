# https://search.naver.com/project명/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=python
# <-----------------------------------------url------------------------------------------------------>
# <----------domain-------><------url-----------><----------query string----------------------------->
#                         <project명 = contextPath : /

import urllib.request
url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=python"
mem = urllib.request.urlopen(url).read()
text = mem.decode("utf-8")
print(text)
