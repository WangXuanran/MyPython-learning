#这样可以书写向量a,b,c和某个矩阵相乘
a=10
b=20
a,b,c=b,a,a+2*b            #这是元组分解赋值
print(a,b,c)
[a,b,c]=[3*a+2*b+c,6*a+3*b+5*c,10*a+6*b+3*c]     #这是列表分解赋值
print(a,b,c)
a,b,c,d="room"             #这是字符串分解赋值
print(a,b,c,d)
a,*b="hello"               #*匹配赋值
print(a,b)