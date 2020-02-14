n=int(input('Enter the number of rational numbers'))
l=[]
for i in range(n):
    a=input()
    l.append(a)
m=1
x=[]
for i in range(len(l)):

    l1=l[i].split(' ')
    x.append(l1)
print(x)
z=1
o=1
r=1
for i in x:
    z=z*int(i[0])
for i in x:
    o=o*(int(i[1]))
    if z%int(i[1])==0:
        z=z/int(i[1])
        y=(int(i[1]))
    else:
        r=r*int(i[1])
print(int(z/n),'/',int(r/n))