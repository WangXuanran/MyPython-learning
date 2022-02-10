#相关联的变量代表的地址
message="你好，中国"
print(type(message))
no=message=1024
print(no,message,id(no),id(message))
no=1023
print(no,message,id(no),id(message))
no=1e-015 #科学计数法表示的浮点数
print(no)
