# 리스트를 포함한 반복문
l = []
for num in range(1, 10):
    l.append(num)
print(l)

l = [num for num in range(1, 10)]
print(l)

# 로또
lotto = []
i = 1
while i <= 45:
    lotto.append(i)
    i += 1
lotto = []
for i in range(1, 46):
    lotto.append(i)

print("==" * 30)

lotto = [i for i in range(1, 46)]
print(lotto)

print("==" * 30)

# 튜플에 있는 값에 3을 곱해서 리스트에 저장해라.
t = (1, 2, 3, 4)
l = []
for num in t:
    l.append(num * 3)
print(l)

print("==" * 30)

l = [num * 3 for num in t]
print(l)

print("==" * 30)

# 튜플에 있는 값 중 짝수만 3을 곱해서 리스트에 저장
t = 1, 2, 3, 4, 5, 6, 7, 8, 9
l = []
for num in t:
    if num % 2 == 0:  # 짝수 표기
        l.append(num * 3)
print(l)

print("==" * 30)

l = [num * 3 for num in t if num % 2 == 0]
print(l)

print("==" * 30)


l = []
for dan in range(3, 6):  # 3~5까지
    for gop in range(1, 10):  # 1~9까지
        l.append(dan * gop)
print(l)

print("==" * 30)

l = [dan * gop for dan in range(3, 6)
     for gop in range(1, 10)]
print(l)

print("==" * 30)

# 3 ~ 5 단의 곱의 값이 짝수만 리스트에 저장
l = []
for dan in range(3, 6):
    for gop in range(1, 10):
        if dan * gop % 2 == 0:
            l.append(dan * gop)
print(l)

print("==" * 30)

l = [dan * gop for dan in range(3, 6)
     for gop in range(1, 10) if dan * gop % 2 == 0]  # append 로 쓰일 때만 이런 경우로 많이 쓰인다.
print(l)

print("==" * 30)

# 제어문 : 조건문(단일 if문, if ~ else, if ~ elif ~ else, 중첩 if문 )
#          반복문( while, for each, continue, break, 리스트를 포함한 반복문)
