def f1(a,L=[]):    #程序调用时的默认值只计算一次并保存在默认值集合里
    L.append(a)
    return L
print(f1(1))       #当调用函数时未指定具有默认值的参数L时，根据函数定义，程序将创建空列表对象与参数L相关联
print(f1(2))       #当参数关联到一个可变数据类型的对象时，在程序运行期间该对象改变之后仍然会在第二个参数未指定时被关联到之后的L
print(f1(1,[3,4])) #本句第二个参数指定了实参，直接关联到形参，和之前的默认值无关
print(f1(7))       #本句第二个实参未指定，在程序运行期间仍然会将原先创建的默认列表关联到L
print(f1(2,[3,4]))
print(f1(8))

def f2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
#按照如上方式编写的函数，可以应对此问题
#其原理是此函数先将L默认关联到对象None，其是不可变对象
#之后通过判断是否仍然是对象None来考虑是否使用初始值空列表[]
#对此空列表的创建是在每个调用内部的，会随着每个调用依依计算，与默认值只关联一次的规则不同。