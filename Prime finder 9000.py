
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

def sieve(limit):
    arrs = [i for i in range(2,limit)]
    li = math.sqrt(limit)+1
    i = 0
    while arrs[i]<=li:
        for j in arrs[i+1:]:
            if j%arrs[i] == 0:
                arrs.remove(j)
        i+=1
    print("prime list generated")
    return arrs

"""pri = sieve(100000)
leng = len(pri)
print(leng)
ind = 50
while ind < leng:
    #x = random.randint(2**3317, 2**3318)
    x = 2**pri[ind]- 1
    if isprime(x,10):
        print("prime found: ", pri[ind])
        file.writelines(str(pri[ind]) + "\n")
    ind+=1
file.close()
"""
#x = random.randint(2**30000, 2**30001)
#x = random.randint(12, 1000000)
#while not(isprime(x,10)):
#    print("go")
#    x = random.randint(2 ** 30000, 2 ** 30001)
#    #x = random.randint(12,1000000)
#print("prime found: ", x)
#file.writelines(str(x))
#file.close()

print(isprime(98764321261,10))