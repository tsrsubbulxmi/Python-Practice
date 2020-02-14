#1


#2
t=[(),(1,2,3),('a','b'),(''),('','')]
for i in t:
    pass
    if len(i)==0 and '' not in i:
        print(i,'is an empty set')
    
#3

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

