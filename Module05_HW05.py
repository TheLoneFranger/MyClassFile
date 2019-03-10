"""
Name: Geoffrey Franger
Date: 3/09/19
Task: Assignment 05, Practice with Lists and Dictionaries
"""

# Open text file as r+
objFile2 = open(r"/Users/Geoffery/PycharmProjects/intro_to_python/Module05/Todo.txt", "r+")

# Read in rows. Strip line break characters from end. Split row at comma and separate values into a list
objFile2.seek(0)
readlist1 = objFile2.readlines()
print(readlist1)
# Create dictionary
myDict = {}

# Loop through list, extract key,value combinations and insert into dictionary
for Row in readlist1:
    rowlist = Row.rstrip('\n').split(',')
    myDict[rowlist[0]] = rowlist[1]

print('Welcome. Here are your options:\n----------------------------')
while(True):

    # print menu selections
    print('(1) Display All Records \n'
          '(2) Add a new Record\n'
          '(3) Delete a Record\n'
          '(4) Save Data to File\n'
          '(5) Exit Program\n')

    # prompt user for choice
    strUserSelect = input('Enter your selection (1-5): ')

    # if statement that will cycle through options. Elseif will be used for each option
    if strUserSelect == '1':  # user selects 1, print current list
        print('Here are the current records: \n--------------------------------')
        print(myDict)
        print('\nPlease choose another option:\n--------------------------------')

    elif strUserSelect == '2':  # user selects 2, prompt for new key and value
        strdictkey = input('Enter a chore: ')

        # if statement to check and see if the chore is already there
        if strdictkey not in myDict:
            strdictvalue = input('Enter the priority for that chore: ')
            myDict[strdictkey] = strdictvalue  # add new record to dictionary
            print('The record', strdictkey, ':', strdictvalue, 'has been added to dictionary.')
        else:
            print('That chore is already captured. Please try again.')
        print('\nPlease choose another option:\n--------------------------------')

    elif strUserSelect == '3':  # user selects 3, print and prompt for key of record to delete
        while(True):
            print('Here are the current records:\n--------------------------------')
            print(myDict)
            strdictdelete = input('Please enter which chore to delete: ')
            if strdictdelete not in myDict:
                print('You entered an invalid chore. Please try again')
            else:
                del myDict[strdictdelete]
                print('The chore', strdictdelete, 'has been deleted')
                break
        print('\nPlease choose another option:\n--------------------------------')

    elif strUserSelect == '4':  # user selects 4, save dictionary into file

        # loop through dictionary, write key and value
        for MyKey, MyValue in myDict.items():
            # print('\n'+str(MyKey)+','+str(MyValue)) --for troubleshooting
            objFile2.write('\n'+str(MyKey)+','+str(MyValue))
        print('Dictionary has been written to file Todo.txt')
        print('\nPlease choose another option:\n--------------------------------')

    elif strUserSelect == '5':  # exit while loop
        break
    else:
        print('The value you entered is not valid. Please try again')

# save any values written to file and close file
objFile2.close()
print('You chose to exit. This is the end of the program')


