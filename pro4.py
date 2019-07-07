viji,son=map(str,input().split())
wave=0
if len(viji)>len(son):
  viji,son=son,mah
i=0
while i<len(viji):
  wave+=(ord(son[i])-ord(viji[i]))
  i+=1
for i in range(i,len(son)):
  wave+=ord(son[i])-ord('a')+1
print(wave)
