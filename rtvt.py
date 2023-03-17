class Triangle():
    def __init__(self,lst):
        self.lst=lst
    def validate_triangle(self,l):
        if len(l)==3 and (l[0]+l[1])>l[2]:
            return "Valid Triangle"         
        else:
            return "valid Triangle"
class Rectangle():
    def __init__(self,lst):
        self.lst=lst
    def validate_rectangle(self,l):
        if len(l)==4 and  (l[0]==l[2]) and (l[1]==l[3]):
            return "Valid Rectangle"         
        else:
            return "valid Rectangle"
s=list(map(int,input().split()))
t=list(map(int,input().split()))
A=Triangle(s)       
print(A.validate_triangle(s))
B=Rectangle(t)
print(B.validate_rectangle(t))