import random

cnt = int(input('구매수량을 입력하세요 : '))
for qty in range(0, cnt):
    lotto = []
    for i in range(1, 45 + 1):
        lotto.append(i)
    size = len(lotto)
    for count in range(0, 7):
        lotto.append(count)
    size -= 1
    idx = random.randint(0, size)
    lottoNum = lotto.pop(idx)
    print(lottoNum, end=", ")
print()
