import math

def modexp(a,k,n,count):
    if k<0: raise("k cant be less then zero")
    if k == 0: return 1
    if k&1 == 1:
        if k != 1:
            count["odd"] += 1
        return((a*modexp(a,k-1,n,count))%n)
    else:
        count["even"] += 1
        c = modexp(a,k//2,n,count)
        return(c*c)%n
cou = {"even":0,"odd":0}
print(modexp(423,17,1517,cou))
print(cou)