
# import - 다른 모듈의 멤버를 접근 할것이다 (모듈.멤버) , include 개념은 아니다
import socket        # import standard module
import numpy as np   # import other 3rd party module
from basic import datatype    # import my package module

# 내 모듈에서 사용하는 외부 모듈은  아래 3가지로 분류
# 1. standard built-in modules (Python Interpreter 내에 존재) : import 없이 사용 , 68개 기본
#    -. class for built-in data type : new 객체 생성시 사용
#    -. Utility function : print, dir, type, help,,,
#    -. Data 조작 function : min, max, sum,,,,
# 2. standard package : sys, socket,,,,
# 3. 3'rd party package : anaconda (data-science), tensorflow

# Module
# Module 은 전역으로 사용되는 모듈 멤버들 (data, function, class) 로 구성된다
# Module 은 namespace 가 되어지며, 접근지정자 개념은 없다
# Module 의 모든 멤버는 객체이다 - 모듈은 object 을 define 한다
# class 는 객체지향을 위한 user-defined data type
# function 은 프로그램이 지니는 context (code) 를 지닌다

data1 = 10 # data declaration-initialization , instanced
data2 = datatype.a1
def myFunc():   # function declaration-define  instanced
    print("iamfunction")
class Myclass():  # class declaration-define
    pass


