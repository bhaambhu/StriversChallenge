from math import *
from collections import *
from sys import *
from os import *

from typing import List
from s import *

def setZeros(matrix: List[List[int]]) -> None:
	# Write your code here.
    rowsToSkip = set()
    colsToSkip = set()
    
    # First pass to find which rows and cols need to be zeroed
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            thisElement = matrix[i][j]
            if thisElement == 0:
                colsToSkip.add(j)
                rowsToSkip.add(i)
    
    # Second pass to actually zero them
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if x in rowsToSkip or y in colsToSkip:
                matrix[x][y] = 0
    return matrix

# setZeros([[1,2,3], [4,5,6]])
printMatrix(setZeros([[1,1,1],[1,0,1],[1,1,1]]), "Output")
setZeros([[0,1,2,0],[3,4,5,2],[1,3,1,5]])