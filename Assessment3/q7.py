a=input()
a=a.split(' ')
b=input()
b=b.split(' ')
l=[]
for i in a:
    for j in b:
        t=(i,j)
        l.append(t)
print(l)