#序列主要包括列表，元组，字典，集合，字符串
#索引从第一个元素到最后一个元素为0到n-1或-n到-1,对每个单独元素来说，正索引-负索引=n
#索引的切片语法为   序列[start:end:step],其中start默认为第一个元素，end默认为最后一个元素，step默认为1,如下例
lst=[1,2,3,4,5,6,7,8,9,10]
lst1=lst[2:8:2]        #取出索引为2,4,6的元素
lst2=lst[-8:-2:2]      #取出索引为-8,-6,-4的元素
lst3=lst[8:2:-2]       #取出索引为8,6,4的元素
print(lst1,lst2,lst3)
#序列相加，与正整数相乘
#序列相加要求相加的两个序列类型相同，但不要求其元素的类型相同，见下例
m1=[1,2,3,"hello","world"]
m2=[3,4,56,9]
m12=m1+m2
m3={1,2,3,4,5,6}
m4={1,2,5,6,10,11}
m34=m3|m4         #这是集合的并
m5=(1,2,4,5)
m6=(3,4,"my","name","my")
m56=m5+m6
print(m12,m2*2,m56)
#方法.index(x)给出元素x在序列中第一次出现的索引，
#方法.count(x)给出元素x在序列中总共出现的次数。
print(m56.index(4),m6.count("my"))
m7=m1
print(m1)
m7[2]=10
print(m7,m1)
del m1
print(m7)
