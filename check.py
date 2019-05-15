listvalues=list()
#for i in range(1,11)
#listvalues.append(i**2) 
listvalues=[i**2 for i in range(1,11,2)]
listvalues.insert(3,10)
if(listvalues.couint(100)!=0):
    print(yes)
else:
    print(no)
