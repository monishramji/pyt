vj1=int(input())
vk1=list()
for i in range(vj1):
    ba=input().split()
    ba=[int(d) for d in ba]
    for j in ba:
        vk1.append(j)
vk1.sort()
for i in vk1:
    print(i,end=" ")
