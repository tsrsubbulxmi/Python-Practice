#===============================(1)==================================================

x=lambda x:x**2
print(x(2))
#4


#===============================(2)==================================================

print((lambda x:x**2)(2))
#4


#===============================(3)==================================================

#---------------------in python 2.7 shell----------------------------check
l1=[1,2,3,4]
l2=[5,6,7,8]
l=list(map(lambda a,b:a+b,l1,l2))

# Traceback (most recent call last):
#   File "<pyshell#8>", line 1, in <module>
#     l2=list(map(lambda a,b:a+b,l,l1))
#   File "<pyshell#8>", line 1, in <lambda>
#     l2=list(map(lambda a,b:a+b,l,l1))
# TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
# >>> l2=[1,2,3,4,5]
# >>> l3=list(map(lambda a,b:a+b,l,l2))

# Traceback (most recent call last):
#   File "<pyshell#10>", line 1, in <module>
#     l3=list(map(lambda a,b:a+b,l,l2))
#   File "<pyshell#10>", line 1, in <lambda>
#     l3=list(map(lambda a,b:a+b,l,l2))
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
# >>> 



#===============================()==================================================

def square(a):
    n=a**2
    return n
l1=[1,2,3]
sq=list(map(square,l1))
print(sq)

#=================o/p===============
#[1, 4, 9]


#===============================(4)==================================================

def square(a):
    n=a**2
    print(n)
l1=[1,2,3]
sq=list(map(square,l1))
print(sq)

#=================o/p===============

#1                                                                                                                             
#4                                                                                                                             
#9                                                                                                                             
#[None, None, None]


#===============================()==================================================

import math
p=list(map(pow,[2,3],[3,2]))
print(p)

#=================o/p===============

#[8, 9]      


#===============================(5)==================================================

l1=[1,2,3,4]
two=list(map(lambda a:a%2==0,l1))
print(two)
two=list(filter(lambda a:a%2==0,l1))
print(two)

#=================o/p===============

#[False, True, False, True]                                                                                                               
#[2, 4] 


#===============================(6)==================================================

l1=['subbu','surudhi','aravind','akku','kanth']
l=list(map(lambda a:a+str(5),l1))
print(l)

#=================o/p===============

#['subbu5', 'surudhi5', 'aravind5', 'akku5', 'kanth5']         


#===============================(7)==================================================

import itertools
l=[1,2,3,4]
l1=list(itertools.accumulate(l,lambda a,b:a+b))
print(l1)


#=================o/p===============

#[1, 3, 6, 10]    