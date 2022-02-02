l = int(input())
even_count =  0
odd_count = 0
for i in range(1,l):
    if i%2==0:
        even_count+=1
    elif i%2!=0:
        odd_count+=1
print("The nuber of even numbers is",even_count)
print("The number of odd numbers is",odd_count)