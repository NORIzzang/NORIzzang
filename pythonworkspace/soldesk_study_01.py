
# 담주수업때 물티슈 꼭 챙기기


# jupyter 실행 방법
# pip install jupyter
# jupyter notebook

# 설치 후 브라우저 열리고 나면 new 해서 파일을 생성 한 뒤 python3(ipykernel) 실행 하면 됨

##################################################################################################


# 파이썬은 행단위 명령어, 줄바꿈을 할 수 없다.
print(3+5)
print("hellp python")

# 만약 한 줄에 한 개 이상의 명령어를 사용할 경우 세미콜론 찍어 주기
print(3+5)
print("hello python")


##################################################################################################

# 파이썬 기본 자료형
# 숫자 : 정수(1,3,10) / 실수(0.5)

# 파이썬 기본 자료형
# 숫자 : 정수(1,10,21) / 실수(0.5, 1.5)
# 문자 : a, 김, 나누리
# 논리 : True, False

# 위에 처럼 숫자와 문자를 통틀어서 "리터널" 이라고 명칭
# 10 : 정수리터널 / 김 : 문자리터널 / True : 논리리터널
print(10.5)
print(12)


# 변수 : 담은 값을 그대로 출력한다, 변하는 수 라고 칭함
a = 10  # a 는 정수형 변수
print(a)
a = "과자"  # a 는 문자형 변수
print(a)
a = 10.5  # a 는 실수형 변수
print(a)

# 즉 변수란 리터널의 모든 값을 저장하는 문자

##################################################################################################

# 숫자 리터널을 이용한 연산자 : +, -, *, /
a = 10 * 2
print(a)
a = 10 / 2
print(a)
a = 10 + 2
print(a)
a = 10 - 2
print(a)


# 나머지 연산자 : %
a = 10 % 3
print(a)

# 몫 연산자 : //
a = 10 // 3
print(a)

# 제곱 연산자 : **
a = 10 ** 3
print(a)

# 숫자리터널(정수, 실수) 연산자 : +, -, *, /, %, //, **

##################################################################################################

# 문자 리터널 : 'a', "김"

a = 10
b = 'a'  # 문자형 a
print(b)

a = 10
b = a  # 변수형 a
print(b)

김 = 10
print(김)  # 변수형 김
print("김")  # 문자형 김

나누리 = "김"
print(나누리)  # 변수형 나누리
print("나누리")  # 문자형 나누리

a = 10
print(a + 20)

"""
a = "10"
print(a + 20) 문자와 정수는 연산이 불가능"""

a = "10"
print(a + "10")  # 문자와 문자는 더하기 가능

##################################################################################################

# 문자리터널 연산자 : +, *
print("python " + "is fun")  # "+" 는 문자를 연결하는 연결연산자이다

a = "python"
b = "is"
c = "fun"
print(a + b + c)

# 띄어쓰기 넣고싶으면
a = "python "
b = "is "
c = "fun"
print(a + b + c)

나누리 = "Rhee"
print(나누리)
print(나누리 * 3)  # "*" 는 문자를 반복하는 반복연산자이다

##################################################################################################

# 행바꿈 : 개행문자 \n, """
# 역슬레시 \ = escape 문자
# escape : 탈취시키다 , 달아나다

str1 = "Life is short, \n You need Python"
print(str1)

str1 = """Life is short,
You need Python"""
print(str1)

# 문자열 안에 강조 부호 ' 사용하고 싶을 때
str1 = "Life's fun"
print(str1)

str1 = 'Life\'s fun'
print(str1)

# 문자열 안에 인용 부호 "" 사용하고 싶을 때
str1 = 'Life is fun, "You need python"'
print(str1)

str1 = "Life is fun, \"You need python\""
print(str1)

# 문자열을 표기할 때 쓰는 기호 : "a" , 'a', """a""", '''a'''

##################################################################################################

