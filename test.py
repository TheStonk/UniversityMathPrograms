import time

start_time = time.time()
v = 2
arrr = [[False]*v for _ in range(2**v)]

def truthtable (n, arr):
    for i in range (0 , n):
        for j in range (0,2**n):
            arr [j][i] = (j>>n-(i+1)) & 1 == 0
    return arr
arrr = truthtable(v, arrr)
print("time to create table: ",time.time()-start_time)



   