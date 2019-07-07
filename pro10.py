agk1=int(input())
bgk1=[int(i) for i in input().split()]
x=0
for k in range(agk1):
   for j in range(k):
      if bgk1[j]<bgk1[k]:
         x+=bgk1[j]
print(x)
