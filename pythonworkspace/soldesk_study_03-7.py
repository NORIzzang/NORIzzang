# 함수(function) : x 값에 따른 y 값의 변화
'''
f(x) = 2x + 3일때
y = f(4)라면 y 값은 얼마가 되나요? = 11
y = f(5)라면 y 값은 얼마가 되나요? = 13
'''


def f(x):  # 피호출함수 : x를 가인자(parameter, 값을 안가지고 있음)
    return 2 * x + 3


y = f(4)  # 호출함수 : 4를 인자(argument, 값을 가지고 있음)
print(y)

y = f(5)  # 호출함수
print(y)

print("=="*30)

'''
f(x1, x2) = 3x1 + 5x2 + 4 일 때
y = f(4,5) 라면 y값은?
'''


def f(x1, x2):  # x1, x2 = 가인자 = parameter = 매개변수
    return 3 * x1 + 5 * x2 + 4


y = f(4, 5)
print(y)

# argument 값을 parameter 에 전달
# argument 와 parameter 는 1대1 대응해야 한다.
# argument 와 parameter 의 갯수는 같아야 한다.
# 호출함수를 실행하려면 피호출함수는 먼저 실행되어있어야 한다.
# 피호출함수를 호출하기 위해서는 호출함수의 이름은 피호출함수와 같아야 한다.

'''
함수의 정의 : 피호출함수 정의
def 함수면(parameter_1, parameter_2, ... , parameter_n):
  명령어1 
  명령어2
  ...
  명령어n
  
함수명(argument_1, parameter_)
  '''
