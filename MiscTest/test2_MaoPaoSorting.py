
array = [9,8,7,6,5,4,3,2,1]

# 冒泡排序法

for i in range(len(array) - 1, 0, -1):
    print('i = '+str(i))
    for j in range(0, i):
        print('\tj = '+str(j))
        if array[j] > array[j + 1]:
            print('\t\t',array[j],'>',array[j + 1])
            array[j], array[j + 1] = array[j + 1], array[j]
        print('\t\t'+str(array))
    print('==================')
