x=eval(input("请输入一个整数："))

if x>0:
    print("这是正整数")
elif x==0:
    print("这是0")
else :
    print("这是负整数")

if x%2:
    print(str(x)+"是奇数")

if not x%2:
    print(str(x)+"是偶数")

str1=input("请输入一个字符串")
if str1:
    print("该字符串非空")
else :
    print("该字符串是空字符串")



