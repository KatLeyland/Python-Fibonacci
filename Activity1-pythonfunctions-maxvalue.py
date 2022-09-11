"""Write 2 Python functions to:

show the list content.
find the max value in the list.
Sample List : [10, 2, 3, 4, 7]

Expected Output :

The content of the list is: [10, 2, 3, 4, 7]

The max value in the list: 10"""


def find_max_value():  # create function
    max_value = 0  # set initial value to compare against
    for numbers in list:
        if numbers > max_value:
            max_value = numbers  # compare each number to current highest value,
            # if new number greater than that becomes max
        else:
            return  # otherwise move on to next number in list
        print("The max value in the list :", max_value)  # print final max value (comma to join string and int)


list = [10, 2, 3, 4, 7]
print("The content of the list :", list)
find_max_value()

list = [249, 923, 23, 853, 11]
print("The content of the list :", list)
find_max_value()
# fix first two highest values showing
