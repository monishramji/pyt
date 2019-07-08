l1=input()
y1=map(int,input().split())
p1=[]
for i in y1:
    e1=bin(i)
    p1.append(e1)
f=sorted(p1)
f.reverse()
for j in f:
    print(int(j,2))
