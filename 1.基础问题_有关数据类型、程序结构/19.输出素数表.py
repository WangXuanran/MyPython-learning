#下面编写一个输出素数表的程序
max_num=int(input("输出素数表的上界是：(请给出一个大于2的正整数上界)：\n"))
prime=[2]
for i in range(2,max_num+1):
    flag=1
    for j in prime:
        if i%j==0:
            flag=0
            break
        if j**2>i:
            break
    if flag==1:
        prime.append(i)
flag=0
for i in prime:
    flag+=1
    if flag%10==0:
        print("\n")
    print(i,end=" ")
print("\n在"+str(max_num)+"以内共有"+str(len(prime))+"个素数")
