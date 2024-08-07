#0807

# 함수의 매개변수
# 기본적으로 필요한 만큼 선언할 수 있음

def sum_val(a,b):
    return a + b

def incr(a, step=1): # 두번째 인수 (step)은 기본값이 있음
    return a + step

print(sum_val(3,4))
print(incr(7))
print(incr(5, 6))

def sum(a,b):
    return a + b
print("sum:", sum(8,9))

def incr(a, step=1):
    return a + step
print("incr1:", incr(11))
print("incr2:", incr(12,13))


# 키워드 인수
def area(w, h):
    return w * h
print("area1:" ,area(10,20))  # 설계된 매개변수 순서대로 호출
print("area2:", area(w=30, h=40))   # 매개변수의 이름값으로 호출
print("area3:", area(h=40, w=30))   # 호출 순서 중요X

# 가변 인수 : 정해지지 않은 수의 매개변수 => 매개변수 앞에 *
def get_toal(*args):
    sum = 0
    for x in args:
        if isinstance(x, (int,float)): # if 설정
            sum += x
    return sum
print("get_toal:", get_toal(1,3,5,7,9))
print(get_toal(1,2,3,4,5,"a"))


# 키워드 인수 : **
# 함수에 고정인수, 가변인수, 키워드인수
# 선언부에 고정인수, 가변인수, 키워드인수 순으로 선언

def func_args(a,b, *args, **kwargs):
    print("고정인수:", a, b)
    print("가변인수:", args, type(args))
    print("키워드인수:", kwargs, type(kwargs))

func_args(10, 20, 30,40,50,60,70, option1="test", option2="kwargs")