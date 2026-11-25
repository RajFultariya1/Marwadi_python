#r+ = read and write
file = open("security_log.txt","r+")
file.write("r+ mode:")
print(file.read())
file.write("additional data using r+ mode \n")
file.close()

#w+ = write and read mode
file = open("security_log.txt","w+")
file.write("security report \n")
file.write("threat analysis completed \n")
file.seek(0)
print("w+ mode:")
print(file.read())
file.close()
#a+ = append and read mode
file = open("security_log.txt","w+")
file.write("security report updated\n")
file.seek(0)
print("a+ mode:")
print(file.read())
file.close()