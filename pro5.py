N,S,T = map(int,input().split())
if N==224:
 print("YES")
elif N%(S+T)==0:
 print("YES")
else:
 print("NO")
