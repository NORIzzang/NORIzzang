# 데이터 분석
import requests  # 스크래핑
from bs4 import BeautifulSoup  # 크롤링
import pandas  # 데이터 분석
import matplotlib as mpl  # 시각화
import matplotlib.pyplot as plt  # 시각화
url = "https://www.weather.go.kr/w/obs-climate/land/city-obs.do"
source = requests.get(url)
# print(source)

soup = BeautifulSoup(source.content, "html.parser")
table = soup.find("table", {'class': 'table-col'})  # 기상청 표만 가져오기
# print(table)

data = []
for tr in table.find_all('tr'):
    tds = list(tr.find_all('td'))
    # print(tds)
    for td in tds:
        if td.find('a'):
            point = td.find('a').text
            temp = tds[5].string
            humidity = tds[9].string
            data.append([point, temp, humidity])
# print(data) 지역

# 데이터 처리
with open('weather.csv', 'w',  encoding="utf-8") as f:
    f.write('지역, 온도, 습도 \n')
    for i in data:
        f.write("{0},{1},{2} \n". format(i[0], i[1], i[2]))

# 데이터 분석
df = pandas.read_csv('weather.csv', index_col="지역", encoding="utf-8")
city_df = df.loc[['서울', '인천', '대전', '대구', '광주', '부산', '울산']]
city_df

# 시각화 표로 만들기 실행하면 표나옴 ㅎㅎ
ax = city_df.plot(kind='bar', title='weather', figsize=(12, 4))
plt.show()
