sa=int(input())
se=list(map(int,input().split()))
st=0
for i in range(len(se)-2):
   for j in range(i+1,len(se)-1):
         for e in range(j+1,len(se)):
            if se[i]<se[j]<se[e] and i<j<e:
                st+=1
print(st)
