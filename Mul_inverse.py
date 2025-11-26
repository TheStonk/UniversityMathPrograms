def mul_inverse(b,n):
    (r1,r2) = (n,b)
    t1 = 0
    t2 = 1
    s1 = 1
    s2 = 0
    print("\\displaylines{")
    while r2 != 0:
        q = r1//r2
        (r1,r2) = (r2,r1%r2)
        stemp = s1 #FOR PRINT
        (s1,s2) = (s2,s1-q*s2)
        ttemp = t1 # FOR PRINT
        (t1,t2) = (t2,t1-q*t2)
        # PRINT STEPS
        print(stemp,"-",s1,"\\cdot",q,"=",s2,",\:",stemp,"-",t1,"\\cdot",q,"=",t2," \\\ ")
        
    print("t_{1} \\bmod n = \\bar{a}\\to",t1,"\\bmod",n,"=",t1%n)
    print("}")
    if r1 != 1: return False
    return (t1%n)

print(mul_inverse(9,10))
