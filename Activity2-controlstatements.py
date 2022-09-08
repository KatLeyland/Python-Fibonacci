'''Write a Python program that accepts three numbers from the user and prints
"Increasing order" if the numbers are in the increasing order, "Decreasing order"
if the numbers are in the decreasing order, and "Neither increasing or decreasing
order" otherwise.

Test Data:

Input first number: 1524
Input second number: 2345
Input third number: 3321

Expected Output :

Increasing order.'''

#Get input
a=int(input("Enter first number "))
b=int(input("Enter second number "))
c=int(input("Enter third number "))


if a < b < c: #increasing
    print("Increasing order")
elif a > b > c: #decreasing
    print("Decreasing order")
else: #otherwise
    print("Neither increasing or decreasing order")