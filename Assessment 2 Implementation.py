#=====================Currency conversion using some function implementations==========================





import datetime
def cur_time(pos,time,time_zone):       #Method to calculate the time in the specified country
    t=time_zone[pos]
    x=dict(zip(time_zone,time))         #Use of dictionary and zip function
    h1=float(datetime.datetime.now().strftime("%H"))    #getting hours
    m1=float((datetime.datetime.now().strftime("%M")))/60   #getting minutes
    t1=h1+m1+float(x[t])
    if t1<0:
        t1=12+t1
    t1=t1*60
    h=int((t1/60))
    m=int(t1%60)
    s=str(h)+':'+str(m)
    return s,t
def lang(pos,language):                 #Method to get the language spoken in the specified country
    return language[pos]
def cur_val(pos,currency_rate,currency):#Method to get the currency value in the specified country
    return float(currency_rate[pos]),currency[pos]


country=["UK","USA","INDIA","MEXICO","AUSTRALIA"]
time_zone=("GMT","EST","IST","CST","ADET")
time=("-5.5","-10.5","0.0","-11.5","5.5")
currency=('POUND','USD','INR','USD','AUD')
language=('ENGLISH','ENGLISH','HINDI','SPANISH','ENGLISH')
currency_rate=['92.72','71.32','1','71.32','47.73']

cntry=input("Enter country name from (UK,USA,MEXICO,AUSTRALIA):") #getting the country name
amt=int(input("Enter amount in INR:"))                            #getting the amount to be converted
for i in range(0,len(country)):
    if country[i]==cntry:
        pos=i
print("\nCountry:",cntry)
t,z=cur_time(pos=pos,time_zone=time_zone,time=time)     #for calculating the Current-time in that country 
print("Current Time:",t,z)
print("Language:",lang(pos,language))       #for getting the language of that country
currency_value,currency_name=cur_val(pos,currency_rate,currency)#to get the currency name and value equivalent to INR
print("Currency Value:",currency_value,"INR")
s="Equivalent Currency value for {0} INR : {1} {2}" # use of string formatting
eq_cur_val= lambda a,b:a/b     #lambda function for getting the Equivalent currency value for INR
print(s.format(amt,eq_cur_val(amt,currency_value),currency_name))





# Enter country name from (UK,USA,MEXICO,AUSTRALIA):USA                                                                                    
# Enter amount in INR:700000                                                                                                               
                                                                                                                                         
# Country: USA                                                                                                                             
# Current Time: 7:40 EST                                                                                                                   
# Language: ENGLISH                                                                                                                        
# Currency Value: 71.32 INR                                                                                                                
# Equivalent Currency value for 700000 INR : 9814.918676388112 USD  