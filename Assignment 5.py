#1
a=input()
x=''
l=[]
for i in range(0,len(a)-1):		
    if ord(a[i+1])-ord(a[i])==0:		#checks i the characters next to each other
        if i!=len(a)-2:
            x=x+a[i]
        else:
            x=x+a[i]
            l.append(x)
    else:
        x=x+a[i]
        l.append(x)
        x=''
if ord(a[i])-ord(a[i+1])==0:        #condition for the last character
    l[len(l)-1]=l[len(l)-1]+a[i+1] 
else:
    l.append(a[i+1])
cnt=[]
for i in range(0,len(l)):			#gets the length of each element 
    cnt.append(len(l[i]))
for i in range(len(l)):
    print(l[i],end='')
    print(cnt[i],end='')

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
ip=input("Enter an IP address:")
op=re.match(r"\b(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])",ip)
#pattern to check ip address 0.0.0.0 -- 255.255.255.255
if op:
    print(op.group(),"is a valid IP address")
else:
    print(ip,"not a valid IP address")

 
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

