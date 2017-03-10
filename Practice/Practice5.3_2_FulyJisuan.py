import math

def invest(amount, rate, time):
    return float(amount)*math.pow(1+float(rate),int(time))

a = input("please input the amount you want to invest:  ")
b = input("please input the rate:   ")
c = input("please input the years that you want to invest:  ")

print(invest(a,b,c))


