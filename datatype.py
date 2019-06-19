
# data type
# 모든 data type 은 참조형이다 (객체의 reference 이다)
# 크게 3가지로 분류한다
# 1. built-in data types    : bool, Number, string, list, tuple, set, dict , Array 는 없다
# 2. program data type : type, function, object, module
# 3. user defined data type : class
# 특징
# 1. implicit data type , dynamic type (해서 상수가 없다)
# 2. 객체생성 방법 : literal, new
#    -. List 류에 대한 literal 객체 생성방법 과 operator 지원으로 data-science 에 강점
#    -. java 는 array 와 string 만 literal 방법으로 객체화 가능

# built-in data type
a1 = 10      # literal - int
a2 = int(20) # new
a3: int = 10 # literal , hint
b1 = False # bool
f1 = 10.04 # floating
# list - mutable , element 중복가능
list1 = [] # literal -empty
list2 = list()  # new
list3 = [1, 2, 3, 4, 5, 6] # literal - 1차원
list4 = [1, 2, 3, "abc", "def", "kkk"]  # elements are different
list5 = [[1,2,3],[4,5,6]] # 2차원 (matrix) 2*3
list6 = list3 + [7,8] # [1, 2, 3, 4, 5, 6, 7, 8]
list7 = list3*2  # [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
list8 = list3[1:3] # [2,3]

print(list6)

tuple1 = (1, 2, 3) # immutable list
set1 = {1, 2, 3, 1} # 중복 불가능 --> {1,2,3}
dict1 = {'a': 1, 'b':tuple1, 'c':list4} # key-value, key는 중복 불가능
list6 = list3*2 # [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
list7=list3[1:3] # [2,3]


if a1==a3:print('equal value')  # equal
if list1==list2:print('equal value')  # equal
if list1 is not list2:print('not equal object')  # not equal

# for statement
def forTest():
    for item in range(20): return
    for item in range(5, 20): return
    for item in list3: return
    sum(item**2 for item in list3 )
