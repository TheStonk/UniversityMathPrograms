def mul_inverse(b,n):
    (r1,r2) = (n,b)
    t1 = 0
    t2 = 1
    s1 = 1
    s2 = 0
    while r2 != 0:
        q = r1//r2
        (r1,r2) = (r2,r1%r2)
        stemp = s1 #FOR PRINT
        (s1,s2) = (s2,s1-q*s2)
        ttemp = t1 # FOR PRINT
        (t1,t2) = (t2,t1-q*t2)
        # PRINT STEPS
        print(s2, "=", stemp,"-",s1,"*",q)
        print(t2,"=",stemp,"-",t1,"*",q)
    if r1 != 1: return False
    return (t1%n)

def solver(a,b,m):
    i = mul_inverse(a,m)
    return (i*b)%m

def hand(a,b,m):

    print("x is ", solver(a,b,m))
    
#Hvis du skal solve en opgave hvor du bliver givet, p, q og e
#Kan den løses ved at sige ex == 1 mod (p-1)(q-1)
# så i det her tilfælde er e = 17, ig (p-1)(q-1) = 1440
hand(17,1,1440)
