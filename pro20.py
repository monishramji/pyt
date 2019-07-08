tx,ty=map(int,input().split())
nh=list(map(int,input().split()))
nh.sort()
nh.reverse()
th=ty
z=0
for i in nh:
    if(th>=i):
        no=int(th/i)
        z=z+no
        th=th-no*i
    if th==0:
        break
if(th==0):
   print(z)
else:
   print("it's not posiible to select coins in such a way that they sum upto",S)        
