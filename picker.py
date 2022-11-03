import random
import os
print("Type in mutiple inputs. When you're done, leave the input blank and press Enter.")
inparr = []
while True:
    inp = input()
    if inp == "":
        break
    inparr.append(inp)
print(random.choice(inparr))
