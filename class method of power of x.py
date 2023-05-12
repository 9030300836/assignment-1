class Power():
    
    def __init__(self,x,n):
        self.x = x
        self.n = n
    
    def power(self):
        return pow(self.x,self.n)



p = Power(10,2)
print(p.power())