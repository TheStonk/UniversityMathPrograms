import doctest
import ast
import re
import sys
#for _ in matrix:
#    print(_)
letters = []
w = 15 # coolum width


def rMatrix(A,B):
    return [[1 if A[c] == B[r] or A[c] == -B[r] else 0 for c in range(len(A))] for r in range(len(B))]
def relation(A,B):
    return {(a,b) for a in A for b in B if a<b}

def isTransitive(R):
    for (a,b) in R:
        for (x,c) in R:
            if b == x and (a,c) not in R:
                    return False
    return True

def isReflexive(R):
    if not(R): return False
    for (a,b) in R:
        if (a,a) not in R:
         return False
    return True


def isSymmetric(R):
    for (a,b) in R:
        if (b,a) not in R:
            return False
    return True

def isAntiSymmetric(R):
    for (a,b) in R:
        if (b,a) in R and a != b:
            return False
    return True

def rClose(R:set):
    for (a,b) in R:
        if (a,a) not in R:
            R.update((a,a))
    return R
def sClose(R:set):
    for (a,b) in R:
        if (b,a) not in R:
            R.update((b,a))
    return R
def tClose(R:set):
    R1 = {t for t in R}
    for (a,b) in R:
        for (x,c) in R:
            if b == x and (a,c) not in R1:
                R1.update((a,c))
    if R1 == R: return R1
    return tClose(R1)
def isEqual(Rel):
    return isTransitive(Rel) and isSymmetric(Rel) and isReflexive(Rel)

def isPartial(Rel):
    return isAntiSymmetric(Rel) and isReflexive(Rel) and isTransitive(Rel)

def test(label,Rel:set):
    print(f'{chr(label+97)} ==> {isReflexive(Rel):^{w}}{isSymmetric(Rel):^{w}}{isAntiSymmetric(Rel):^{w}}{isTransitive(Rel):^{w}}{isEqual(Rel):^{w}}{isPartial(Rel):^{w}}')
def inputer():
    print("Write the relations, then press Ctrl-Z")
    x = sys.stdin.read()
    x = re.sub(r"\s*","",x)
    print("iran")
    y = re.findall(r"{\([^()],[^()]\)(?:,\([^()],[^()]\))*}",x)
    print(f'Label  {"Reflexsive":^{w}}{"Symmetric":^{w}}{"Antisymmetric":^{w}}{"Transitive":^{w}}{"Equivalent":^{w}}{"Partial":^{w}}')
    for k,l in enumerate(y):
        test(k,set(ast.literal_eval(l)))
    inputer()
inputer()
