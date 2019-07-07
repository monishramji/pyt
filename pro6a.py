a2sj = int(input())
b3sj= list(map(int,input().split()))
cam = []
var = []
for i in enumerate(b3sj):
  cam.append(i)
for i in range(0,len(b3sj)):
  for j in range(0,len(b3sj)):
    for k in range(0,len(b3sj)):
      if(cam[i][1] < cam[j][1] < cam[k][1]):
        if(cam[i][0] < cam[j][0] < cam[k][0]):
          d = [cam[i][1],cam[j][1],cam[k][1]]
          var.append(d)
if(len(var) != 0):
  print(len(var))
else:
  print("0")
