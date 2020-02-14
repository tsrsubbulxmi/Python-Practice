

import functools
s = 'aasd785aqr75f78'
l = list(filter(lambda a: a.isdigit(), s))		#getting the numbers from the string
l = list(map(lambda a: int(a), l))			#converting to integer
print(l)
sum_of_d = functools.reduce(lambda a, b : a+b, l)	#sum of digits calculation
print(sum_of_d)


email=['abc@gmail.com','def@xyz.com','ghdf@hotmail.com','subbu.@outlook.com','as@gmail.com','u.@hotmail.com']
for i in email:
    op=re.search(r'([a-z|A-Z]+)([@])([gmail\.com]{9}|[hotmail\.com]{11}|[yahoo\.com]{9}|[outlook\.com]{11})',i)
    #Regex for mail validation
    #It should contain atleast 1 character before @ symbol and it should have valid email extensions
    if op:
        print(op.group(0))
		
		
import re
email=['abc.@gmail.com','def@xyz.com','ghdf@hotmail.com','subbu.@outlook.com','as@gmail.com','u.@hotmail.com']
for i in email:
    op=re.search(r'([a-z|A-Z][a-z|A-Z]+)(\.)([@])([gmail\.com]{9}|[hotmail\.com]{11}|[yahoo\.com]{9}|[outlook\.com]{11})',i)
    #Regex for mail validation
    #It should contain atleast 2 characters and a . before @ symbol and it should have valid email extensions
    if op:
        print(op.group(0))

		
s='ashafsnfnwsgwjnwnefqaa'
x='asf'
if len(x)==3:
    cnt=0
    for i in x:
        if i in s:				#if all the three characters available in the string,the substring should be accepted
            cnt=cnt+1
    if len(x)==cnt:
        print('The substring is available in the string')
    else:
        print('The substring is not available in the string')
elif len(x)<3:
    print('The substring is too small')
else:
    print('The substring is too large')
	
	
vowels={'a':1,'e':2,'i':3,'o':4,'u':5}
s='madmeesicqiqihduqwqwo'
sum_of_vowels=0
for i in s:
    if i in vowels.keys():				#getting the equivalent value for vowels and calculating their sum
        sum_of_vowels=sum_of_vowels+vowels.get(i)
print(sum_of_vowels)


a=int(input())
if a>=0:
    org=a
    rev=0
    while(a>0):			#checking palindrome
        rem=a%10
        rev=(rev*10)+rem
        a=int(a/10)
    if org==rev:
        print(org,'is a palindrome')
    else:
        print(org,'is not a palindrome')
else:
    print(a,'is not a palindrome')
	
	
s='AZazbuGuAgiASuNJg'
for i in s:
    if ord(i)>=97:				#check if the character is small using ord() then convert it to capital 
        a=ord(i)-32
        print(chr(a),end='')
    elif ord(i)>=65 and ord(i)<=90:		#check if the character is capital using ord() then convert it to small 
        a=ord(i)+32
        print(chr(a),end='')
		
		
l=['adae','wqef','effg','anudb','aqdwa']
ch=[]
dic={}
for i in l:
    if i[2] not in ch:
        ch.append(i[2])		#get the 3rd character
    dic[i]=i[2]			#store it dictionary with the string as key and the 3rd character as value
ch.sort()			#sort the list which has 3rd chracters
s=[]
for i in ch:
    for k,v in dic.items():	#based on the sorted list get the keys of that values and append it another list
        if i==v:
            s.append(k)
for i in s:
    print(i)			#the sorted list
	
	
for i in range(0,5):
    for j in range(i,4):
        print(end=' ')			#pyramid pattern
    for k in range(0,i+1):
        print(end='* ')
    print('\n')


a='abckefunefghijklueffdefghiihk'
x=''
l=[]
for i in range(0,len(a)-1):		
    if ord(a[i+1])-ord(a[i])==1:		#checks i the characters next to each other are in sequence
        x=x+a[i]
    else:
        x=x+a[i]
        l.append(x)
        x=''
print(l)
cnt=0
for i in range(0,len(l)):			#checks the highest length of the substring 
    if len(l[i])>cnt:
        cnt=len(l[i])
        k=l.index(l[i])
print(l[k])


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
