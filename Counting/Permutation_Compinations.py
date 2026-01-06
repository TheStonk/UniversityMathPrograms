from math import factorial

def perm(n,r):
    if 0<= r and r <= n:
        return factorial(n)//factorial(n-r)
    return False

def comp(n,r):
    if 0<= r and r <= n:
        return factorial(n)//(factorial(r)*factorial(n-r))

print(perm(100,3))
print(comp(52,5))

def other(n,r):
    result = n
    for i in range(1,r):
        print(n-i)
        result *= n-i
    return result

print(other(100,3))