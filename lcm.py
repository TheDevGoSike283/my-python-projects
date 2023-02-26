print("Enter a number: ")
num1 = int(input())
print("Enter another number: ")
num2 = int(input())
result1 = num1
while result1 % num2 != 0:
    result1 = result1 + num1
print("The lowest common multiple of your numbers is " + str(result1) + ".")
