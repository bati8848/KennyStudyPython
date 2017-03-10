import math

while True:
    a=int(input('please input the 1st length:  '))
    b=int(input('please input the 2nd length:  '))
    # 读取数字之后，要记得做强制类型转换

    c=math.sqrt(a*a+b*b)

    print('\nThe third length is: {}\n\n'.format(c))


