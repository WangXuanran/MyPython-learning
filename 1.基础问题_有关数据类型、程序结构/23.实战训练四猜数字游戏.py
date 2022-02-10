#猜数字游戏
import random                #random模块是python中的随机数模块
m=random.randrange(1,101)    #.random生成0到1之间的随机数，randrange(m,n)生成m到n(不包含n)之间的正整数
#print(m)
str1="""
这是一个猜数字游戏，接下来会随机生成一个1到100之间的正整数
你给出你的猜测，计算机提示你猜的数字和生成数字的大小关系
直到你猜出这个数字
下面请输入你猜测的数字\n
"""
num=eval(input(str1))
i=1
while num!=m:
    if 0<=num<m:
        print("猜小了")
    elif m<num<=100:
        print("猜大了")
    else:
        print("输入的数字不符合规定")
    num=eval(input("请再次输入你的猜测\n"))
    i+=1
else:
    print("恭喜你猜对了，生成的数字是",m,"你的猜测次数是",i)



