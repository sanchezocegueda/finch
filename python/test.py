from wff import *

A = SentenceSymbol("A")
B = SentenceSymbol("B")
C = SentenceSymbol("C")
X = SentenceSymbol("A")

print(is_equal(A, B))
print(is_equal(A, X))

wff1 = And(A, B)
wff2 = And(A, B)
wff2 = Or(A, And(B, C))

print(is_equal(wff1, wff2))
print(wff2)