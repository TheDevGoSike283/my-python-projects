from colorama import Fore
print(Fore.BLUE + "Type a word and I'll check if it is a palindrome: ")
x = input()
y = ""
for i in range(len(x) - 1, -1, -1):
	y += x[i]
if x == y:
    print(Fore.GREEN + x + " is a palindrome.")
else:
    print(Fore.RED + x + " is not a palindrome.")
