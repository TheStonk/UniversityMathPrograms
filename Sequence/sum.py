
def test(n):
    print(sum([(4/5)**x for x in range(1,n+1)])**2)
    print(4-((4**(n+1))/(5**n)))


test(10)