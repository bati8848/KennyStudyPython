path_folder=input('please input the folder:  ')
path_filename=input('please input the filename with extension:  ')
path=path_folder+'\\'+path_filename     # 文件名拼接

if path_folder.__contains__('C:\\'):
    str(path_folder).replace('C:\\','aaa')
    print(1)
elif path_folder.__contains__('D:\\'):
    str(path_folder).replace('D:\\','D:\\\\')
    print(2)

print(path_folder)

