def gcd(a,b):
    while(b!=0):
        r = a%b
        a = b
        b = r
    return(a)

def coprime(i:int):
    b = 2
    while(b<i and gcd(i,b)!= 1):
        b+=1
    if i>b: return b
    return False

print(coprime(3249320))