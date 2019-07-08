inpta1,inpta2=map(int,input().split())
inpta3=list(map(int,input().split()))
for a in range (1,inpta1):
    inpta3[a]+=inpta3[a-1]
for a in range (inpta2):
    x,y=map(int,input().split())
    z=inpta3[y-1] if x==1 else inpta3[y-1]-inpta3[x-2]
    print(z)
