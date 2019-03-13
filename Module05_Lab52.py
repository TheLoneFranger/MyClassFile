"""
Create an application to hold data
Add Code that lets users append a new row of data
Add a loop that lets the user keep adding rows
Askt ehuser if they want to save the data to a file
Save the data to a file if they say yes
Using dictionary records inside of a list
"""

# define the three dictionary records
dct1 = {'ID': '1', 'Name': 'Bob Smith', 'Email': 'BSmith@hotmail.com'}
dct2 = {'ID': '2', 'Name': 'Sue Jones', 'Email': 'SueJ@yahoo.com'}
dct3 = {'ID': '3', 'Name': 'Joe James', 'Email': 'JoeJames@gmail.com'}

# combine separate dictionary records into table
listTable = [dct1, dct2, dct3]

print('This is your current dictionary')
# For each row in the list table, listTable
for Row in listTable:
    print('\n')

    # now we are looking at just the items in the list, the dictionary records
    # myKey, myValue are variables that take the place of the items within the dictionaries.
    for myKey, myValue in Row.items():
        print(myKey, '=', myValue)

# while loop that runs until user doesnt want to add any more dictionaries
while True:
    newrow = input('\n Would you like to add another row? (y/n):').lower()
    if newrow == 'n':
        break  # if no, then exit the loop and move on
    else:  # otherwise, prompt for new list inputs and insert into list
        dctId = str(input('Enter the ID you wish to insert:'))
        dctName = input('Enter the name you wish to insert:')
        dctEmail = input('Enter the email address you wish to insert:')
        newdct = {'ID': dctId, 'Name': dctName, 'Email': dctEmail}

        # insert newlst into listTable
        listTable.insert(0, newdct)

        print("This is your new dictionary")

        for Row in listTable:
            print('\n')

            # now we are looking at just the items in the list, the dictionary records
            # myKey, myValue are variables that take the place of the items within the dictionaries.
            for myKey, myValue in Row.items():
                print(myKey, '=', myValue)

# prompt user if they wish to save data to a file
saveprompt = input("Would you like to save the list to a file? (y/n) :").lower()
if saveprompt == 'n':
    print("No records will be saved")
else:
    objFile = open(r"/Users/Geoffery/PycharmProjects/intro_to_python/Module05/Lab52.txt", "a")
    for Row in listTable:
        print('\n')

        # now we are looking at just the items in the list, the dictionary records
        # myKey, myValue are variables that take the place of the items within the dictionaries.
        for myKey, myValue in Row.items():
            print(myKey, '=', myValue)
            objFile.write(str(myKey)+': '+str(myValue)+'\n')

    # close file and save inputs
    objFile.close()
    print('Your list has been saved in Lab52.txt file')
print('This is the end of the program')