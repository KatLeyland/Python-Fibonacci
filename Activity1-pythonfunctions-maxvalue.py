'''Write 2 Python functions to:

show the list content.
find the max value in the list.
Sample List : [10, 2, 3, 4, 7]

Expected Output :

The content of the list is: [10, 2, 3, 4, 7]

The max value in the list: 10'''

def findMaxValue():    #create function
    maxValue = 0            #set initial value to compare against
    for numbers in list:
        if numbers > maxValue:
            maxValue = numbers          #compare each number to current highest value, if new number greater then that becomes max
        else:
            return   #otherwise move on to next number in list
        print("The max value in the list :", maxValue)  #print final max value (comma to join string and int)

list=[10, 2, 3, 4, 7]
print("The content of the list :", list)
findMaxValue()


list=[249, 923, 23, 853, 11]
print("The content of the list :", list)
findMaxValue()


