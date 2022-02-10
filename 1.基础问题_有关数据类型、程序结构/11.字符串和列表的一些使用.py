#字符串在使用索引时和列表相同
message=["hello",15,"world",56,98.5]
print(message[0],message[-1],message[0][-1]) #字符串和列表的索引
print(message[1:3],message[-4:-2],message[2:-1])  #列表的切片
print(message[:3],message[2:])      #切片的第一位默认为0，最后一位默认为列表索引最大值+1
s1=" apple "
s2=" banana "
s3=" apple banana "
print(s1+s2)             #使用+号连接两个字符串
print(s1*3)              #使用*n(或n*)(n为正整数)操作来将字符串复制n次
print(s2 in s3)          #使用in检查字符串s2是否是s3的字串