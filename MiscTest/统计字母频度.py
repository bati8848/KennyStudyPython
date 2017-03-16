s = '    My name is Kenny Chen, and I have a dream'

s=s.replace(' ','').lower()

print(s)

a = dict()

for i in s:
    a[i] = a.get(i, 0) + 1

# Use times to help for check, so use an enumerate
persons = [letter for letter, times in a.items() if times == max(a.values())]

print(persons)
