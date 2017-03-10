import time
import random
import math

n = 1

time1 = time.time()

while n < 500:

    folder = 'C:\\Users\kenny_chen\Desktop\\test'
    file_name = str(n)+'.json'
    full_path = folder + '\\' + file_name

    file = open(full_path, 'w')

    num = random.uniform(0,100000)
    file.write(str(math.sqrt(num*n*n)))
    file.close()

    n = n + 1

time2 = time.time()

print(time2-time1)