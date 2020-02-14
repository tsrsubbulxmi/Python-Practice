n=int(input('Enter the number of words'))
words=[]
w={}
c=[]
print('Enter the words')
for i in range(n):
    a=input()
    if a not in words:
        cnt=1
        w[a]=cnt
        words.append(a)
    else:
        w[a]=cnt+1
        cnt+=1
print(len(w))
for k,v in w.items():
    print(v,end=' ')