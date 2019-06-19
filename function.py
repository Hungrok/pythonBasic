

# function 속성
# first-class object (can be used as function-parameter or return)
def func():print("iamfunction")
print(func)        # function func at 0x..
print(type(func))  # class 'function'
func.__call__()  # iamfunction  - funtion 호출시 불리어지는 method --> code object 호출
print(func.__code__)  # code object func at 0x..
fun1 = func   # reference
fun2 = func   # reference
if fun1==fun2: print("== true")    # True - value compare
if fun1 is fun2: print("is true")  # True - reference compare

# function - global variable access
x,y,z = 10,20,30
def func1a():  print(x+y+z)  # global access
def func1b():  x=100 ; y=200 ; z=300   # local variable
def func1c():  global x,y,z ; x=100 ; y=200 ; z=300   # global access
func1a() #60
func1b()
print(x,y,z) #10,20,30
func1c()
print(x,y,z) #100,200,300

# function - nonlocal keyword (inner function)
def func2():
    a=10
    def inner(): nonlocal a ; a=20
    inner()
    print(a) #20

func2()

# function - parameter & arguments
# parameter : a, b=10, *args, **kwargs
# argument : 순서, keyword

def func3(a, *b, c=1, **d):  # * (list), ** (dict)
    print(a, b, c, d)

func3(1,2,3,4,x=6, y=7, z=8)     # 1 (2, 3, 4) 1 {'x': 6, 'y': 7, 'z': 8}
func3(1,2,3,4,c=5,x=6, y=7, z=8) # 1 (2, 3, 4) 5 {'x': 6, 'y': 7, 'z': 8}
lia = [2,3,4]
dia = {'x':6, 'y':7, 'z':8}
func3(1,*lia,c=8,**dia)          # 1 (2, 3, 4) 5 {'x': 6, 'y': 7, 'z': 8}

# function - recursive : 재귀적사용, compiler stack 구조에 의한 지원
def func6(num):
    if(num==0): # base expression
        return 0
    return num + func6(num-1)

print(func6(5)) #15

# function - closure : inner function 이 소멸된 outer function 의 지역변수를 참고 가능
def func4(x):
    msg = "hello,sum="
    def inner(y):
        print(msg,x+y)
    return inner

f1 = func4(10) # inner function object
f1(20) # hello,sum=30

# function - decorator 1 (basic)
def func7(message):
    def greeting(name):
        print(f'{message}-{name}!')
    return greeting

greet = func7('hello')
greet('kwon') # hello-kwon!
greet('kim')  # hello-kim!

# function - decorator 2 (decorator 함축)
def func8(func):
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        print(f'Result:{result}')
        return result
    return wrapper

@func8 # decorator 함축 (func8(add) --> object (a,b) )
def add (a,b):
    return a+b
add(20,22) # Result:42

# function - generator (iterator)
# 함수를 대상으로 for-loop 를 하기위한 iterator (반복자) 객체가 만들어지는 함수 이다
# yield keyword 에 의하여 iterator 객체가 만들어지고 item 은 return 된다
# list 와 함께 data 조작에 유능한 특징을 보여준다
def func5(max=0):
    n=0
    print("n1=",n)  # 0
    while n<max:
        yield 2**n  # return here, item = Iterator 객체 ( next(){2**n})
        n+=1 # next call
    print("n2=", n) # 3

print(func5(3)) # to see generator object
for item in func5(3): print(item)  # 1 2 4




