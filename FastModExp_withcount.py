import math

def modexp(a,k,n,count):
    if k<0: raise("k cant be less then zero")
    if k == 0: return 1
    if k&1 == 1:
        if k != 1:
            count["o"] += 1
        return((a*modexp(a,k-1,n,count))%n)
    else:
        count["e"] += 1
        c = modexp(a,k//2,n,count)
        return(c*c)%n
cou = {"e":0,"o":0}
print(modexp(43,13,1517,cou))
print(cou)