'''Write a Python program to create the multiplication table (from 1 to 10) of a number.

Expected Output:
Input a number: 6
6 x 1 = 6
6 x 2 = 12
6 x 3 = 18
6 x 4 = 24
6 x 5 = 30
6 x 6 = 36
6 x 7 = 42
6 x 8 = 48
6 x 9 = 54
6 x 10 = 60'''

multiplicand = int(input("Input a number: ")) #Input for which table
factor = 1
while factor < 11:
    product = multiplicand * factor
    print(multiplicand,"x",factor,"=",product)
    factor += 1

