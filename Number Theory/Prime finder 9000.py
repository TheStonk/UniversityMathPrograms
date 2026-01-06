
import math
import random
import sys
sys.set_int_max_str_digits(1000000)
primelist = []
file = open("C:/New folder/testtt.txt", "w")



def rectest (x,r,n):
    for j in range(0, r-1):
        x = pow(x,2,n)
        if x == 1 or x == n-1:
            return False
    return True
def isprime(n:int, k):
    if n & 1 == 0: return False
    d = n-1
    r = 0
    while d & 1 == 0:
        d //= 2
        r+= 1
    for i in range(k):
        a = random.randint(2,n-2)
        x = pow(a, d, n)
        if x != 1 or x != n - 1:
            if r < 0: return False
            if rectest(x, r, n): return False
    return True

print(isprime(98764321261,10))