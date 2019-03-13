"""
Lab 3
Create a script that lets a user add two numbers together and saves the answer to a file
Let the user continue adding numbers together until they type exit
"""

# create/open txt file using objfile.Open
objFile = open(r"/Users/Geoffery/PycharmProjects/intro_to_python/Module03/Lab03.txt", "a")

# nfo for the user
print('You will be prompted for two numbers.'\
      '\nThey will be added together and the result written to a file'\
      ' called Lab03.txt'
)
while(True):
    strUserInput = input('Enter your first number: ')
    if(strUserInput == 'exit'): break
    else: intUserInput = int(strUserInput)
    strUserInputTwo = input('Enter your second number: ')
    if(strUserInputTwo == 'exit'): break
    else: intUserInputTwo = int(strUserInputTwo)
    intSum = intUserInput + intUserInputTwo
    print('The value '+str(intSum)+' will be written to the file')
    # print(strUserInput + ', ' + strUserInputTwo + ', ' + str(intSum))
    objFile.write(str(intSum)+"\n")
    # write strSum to file
objFile.close()
# close file and save inputs
print('You have chosen to exit. Inputs have been saved in file. Auf wiedersehen!')