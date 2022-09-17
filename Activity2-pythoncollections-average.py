"""Write a Python program to calculate the average value of a list elements.

Test Data:

Sample List: [20, 30, 25, 35, -16, 60, -100]

Expected Output: Average value of the list elements is : 7.7."""

mylist=[20, 30, 25, 35, -16, 60, -100]
total = sum(mylist)
len = len(mylist)
avg = total / len
print("Average value of the list elements is :", avg)