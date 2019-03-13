# declare and define tuples
tplData00 = ('ID', 'Name', 'Email')
tplData01 = (1, 'Bob Smith', 'BSmith@hotmail.com')
tplData02 = (2, 'Sue Jones', 'SueJ@yahoo.com')
tplData03 = (3, 'Joe James', 'JoeJames@gmail.com')

# combine tuples into tuple table
tplTableA = (tplData00, tplData01, tplData02, tplData03)

# add code that searches for customers by name and returns the row/customer id

# declare and set boolean variable for found/not found
blnFound = False

while(True):
    # prompt user for a name
    # case sensitive!
    strUser = input('Enter a name to search:')
    for Row in tplTableA:
        # print(Row)
        if strUser in Row:
            print('We found ', str(Row[1]), '. Their ID is', str(Row[0]), '.')
            blnFound = True

    if(blnFound == False):
        print("Customer",strUser,"not found.")

    strContinue = input('Would you like to continue? y/n:')
    if strContinue == 'n':
        print('Goodbye')
        break