print("10" + str(3))
# str : 변수 / str() : 함수
# 함수명과 변수명이 같아서는 안된다


##################################################################################################

# indexig
str1 = "Life is too short"
#       01234567890123456 # index = 각 문자에 순서대로 부여되는 고유의 번호 (순서를 나타대는 게 아님)
#                 1

print(str1[0])
print(str1[5])

idx = 8
print(str1[idx])  # = print(str1[8])


idx = 12
print(str1[idx])  # = print(str1[12])

print(str1[16])
print(len(str1))  # len(): 크기를 가지고오는 함수

print(str1[3])
print("Life is too short"[3])

##################################################################################################

str1 = "Life is too short"
#       01234567890123456 (양수일때 : 왼쪽 > 오른쪽)
#                 1
#      -76543210987654321 (음수일떄 : 오른쪽 > 왼쪽)
#              1        음수일 때는 1부터 시작


print(str1[16])
print(str1[-1])

print(str1[-len(str1)])

# Life 를 출력하자
print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[0]+str1[1]+str1[2]+str1[3])

##################################################################################################

# slicing

str1 = "Life is too short"
#       01234567890123456 (양수일때 : 왼쪽 > 오른쪽)
#                 1
#      -76543210987654321 (음수일떄 : 오른쪽 > 왼쪽)
#              1        음수일 때는 1부터 시작

print(str1[0:4])  # 4번까지가 아니라 4번 전까지 숫자를 가져옴
print(str1[0:0+4])
print(str1[8:8+3])

# short 를 출력하자
print(str1[12:12+5])  # 12번 부터 17번 전까지

# l 문자로 부터 10글자를 출력
print(str1[0:0+10])


start = 2
cnt = 10
print(str1[start:start+cnt])  # 2번 부터 12번 전까지


##################################################################################################

str1 = "Life is too short"
#       01234567890123456 (양수일때 : 왼쪽 > 오른쪽)
#                 1
#      -76543210987654321 (음수일때 : 오른쪽 > 왼쪽)
#              1        음수일 때는 1부터 시작

# too short 출력하자

print(str1[8:8+17])
print(str1[8:len(str1)])
print(str1[8:])
print(str1[-9:])
print(str1[-9:17])

# too 출력하자
print(str1[8:8+3])
print(str1[-9:-9+3])

##################################################################################################

# 날짜와 이름을 분리하여 출력
a = "20010331Rainy"
#    0123456789012

print(a[0:4])
print(a[4:6])
print(a[6:8])

년 = a[0:4]
월 = a[4:6]
일 = a[6:8]
이름 = a[8:]

print("날짜 : ", 년+월+일)
print("이름 : ", 이름)

date = a[:8]
name = a[8:]

print("년월일 : ", date)
print("이름 : ", name)

print(a[:0+8])


##################################################################################################

print(str1)
print(str1[:])

# 하나 건너서 출력
print(str1[::2])

# reverse
print(str1[::-1])

# 두개 건너서 출력
print(str1[::3])

# 2번부터 13번까지 하나 건너서 출력
print(str1[2:14:2])

# 13번 부터 2번까지 reverse
print(str1[2:14])
print(str1[13:1:-1])

##################################################################################################

str2 = "pithon"
print(str2)
print(str2[1])

# 입력시 str1[1] = 'y' # 오류 : 문자열에서는 문자를 수정할 수 없다

print(str2[0:1] + 'y' + str2[2:])


##################################################################################################

# 문자열 포매팅

'나의 이름은 이숭무이고 나이는 20살입니다'

name = '이숭무'
age = 20

# print('나의 이름은 ' + name + '이고 나이는 ' + str(age) + ' 살입니다.')
print('나의 이름은 %s이고 나이는 %d살입니다.' % (name, age))


'이숭무의 계좌번호는 1111이고 잔액은 100입니다'

name = '이숭무'
account = '1111'
money = 100
height = 175.3

