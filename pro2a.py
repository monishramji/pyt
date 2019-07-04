from itertools import combinations
Number,K1=input().split()
K1=int(K1)
leng=[]
dd=combinations(Number,len(Number)-K1)
for i in list(dd):
  leng.append("".join(i))
print(min(leng))
