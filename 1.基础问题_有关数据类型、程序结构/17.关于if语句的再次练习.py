x=eval(input("请输入您的成绩\n"))
str="您的成绩等级为"
if x>100 or x<0:
    str="您的成绩有误"
elif x<60:
    str=str+"E"
elif 60<=x<70:
    str=str+"D"
elif 70<=x<80:
    str=str+"C"
elif 80<=x<90:
    str=str+"B"
else:
    str=str+"A"
print(str)

str="您的成绩等级为"
if x>=60:
    if x>=70:
        if x>=80:
            if x>=90:
                if x>100:
                    print("您的成绩有误")
                else:
                    str=str+"A"
            else:
                str=str+"B"
        else:
            str=str+"C"
    else:
        str=str+"D"
elif x<0:
    print("您的成绩有误")
else:
    str=str+"E"
if 0<x<=100:
    print(str)
