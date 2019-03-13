"""
Create an application to hold data
Add Code that lets users append a new row of data
Add a loop that lets the user keep adding rows
Askt ehuser if they want to save the data to a file
Save the data to a file if they say yes
Using lists that will be combined into a greater list
"""

# define the three rows
list1 = ['1', 'Bob Smith', 'BSmith@hotmail.com']
list2 = ['2', 'Sue Jones', 'SueJ@yahoo.com']
list3 = ['3', 'Joe James', 'JoeJames@gmail.com']

# combine seperate list records into table
listTable = [list1, list2, list3]
print('This is your current list \n', listTable)
# while loop that runs until user doesnt want to add any more lists
while(True):
    newrow = input('\n Would you like to add another row? (y/n):').lower()
    if newrow == 'n': break # if no, then exit the loop and move on
    else: # otherwise, prompt for new list inputs and insert into list
        lstId = str(input('Enter the ID you wish to insert:'))
        lstName = input('Enter the name you wish to insert:')
        lstEmail = input('Enter the email address you wish to insert:')
        newlst = [lstId, lstName, lstEmail]

        # insert newlst into listTable
        listTable.insert(0,newlst)

        # sort new list for display purposes
        listTable.sort()
        print("This is your new list \n", listTable)

# prompt user if they wish to save data to a file
saveprompt = input("Would you like to save the list to a file? (y/n) :").lower()
if saveprompt == 'n': print("This is the end of the program")
else:
    objFile = open(r"/Users/Geoffery/PycharmProjects/intro_to_python/Module05/Lab51.txt", "a")
    for Row in listTable:
        print('\n', Row)
        objFile.write(str(Row)+'\n')

    # close file and save inputs
    objFile.close()
    print('Your list has been saved in Lab51.txt file')

print('This is the end of the program')
