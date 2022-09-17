"""Write a Python function that takes a number as a parameter and check the number is prime or not.
Note:
Prime numbers are the numbers that are only divisible by themselves and 1, in other words,
if we try to divide them by another number, the result is not a whole number.
So, if we divide the number by anything other than 1 or itself, we will get a remainder that is not zero.
Negative numbers can not be prime."""


def primeOrnNo():
    number = int(input("Input your number here: "))
    if number < 0:
        print("Negative numbers can not be prime") # Weed out the negative Nancy's
    else:
        for i in range (1, number): #i is each number from 1 to the input
            if number % i == 0: #divide number by every lower number to test. If no remainder then not prime
                print("The number is not Prime")
                break   #if it's not prime then can stop running code
            else:
                print("The number is prime")
                break


primeOrnNo()  #run function