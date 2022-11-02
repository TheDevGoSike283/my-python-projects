import os
print("Type in a word: ")
word = input()
os.system("clear;")
for i in [*word]:
    os.system("echo -n \"" + i + "\"" + "; sleep 0.1")
print()
    

