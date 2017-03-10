a=999
b='1234567890'
c="ABCDEFGHI"

print(type(b))
# #print(str(a)+b)         #类型转换
# #print(a+int(b))         #类型转换
#
# print(type(a))
# print(type(b))
#
# print(b*3)              # 字符串可以直接相乘，从而变成连接效果
# print(len(b*3*3))       # 求字符串长度
#
# print(b[-1]+b[-2]+b[-3]+b[-4]+b[-5])        #负的索引，在字符串里的定位
#
# #print(b[-2:2])
#
# print(b[:3])
# print(b[3:])

print(c[3:50])

d='18951810051'
d_hide=d.replace(d[3:7],'*'*4,1)
print(d_hide)


num=d.find("518")
print(num)

def sum(a,b):
    c=a+b
    return(c)

print('总共有'+str(sum(45,10))+'人')



