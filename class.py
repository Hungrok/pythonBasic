

# class 속성
# type - object - class
# object : 모든 data type 이 상속받는 base class (JAVA 의 Object class)
# type : type of all types (metaclass) , object 과 class 와 단순한 부모관계는 아님
# function 도 define 되어지면 객체가 되듯
# class 도 define 되어지면 객체가 된다 (객체모형 역할과는 다른 관점)
# module (__main__) 도 만들어지면서 객체가 된다 (import 의미는 module 객체를 사용하겠다..)

class myclass1():pass
clsobj = myclass1()
print(myclass1)       # class '__main__.myclass1'
print(clsobj)         # __main__.myclass1 object at 0x..
print(type(myclass1)) # class 'type'
print(type(clsobj))   # __main__.myclass1
print(type(type))     # class 'type'
print(type(object))   # class 'type'
print(type(int))      # class 'type'

print(issubclass(type,object))     # True , object is base class of type (derived)
print(isinstance(type,object))     # True

# add on June 19,2019 to see more
print(issubclass(object,type))     # False
print(isinstance(object,type))     # True

print(issubclass(myclass1,type))   # False
print(issubclass(myclass1,object)) # True

print(isinstance(myclass1,type))   # True
print(isinstance(myclass1,object)) # True

print(isinstance(clsobj,myclass1))   # True
print(isinstance(clsobj,object)) # True
print(isinstance(clsobj,type))   # False

# class - sample
class myclass2():
    # class variable (class 공통으로 지니는 변수)
    cvar1 = 10
    cvar2 = "abc"
    def __init__(self,a,b): # constructor
        self.ivar1 = a
        self.ivar2 = b
    def im1(self): # only access instance variable member
        print("im1,ivar1,2=",self.ivar1,self.ivar2)
    @classmethod
    def cm1(cls):  # only acess class variable member
        cls.var1 = 100
        print("cm1, var1,2= ",cls.cvar1,cls.cvar2)
    @staticmethod
    def sm1(): # can't access class or instance variable member
        print("sm1")


cobj1 = myclass2("kwon","24")
cobj2 = myclass2("kang","29")
cobj3 = myclass2("kim","32")
cobj1.im1()
cobj1.cm1()
cobj1.sm1() # being called even static method

# class - decorator
class myclass3():
    def __init__(self,func):  # constructor
        self.func = func
    def __call__(self,*args, **kwargs):
        result = self.func(*args, **kwargs)
        print(f'Result:{result}')
        return result

@myclass3   # decorator class
def add (a,b):
    return a+b
add(20,22) # Result:42

# class - Base & derived
class myclass4a():
    def __init__(self,a):
        self.a = a
        print("base class __init__")
    def m1(self):
        print("base class m1")
    def m2(self):
        print("base class m2")

class myclass4b(myclass4a):
    def __init__(self, b):
        self.b = b
        print("derived class __init__")
        super().__init__(100) # we have to call constructor to have instance variable

    def m1(self): # overriding
        print("derived class m1")
        super().m1()

c4 = myclass4b(200)
c4.m1()
c4.m2()           # instance member method is inherited
print(c4.a, c4.b) # instance member variable is inherited
print(type(c4.m1())) # class 'NoneType'

# add on June 19,2019 to see more
print(issubclass(myclass4a,object))     # True
print(issubclass(myclass4b,object))     # True
print(issubclass(myclass4b,myclass4a))     # True
print(isinstance(myclass4b,myclass4a))     # False
print(issubclass(myclass4a,myclass4b))     # False
print(isinstance(myclass4a,myclass4b))     # False
print(isinstance(c4,object))        # True
print(isinstance(c4,myclass4a))     # True
print(isinstance(c4,myclass4b))     # True
