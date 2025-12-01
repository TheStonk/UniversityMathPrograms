from math import gcd, lcm

import math

# meget simpel primesøgning (nok til dine øvelser)
def factorize(n):
    """
    Faktoriserer et heltal n i dets primfaktorer.

    Parametre
    ----------
    n : int
        Det tal, der skal faktoriseres.

    Returnerer
    ----------
    list
        En liste med primfaktorer af n, i stigende rækkefølge.

    Eksempel
    -------
    factorize(91) -> [7, 13]
    factorize(231) -> [3, 7, 11]
    """
    factors = []
    f = 2
    while f * f <= n:
        while n % f == 0:
            factors.append(f)
            n //= f
        f += 1
    if n > 1:
        factors.append(n)
    return factors


def is_valid_rsa_keypair(N, e, d):
    """
    Tjekker om et RSA-nøglepar (public e, secret d) er gyldigt for et givet N.

    Parametre
    ----------
    N : int
        Modulus for RSA, produkt af to primtal.
    e : int
        Den offentlige eksponent fra public key.
    d : int
        Den private eksponent fra secret key.

    Returnerer
    ----------
    bool
        True hvis (e, d) er et gyldigt RSA-nøglepar for N, ellers False.
    """
    #   e er fra publik PK
    #   d er fra secret SK
    # trin 1: faktorisér N
    factors = factorize(N)

    # RSA kræver præcis to primtal
    if len(factors) != 2:
        print("For mange eller for få primtalsfaktorer")
        return False

    p, q = factors

    # trin 2: beregn φ(N)
    phi = (p - 1) * (q - 1)
    print(f"{p}, {q} det bliver altså; {e}*{d} % {phi} = {e*d%phi}")
    # trin 3: tjek e*d ≡ 1 mod φ(N)
    return (e * d) % phi == 1


# --- Eksempler fra opgaven ---
#tests = [
#    (91, 37, 23),
#    (143, 77, 53),
#    (231, 59, 47),
#    (107, 25, 30)
#]

#for N, e, d in tests:
#    print(N, e, d, "->", is_valid_rsa_keypair(N, e, d))


def sieve(n):
    """
    Finder alle primtal op til n ved hjælp af Eratosthenes' sigte.

    Parametre
    ----------
    n : int
        Det øverste tal der skal tjekkes for primtal.

    Returnerer
    ----------
    list
        En liste med alle primtal mindre end eller lig med n.
    """
    # Start med en liste hvor vi antager alle tal er primtal
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 og 1 er ikke primtal

    for i in range(2, math.isqrt(n) + 1):
        if is_prime[i]:
            # Fjern alle multipler af i
            for j in range(i*i, n+1, i):
                is_prime[j] = False

    # Lav en liste med de primtal vi har tilbage
    primes = [i for i, prime in enumerate(is_prime) if prime]
    print(f"{primes} {n} er {len(primes)}. element")

def mul_inverse(b,n):
    """
    Beregner den modulære inverse af b modulo n vha. den udvidede Euklidiske algoritme.

    Parametre
    ----------
    b : int
        Tallet der skal have en modulær inverse.
    n : int
        Modulus.

    Returnerer
    ----------
    int eller bool
        Den modulære inverse af b modulo n, eller False hvis den ikke findes.
    """
    (r1,r2) = (n,b)
    t1 = 0
    t2 = 1
    s1 = 1
    s2 = 0
    #print("\\displaylines{")
    while r2 != 0:
        q = r1//r2
        (r1,r2) = (r2,r1%r2)
        stemp = s1 #FOR PRINT
        (s1,s2) = (s2,s1-q*s2)
        ttemp = t1 # FOR PRINT
        (t1,t2) = (t2,t1-q*t2)
        # PRINT STEPS
        #print(stemp,"-",s1,"\\cdot",q,"=",s2,",\:",stemp,"-",t1,"\\cdot",q,"=",t2," \\\ ")
        
    #print("t_{1} \\bmod n = \\bar{a}\\to",t1,"\\bmod",n,"=",t1%n)
    #print("}")
    if r1 != 1: return False
    return (t1%n)

"""def phi_func(N):
    l = [i for i in range(0,N) if gcd(i,N) == 1]
    print(l)
    print(f"Der er {len(l)} tal mellem 1 og {N-1} som har GCD af 1 med {N}")
    return l

phi_func(12)

def gcd(a,b):
    
    Beregn den største fælles divisor (GCD) af to tal a og b
    ved hjælp af Euklids algoritme.

    Returnerer gcd(a, b).
    
    while(b!=0):
        r = a%b
        a = b
        b = r
    return(a)"""


def coprime(i:int):
    """
    Find det mindste tal b > 1 som er relativt primisk med i,
    dvs. gcd(i, b) = 1.

    Returnerer tallet b hvis det findes, ellers False.
    """
    b = 2
    while(b<i and gcd(i,b)!= 1):
        b+=1
    if i>b: return b
    return False


def extended_euclidean(a,b):
    """
    Beregn den udvidede Euklidiske algoritme for to tal a og b.

    Returnerer Bézout-koefficienterne (s, t) sådan at s*a + t*b = gcd(a, b),
    samt den største fælles divisor (gcd) af a og b.

    Udskriver også de mellemregninger (kvotienter) under processen.
    """
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
