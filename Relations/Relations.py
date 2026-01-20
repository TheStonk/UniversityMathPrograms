import doctest
import ast
import re
import sys
#for _ in matrix:
#    print(_)
letters = []
w = 15 # coolum width


def make_relation_matrix(A:set,B:set,relation)->list:
    #Creates matrix representation of relation 
    return [[1 if relation(A[i],B[j]) else 0 for i in range(len(A))] for j in range(len(B))]


def create_relation(A:set,B:set,relation)->set:
    #Create a binary relation, from two sets and a given   
    return {(a,b) for a in A for b in B if relation(a,b)}

def isTransitive(R:set)->bool:
    for (a,b) in R:
        for (x,c) in R:
            if b == x and (a,c) not in R:
                    return False
    return True

def isReflexive(R:set)->bool:
    if not(R): return False
    for (a,b) in R:
        if (a,a) not in R:
         return False
    return True


def isSymmetric(R)->bool:
    for (a,b) in R:
        if (b,a) not in R:
            return False
    return True

def isAntiSymmetric(R)->bool:
    for (a,b) in R:
        if (b,a) in R and a != b:
            return False
    return True

def reflexive_closure(R:set)->set:
    for (a,b) in R:
        if (a,a) not in R:
            R.update((a,a))
    return R
def symmetric_closure(R:set)->set:
    for (a,b) in R:
        if (b,a) not in R:
            R.update((b,a))
    return R
def tClose(R:set)->set:
    R1 = {t for t in R}
    for (a,b) in R:
        for (x,c) in R:
            if b == x and (a,c) not in R1:
                R1.add((a,c))
    if R1 == R: return R1
    return tClose(R1)
def isEqual(Rel:set)->bool:
    return isTransitive(Rel) and isSymmetric(Rel) and isReflexive(Rel)

def isPartial(Rel)->bool:
    return isAntiSymmetric(Rel) and isReflexive(Rel) and isTransitive(Rel)

def evaluate_relation(label,Rel:set)->None:
    print(f'{chr(label+97)} ==> {isReflexive(Rel):^{w}}{isSymmetric(Rel):^{w}}{isAntiSymmetric(Rel):^{w}}{isTransitive(Rel):^{w}}{isEqual(Rel):^{w}}{isPartial(Rel):^{w}}')


def from_file():
    relations = ""
    with open("Relations/input.txt") as f:
        relations = f.read()
    relations = re.sub(r"\s*","",relations)
    print("iran")
    list_of_relations = re.findall(r"{\([^()],[^()]\)(?:,\([^()],[^()]\))*}",relations)
    print(f'Label  {"Reflexsive":^{w}}{"Symmetric":^{w}}{"Antisymmetric":^{w}}{"Transitive":^{w}}{"Equivalent":^{w}}{"Partial":^{w}}')
    for k,l in enumerate(list_of_relations):
        evaluate_relation(k,set(ast.literal_eval(l)))


#from_file()
print(tClose({(0,1),(1,1),(1,2)}))
#print(create_relation({1,2,3,4,5,6,7,8,9},{1,2,3,4,6,7,8,9},lambda a,b: a<b))