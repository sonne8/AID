file=open("myfile","w+")
file.write("先帝创业未半")
file.flush()

print(file.tell())
file.seek(6.0)
data=file.read()
print(data)

file.close()
