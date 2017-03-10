for i in 'my name is Kenny':
    print(i, end = '')

print(3*'\n')


# 打印乘法口诀表
for i in range(1,10):
    for j in range(1,10):
        print(i*j,'\t\t\t', end='')     # 此处的end=''代表不需要换行，直接输出下一个对象
    print('\n')                         # 对于每一行打印完毕，还是要换行，所以此处在外循环处输出一个换行


