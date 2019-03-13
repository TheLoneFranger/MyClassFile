"""
HW4
1. Create new program that asks the user for the name of a household item,
and then asks for its estimated value. (This project is similar to the last one!)
2. Ask the user for new entries and store them in the 2-dimensional Tuple
(see programming notes for a hint)
3. When the program exits, ask the user if they would like to save/add the data
to a text file called, HomeInventory.txt.
4. Turn in your python script and HomeInventory.txt
"""
# prompt user for item, string
strItem = input('Please enter a household item:')

# prompt user for estimated value, float
intItem = int(input('What is the estimated value of that item? (nearest whole $US):'))

# first tuple to fill table
tplone = (strItem,intItem)

# define and insert first entry into tuple table
tplItemTable = (tplone),

while(True):
    # prompt y/n for more entries
    strEntries = input('Would you like to add another entry? (Y/N):').lower()

    # if no, break while loop
    if(strEntries == 'n'): break
    # create tuple table, 2D, append to with recent tuple

    # prompt user for item, string
    strItem = input('Please enter a household item:')

    # prompt user for estimated value, float
    intItem = int(input('What is the estimated value of that item? (nearest whole $US):'))

    # insert into new tuple
    tplItem = (strItem, intItem),

    # append tplItem to running tuple table tplItemTable
    tplItemTable += tplItem

# prompt for saving/adding data to homeinventory.txt file
# first time file will be created and populated with first series of entries
# every time after, file will be appended to. how do we handle this?
strSave = input('Would you like to save your entries to a file called HomeInventory? (y/n):').lower()


# if yes, open/create homeinventory file using open function
# loop through records (tuples) and adds them to file
# close connection to save changes
if(strSave == 'y'):
    # open/create HomeInventory file, append so current entries arent wiped
    objFile = open(r"/Users/Geoffery/PycharmProjects/intro_to_python/Module04/HomeInventory.txt", "a")
    # for each Tuple in the the tplItemTable, loop through and write each to file
    for Row in tplItemTable:
        print('\n', Row)
        objFile.write(str(Row)+'\n')

    # Save inputs and close file
    objFile.close()
    print('\n The above values have been saved to HomeInventory.txt file')
else:
    print('\nNo values will be saved to file')

print('\nThis is the end of the program.')