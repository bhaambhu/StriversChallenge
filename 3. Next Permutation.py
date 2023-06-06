from os import *
from sys import *
from collections import *
from math import *
from typing import List

def nextPermutation(nums: List[int]) -> None:
        return nums

print(nextPermutation([1,2,3]))
print(nextPermutation([1,3,2]))

# 1 2 5 4 3 -> 1 5 2 4 3 -> 1 5 2 3 4
# 1 3 5 4 2 -> 1 5 3 4 2 -> 1 5 3 2 4 -> 1 5 2 3 4
# 5 4 3 2 1 -> 1 2 3 4 5
# 5 3 4 2 1 -> 5 4 1 2 3
# 5 4 3 1 2 -> 5 4 3 2 1
# 5 3 4 1 2 -> 5 3 4 2 1