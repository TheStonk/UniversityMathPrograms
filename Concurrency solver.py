def mul_inverse(b,n):
    (r1,r2) = (n,b)
    t1 = 0
    t2 = 1
    s1 = 1
    s2 = 0
    while r2 != 0:
        q = r1//r2
        (r1,r2) = (r2,r1%r2)
        (s1,s2) = (s2,s1-q*s2)
        (t1,t2) = (t2,t1-q*t2)
    if r1 != 1: return False
    return (t1%n)

def solver(a,b,m):
    i = mul_inverse(a,m)
    x = (i*b)%m
    return x
def hand(a,b,m):
    print(a,"*",solver(a,b,m),"≡",b, "mod" ,m)
    print("x is ", solver(a,b,m))
    
hand(89,2,232)