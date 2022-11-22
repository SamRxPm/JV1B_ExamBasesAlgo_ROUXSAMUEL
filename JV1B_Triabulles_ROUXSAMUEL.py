####/exo 1/####
myTable = [7,25,69,10]
score = 0

score = myTable[2]
myTable[2] = myTable[1]
myTable[1] = score

print(myTable)

####/exo 2/####
myTable = [2,9,4,7]
LePlusGrand = myTable[0]
Petit = 0
score = 0
for iteration in range(len(myTable)):
    if LePlusGrand < myTable[iteration]:
        score = LePlusGrand
        LePlusGrand = myTable[iteration]
        myTable[iteration] = score
        myTable.pop(iteration)
        myTable.append(LePlusGrand)
print (myTable)

####/exo 3/####
myTable = [7,25,69,10]
score = 0
Grand = 0
for i in range(len(myTable)):
    Grand = myTable[i]
    Placement = i
    for iteration in range(len(myTable)):
        if Grand < myTable[iteration]
         score =  Grand
         Grand = myTable[iteration]
         myTable[iteration] = score
         myTable.pop(iteration)
         myTable.append(Grand)
print(myTable)

####/exo 4/#### je ne sais pas, peut être à cause du déplacement des chiffre "grand"

