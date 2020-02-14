n=int(input(''))
dic={}
for i in range(0,n):
    a=input()
    l=a.split(' ')
    dic[l[0]]=[l[1],l[2],l[3]]
s=input()
l=dic.get(s)
avg=(int(l[0])+int(l[1])+int(l[2]))/3
print(avg)