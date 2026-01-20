a = {1,2,3,4,34,534,534,5,345,34,534,1231,4}
b = {4,6,8,4,1,324,432,43,5,43,5,5,4}
c = {1,4,6,7,9,5,8,4,3,45}

print(a.difference({2,3}))

print(a.union(b).difference(b.union(c)))
print(a.difference(c))