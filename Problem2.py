#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    c = 0
    m = 0
    for i in candles:
        if m < i:
            m = i
            c = 0
        if m == i:
            c += 1
    return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2, inti = True):
    if inti:
        if x1 > x2:
            return kangaroo(x2, v2, x1, v1, False)
        elif v2 > v1 or v1 == v2:
            return 'NO'
    if (x2 - x1)% (v2-v1)==0:
        return 'YES'
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    nt = 5
    nv = 0
    for i in range(n):
        nv += nt//2
        nt = (nt//2)*3
    return nv
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):
    n = str(k*sum([int(x) for x in n]))
    if len(n) == 1:
        return n
    else:
        return superDigit(n,1)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def cprint(arr):
    st = ""
    for i in range(len(arr)):
        if i == 0:
            st += str(arr[i])
        else:
            st += " " + str(arr[i])
    print(st)

def insertionSort1(n, arr):
    basev = arr[-1]
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > basev:
            arr[i + 1] = arr[i]
            cprint(arr)
        else:
            arr[i + 1] = basev
            cprint(arr)
            break
    if arr[0] > basev:
        arr[0] = basev
        cprint(arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)

	
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def cprint(arr):
    st = ""
    for i in range(len(arr)):
        if i == 0:
            st += str(arr[i])
        else:
            st += " " + str(arr[i])
    print(st)

def insertionSort2(n, arr):
    for i in range(len(arr)):
        if i==0:
            continue
        index = i - 1
        va = arr[i]
        while index >= 0 and arr[index] > va:
            arr[index + 1] = arr[index]
            index -= 1
        arr[index+1] = va
        cprint(arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)

