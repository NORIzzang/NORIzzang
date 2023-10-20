# class : 변수와 함수를 하나로 묶어 놓은 것
# class 를 사용하는 이유는 변수와 함수를 반복적으로 사용해야 하는 경우에 선언해서 편하게 사용하려고
class TestClass:  # 변수와 class 명을 구분하기 위해 class 명은 맨 첫글자 대문자로
    result = 1

    def f(self, x):
        self.result = x


a = TestClass()  # 변수는 소문자로 작성 class 로 만들어진 a, b, c는 객체라고 불린다
print(a.result)

a.f(10)
print(a.result)

b = TestClass()
print(b.result)
b.f(100)
print(b.result)

c = TestClass()
print(c.result)
c.f(1000)
print(c.result)


class Men:
    name = ""  # 멤버필드, 멤버변수
    age = 0

    def __init__(self, name, age):  # 객체가 생성될 때 자동으로 실행 되는 애
        self.name = name
        self.age = age

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age


'''danzl = Men()
danzl.setName("나단지")
print(danzl.name)

na = Men()
na.setName("뚱단지")
print(na.name)

danzl.setAge(100)
na.setAge(20)
print(danzl.age)
print(na.age) '''


nuri = Men("나누리", 22)  # 객체 생성과 동시에 기존에 사용했던 값은 삭제
print(nuri.name)
print(nuri.age)


class FourCal:
    def __init__(self, first, second):  # __init__ 에 self 뒤에 오는 변수는 멤버필드임
        self.first = first
        self.second = second


calc = FourCal(10, 20)
print(calc.first)
print(calc.second)

# 모듈 : 변수, 함수, 상수, 클래스, 객체를 하나로 묶어 놓은 것을 모듈이라고 한다.

i = 10


def add(num1, num2):
    result = num1 + num2
    return result


Pi = 3.141592


class FourFal:
    def add(self, num1, num2):
        self.result = num1 + num2

    def div(self, num1, num2):
        self.result = num1 + num2


calc5 = FourCal()
