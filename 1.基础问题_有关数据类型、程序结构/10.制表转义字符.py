#转义字符\t是字符(在print中输出时需要加上引号)，实际意义是跳转到下一个制表位，每个制表位可容纳8个空格
print("1234567"+"\t12345678")
print("12345678"+"\t12345678")

