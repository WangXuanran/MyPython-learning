favorite_language = 'python '
print(favorite_language+"10")              #1
print(favorite_language.rstrip()+"10")     #2方法rstrip 将字符串末尾的多余空格消除
favorite_language=favorite_language+"\t"   #3转义字符\t指制表符
print(favorite_language+"10")              #4疑问：对比(#1)为什么这里的制表符长度是一个空格？
print(favorite_language.rstrip()+"10")
print("\t"+favorite_language.rstrip()+"10")#5这里的制表符长度却是四个空格？
#剔除开头的空白 方法lstrip；剔除两头的空白 方法strip。


#注意，在命令行模式中，一个完整制表符的长度是八个空格，并且\t的意义是跳转到下一个制表符的位置
