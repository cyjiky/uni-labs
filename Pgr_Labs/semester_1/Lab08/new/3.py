# Реализуйте функцию contract(fn, ...types)
#   которая оборачивает fn (первый аргумент)
#   и проверяет типы аргументов (все аргументы
#   кроме первого и последнего) и результата
#   (последний аргумент), генерируя исключение
#   TypeError, если типы не совпадают.
#   Как в следующем примере:

"""
const add = (a, b) => a + b;
const addNumbers = contract(add, Number, Number, Number);
const res = addNumbers(2, 3);
console.dir(res); // Output: 5
"""

"""
const concat = (s1, s2) => s1 + s2;
const concatStrings = contract(concat, String, String, String);
const res = concatStrings('Hello ', 'world!');
console.dir(res); // Output: Hello world!
"""
from typing import Any


def contract(fn, *types: Any):
    def wrapper(*args):
        for type, arg in zip(types, args):
            if not isinstance(arg, type):
                raise TypeError("Hello World")
            
        res = fn(*args)
        if not isinstance(res, list(types)[-1]):
            raise TypeError("Hello World x2")
        return res

    return wrapper


def func(a, b):
    return a + b


add_num = contract(func, int, int, int)
print(add_num(2, 3))

concat_strings = contract(func, str, str, str)
print(concat_strings("Hello ", "World"))
