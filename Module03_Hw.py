"""
Homework 3
Create a new program that asks the user for the name of a household item and then
asks for its estimated value.
Store both pieces of data in a text file called HomeInventory.txt
"""

# create/open txt file using open
objFile = open(r"/Users/Geoffery/PycharmProjects/intro_to_python/Module03/HomeInventory.txt", "a")

# info for the user
print('You will be prompted for a household item and its estimated value.'\
      '\nThose inputs will be stored in a text file called HomeInventory.txt'\
)
# prompt user for household item and estimated value
strUserInput = input('Enter a household item: ')
strUserInputTwo = input('What is the estimated value for that item? Enter a number only: ')

# general print statement that reads back input to user
print('The '+strUserInput+' is worth roughly $' + strUserInputTwo+'. This will'\
    ' be written to the HomeInventory.txt file')

# print(strUserInput+" "+strUserInputTwo+"\n")
objFile.write(strUserInput+" "+strUserInputTwo+"\n")

# write inputs to file
objFile.close()
# close file and save inputs
