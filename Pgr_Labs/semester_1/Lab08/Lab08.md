## 👾 Lab08: Higher-order functions having functions as arguments or result

1. Реализуйте функцию `iterate(object, callback)` которая будет итерировать
все ключи переданного объекта, вызывая для каждого `callback` со следующим
контрактом `callback(key, value, object)`. 

```py
def iterate(obj, callback):
    for key, value in obj.items():
        callback(key, value, obj)

obj = {'a': 1, 'b': 2, 'c': 3}
iterate(obj, lambda k, v, o: print({'key': k, 'value': v}))
```
2. Реализуйте функцию `store(value)` которая сохранит значение в замыкании
возвращаемой функции, а после ее вызова вернет значение из замыкания

```py
def read():
    store = 5
    def value():
        print(store)

    value()
read()
```
3. Реализуйте функцию `contract(fn, ...types)` которая оборачивает `fn` (первый
аргумент) и проверяет типы аргументов (все аргументы кроме первого и последнего)
и результата (последний аргумент), генерируя исключение `TypeError`, если типы
не совпадают

```py
add = lambda a, b: a + b

def contract(func, *types):
    arg_types = types[:-1]
    return_type = types[-1]

    def wrapper(*args):
        if len(args) != len(arg_types):
             raise TypeError(f"Expected {len(arg_types)} arguments, got {len(args)}")

        for i, (arg, expected_type) in enumerate(zip(args, arg_types)):
            if not isinstance(arg, expected_type):
                raise TypeError(f"Arg {i} must be {expected_type.__name__}, got {type(arg).__name__}")

        result = func(*args)

        if not isinstance(result, return_type):
            raise TypeError(f"Return value must be {return_type.__name__}")

        return result

    return wrapper

add_numbers = contract(add, int, int, int)

try:
    res = add_numbers(2, 3)
    print(res)
except TypeError as e:
    print(f"Error: {e}")
```

or 

```py
add = lambda a, b: a + b

def contract(func, *types):
    arg_types = types[:-1]
    return_type = types[-1]

    def wrapper(*args):
        if len(args) != len(arg_types):
             raise TypeError(f"Expected {len(arg_types)} arguments, got {len(args)}")

        for i, (arg, expected_type) in enumerate(zip(args, arg_types)):
            if not isinstance(arg, expected_type):
                raise TypeError(f"Arg {i} must be {expected_type.__name__}, got {type(arg).__name__}")

        result = func(*args)

        if not isinstance(result, return_type):
            raise TypeError(f"Return value must be {return_type.__name__}")

        return result

    return wrapper

add_numbers = contract(add, str, str, str)

try:
    res = add_numbers('Hello ', 'World!')
    print(res)
except TypeError as e:
    print(f"Error: {e}")
```
