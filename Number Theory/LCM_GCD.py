

def gcd(a,b):
    while(b!=0):
        r = a%b
        a = b
        b = r
    return(a)

def gcd_lcm(a,b):
    g = gcd(a,b)
    print("Greast common divider: ", g)
    print("least common multible: ", (a*b)//g)
    
gcd_lcm(7,5)