'''Write a Python program to get the Fibonacci series between 0 to 50.

Note :The Fibonacci Sequence is the series of numbers : 0, 1, 1, 2, 3, 5, 8, 13, 21, ....

Every next number is found by adding up the two numbers before it.'''

a = 0 #set initial two numbers
b = 1
print(a) #print initial 2 numbers
print (b)
while a + b < 50: #limit to numbers below 50
    c = a + b #creates third number
    a = b #second number becomes a
    b = c #third number becomes b
    print(c) #prints third number on first run then subsequent numbers







