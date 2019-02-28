#1. Using for loop, write and run a Python program to find factorial from 0 to 10.(And Using
# recursion).

def Factorial(n):
    if n >=1:
        return n* Factorial(n-1)
    else:
        return 1

def NumberFactorial():
    Numbers = list(range(0,10))

    for value in Numbers:
        factorial =1
        factorial = Factorial(value)
        print(" Factorial of {} is {} ".format(value,factorial))


NumberFactorial()

