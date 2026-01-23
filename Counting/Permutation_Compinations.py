from math import factorial

def permutaion(n,r):
    if 0<= r and r <= n:
        return factorial(n)//factorial(n-r)
    return False

def combination(n,r):
    if 0<= r and r <= n:
        return factorial(n)//(factorial(r)*factorial(n-r))


print(combination(9,7))

print(([(x,y,z) for x in range(1,10) for y in range(1,10) for z in range(1,10) if x+y+z==7]))