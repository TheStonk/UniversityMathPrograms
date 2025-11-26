from functools import reduce 

class System_solver: 

  def __init__(self, c, a, m):
    self.c = c%m
    self.a = a%m
    self.m = m
    
  def solve(self, x):
    return (x*self.c)%self.m == self.a
    
def find(cil):
  reducer = reduce(lambda acc, ci: acc*ci.m, cil, 1)+1
  for x in range(0, reducer):
    if reduce(lambda acc, ci: acc and ci.solve(x), cil, True):
      return x
        
print(find([System_solver(1,1,20),System_solver(1,2,44)]))