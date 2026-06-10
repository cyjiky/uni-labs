# Реализуйте композицию функций 
#   справа налево (без использования рекурсии), 
#   которая будет подавлять ошибки, если
#   композируемые функции будут их бросать, 
#   то, исполнение функции завершается с undefined, 
#   а на ошибки можно будет подписаться через 
#   f.on('error', e => { ... });.

from typing import Callable
from functools import reduce 

def pipe2(*func, revers=False) -> Callable:
    for f in func:
        if not callable(f):
            raise TypeError(
                'All pipe arguments should be functions'
            )
        
    if revers == True:
        func = func[::-1]
     
    return lambda x: reduce(
        lambda arg, f: f(arg), func, x
    )

inc = lambda x: x + 1
twice = lambda x: x * 2
cube = lambda x: x ** 3 

print(pipe2(inc, twice, cube, revers=True)(5))
print(pipe2(inc, twice, cube, revers=False)(5))