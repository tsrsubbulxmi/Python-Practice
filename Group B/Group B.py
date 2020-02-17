class bike:
    def __init__(self):
        self.model=['NS200','R15','350x','ninja650','RTR','ninja1000r','dominar']
        self.c_name=['bajaj','yamaha','royal enfield','kawasaki','tvs','kawasaki','bajaj']
        self.cc=[200,150,350,650,180,1000,400]
        self.ex_price=['1.5-L','1.4-L','1.9-L','6.5-L','1.25-L','15.0-L','2.0-L']
        self.on_road=[]
        self.mapp={}
    def k_val(self):
        mapped = list(zip(self.c_name,self.cc,self.ex_price,self.on_road))
        self.mapp = dict(zip(self.model, mapped))
    def on_road_price_calc(self):
        self.on_road=[]
        for i in self.ex_price:
            a=i.split('-')
            self.on_road.append(float(a[0]))
        on_road_price=list(map(lambda a:round(a+(a*1.3),2),self.on_road))
        self.on_road=[]
        for i in on_road_price:
            i=str(i)+'-L'
            self.on_road.append(i)
    def get_model(self):
        return self.model
    def get_details(self,model):
        return self.mapp.get(model)
bike1=bike()
bike1.on_road_price_calc()
bike1.k_val()
while True:

    print(bike1.get_model())
    model=input('Enter the model you are looking for from the above list!!! Or Done to end')
    if(model!='Done'):
        c_name,cc,price,on_road=bike1.get_details(model)
        print('Company name:',c_name)
        print('Bike-CC:',cc)
        print('Showroom-Price:',price)
        print('On road price:',on_road)
    else:
        break



#==========================================Output====================
# ['NS200', 'R15', '350x', 'ninja650', 'RTR', 'ninja1000r', 'dominar']
# Enter the model you are looking for from the above list!!! Or Done to endR15
# Company name: yamaha
# Bike-CC: 150
# Showroom-Price: 1.4-L
# On road price: 1.82-L
# ['NS200', 'R15', '350x', 'ninja650', 'RTR', 'ninja1000r', 'dominar']
# Enter the model you are looking for from the above list!!! Or Done to endNS200
# Company name: bajaj
# Bike-CC: 200
# Showroom-Price: 1.5-L
# On road price: 1.95-L