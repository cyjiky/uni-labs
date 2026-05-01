import math 

# TODO 
def recursion_1(x, n, i=1, F=1.0, cur_sum= 0.0):
    if i > n:
        return cur_sum 
    
    new_sum = cur_sum + F
    calculate = (x**2) / (4*(i**2) - 2*i)
    val = F * calculate

    return recursion_1(x, n, i +1, val, new_sum)

def recursion_2(x, n):
    if n == 1:
        return 1.0, 1.0
    
    F, sum = recursion_2(x, n - 1)
    i = n - 1 
    calculate = (x**2) / (4*(i**2) - 2*i)
    cur_F = F * calculate
    cur_sum = sum + cur_F

    return cur_F, cur_sum

def recursion_3(x, n, i=1, F=1.0):
    if i > n: 
        return 0.0
    
    calculate = (x**2) / (4*(i**2) - 2*i)
    cur_F = F * calculate

    return F + recursion_3(x, n, i+1, cur_F)

# n = int(input("n: "))
# x = float(input("x: "))

n = 5
x = 0.1

res_1 = recursion_1(x, n)
cur_F, res_2 = recursion_2(x, n)
res_3 = recursion_3(x, n)
result = math.cosh(x)

print(f"n: {n}, x: {x}")
print(f"res1: {res_1}")
print(f"res2: {res_2}")
print(f"res3: {res_3}")
print(f"result (chx): {result}")
