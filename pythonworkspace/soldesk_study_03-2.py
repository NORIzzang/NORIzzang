

# 3단
start = 1
while start <= 9:
    print(f"3 * {start} = {3 * start}")
    start += 1

# 4단
start = 1
while start <= 9:
    print(f"4 * {start} = {4 * start}")
    start += 1


# 이중반복문 / 반복문 안에 반복문
dan = 1
while dan <= 9:
    start = 1
    while start <= 9:
        print(f"{dan} * {start} = {dan * start}")
        start += 1
    dan += 1
