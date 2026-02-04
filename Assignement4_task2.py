import os
a=input("Enter text to write to the file:")

with open("output.txt","w") as fh:
    fh.write(a+"\n")
print("\n Data successfully written to output.txt")

b=input("Enter additional text to append:")

with open("output.txt","a") as fh:
    fh.write(b +"\n")

print("\n Data Successfully appended.\n")

print("Final Content of output.txt:\n")

with open("output.txt","r") as fh:
    print(fh.read())

