
class Point:

    instance_count = 0 # 클래스 멤버
    # 클래스 멤버 : 클래스 이름 공간 내에 생성, 모든 인스턴스 객체가 공유
    # 인스턴스 멤버 : 인스턴스 공간 내에 생성, 개별 인스턴스 객체 내부에서만 활용


    # init & del
    def __init__(self, x=0, y=0): #매개변수 x,y
        self.x, self.y = x, y
        Point.instance_count += 1

    def __del__(self):
        Point.instance_count -= 1


    # str & repr
    def __str__(self):
        # 객체를 문자열로 변환
        return f"Point x = {self.x}, y = {self.y}"
    def __repr__(self):
        # 객체를 문자열로 변환 ->
        # 원래 목적: 객체 재현
        return f"Point({self.x}, {self.y})"


    # 연산자 오버로딩

    # 산술 연산자 + 오버로딩
    # Point + Point
    # Point + int
    def __add__(self, other): # Point + {other}
        if isinstance(other, int): # x,y 값에 int 값을 합산
            self.x += other
            self.y += other
        elif isinstance(other, Point):
            self.x += other.x
            self.y += other.y
        return self

    # 역이항 + 산술연산자
    def __radd__(self, other): # {other} + Point
        if isinstance(other, int):
            self.x += other
            self.y += other
        return self

    # 산술 연산자 - 오버로딩
    # Point - Point
    # Point - int
    def __sub__(self, other):  # Point - {other}
        if isinstance(other, int):  # other-> int일경우
            self.x -= other
            self.y -= other
        elif isinstance(other, Point):  # other-> Point일 경우
            self.x -= other.x
            self.y -= other.y
        return self

    # 역이항 - 산술연산자
    def __rsub__(self, other):  # {other} - Point
        if isinstance(other, int):
            self.x -= other
            self.y -= other
        return self

    # 비교 연산자
    def __eq__(self, other): # Point == {other}
        if (isinstance(other, Point)):
            return self.x == other.x and \
                    self.y == other.y
        return False

    # setter & getter
    def setX(self, x):  # 인스턴스 메서드의 첫번째 인자는 self
        self.x = x

    def getX(self):
        return self.x

    def setY(self, y):
        self.y = y

    def getY(self):
        return self.y


# 정적 메서드와 클래스 메서드
# - 클래스 메서드 : 모든 인스턴스들이 공유하는 메서드
# - 정적 메서드: 현재 클래스의 네임스페이스만 공유
# @staticmethod, @classmethod라는 데코레이터로 선언 가능
# Singleton Pattern 예제 ->

class Singleton:
    # 인스턴스를 저장할 객체
    __instance = None


    def __init__(self):
        # 유일 객체만 유지해야
        if Singleton.__instance != None:
            raise Exception("이 객체는 싱글턴입니다. 유일 객체만 유지해야되요 use getInstance()")
        else:
            Singleton.__instance = self


    # 클래스 메서드
    @classmethod
    def getClassInstance(cls):
        print(cls.__instance)
        if cls.__instance == None:
            Singleton()
        return cls.__instance


    # 정적 메서드
    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

class MyNumber:
    def __init__(self, value):
        self.value = value

    def __iadd__(self, other):
        self.value += other.value
        return self

    def __isub__(self, other):
        self.value -= other.value
        return self

    def __iand__(self, other):
        self.value &= other.value
        return self

    def __repr__(self):
        return f"비트연산자 &=: {self.value}"