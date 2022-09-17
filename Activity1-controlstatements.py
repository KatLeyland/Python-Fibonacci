'''Write a Python program that accepts three numbers and prints "All numbers are equal"
if all three numbers are equal, "All numbers are different" if all three numbers are different
and "Neither all are equal or different" otherwise.

Test Data:

Input first number: 2
Input second number: 3
Input third number: 4

Expected Output :

All numbers are different.'''

#Get inputs
a=int(input("Enter first number "))
b=int(input("Enter second number "))
c=int(input("Enter third number "))

#Compare numbers
if a == b == c:
    print("All numbers are equal")
elif a != b and b != c and a != c:
    print("All numbers are different")
else:
    print("Neither all are equal or different")