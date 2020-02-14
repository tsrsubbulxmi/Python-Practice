import re
n=int(input())
l=[]
for i in range(n):
    a=input('')
    op=re.search(r'([a-z|A-Z|0-9|\-|_]+[@]?[a-z|A-Z|0-9]+\.[a-z]+)',a)
    l.append(str(op.group(0)))
print(sorted(l))