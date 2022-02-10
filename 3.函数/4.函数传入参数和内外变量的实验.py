#对函数传入参数的实验:函数传入参数时是按照 对象引用调用 来传递的
def MyFunction(arg1=()):
    arg1[0][0]=10
    return

tup=([5,15,25],10,20,30)
print(tup)
MyFunction(tup)
print(tup)

name="python"
def MyFunction2(name0=name):
    "函数定义时函数参数的默认值会在函数定义之后直接求值"
    print(name0)
name="world"
MyFunction2()

name="python"
def MyFunction3():
    "函数内部使用外部变量时，会直接使用调用处外部变量的值"
    print(name)
name="world"
MyFunction3()