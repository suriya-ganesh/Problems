#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha = list(alphabet)
    alpha_u = list(alphabet_u)

    st = list(s)
    arr = []
    result = ''

    for i in st:
        char = i
        if i not in alpha_u and i not in alpha:
            result += i
        else:
            if (char.isupper()): 
                result += chr((ord(char) + k -65) % 26 + 65)
            else: 
                result += chr((ord(char) + k - 97) % 26 + 97)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
