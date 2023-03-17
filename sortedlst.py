def anjan(lst):
    lst.sort(key=lambda x: (x[-2]))
    return lst


a = int(input())
b = input()
t = b.split()
c = t[:a]
print(c)
anjan(c)