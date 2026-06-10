arr = [True, "hello", 5, 12, -200, False, False, "word"]

arr2 = {
    "int": 0, 
    "str": 0, 
    "bool": 0
}

# 1
for i in arr:
    if type(i) == int: 
        arr2["int"] += 1
    elif type(i) == str:
        arr2["str"] += 1
    else: 
        arr2["bool"] += 1

print(f'1: {arr2}')

# 2 
dict_ = {}
for x in arr:
    a =  type(x).__name__
    if a not in dict_:
        dict_[a] = 0
        
    dict_[a] += 1 
    
print(f'2: {dict_}')
