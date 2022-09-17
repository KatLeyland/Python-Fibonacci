"""Write a Python program to find the maximum and minimum value of a list.

Test Data:

Sample List: [25, 14, 56, 15, 36, 56, 77, 18, 29, 49]

Expected Output:

Original List: [25, 14, 56, 15, 36, 56, 77, 18, 29, 49]

Maximum value for the above list = 77

Minimum value for the above list = 14"""


mylist = [25, 14, 56, 15, 36, 56, 77, 18, 29, 49]
print ("Original List: ", mylist) # print list
maxValue = max(mylist)
print("Maximum value for the above list = ", maxValue)
minValue = min(mylist)
print("Minimum value for the above list = ", minValue)