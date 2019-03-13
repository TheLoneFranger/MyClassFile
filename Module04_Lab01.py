"""
create application to that uses a two dimensional tuple to hold data
"""

# declare and define tuples
tplData00 = ('ID', 'Name', 'Email')
tplData01 = (1, 'Bob Smith', 'BSmith@hotmail.com')
tplData02 = (2, 'Sue Jones', 'SueJ@yahoo.com')
tplData03 = (3, 'Joe James', 'JoeJames@gmail.com')

# combine tuples into tuple table
tplTableA = (tplData00, tplData01, tplData02, tplData03)

# for loop to print tuples
for row in tplTableA:
    for item in row:
        print(item)

    # v1, v2, v3 = tplTableA[i]
    # print tuple value and line break with dividers ----
    # print(v1, '\n', str(v2), '\n', v3, '\n-------------------------\n')
    # print(tplTableA[i], "\n---------------------------------------")

# now add nested for loop to extract individual elements and change display

