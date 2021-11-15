import numpy as np
import pandas as pd

#by Paul Court for SE512 HA 5 Problem 1
# This program will establish the 
# read from csv file
data = r'C:\Users\court\Google Drive\SCSU\SE 512\Assignments\HA 5\Problem_1_Data.txt'
Object = np.loadtxt(data)

#print (temp)
rows = Object.shape[0]
cols = Object.shape[1]

#Initialize matricies.
ManhattanDist = np.zeros([rows, rows])
TempObject = np.zeros([1, cols])
temp = 0.0
failSafe = 0
TempDist = np.zeros([rows, 1])
Ci = np.zeros([rows])
Cj = np.zeros([rows])

MoreIterations = True

def PopulateDistances(i, TempObject, Object, rows, cols): 
    for j in range (0, rows):
        for k in range (0, cols):
            temp = abs(TempObject[0, k] - Object[j, k])
            ManhattanDist[i,j] = "{:.2f}".format(ManhattanDist[i, j] + temp)
        Ci[j] = j + 1

def findMaxDist(ManhattanDist, Ci, Cj, rows):
    positionOfMax = 0
    for i in range (0, rows):
        for j in range (0, rows):
            temp = ManhattanDist[i, j]
            TempDist[i] = temp + TempDist[i]
        TempDist[i] = TempDist[i]/(rows - 1)
        if (i == 0):
            max = TempDist[i]
            positionOfMax =  1
        else:            
            if (TempDist[i] > max):
                max = TempDist[i]
                positionOfMax = i + 1
        print('The Average Distance for point ', i + 1, 'is:  ', TempDist[i])
    print('The initial point to be moved to Cj is: P', positionOfMax)
    print()
    Ci[positionOfMax - 1] = 0
    Cj[positionOfMax - 1] = positionOfMax
      
def findAveDist(ManhattanDist, Ci, Cj, rows):
    counti = 0
    countj = 0
    tempCi = np.zeros([rows])
    tempCj = np.zeros([rows])
    Flag = False

    for n in range (0, rows):
        if (Ci[n] != 0):
            tempCi[counti] = Ci[n]
            counti = counti + 1

        if (Cj[n] != 0):
            tempCj[countj] = Cj[n]
            countj = countj + 1
    print('Ci = ',Ci[np.nonzero(Ci)])
    print('Cj = ',Cj[np.nonzero(Cj)])

    for i in range (0, counti):
        sumi = 0
        sumj = 0
        for j in range (0, counti):
            index1 = int(tempCi[i]) - 1
            index2 = int(tempCi[j]) - 1
            sumi = sumi + ManhattanDist[index1, index2]
            
        print('For object : ', index1 + 1)
        print('sumi = ', sumi)
        for jj in range (0, countj):
            index3 = int(tempCj[jj]) - 1
            sumj = sumj + ManhattanDist[index1, index3]
            
        print('sumj = ', sumj)
        temp2 = sumi - sumj
        print ('temp2', temp2)
        temp1 = (temp2)/((counti - 1)*(countj))
        print('Average (sumi - sumj)/((counti)*(countj)) = ', "{:.4f}".format(temp1))
        print()
        if (temp1 > 0):
            Ci[index1] = 0
            Cj[index1] = index1 + 1
            Flag = True
    return Flag
            
#Main Program for hierarchical clustering algorithm using MIN strategy and draw the dendrograms.

print('The original Data set is: ')
print()
print(Object)
print()

for i in range (0, rows): 
    TempObject[0, :] = Object[i, :]
    PopulateDistances(i, TempObject, Object , rows, cols)
    
print('The Manhattan distance matrix is: ')
print()
print(ManhattanDist)
print()
round = 0
print('Done with round: ', round, ', the intitial assignment.')

findMaxDist(ManhattanDist, Ci, Cj, rows)

while (MoreIterations == True):
    MoreIterations = findAveDist(ManhattanDist, Ci, Cj, rows)
    round = round + 1
    print('Done with round:', round)
    print('More iterations?',MoreIterations)
            
print('The final clusters are: ')
print('Ci = ',Ci[np.nonzero(Ci)])
print('Cj = ',Cj[np.nonzero(Cj)])

