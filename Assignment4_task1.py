import os 
a="sample.txt"
try:
    with open("sample.txt") as fh:
        content=fh.read()
        print(content)
except FileNotFoundError:
    print(f"The file '{a}' was not found.") 