# numpy
# python 자료형 : 정수, 실수, 문자열, 리스트, 튜플, 딕셔너리, 집합, 부울
# numpy.py : 배열 자료형
# 배열 자료형 : 숫자만 다루는 자료형, numeric python

import numpy as np
num = np.random.randint(10)  # 0 ~ 9 까지 랜덤 출력
print(num)

# 1차원 배열
num = np.random.randint(10, size=6)  # 0~9까지 6개 랜덤 출력
print(num)

# 배열과 리스트의 차이
# 리스트는 콤마가 있고 배열은 콤마 없이 띄어쓰기로만 출력 됨
l = [2, 1, 2, 2, 0, 3]  # 리스트
print(l)
print(num)

print(l[1])  # 리스트
print(num[1])  # 배열

print(l[2:4])  # 리스트
print(num[2:4])  # 배열

# 2차원 배열
num2 = np.random.randint(10, size=(2, 6))  # 0~9 까지 6배열을 2개 출력
print(num2)

l2 = [[4, 0, 3, 2, 5, 2,], [0, 2, 9, 8, 1, 9]]
print(l2)

print(num2)  # 배열
print(num)  # 배열
print(l)  # 리스트
print(l2)  # 리스트
