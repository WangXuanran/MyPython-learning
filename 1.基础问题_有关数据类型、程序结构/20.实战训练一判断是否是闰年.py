#输入一个年份，请判断是否是闰年
year=eval(input("请输入一个正整数年份：\n"))
if year%4==0:
    str1="是闰年"
    if year%100==0:
        str1="不是闰年"
        if year%400==0:
            str1="是闰年"
else:
    str1="不是闰年"
print(year,str1)

#year=eval(input("请输入一个正整数年份：\n"))
#if (year%4==0 and year%100!=0) or (year%400==0):
#   print(year,"是闰年")
#else:
#   print(year,"不是闰年")

