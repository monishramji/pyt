x1,j1=map(int,input().split())
y1=list(map(int,input().split()))[:x1]
count=0
for k in range(0,len(y1)-1):
  for sec in range(k+1,len(y1)-1):
    if(y1[k]+y1[sec]==j1):
      count+=1  
if count==1:
  print("yes")
else:
  print("no")
