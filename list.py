# add this on June 24, 2019
# list element 의 dimension 과 shape 는 dynamic 하게 mutable 하다
# 모든것이 객체이기 때문에  - list1[0] 번 객체, list1[1] 번 객체 ,,
# indexing 은 일반적인 기준을 따른다 , 3차원시
# [d2] [d1] [d0] : [z] [y] [x] : [z] [행] [열]
# [] 1차원, [[],[]] 2차원
list1 = [] # can be any dimension
list1 = [33,2,4,7,55,45] # 초기화 - 1차원 배열
print(list1)
list1 = [[1,2,3,4,5,6],[4,5,6]] # 초기화 - 2차원 배열
list1.append([7,8,9,10]) # 상위차원 기준으로 append
print(list1)
list1[2] = [1,2]  # 상위차원 (2차원) 기준 indexing
print(list1)
list1[2][0] = 5  # 2차원이 지닌 1차원 indexing
print(list1)
print(list1[0])

# for 문 결과 value 를 가지고 객체화
list2 = [item*2 for item in range(10)]
print(list2) # 1차원


# Tensorflow 사용 pattern
#  2차원 기준으로 append 되어진다 - WHY ??????
list3 = []
list3.append([0,1])  # 2차원 1st
print(list3)
list3.append([2,3])  # 2차원 2nd
print(list3)
list3.append([4,5,6])  # 2차원 3rd
print(list3)
# item[0] 은 list3[0] 이 아니다 - 각 행이 지니는 첫번째 의미로 사용된다
x_data = [item[0] for item in list3]
y_data = [item[1] for item in list3]
print(x_data)
print(y_data)