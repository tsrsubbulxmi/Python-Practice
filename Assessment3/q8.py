a=input()
x=input()
l=x.split(' ')
dic={}
y='1234567890'
cnt=1
for i in y:
    for j in x:
        if i == j:
            dic[i]=cnt
            cnt+=cnt
    cnt=1
for k,v in dic.items():
    if v==1:
        print(k)

