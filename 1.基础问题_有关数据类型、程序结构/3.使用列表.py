message=[12,3.5,"play","family's home"]       #创建列表
print(message)                #输出该列表
print(message[3].title())     #对列表中第四个元素(其为字符串)使用方法title

message[0]=51                 #修改列表中第一个元素
print(message)

message[-1]="mother's home"   #修改列表中倒数第一个元素
print(message)
print("I want to go to "+message[3]+".")

message.append(15)            #在列表末尾添加元素15
print(message)

message.insert(4,"include")   #在列表第5个位置处添加元素，其他元素依次向右移
print(message)

del message[4]                #del 语句删除列表中的某个给定索引处的值
print(message)

popped_message=message.pop(2)  #方法pop将删除列表中第三个元素，如果不写索引值将默认为-1
print(message)
print(popped_message)
