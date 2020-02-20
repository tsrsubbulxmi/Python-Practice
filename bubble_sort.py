n=int(input('Enter the size of the list'))
b=[]
print('Enter the elements')
for i in range(0,n):
    a=int(input())
    b.append(a)
for i in range(0,len(b)-1):
    for j in range(i+1,len(b)):
        if b[i]>b[j]:
            b[i],b[j]=b[j],b[i]
print('Sorted array',b)

#==============op================
# Enter the size of the list5                                                                                                     
# Enter the elements                                                                                                              
# 9                                                                                                                               
# 5                                                                                                                               
# 8                                                                                                                               
# 6                                                                                                                               
# 4                                                                                                                               
# Sorted array [4, 5, 6, 8, 9] 