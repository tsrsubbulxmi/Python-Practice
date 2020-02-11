# 1. Find the number:
# Generate 10 random numbers between 0 to 50 and ask user to predict one number with three chances
# and return True/False

# Ex. OP
# op: Hi, Could you guess one number between 0 to 50.. ??
# ip: 34
# op: Sorry!! But you are close to that.. Try again
# ip: 21
# op: Yeah... right...!!!
import random
def check(n,num_list,choice):
    if n == choice:			#if the chosen number is correct
        print("Yeah...! You guessed it correctly!!!Congrats!!!")
        return 1
    else:
        pos1=l.index(choice)		#getting the index of randomly chosen number
        pos2=l.index(n)			#getting the index of user chosen number
        if abs(pos1-pos2)<=3:		#if they are 1-3 indices away
            print("You are closer to success!!!")
            return 0
        else:				#if they are more than 3 index
            print('You are far away from the target!!!')
            return 0
            
l=[]
while True:
    a=random.randrange(50)			#getting random numbers of range 1-50
    if a not in l and len(l)<=10:		#since the elements should not repeat,checking if the number already exists
        l.append(a)
    elif len(l)>10:
        break
s=random.choice(l)				#selecting a random number from the list
x=2
for i in range(0,3):
    if x==0:
        print('Try again')			#if the number is not selected correctly
    elif x==1:					
	break
    else:
        print("Hello There!!! Could you select one number from the list:",l)
    a=int(input())
    x=check(a,l,s)				#calling the check method to check if the chosen number is the randomly picked one or not
    
if x==0:
    print('Sorry better luck next time')
elif x==1:
    print('Enjoy your win!!!@@!!!')

#====================================i/p========================================
#

#====================================o/p========================================
#Hello There!!! Could you select one number from the list: [40, 44, 45, 20, 14, 12, 8, 42, 9, 32, 15]                          
# 14                                                                                                                            
# You are far away from the target!!!                                                                                           
# Try again                                                                                                                     
# 8     
# You are closer to success!!!                                                                                                  
# Try again                                                                                                                     
# 9                                                                                                                             
# You are closer to success!!!                                                                                                  
# Sorry better luck next time 

#====================================o/p========================================

# Hello There!!! Could you select one number from the list: [10, 29, 33, 35, 25, 37, 19, 21, 49, 40, 44]                        
# 33                                                                                                                            
# Yeah...! You guessed it correctly!!!Congrats!!!                                                                               
# Enjoy your win!!!@@!!! 


#====================================o/p========================================
# Hello There!!! Could you select one number from the list: [49, 44, 3, 25, 15, 14, 48, 47, 45, 0, 35]                          
# 45                                                                                                                            
# You are closer to success!!!                                                                                                  
# Try again                                                                                                                     
# 0          
# Yeah...! You guessed it correctly!!!Congrats!!!                                                                               
# Enjoy your win!!!@@!!!




#2. ONE PLUS TWO o/p THREE
#TWO DIVIDE TWO o/p ONE
#FOUR MINUS ONE o/p THREE

#Note: use one digit ip and op


dic={'ONE':'1','TWO':'2','THREE':'3','FOUR':'4','FIVE':'5','SIX':'6','SEVEN':'7','EIGHT':'8','NINE':'9','ZERO':'0','PLUS':'+','MINUS':'-','DIVIDE':'/','MULTIPLY':'*'}
s=input("Enter the expression")
l=s.split(" ")      # splitting the expression with ' ' space
l1=[]
x=''
for i in l:
    x=x+dic.get(i)          # converting the word expression into number expression
y=str(int(eval(x)))         # calculating the expression
for i in y:
    k=list(dic.keys())
    v=list(dic.values())
    print(k[v.index(i)],end=' ')        #getting the words for each number returned by the eval function

	
	
	
#====================================i/p========================================
#Enter the expressionTWO MULTIPLY THREE   

#====================================o/p========================================
#SIX




#3. Ask user to enter number & check whether the number is divisible by 3, 5 and both


a=int(input("Enter the number"))
if a % 3 == 0 and a % 5 == 0:
    print(a,'is divisible by both 3 and 5')
elif a % 5 == 0:
    print(a,'is divisible by 5')
elif a % 3 == 0:
    print(a,'is divisible by 3')
else:
    print(a,'is not divisible by either 3 or 5')




#====================================i/p========================================
#Enter the number25 

#====================================o/p========================================
#25 is divisible by 5  



	
#4. Get the range from user and find sum of series which is divisible by 3


s=int(input("Enter the starting range"))
e=int(input('Enter the range end'))
sum1=0
for i in range(s,e+1):
    if i%3==0:
        sum1=sum1+i
print('The sum of series divisible by 3 is',sum1)




#====================================i/p========================================
#Enter the starting range2                                                                                                                
#Enter the range end14  

#====================================o/p========================================
#The sum of series divisible by 3 is 30  




#5. What day is this date: 
#Ask user to enter Birthdate with Year -- print the day
#(NOTE: Use calendar.day_name function)


import calendar
a=input('Enter your birthday with year in the format yyyy-mm-dd')
d=a.split('-')
dat=calendar.weekday(int(d[0]),int(d[1]),int(d[2]))
print(calendar.day_name[dat])



#====================================i/p========================================
#Enter your birthday with year in the format yyyy-mm-dd1997-12-04

#====================================o/p========================================
#Thursday 
