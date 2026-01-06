"""
def gcd(a,b):
    while(b!=0):
        r = a%b
        a = b
        b = r
    return(a)



print("Greatest common divider is ",gcd(1000,625))
"""

def extended_euclidean(a,b):
    (r1,r2) = (a,b)
    (t1,t2) = (0,1)
    (s1,s2) = (1,0)
    while r2 != 0:
        q = r1//r2
        (r1,r2) = (r2,r1%r2)
        (s1,s2) = (s2,s1-q*s2)
        (t1,t2) = (t2,t1-q*t2)
    print("Bezout coefficients:", s1, t1)
    print("greatest common divisor:", r1)
    print("quotients:", t2, s2)
    
extended_euclidean(1000,625)