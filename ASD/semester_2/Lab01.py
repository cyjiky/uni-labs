import math


def recursion_1(x, n, i=1, F=None, cur_sum=0.0):
    if F is None:
        F = x

    if i > n:
        return cur_sum

    new_sum = cur_sum + F
    calculate = (x**2) / (4 * (i**2) + 2 * i)
    val = F * calculate

    return recursion_1(x, n, i + 1, val, new_sum)


def recursion_2(x, n):
    if n == 1:
        return x, x

    F, sum = recursion_2(x, n - 1)
    i = n - 1
    calculate = (x**2) / (4 * (i**2) + 2 * i)
    cur_F = F * calculate
    cur_sum = sum + cur_F

    return cur_F, cur_sum


def recursion_3(x, n, i=1, F=None):
    if F is None:
        F = x

    if i > n:
        return 0.0

    calculate = (x**2) / (4 * (i**2) + 2 * i)
    cur_F = F * calculate

    return F + recursion_3(x, n, i + 1, cur_F)


def test_func(x, n):
    cur_sum = 0.0
    F = x
    for i in range(1, n + 1):
        cur_sum += F
        calculate = (x**2) / (4 * (i**2) + 2 * i)
        F = F * calculate

    return cur_sum


_n = 5
x_val = [1.0, 2.0, 3.0, 4.0, 5.0]
for i in x_val:
    _sum = test_func(i, _n)
    _val = math.sinh(i)

    diff = abs(_sum - _val)
    print(f"{i}\t{diff}")

# res_1 = recursion_1(x, n)
# cur_F, res_2 = recursion_2(x, n)
# res_3 = recursion_3(x, n)
# result = math.sinh(x)

# print(f"n: {n}, x: {x}")
# print(f"res1: {res_1}")
# print(f"res2: {res_2}")
# print(f"res3: {res_3}")
# print(f"result (shx): {result}")
