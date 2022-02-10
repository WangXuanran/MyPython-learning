#复数运算
x=1+2j
y=3+4j
print(x/y)
print(round((x/y).real,1)+round((x/y).imag,1)*1j)
#round（value，数位m）函数表示四舍五入到小数点后第m位