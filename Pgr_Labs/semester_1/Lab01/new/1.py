def inc(n: int) -> int:
    return n + 1

a = 2 
b = inc(a)
print(f"a: {a}, b: {b}")

# or
inc_2 = lambda x: x + 1 
print(inc_2(2))
