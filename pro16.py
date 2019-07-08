a1=int(input())
c1=list(map(int,input().split()))
x1=[1]*a1
for i in range(a1):
    if i==0:
        if c1[i]>c1[i+1]:
            x1[i]=x1[i]+x1[i+1]
    elif i>0:
        if c1[i]>c1[i-1]:
            x1[i]=x1[i]+x1[i-1]
print(sum(x1))
