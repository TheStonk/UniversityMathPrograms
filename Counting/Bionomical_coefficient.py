from math import factorial

def coefficient(n:int,j:int,a_coefficent:int=1,b_coefficient:int=1)->int:
    return((factorial(n)//(factorial(j)*factorial(n-j)))*(a_coefficent**(n-j)*b_coefficient**j))


print(coefficient(17,9,3,2))    