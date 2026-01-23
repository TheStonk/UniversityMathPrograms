
def recursive_sequence(n):
    #Base cases
    if n == 1:
        return 1
    if n == 2:
        return 2
    #recursive step
    return recursive_sequence(n-1)/recursive_sequence(n-2)
    
print([recursive_sequence(x) for x in range(1,30)])
    