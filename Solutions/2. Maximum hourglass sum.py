import math
import os
import random
import re
import sys

#logic for the hourglass problem
def hourglassSum(arr):
    max_sum = -10000
    for i in range (len(arr)-2):
        for j in range (len(arr)-2):
            total = (arr[i][j]+arr[i][j+1]+arr[i][j+2])+ (arr[i+1][j+1])+(arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]);
            max_sum = max(max_sum, total)
    return max_sum

arr[][] = input()
