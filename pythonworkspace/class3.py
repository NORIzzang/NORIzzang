### class 는 들어는 봤지만 쓸 줄을 모르는 나 어려워 죽겠네 진짜 ###

class NORI:
    def __init__(self): #initiate : 시작하다 , 클래스를 선언하는 순간 실행되는 함수 , a = JSS() 안에 내용 실행 #
        self.name = input("이름 : ") #self 클래스를 저장할 변수 
        self.age = input("나이 : ")
    def show(self):
        print("나의 이름은 {}. 나이는 {} 세 입니다.".format(self.name,self.age))

class NORI2(NORI): #NORI 클래스를 상속 받은 NORI2 클래스 
    def __init__(self):
        super().__init__() #super 함수를 받음으로서 위에 NORI init 내용 가져옴 
        self.gender = input("성별 : ")

a = NORI2()
a.show()
