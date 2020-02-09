# 1. Find the number:
# Generate 10 random numbers between 0 to 50 and ask user to predict one number with three chances
# and return True/False

# Ex. OP
# op: Hi, Could you guess one number between 0 to 50.. ??
# ip: 34
# op: Sorry!! But you are close to that.. Try again
# ip: 21
# op: Yeah... right...!!!


#====================================i/p========================================
#

#====================================o/p========================================
#



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