import math
cc=[]
a1,b1=map(int,input().split())
c1=list(map(int,input().split()))
for i in range(b1):
    e1,f1=map(int,input().split())
    cc.append([e1,f1])
for j in cc:
     w=j[0]-1
     z=j[1]-1
     print(math.gcd(c1[w],c1[z]))
