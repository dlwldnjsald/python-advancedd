from point import Point

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



if __name__ == "__main__":
    #bound_instance_method()
    #unbound_instance_method()
    class_member_test()