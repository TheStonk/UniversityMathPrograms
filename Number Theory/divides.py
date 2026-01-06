def divides(num)->list:
    ans = []
    for i in range(1,(num//2)+1):
        #ans.append(gcd(num,i))
        if num%i == 0:
            ans.append(i)
    return ans
start = time.time()
print(divides(235967430))
print("done, ",time.time() - start)
