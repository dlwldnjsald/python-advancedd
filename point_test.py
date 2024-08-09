from point import Point
from point import MyNumber
from point import Adder

def bound_instance_method():
    """
    bound instance method: 인스턴스에 직접 바인딩된 메서드
    """
    p = Point() # Point 인스턴스 객체 생성
    p.setX(10)
    p.setY(20)

    print(p.getX(), p.getY(), sep=",")
    print(p.getX, p.getY) # bound method방식 확인

def unbound_instance_method():
    """
    unbound instance method: 클래스 메서드에 인스턴스 참조주소를 전달해서 우회접근방법
    :인스턴스 메서드의 첫번째 인자가 self 인 이유이기도 함
    """
    p = Point()
    Point.setX(p,10)
    Point.setY(p,20)

    o = Point()
    Point.setX(o,30)
    Point.setY(o,40)

    print(Point.getX(p), Point.getY(p))
    print(Point.getX(o), Point.getY(o))

    #unbound 추천 메모리효율이 더 좋음
    #좀더 명시적인 코드구현 가능의 장점 ㅇ
    #bound 메서드는 인스턴스입장에서 보면 더 명확한 장점 ㅇ
    #둘다 메모리접근 방식의 차이 및 장단점 존재


def class_member_test():
    p1 = Point()
    p1.setX(10)
    p1.setY(20)
    print(p1.getX(), p1.getY(), p1.instance_count)
    # p1.instance+count는 클래스 멤버(인스턴스멤버x)

    p2 = Point()
    p2.setX(20)
    p2.setY(30)
    print(p2.getX(), p2.getY(), p2.instance_count)
    # p2.instance_count는 클래스 멤버(인스턴스멤버X)

    print(p1.x is p2.x)
    print(p1.instance_count is p2.instance_count) # is 같은객체

def constructor_test():
    p1 = Point(10,20)
    print("instance_count:", Point.instance_count)
    p2 = Point()
    print("instance_count:", Point.instance_count)
    p3 = Point(x = 30, y = 40)
    print("instance_count:", Point.instance_count)

    del p1
    del p2

    print("instance_count:", Point.instance_count)

def stringify():
    p = Point(10, 20)
    print(p)    # 문자열화 -> __str__이 호출
    print(repr(p)) # 문자열화 -> 원래 객체를 재현할 수 있는 문자열

    p_repr = eval(repr(p))
    print(p_repr) # 똑같은 원래 객체를 재현 가능

    print(p.x == p_repr.x)
    print(p.y == p_repr.y)


from point import Singleton

def singleton_test():
    s = Singleton()
    print(s)

    #s2 = Singleton()
    s2 = Singleton.getClassInstance()
    print(s2)

    print(s is s2) # True


def oper_overriding():
    print("++++++++++++++++++++++++++++")
    # 산술연산자 + 오버로딩
    print("산술연산자 +:", Point(10,20) + Point(30, 40))
    print("산술연산자 +:", Point(10,20) + 30)

    # 역이항 + 산술연산자 오버로딩
    print("역이항 r+:", Point(30, 40) + Point(10, 20))
    print("역이항 r+:", 30 + Point(10,20))   #__radd__ => {other} + Point 추가 설정 필요


    print("-----------------------------")
    # 산술연산자 - 오버로딩
    print("산술연산자 -:", Point(10, 20) - Point(30, 40))
    print("산술연산자 -:", Point(10, 20) - 30)

    # 역이항 - 산술연산자 오버로딩
    print("역이항 r-:", 30 - Point(10,20))

    print("<<<<<<>>>>>><<<<<<>>>>>>")
    # 비교연산자
    print("비교연산자:", Point(10,20) == Point(10,20))
    print("비교연산자:", Point(10,20) == Point(30,40))

    print("+=+=+=+=+=++=+=+=+=+=+=")
    # 확장 연산자 +=
    a = MyNumber(10)
    b = MyNumber(5)
    a += b
    print("확장 연산자 +=:", a.value)  # 출력: 15

    print("-=-=-=-=-=-=-=-=--=-=-=-=")
    # 확장 연산자 -=
    a = MyNumber(3544634)
    b = MyNumber(43562345)
    a -= b
    print("확장 연산자 -=:", a.value)

    print("&=&=&=&=&=&=&=&=&=&=&=&=&=&=")
    # 비트 연산자 &=
    # 두 숫자의 비트 AND 연산을 수행한 후 결과를 왼쪽 변수에 할당
    a = MyNumber(12) # 12는 1100(2진수)
    b = MyNumber(10) # 10은 1010 (2진수)
    a &= b
    print(a)  # 출력: BitwiseAnd(8), 8은 1000 (2진수)



    # Adder 클래스의 인스턴스를 생성
    add_five = Adder(5)
    # 인스턴스를 함수처럼 호출
    result = add_five(10)
    print(result)



if __name__ == "__main__":
    #bound_instance_method()
    #unbound_instance_method()
    #class_member_test()
    #constructor_test()
    #stringify()
    #singleton_test()
    oper_overriding()