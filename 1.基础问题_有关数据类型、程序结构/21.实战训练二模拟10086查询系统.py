str1="""
欢迎来到10086查询系统：
查询话费余额请输入1；
查询流量余额请输入2；
查询剩余通话时间请输入3；
退出查询系统请输入0；\n
"""
num=eval(input(str1))
while num!=0:
    if num==1:
        print("您的话费余额还有30元")
    elif num==2:
        print("您的流量余额还有4G")
    elif num==3:
        print("您的通话时间还剩150分钟")
    else:
        print("您的输入有误")
    num=eval(input("请您选择继续查询或者输入0退出查询\n"))
print("欢迎下次再见")
