s1,t1 = map(int, input().split())
l1 = list(map(int, input().split()))
for i in range(t1):
  y,z = map(int, input().split())
  print(min(l1[y-1:z]))
