tr=int(input())
q=0
while 2**q < tr:
    q=q+1
if 2**q == tr:
    print(0)
elif tr-2**(q-1)<=2**q-tr:
    print(tr-2**(q-1))
else:
    print(2**q-tr)
