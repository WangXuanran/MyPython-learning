#嵌套的列表生成式
lst=[[abs(x-y) for x in range(1,11)] for y in range(1,11)]
for item in lst:
    print(item)
lst2=[sum(i) for i in lst if i[0]%3==1]
print(lst2)
tup= (i for i in [1,3,5,7,9])
print(tup)
print(tup.__next__())
print(tuple(tup))
print(tuple(tup))

import copy
matrix=[1,2,3,4,[1,2,3,4]]
matrix_copy=copy.copy(matrix)
print(matrix[4] is matrix_copy[4])
