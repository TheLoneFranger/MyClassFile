"""
Name: Geoffrey Franger
Date: 3/09/19
Task: Assignment 08, Work With Functions
1. Using your script from HW6, wrap all of your functions inside of a class.

2. Use if __name__ == '__main__' at the end of your script to run the menu function that does the following:

- instantiates the class your created

- runs the functions inside your class as they are selected by menu option
"""


class Data(object):
    # --Fields--
    # lstTable = []
    # dicRow = {}
    # objFile = open(r"/Users/Geoffery/PycharmProjects/intro_to_python/Module06/Todo.txt", "r+")

    # --Constructor--
    def __init__(self, lstTable = [],
                 dicRow = {},
                 objFile = open(r"/Users/Geoffery/PycharmProjects/intro_to_python/Module06/Todo.txt", "r+")
                 , struserinput = None):
        # Attributes
        self.__lstTable = lstTable
        self.__dicRow = dicRow
        self.__objFile = objFile
        self.__struserinput = struserinput

    # --Properties--
    #lstTable
    @property
    def lstTable(self):
        return self.__lstTable

    @lstTable.setter
    def lstTable(self, Value):
        self.__lstTable = Value

    #dicRow
    @property
    def dicRow(self):
        return self.__dicRow

    @dicRow.setter
    def dicRow(self, Value):
        self.__dicRow = Value

    # objFile
    @property
    def objFile(self):
        return self.__objFile

    @objFile.setter
    def objFile(self, Value):
        self.__objFile = Value

    # struserinput
    @property
    def struserinput(self):
        return self.__struserinput

    @struserinput.setter
    def struserinput(self, Value):
        self.__struserinput = Value

    # --Methods--
    def OpenFile(self):
        for line in self.objFile:
            strData = line.split(",")
            self.dicRow = {"Task": strData[0].strip(), "Priority": strData[1].strip()}
            self.lstTable.append(self.dicRow)
        self.objFile.close()
        return self.lstTable

    def Menu(self):
        # print menu selections
        print("---------Menu---------")
        print('(1) Display All Records \n'
              '(2) Alter Current List\n'
              '(3) Save Data to File\n'
              '(4) Exit Program\n')

        # prompt user for choice
        self.struserinput = str(input('Enter your selection (1-4): ').strip())
        return self.struserinput

    def CurrentList(self):
        print("This is your current list\n")
        for row in self.lstTable:
            print(row["Task"] + "(" + row["Priority"] + ")")

    def AlterList(self):
        # dictRow = {}
        while True:
            self.CurrentList()
            stralter = input('Would you like to (a)dd or (r)emove a task? Or (e)xit?: ').strip().lower()
            if stralter == 'a':  # add a record
                strdictval1 = input('Enter a task: ').strip().lower()
                strdictval2 = input('Enter the priority for that chore: ').strip().lower()
                self.dictRow = {"Task": strdictval1, "Priority": strdictval2}  # add new record to dictionary
                self.lstTable.append(self.dictRow)
                self.CurrentList()
                break
            elif stralter == 'r':  # remove a record
                self.CurrentList()
                strremove = input('Which task would you like to remove:').strip().lower()
                blnItemRemoved = False  # initialize boolean variable for later use
                intRowNumber = 0  # initialize looping variable
                while (intRowNumber < len(self.lstTable)):
                    # (adopted from HW5 answer) loop through values in row searching for input
                    if (strremove == str(list(dict(self.lstTable[intRowNumber]).values())[0])):
                        del self.lstTable[intRowNumber]  # delete row
                        blnItemRemoved = True
                    intRowNumber += 1
                    if (blnItemRemoved == True):  # boolean variable to tell user record was removed
                        print("The task was removed.")
                        break
                    else:
                        continue
            elif stralter == 'e':  # user doesnt want to add or remove a record
                print("You have chosen to exit.")
                break
            else:  # bad user input
                print('Please choose a valid input (a, r, e)')
                continue

    def SaveList(self):
        strsaveprompt = input("Would you like to save the list? (y/n)").strip().lower()
        if strsaveprompt == 'y':
            objFile = open(r"/Users/Geoffery/PycharmProjects/intro_to_python/Module06/Todo.txt", "w")
            for dicRow in self.lstTable:
                objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
            objFile.close()
            print("Data saved to file")
        else:
            print("You chose to not save the data but inputs still exist.")
        # return self.CurrentList()

    def main(self):
        """Main function"""
        obj1 = Data()  # instantiate object
        obj1.OpenFile()  # open file and read in data
        while True:
            obj1.Menu()
            if obj1.struserinput == '1':
                obj1.CurrentList()
                print("----------------------")
                continue
            elif obj1.struserinput == '2':
                obj1.AlterList()
                continue
            elif obj1.struserinput == '3':
                obj1.SaveList()
            elif obj1.struserinput == '4':
                break
            else:
                print("please choose a valid entry")
                continue

# --End of class--