print(name + '의  계좌번호는 ' + account + ' 이고 잔액은 ' + str(money) + '입니다.')

a = '%s 의 계좌번호는 %s 이고 잔액은 %d 입니다.' % (name, account, money)
print(a)


"이숭무의 나이는 20 살이고 키는 175.3 입니다."

print("%s 의 나이는 %d 살이고 키는 %f 입니다. " % (name, age, height))

print("%s 의 나이는 %d 살이고 키는 %5.1f 입니다. " % (name, age, height))
print("%s 의 나이는 %d 살이고 키는 %14.10f 입니다. " % (name, age, height))
print("%s 의 나이는 %d 살이고 키는 %3.1f 입니다. " % (name, age, height))
print("%s 의 나이는 %d 살이고 키는 %1f 입니다. " % (name, age, height))

print("%s 의 나이는 %d 살이고 키는 %s 입니다. " % (name, age, height))
# 실수를 %s 로 표기해도 소숫점 더 나오지 않고 데이터 추출 가능


##################################################################################################

# 정렬: - 는 왼쪽 정렬 / + 는 오른쪽 정렬


'이숭무의 나이는 20         살이고 키는 173.5 입니다.'
a = '%s 의 나이는 %-10d살이고 키는 %5.1f 입니다.' % (name, age, height)
print(a)

'이숭무의 나이는          20살이고 키는 173.5 입니다.'
a = '%s 의 나이는 %10d살이고 키는 %5.1f 입니다.' % (name, age, height)
print(a)


# format 함수를 사용한 포매팅
# str : 변수 str() : 함수
# print() , len(), format()
print("확인")
print('%s 의 나이는 %d 살이고 키는 %f 입니다.' % (name, age, height))
print('{0}의 나이는 {1}살이고 키는 {2}입니다.' .format(name, age, height))
#                                                      0  ,  1 ,   2

print('%s의 나이는 %d살이고요 %s의 키는 %f 입니다.' %
      (name, age, name, height))
# % \ 할 때 \뒤에 공백이 오면 절대 안됨

print('{1}의 나이는 {0}살이고요 {1}의 키는 {2} 입니다.' .
      format(age, name, height))
# format 을 하게 되면 name 을 두번 쓸 필요 없다

# format 함수에 이름으로 넣기
# 이숭무의 나이는 20살이고 키는 173.5입니다.

print('{0}의 나이는 {1}살이고 키는 {2}입니다.' .format(name, age, height))
# 주의 할 점 format 함수를 사용할 때는 앞에 . 필수 / 입력 안 할 시 "Perhaps you forgot a comma?" 문구 확인 할 수 있음


##### f 문자열 포매팅 #####
#  젤 간편한거 같음 처음에 변수만 잘 지정해주면 됨
print(f'{name}의 나이는 {age} 살이고 키는 {height} 입니다.')


####################################### 정리###########################################################

# 1. 포맷문자를 이용한 포맷팅
# 2. format() 함수를 이용한 포맷팅
# 3. f문자를 이용한 포맷팅
# 문자열 연산자 : + , *
# 문자열 추출 : indexing, slicing


######################################################################################################

# 문자열 가공 : 문자열 함수

a = "hobby"

# 길이함수
print(len(a))
print(len("hobby"))

# 특정문자의 갯수
print(a.count("b"))
print(str1.count("i"))

# str1 에서 too 출력하고 싶음
idx = str1.index('too')
print(idx)  # too 가 시작되는 고유 번호
print(str1[idx:idx + 3])
print(str1[str1.index('too'): str1.index('too') + 3])
print(str1[8:8+3])


# str1 에서 i 가 있는 문자부터 2글자
idx = str1.index('i')  # i 가 시작되는 고유 번호
print(idx)
print(str1[idx:idx + 2])
print(str1[str1.index('i'):str1.index('i')+2])


# str1 에서 두번째 i 부터 가지고 오고싶음
print(str1.count("i"))  # 2개 있음

