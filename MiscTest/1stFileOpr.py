import os

file = open('C:\\temp\\test.txt', 'a')

print('1: ', str(file.closed))

print(file.mode)
print(file.name)

myInput = input("please input the strings that you want to write into files:")
file.write(myInput)

print('1.5: ',file.tell())

file.close()

print('2: ',str(file.closed))
