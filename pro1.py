def check(d,e):
    a=e[0]
    s1 = []
    for i in range(len(d)):
        for j in range(1,len(e)):
            y=e[j]
            if j==(len(e)-1) and a[i] == y[i]:
                s1.append(a[i])
            elif a[i] == y[i]:
                continue
            else:
                return s1
    return s1
n=int(input())
e=[]
for i in range(n):
    s1=input()
    e.append(s1)
d=min(e)
print("".join(check(d,e)))
