path_folder = r'C:\temp\TE_Payment.ini'

file = open(path_folder)

for line in file.readlines():

    if line.startswith('id ='):
        print(line[-5:-1])

# 正规block的名字提取
#	if line.startswith('name ='):
#		print(line[7:].replace("\n",""))

# 非正规block的名字提取，提取[]之内的名字
#	if line.startswith('['):
#		print(line.replace("[","").replace("]","").replace("\n",""))