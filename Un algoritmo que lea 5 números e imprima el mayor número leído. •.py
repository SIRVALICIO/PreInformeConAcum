b=0
c=0
while c>-1  and c<6:
    a=float(input("numero: "))
    c+=1
    if c==0:
        b=a
    if a>b:
        b=a

print(b)
