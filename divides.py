def divides(num)->list:
    ans = []
    for i in range(1,(num//2)+1):
        if num%i == 0:
            ans.append(i)
    return ans
print(divides(27))