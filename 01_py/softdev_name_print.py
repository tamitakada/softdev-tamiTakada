# Tami Takada, Tina Nyugen, Naomi Naranjo
# SoftDev
# A function that prints the name of a student from either period 1 or 2, at the index-th position in the list of all students for that period when sorted alphabetically.
# 2021-09-22

# Summary:
# Discoveries:
# Questions: N/A
# Comments: N/A

def printNames(period, index):
    pds = []
    
    for i in range(2):
        pd = []
        fileName = 'softdev_students_pd' + str(i + 1) + '.txt'
        
        with open(fileName) as reader:
            name = reader.readline()
            while name != '':
                pd.append(name.rstrip('\n'))
                name = reader.readline()
        
        pd.sort()
        pds.append(pd)
        
    if period > 0 and period < 3:
        if index < len(pds[period - 1]):
            print(pds[period - 1][index])
        else:
            print('Student does not exist')
    else:
        print('Period does not exist')
