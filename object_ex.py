#글로벌 변수와 로컬 변수를 선언하고, 각각의 심볼 테이블을 출력

# 글로벌 변수 선언
global_a = 1
global_b = "Global"

# 사용자 정의 함수
def func():
    local_a = 2
    local_b = "Local"
    print(locals()) #로컬 심볼 테이블

#func()
#print(globals()) #globals() :현재 모듈의 모든 글로벌 변수와 함수가 포함

# 사용자 클래스
class MyClass:
    x = 10
    y = 20


def symbol_table():
    """
    전역 심볼 테이블
    로컬(지역) 심볼 테이블  확인
    """
    print(globals())
    print("type_of_globals():", type(globals())) #dict

    print("global_a:", globals().get("global_a"))
    print("global_b:", globals().get("global_b"))

    func()

    # 객체 내부의 __dict__를 확인하면 해당 객체 내부의 심볼 테이블 확인 가능
    # 런타임에 속성, 메서드를 추가할 때
    func.dynamic = "Dynamic"
    print(func.__dict__)

    # 인스턴스 객체
    o = MyClass()
    o.dynamic = "Dynamic"
    print(o.__dict__)



import sys
def ref_count():
    """
    객체가 참조될 때 참조 카운트가 증가되면서 관리
    더이상 참조되는 것이 없을때 -> Garbage Collector
    """
    x = object()
    print("type(x):", type(x))
    print("getrefcount(x):", sys.getrefcount(x))

    # 참조 복사
    y = x
    print("getrefcount(x):", sys.getrefcount(x))

    # 참조 삭제
    del(x) # -1됨
    print("getrefcount(y):", sys.getrefcount(y))


def object_id():
    """"
    객체의 ID 관련예제
    """

    # Object ID
    # 객체 ID가 같으면 같은 객체를 참조
    i1 = 10
    i2 = int(10)
    print("int:", hex(id(i1)), hex(id(i2))) # 불변 자료형

    s1 = "hello"
    s2 = str("hello")
    print("str:", hex(id(s1)), hex(id(s2)))  # 불변 자료형

    lst1 = [1, 2, 3]
    lst2 = [1, 2, 3]
    print("lst:", hex(id(lst1)), hex((id(lst2)))) # 가변 자료형 -> 값이 같아도 다른객체 참조

    # == : 동등성의 비교, is == 동일성의 비교
    print(i1 == i2, i1 is i2)
    print(s1 == s2, s1 is s2)
    print(lst1 == lst2, lst1 is lst2) # list -> 값은 같으나(동등) 객체는 다르다( 동일X)

    # is 연산자는 id의 비교
    print(id(lst1) == id(lst2), lst1 is lst2)


def object_copy():
    """
    객체의 복제.
    """

    # 참조 복제 _ 불변자료형
    a = 1
    b = a
    print(a, b, a is b)

    b = 2
    print(a, b, a is b)

    # 가변자료형 list
    a = [1, 2, 3]
    b = [4, 5, 6]
    x = [a, b, 100]

    """
    y = x

    y[2] = 10 
    print("y:", y) 
    print("x:", x) # x[2] == 10 으로 변하게됨
    """

    y = x[:]

    y[2] = 10
    print("y:", y)
    print("x:", x)  # x[2] == 100 으로 원본데이터 유지됨






if __name__ == "__main__":
    #symbol_table()
    #ref_count()
    #object_id()
    object_copy()