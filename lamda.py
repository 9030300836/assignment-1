def func_compute(n):
 return lambda x : x + n
result = func_compute(25)
print("Double the number of 10 =", result(10))