#1


#2
t=[(),(1,2,3),('a','b'),(''),('','')]
for i in t:
    pass
    if len(i)==0 and '' not in i:
        print(i,'is an empty set')
    
#3
x='({)}[]}'
dic={'{':'}','[':']','(':')'}
l={}
cnt=1
for i in range(0,len(x)):
    for j in range(i+1,len(x)):
        if x[i]==x[j] and x[i] not in l.keys():         #counting he occurrence of each character
            cnt=cnt+1
            l[x[i]]=cnt
    cnt=1        
for k,v in dic.items():
    if l.get(k)==l.get(v):                              #checking for balanced position
        if (x.index(v)-x.index(k))>0 and (x.index(v)-x.index(k))%2!=0:
            continue
        else:
            print('Not balanced')
            break

#4
x=input('Enter the statement')
print(x.title())

#5
import re
txt='12.254.259 0.0.0 49.174.165'
txt=txt.split(' ')
for i in txt:
    #op=re.search('([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|2[0-5][0-5])',i)
    op=re.findall(r'([0-2]?[0-9]?[0-9]\.[0-2]?[0-9]?[0-9]\.[0-2]?[0-9]?[0-9])',i)
    #\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|2[0-5][0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|2[0-5][0-5])\.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|2[0-5][0-5])
    print(op)
 
#6

l=[]
while True:
    x=input('If you want to end giving inputs give done:')
    if x=='done':
        break
    else:
        l.append(x)
s=' '.join(l)
print(s)

