def seperator():
    print('========================')


for a in range(5,10):
    print(a)

seperator()

for a in range(-2,-7):
    print(a)

seperator()

for a in range(-7,-2):
    print(a)

seperator()

for a in range(-2,-11,-3): # The 3rd parameter stands for step
    print(a)

seperator()


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in list[::-1]:
    print(i)



'''======================================
那么两个[::]会是什么那？
>>> array[::2]
[1, 5, 6, 4]
>>> array[2::]
[5, 3, 6, 8, 4]
>>> array[::3]
[1, 3, 4]
>>> array[::4]
[1, 6]
如果想让他们颠倒形成reverse函数的效果
>>> array[::-1]
[4, 8, 6, 3, 5, 2, 1]
>>> array[::-2]
[4, 6, 5, 1]
======================================'''