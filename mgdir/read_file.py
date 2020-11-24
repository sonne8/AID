"""
文件的读写
"""
# 打开文件
file = open("myfile", "r")

#读取文件
# data=file.read()
# print(data)
# while True:
#     data1 = file.read(3)
#     if data1 == "":
#     # if not data1:
#         break
#     print(data1,end="")

# line=file.readline(7)
# print(line)
# line=file.readline()
# print(line)

lines=file.readlines(7)
print(lines)

# for line in file:
#     print(line)




#关闭文件
file.close()