idx = str1.index('i')  # 첫번째 i 를 찾는 거
print(idx)  # 고유 숫자 1
idx1 = str1.index('i', 2)
print(idx1)
idx2 = str1.index('i', idx+1)
print(idx2)

# t 부터 세글자
print(str1.count("t"))  # 2개 있음

idx = str1.index('t')
print(idx)  # 고유 숫자 8
print(str1[idx:idx+3])
print(str1[str1.index('t'):str1.index('t') + 3])

# 마지막에 있는 t 부터 2글자
str1 = "Life is too short, you need python"
#       0123456789012345678901234567890123
#                 1         2         3
print(str1.count("t"))  # t 3개 있음
idx = str1.rindex('t')  # index 를 오른쪽에서 부터 실행 - 라고 생각
print(idx)
print(str1[idx:idx + 2])

# t, you 를 출력하시오
idx = str1.index('t')  # 첫번째 t
idx1 = str1.index('t', idx + 1)  # 두번째 t
print(str1[idx1: idx1 + 6])

idx2 = str1.index('t', idx1 + 1)  # 세번째 t
print(str1[idx2: idx + 1])


# find
# 'too' 의 위치 찾기
idx = str1.index('too')
print(idx)
print(str1[idx:idx + 3])

idx = str1.find('too')
print(idx)
print(str1[idx:idx + 3])

idx2 = str1.find('t', idx + 1)
print(idx2)

# find 와 index 차이
result = str1.find('z')
# find는 찾는 문자가 없으면 -1
print(result)

# result = str1.index('z') ===> 실행 시 오류
# index는 찾는 문자가 없는 경우 오류 발생

# find 는 찾는 문자열이 있는지 없는지 확인 하고 싶을 때 주로 사용

################################################################################################

# 문자열을 모두 소문자로
print(str1.lower())
str2 = str1.lower()  # 바뀐 값으로 사용하고 싶을 때 str1 > str2
print(str2)

# 문자열을 모두 대문자로
print(str1.upper())
str2 = str1.upper()
print(str2)

##################################################################################################

# 공백문자
str4 = "             highland       "
if "highland" == str4:
    print("같다")
else:
    print("다르다")

# 공백문자 제거
result = str4.strip()
print(result)
print(str4)

if "highland" == result:
    print("같다")
else:
    print("다르다")


# 양쪽 띄어쓰기 제거
str1 = "    Life is too short    "
result = str1.strip()
print(result)

# 오른쪽만 띄어쓰기 제거
result = str1.rstrip()
print(result)

# 왼쪽만 띄어쓰기 제거
result = str1.lstrip()
print(result)

# 문자 제거 (가운데는 이상데이터라서 지우기 불가)
str1 = "abLife is too shortab"
print(str1)
result = str1.strip("ab")
print(result)

# 공백 / 문자 둘 다 제거 (공백부터 지우고 문자 지워야 함)
str1 = "    abLife is too shortab    "
print(str1)
result = str1.strip()  # 공백 지우기
print(result)
result1 = result.strip("ab")  # 문자지우기
print(result1)


# 단어 바꾸기 : replace
str1 = "Life is too short"  # Life > Your leg 로
str2 = str1.replace("Life", "Your leg")
print(str1)
print(str2)

# 쪼개기 : split (쪼개져 있는 형태를 list 라고 부름)
print(str1)
str2 = str1.split()
print(str2)  # ['Life', 'is', 'too', 'short']

str1 = "Life:is:too:short"
str2 = str1.split(":")
print(str2)  # ['Life', 'is', 'too', 'short']

####### split 의 결과를 list 라고 함 제일 중요한 부분 ###############

# 오늘 한 거 정리
# 정수 / 실수 / 문자열

# 다음 주 할 것 !! list 이어서 할 예정입니다 .........
# 기본 문법은 3주 할 예정 4주째에 클롬? 넘파이 , 판다스 할 예정입니다 ....
