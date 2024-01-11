filename = input("Enter File name: ")


file_extenstion=filename.split(".")

print("youe file extenstion is ",file_extenstion[-1])

f = open(filename, "x")
f.write("hello my name is Malay Thakkar. what's your?")

f = open(filename, "r")
print(f.read())

f.close()

