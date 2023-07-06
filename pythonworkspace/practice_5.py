#자료구조의 변경 

#커피숍
menu = {"커피" , "우유", "주스"}
print(menu, type(menu)) #set 형태로 나옴

menu = list(menu)
print(menu, type(menu)) #대괄호로 묶음

menu = tuple(menu)
print(menu, type(menu)) #괄호로 묶음 

menu = set(menu)
print(menu, type(menu)) #중괄호로 묶음 다시 set 형태 

#set 
""" 순서가 없고 중복된 값을 허용 하지 않음 
중괄호로 정의하며 각 요소는 쉼표로 구분 """

#list
"""순서가 있고 중복된 값을 허용
대괄호로 정의하며 각 요소는 쉼표로 구분
요소들을 변경 할 수 있음"""

#tuple
"""순서가 있고 중복된 값을 허용
괄호 또는 생략 을 사용하여 정의하며 각 요소는 쉼표로 구분
요소들을 변경할 수 없음 (불변성)"""

#Q4) 
"""당신의 학교에서는 파이썬 코딩 대회를 주최합니다
참석률을 높이기 위해 댓글 이벤트를 진행하기로 했습니다
댓글 작성자들 중에 추첨을 통해 1명은 치킨 3명은 커피 쿠폰을 받게 됩니다
추첨 프로그램을 작성하시오


조건 1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
조건 2 : 댓글 내용과 상관 없이 무작위로 추첨하되 중복 불가
조건 3 : randum 모듈의 shufffle 와 sample 을 활용"""

"""출력 예제
-- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 [2,3,4]
-- 축하합니다 --"""

#활용 예제
from random import *
lst = [1,2,3,4,5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst, 1))

#유튜브

from random import *
users = range(1,21)
users = list(users)
print(users)
shuffle(users)
print(users)

winners = sample(users,4) #4명 중 1명은 치킨 3명은 커피

print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}" , format(winners[0]))
print("커피 당첨자 : {0}", format(winners[1:]))
print("-- 축하합니다 --")



