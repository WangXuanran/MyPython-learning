def matrix_det(matrix):
    """请输入一个n*n的矩阵用来计算它的行列式"""
    import copy
    num=len(matrix)
    if num==1:
        return matrix[0][0]
    else:
      sum=0
      for i in range(num):
          matrix_copy = copy.deepcopy(matrix)
          del matrix_copy[0]
          for j in range(num-1):
                del matrix_copy[j][i]
          sum=sum+matrix[0][i]*matrix_det(matrix_copy)*(-1)**(i)
      return sum

print(matrix_det([[1, 2, 3], [4, 5, 6], [7, 8, 11]]))
lst1=[[abs(x-y) for x in range(1,5)] for y in range(1,5)]
for item in lst1:
    print(item)
print(matrix_det(lst1))
lst2=[[i**(j-1) for i in range(1,5)] for j in range(1,5)]
for item in lst2:
    print(item)
print(matrix_det(lst2))