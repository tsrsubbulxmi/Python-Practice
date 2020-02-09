#========================= Implementation of instanca,class,static methods and access specifiers============



class Company:                      #Parent class Company

    __count=0                       #private count variable

    @classmethod
    def disp_cnt(cls):              #class method for calculating np of objects created
        cls.__count=cls.__count+1
        return cls.__count

    @staticmethod
    def company_details():          #static method to provide the Company name and location
        Company._name='Accenture'
        Company._loc='Chennai'
        return Company._name,Company._loc
    
class Employee(Company):            #Employee class derived from Company 

    def __init__(self,name='',id=0):#init method for setting values of id,name during obj creation
        if id>0:
            self.id=id
            Company.disp_cnt()      #use of private variable of Company using method
        else:
            self.id=Company.disp_cnt()  #if no id value is received during obj creation
        self.name=name      #then the no of objs created + the current obj will be assigned to id

    def setId(self,id):         # setting id 
        self.id=id

    def setName(self,name):     # setting name
        self.name=name

    def getId(self):            # getting id
        return self.id

    def getName(self):          # getting name
        return self.name

    def grossSalCalc(self,basicPay):        #gross salary calculation with basicpay
        gross_salary = basicPay + (10 * basicPay) / 100 + (12 * basicPay) / 100
        return self.id,self.name,gross_salary
    def getCompName(self):      #use of protected variables of Company using method
        return Company._name,Company._loc

name,loc=Employee.company_details() #printing Company details
print('Company Name:',name)
print('Location:',loc)

e1=Employee('Subbu',121)            #passing both id and name
n,l=e1.getCompName()                #getting protected variables values of Company
print(n,l)

e2=Employee('surudhi')              #passing only name so id value will be assigned to no of objs createdbefore + 1

id=int(input('Enter the id'))
name=input('Enter the name')
e3=Employee()
e3.setId(id)                        #setting id
e3.setName(name)                    #setting name

print('Id -  name  : gross salary')

id1,name1,gs1=e1.grossSalCalc(20000)    #gross salary calculation
print(id1,'-',name1,':',gs1)

id2,name2,gs2=e2.grossSalCalc(25000)    #gross salary calculation
print(id2,'-',name2,':',gs2)

id3,name3,gs3=e3.grossSalCalc(22000)    #gross salary calculation
print(id3,'-',name3,':',gs3)




#============o/p=========================

# Company Name: Accenture                                                                                                                    
# Location: Chennai                                                                                                                          
# Protected access : Accenture Chennai                                                                                                       
# Id -  name  : gross salary                                                                                                                 
# 121 - Subbu : 24400.0                                                                                                                      
# 2 - surudhi : 30500.0                                                                                                                      
# 143 - sudee : 26840.0