
def modify_immutable(x):
    x = 10
    print("Inside function:", x)

a = 5
modify_immutable(a)
print("Outside function:", a)

def modify_mutable(lst):
    lst.append(4)
    print("Inside function:", lst)

b = [1, 2, 3]
modify_mutable(b)
print("Outside function:", b)

x = 10  # 전역 변수

def use_global():
    global x  # 전역 변수 x를 사용하겠다고 선언
    x = 20  # 전역 변수 x의 값을 변경
    print("Inside function:", x)

use_global()
print("Outside function:", x)

y = 5  # 전역 변수

def read_global():
    print("Inside function:", y)  # 전역 변수 y를 읽기

read_global()
print("Outside function:", y)

z = 15  # 전역 변수

def local_vs_global():
    z = 25  # 지역 변수 z를 선언하고 초기화
    print("Inside function:", z)  # 지역 변수 z를 출력

local_vs_global()
print("Outside function:", z)  # 전역 변수 z를 출력



# 0807

def dummy():
    # 함수 구현부가 없어도 비워두면 안된다
    pass

def times(a, b):
    return a * b

# 매개변수의 유무, 출력의 유무
# return 문
# 기본적으로 함수를 종료하고 함수 호출 지점으로 돌아감
# 돌려줄 출력값이 있을때는 return 뒤에 데이터를 명시함

def none():
    return # 출력없이 return문만 썼을 때는 None

print(none())
# 함수도 객체
# 다른 객체와 동등한 권리를 가진다
# - 변수에 할당될 수 있고
# - 다른 함수의 매개변수로 전달될 수 있고
# - 함수의 결과로 반환될 수 있음

fun = times # 변수에 할당
print(fun, type(fun))

# 실행가능 객체인지를 확인 => callable
print(callable(fun)) # fun은 실행가능한 객체? 여부

if callable(fun):
    print("fun:", fun(10,10)) # fun이 실행 가능한 객체라면 호출


