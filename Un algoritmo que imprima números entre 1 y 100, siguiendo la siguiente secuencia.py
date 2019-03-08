c=1
d=1
for i in range(1,100):
    print(c)
    c=c+d
    d+=1
    if d>5:
         d=1
    if c>100:
            break
