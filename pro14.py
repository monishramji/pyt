vj1,vk1=map(int,input().split())
list1=list(map(int,input().split()))
vj1=[]
list1.insert(0,0)
for y in range(vk1):
     v=[]
     sumup=0
     cc,dd=map(int,input().split())
     for i in range(cc,dd+1):         
         sumup^=list1[i]     
     vj1.append(sumup)
for y in vj1:
    print(y)
