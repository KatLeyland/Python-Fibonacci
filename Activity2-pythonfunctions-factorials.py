'''Write a Python function to calculate the factorial of a number
(a non-negative integer n ). The function accepts the number as an argument.

Note:
The factorial of a number is the product of all the integers from 1 to that
number and it is represented by n!

For example, the factorial of 6! is 1*2*3*4*5*6 = 720.

The factorial is not defined for negative numbers, and the factorial of zero is one, 0! = 1.'''


def factorial():
    number = int(input("Input integer : "))
    if number == 0:
        print('0! = 1')
    else:
        n = number
        a = number
        while number > 2:
            number -=1 #creates each integer
            b = a * number #previous value of number multiplied by current
            a = b # a becomes n bringing current running total returns to top of loop
    print(n,'! = ', b)

factorial()