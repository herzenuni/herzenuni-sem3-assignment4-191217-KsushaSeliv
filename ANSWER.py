import itertools
lst=[1,9,-20,-8,7,14,0,20,20,-20]
a=list(itertools.combinations(lst,3))
print(a)
mul1=0
for comb in a:
 mul=comb[0]*comb[1]*comb[2]
 if mul1 > mul:
   mul1=mul
print(mul1)
