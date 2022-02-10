#利用循环和判断来求解水仙花数
str1=input("请输入一个正整数作为上界限\n")
num=int(str1)
for i in range(1,num+1):
    a=len(str(i))
    num_sum=0
    i_copy=i
    for j in range(1,a+1):
        num_sum=num_sum+(i_copy%10)**3
        i_copy=i_copy//10
    if num_sum==i:
        print(str(i)+"是水仙花数")

