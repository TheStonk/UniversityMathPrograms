
def gcd(a,b):
    while(b!=0):
        r = a%b
        a = b
        b = r
    return(a)

def check(nums):
    for j,i in enumerate(nums):
        print(i)
        for t in (nums[j+1:]):
            temp = gcd(i,t)
            if (temp!=1):
                print(i," ",t," are not relative prime, they share a divider", temp)
                return False
    return True
            
print(check([8,9, 35]))
        
