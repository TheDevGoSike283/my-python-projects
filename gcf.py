print("Enter a number: ")
num1 = int(input())
print("Enter another number: ")
num2 = int(input())
snum = num1
q = num2
rmd = num1 % num2
quo = (snum - rmd) / q
print("Steps to solve (with Euclid's division algorithm) Note that the last highlited number is the answer:")
print(str(snum) + " = \033[33;33m" + str(q) + "\033[0;m x " + str(quo) + " + " + str(rmd))
while not rmd == 0:
    snum = q
    q = rmd
    rmd = snum % q
    quo = (snum - rmd) / q
    print(str(snum) + " = \033[33;33m" + str(q) + "\033[0;m x " + str(quo) + " + " + str(rmd))

print("Greatest common factor is " + str(q) + ".")

