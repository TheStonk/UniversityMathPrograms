from math import factorial

def permutaion(n,r):
    if 0<= r and r <= n:
        return factorial(n)//factorial(n-r)
    return False

def combination(n,r):
    if 0<= r and r <= n:
        return factorial(n)//(factorial(r)*factorial(n-r))

print(combination(100,92))
print(permutaion(100,8))
print(combination(92,3)==permutaion(30,3)/6)
#print(factorial(17)//(factorial(7)*factorial(4)))