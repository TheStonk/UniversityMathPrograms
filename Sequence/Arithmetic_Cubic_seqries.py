def ari_sequence(a1,d, n) -> list[int]:
    l = []
    for i in range(0,n):
        a = a1 + d*i
        l.append(a)
    return l

def geo_sequence(a1,r, n) -> list[int]:
    l = []
    for i in range(0,n):
        a = a1*(r**i)
        l.append(a)
    return l


def approaching_inf(a1,r,n=10000):
    for i in range (1, n):
        print(sum(geo_sequence(a1,r,i)))

#approaching_inf(270,1/3,100)

# sum of 0 to and including n.
s = 0
for j in range(0,8+1):
    #s += expression
    s += (2**(j+1)-2**j)

print(s)