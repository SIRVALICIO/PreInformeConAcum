b=0
for i in range(0,5):
    a=float(input("valor deseado: "))
    if i==0:
        b=a
    if a>b:
        b=a

print("El valor mayor es: ",b)