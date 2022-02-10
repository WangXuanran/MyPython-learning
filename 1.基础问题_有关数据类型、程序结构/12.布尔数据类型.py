#布尔类型(bool)有其对应的整型，True对应1，Fauls对应0
print(True,int(True),False,int(False))
print(True+10,False+10)      #bool类型可以直接和数(整型，浮点型，复型)做四则运算
#所有对象都有bool类型的值，可以使用bool()测试
print(bool(None))
print("\n")
message1=[0,"hello","",56.8]
message2=[]
print(bool(message1))
print(bool(message2))
print(bool(message1[1]))
print(bool(message1[2]))
print(bool(message1[1][0]))
print(bool(message1[3]))
print(bool(message1[0]))

#bool值为False的情况大多数如下
#1.值为False或None
#2.数值0，包括整型、浮点型、复型
#3.空序列，包括空字符串、空列表、空元组、空字典
#4.自定义对象的实例，该对象的__bool__()方法返回False或者__len__()方法返回0