#==============================Implementation of class and objects===============================



import math
class point:        #class for point calculations
    _count=0
    def __new__(cls,*args):     # __new__ method for restricting object creation more than 5
        cls._count=cls._count+1
        if cls._count>5:
            raise TypeError("Can't create more than 5 objects")
        else:
            return object.__new__(cls)
    def __init__(self,a=0,b=0):     #__init__ method to set coordinates of point
        self.x=a
        self.y=b
    def dist(self,p):               #method to find the distance between two points
        d=math.sqrt((p.x-self.x)**2 + (p.y-self.y)**2)
        return d
    def o_dist(self):               #method to find the distance between the point and origin
        d=math.sqrt((self.x**2)+(self.y**2))
        return d
    def midpt(self,p):              #method to find the midpoint of two points
        p.x=(self.x+p.x)/2
        p.y=(self.y+p.y)/2
        return p
p1=point(4,5)                       #point 1
p2=point(7,9)                       #point 2
print("Distance between (4,5) and origin:",p1.o_dist()) #Distance between a point and origin
print("Distance between (4,5) and (7,9)",p1.dist(p2))   #Distance between two points
p=p1.midpt(p2)                                          #Midpoint of two points
print("Midpoint of (4,5) and (7,9):(",p.x,",",p.y,")")
p3=point(3,4)
p4=point(4,5)
p5=point(5,6)
p6=point(6,7)                                           # 6th point object can't be created





#======================o/p===========================================================================
# Distance between (4,5) and origin: 6.4031242374328485                                                                                      
# Distance between (4,5) and (7,9) 5.0                                                                                                       
# Midpoint of (4,5) and (7,9):( 5.5 , 7.0 )                                                                                                  
# Traceback (most recent call last):                                                                                                         
#   File "main.py", line 39, in <module>                                                                                                     
#     p6=point(6,7)                                           # 6th point object can't be created                                            
#   File "main.py", line 14, in __new__                                                                                                      
#     raise TypeError("Can't create more than 5 objects")                                                                                    
# TypeError: Can't create more than 5 objects                                                                                                
                                                   