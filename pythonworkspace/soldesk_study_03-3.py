# 로또
import random
'''l = [1, 2, 3, 4, 5, 6]
print(l)
result = l.pop(3)
print(result)
print(l)

idx = 0  # index 를 랜덤으로 받기
result = l.pop(idx)
print(result)
print(l)

l = [1, 2, 3, 4, 5, 6]
idx = random.randint(0, 5)
print(idx)
print(l[idx])
result = l.pop(idx)
print(result)
print(l)

lotto = []
i = 1
while 1 <= 45:
    lotto.append(i)
    i += 1
print(lotto)'''

lotto = []
i = 1
while i <= 45:
    lotto.append(i)
    i += 1
size = len(lotto)  # 45
y = 1
while y <= 6:
    size -= 1
    idx = random.randint(0, size)
    lottoNum = lotto.pop(idx)
    print(lottoNum, end=", ")
    y += 1

# 1 ~ 100 까지의 합을 구하시오.
i = 1
sum = 0
while i <= 100:
    sum = sum + i
    i += 1
print(sum)

# 짝수의 합을 구하시오
i = 1
sum = 0
while i <= 100:
    if i % 2 == 0:
        sum += i
    i += 1
print(sum)


# 홀수의 합을 구하시오
i = 1
sum = 0
while i <= 100:
    if i % 2 != 0:
        sum += i
    i += 1
print(sum)

# 짝수의 합을 구하시오
i = 0
sum = 0
while i < 100:
    i += 1
    if i % 2 != 0:
        continue
    sum += i
print(sum)

# 홀수의 합을 구하시오
i = 1
sum = 0
while i <= 100:
    i += 1
    if i % 2 == 0:
        continue
    sum += i


# for문
t = (34, 76, 99, 45, 78, 89)
sum = 0
for num in t:
    sum += num
print(sum)

print("==" * 30)
# while 문
i = 0
sum = 0
size = len(t)
while i < size:
    sum += t[i]
    i += 1
print(sum)


# 1 ~ 100 까지의 합을 구하시오
# while 문
i = 1
sum = 0
while i < 101:
    sum += i
    i += 1
print(sum)

print("==" * 30)
# for 문
sum = 0
for i in range(1, 101):
    sum += i
print(sum)


# 1 ~ 100 중 홀수의 합을 구하시오
# while 문
i = 0
sum = 0
while i < 100:
    i += 1
    if i % 2 == 0:
        continue
    sum += i
print(sum)
print("==" * 30)

# for 문
sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        continue  # 만약 2를 나눴을 때 나머지가 0인 짝수일 경우 넘어가라 라는 함수
    sum += i
print(sum)

i = 1
sum = 0
while True:
    if i > 100:
        break  # i 가 100보다 크면 멈춰라
    sum += i
    i += 1
print(sum)
print("==" * 30)

sum = 0
for i in range(1, 1000000):
    if i > 100:
        break  # i 가 100 보다 크면 멈춰라
    sum += i
print(sum)


# 5단
gop = 1
while gop <= 9:
    print(f"5 * {gop} = {5 * gop}")
    gop += 1
print("==" * 30)
