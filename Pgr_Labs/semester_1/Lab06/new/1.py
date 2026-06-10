# Напишите функцию pipe, композирующую передаваемые 
#   в нее аргументы слева направо. 
#   const pipe = (...fns) => x => ... 
#   А если хоть один из аргументов окажется 
#   не функционального типа, то pipe должен 
#   выбросить ошибку. Например, если у нас 
#   есть три функции:

"""
const inc = x => ++x;
const twice = x => x * 2;
const cube = x => x ** 3;
"""

# И нам нужно скомпозировать их так 
#   const f = pipe(inc, twice, cube); 
#   то при вызове const x = f(5); 
#   нужно ожидать, что x примет значение 1728. 
#   А если мы скомпозируем const f = pipe(inc, inc); 
#   то при вызове const x = f(7); значение x будет 9. 
#   Но если мы передадим не функцию в pipe, 
#   например: const f = pipe(inc, 7, cube); 
#   то, не дожидаясь вызова f, сразу получим ошибку

from typing import Callable
from functools import reduce

def pipe(*func) -> Callable:
    for f in func:
        if not callable(f):
            raise TypeError(
                'All pipe arguments should be functions'
            )
    return lambda x: reduce(
        lambda arg, f: f(arg), func, x
    )

inc = lambda x: x + 1
twice = lambda x: x * 2
cube = lambda x: x ** 3 

print(pipe(inc, twice, cube)(5))
print(pipe(inc, inc)(7))
print(pipe(inc, 7, cube))
