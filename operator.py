# OPERATOR 특징
# 기본 : 산술, 상관, 논리, Bitwise
# 추가 : Identity, Membership, Slice
# 산술연산자 : 5가지 기본 이외에 ** (exponential) , // (floor division)
# 논리 : 기호(&&,||,!) 대신 keyword 를 사용 (or, and, not)
# Identity : 객체간 reference 비교시 사용 (is , is not)
# Membership : 반복문에 사용 (in, not in)
# Slice (:) : Collection 객체 data manipulation 에 사용

# MEMBERSHIP
list1 = [1,2,5,8,9,4,3]
if (5 in list1): pass
if (6 not in list1) : pass
for item in list1 : pass
while (4 in list1): break
while (9 not in list1): break

# slice (:) operator
squares = [1, 4, 9, 16, 25]
squares[-3:] # slicing returns a new list  [9, 16, 25]
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# replace some values
letters[2:5] = ['C', 'D', 'E'] # ['a', 'b', 'C', 'D', 'E', 'f', 'g']
# now remove them
letters[2:5] = [] # ['a', 'b', 'f', 'g']
# clear the list by replacing all the elements with an empty list
letters[:] = []  # []

# string :  +, *
s1 = "abc"
s2 = "def"
print (s1+s2) # JAVA same
print (s1*3)

# list : + , *
list2 = [[2,3,4],[5,6,7]]  # 2*3
list3 = list2+[[3,6,8]]    # 3*3
print(list3)
print(list3*2)             # 6*3

# dict : we can use ** to merge between dict





