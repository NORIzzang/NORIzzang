# score 가 60 이상이면 message 변수에 success 를 아니면 message 에 failure 를 저장한 후 출력

import random
score = 78
if score >= 60:
    message = "success"
else:
    message = "failure"
print(message)

# python type으로 변경
message = "success" if score >= 60 else "failure"
print(message)

# 90 이상이면 A, 80 이상이면B, ..., 60 이하면 F

# elif 문
if score > 90:
    message = "A"
elif score >= 80:
    message = "B"
elif score >= 70:
    message = "C"
elif score >= 60:
    message = "D"
else:
    message = "F"
print(message)

# if else 문
if score >= 90:
    message = "A"
else:
    if score >= 80:
        message = "B"
    else:
        if score >= 70:
            message = "C"
        else:
            if score >= 60:
                message = "D"
            else:
                message = "F"
print(message)

# python type 로 변경
message = 'A' if score >= 90 else ('B' if score >= 80
                                   else ('C' if score >= 70
                                         else ('D' if score >= 60
                                               else 'F')))
print(message)

# 사칙연산
# if ~ elif ~ else 문
a = 10
b = 20
opt = "sub"
if opt == "add":
    result = a + b
elif opt == "sub":
    result = a - b
elif opt == "mul":
    result = a * b
else:  # else 뒤에는 조건식이 없다 if 뒤에만 조건식 있음
    resulf = a / b
print(result)

# python type
result = a + b if opt == "add" else (a - b if opt == "sub"
                                     else (a * b if opt == "mul"
                                           else a / b))
print(result)

# 조건식 : if, if ~ else, if ~ elif ~ else, 중첩 if
# switch ~ case : python 은 없다

# 반복문
print("나무를 1번 찍었습니다")
print("나무를 2번 찍었습니다.")
print("나무를 3번 찍었습니다.")
print("나무를 4번 찍었습니다.")
print("나무를 5번 찍었습니다.")
print("나무를 6번 찍었습니다.")
print("나무를 7번 찍었습니다.")
print("나무를 8번 찍었습니다.")
print("나무를 9번 찍었습니다.")
print("나무를 10번 찍었습니다.")
print("나무가 넘어갑니다.")

start = 1
while start <= 10:  # 조건이 True 인 경우에만 , 종료되는 시점은 조건식에있는 수까지
    print("나무를 %d번 찍었습니다." % start)
    start += 1  # start = start + 1

# 구구단 반복문 8단
start = 1
while start <= 9:
    print(f"8 * {start} = {8 * start}")
    start += 1

# f 문 말고 다르게 쓰는 방법
# print("8 * %d = %d" (start, 8 & start))
# print("8 * {0} = {1}" .format(start, 8 * start))

dan = 3
start = 1
while start <= 9:
    print(f"{dan} * {start} = {dan * start}")
    start += 1

dan = int(input("단을 입력하세요 : "))  # 키보드에 있는 모든 키를 문자로 인식하기에 int 필수 입력
start = 1
while start <= 9:
    print(f"{dan} * {start} = {dan * start}")
    start += 1


dan = int(input("단을 입력하세요 : "))
startGop = int(input("시작 곱을 입력하세요 : "))
endGop = int(input("마지막 곱을 입력하세요 : "))
start = startGop
while start <= endGop:
    print(f"{dan} * {start} = {dan * start}")
    start += 1
