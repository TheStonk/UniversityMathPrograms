import math
def modexp(a,k,n):
    if k<0: raise("k cant be less then zero")
    if k == 0: return 1
    if k&1 == 1:
        return((a*modexp(a,k-1,n))%n)
    else:
        c = modexp(a,k//2,n)
        return(c*c)%n
    
print(modexp(423,17,1517))