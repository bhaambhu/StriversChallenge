from typing import List


def printMatrix(matrix = List[List[int]], title=None) -> None:
    # Print title if exists
    if title:
        print(title, ":")
    
    # If matrix is empty
    if len(matrix) == 0:
        print([])
    
    # Print dat matrix
    for i in matrix:
        print(i)
