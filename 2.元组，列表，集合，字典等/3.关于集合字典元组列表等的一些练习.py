A=set(range(0,9))
B=set(range(4,15))
print(A&B)
print(A|B)
print(A-B)
print(A^B)
A.remove(0)
A.add(15)
print(A,A.add(16),(A|B))
lst1=["hello","world","python",2002,6_6]
lst2=[101,202,303,404,505]
A=dict(zip(lst1,lst2))
print(A)
A=(1,2,3,5,[1,2,3])    #元组是不可变数据类型，其不可变性体现在它的元素一旦赋值之后不能更改，
A[4][0]=5              #当列表作为元组的元素时，元组内存储的是列表的地址，更改列表内部元素不会改变其首地址。
print(A,A[4],id(A[3]),id(A[4]),id(A[4][0]),id(A[4][1]))
print(A[4][0]==1)

B=(1,2,3,(1,2,[1,10,30,20]))
B[3][2][0]=15
B[3][2].sort()
print(B)

#a={(1,2,(15,16,[1,2,3])):10,(1,2,(15,16,[1,2,5])):15}
#print(a)
#TypeError: unhashable type: 'list'

lst1=[1,2,3,5,7]
lst2=["hello","world","python","pop",(102,203,304)]
print(zip(lst1,lst2),type(zip(lst1,lst2)))
print(dict(zip(lst1,lst2)),list(zip(lst1,lst2)),sep="\n")

m=range(10)
print(m,type(m))

k=(i for i in range(10))
print(k,type(k))
