import random

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
        if not (x == 1 or x == n - 1):
            if r < 0: return False
            if rectest(x, r, n): return False
    return True

def divides(num)->list:
    ans = []
    for i in range(1,(num//2)+1):
        if num%i == 0:
            ans.append(i)
    return ans
lol = int(input("Write a number to test:"))
if isprime(lol,10):
    print(lol, "is prime it is only divdes by", lol," ", 1)
else: print("it is not prime, it divedes by: ",divides(lol))