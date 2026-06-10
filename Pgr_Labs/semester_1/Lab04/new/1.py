
# Реализуйте функцию sum(...args), 
#   которая суммирует все свои аргументы, 
#   пятью разными способами. 
#   Примеры вызовов с результатами:

"""
const a = sum(1, 2, 3) // a === 6
const b = sum(0) // b === 0
const c = sum() // c === 0
const d = sum(1, -1, 1) // d === 1
const e = sum(10, -1, -1, -1) // e === 7
Цикл for
Цикл for..of
Цикл while
Цикл do..while
Метод Array.prototype.reduce()
"""

def a(*args) -> list:
    x = 0
    for i in range(len(list(args))):
        x += list(args)[i]
    return x 

def b(*args) -> list:
    x = 0
    for i in range(len(args)):
        x += list(args)[i]
    return x 

def c(*args) -> list:
    i, x = 0, 0
    while i < len(args):
        x += args[i]
        i += 1
    return x 

# def d(*args) -> list:
#     return [x for x in list(args)]

print(f'a: {a(1, 2, 3)}')
print(f'b: {b(0)}')
print(f'c: {c()}')
# print(f'd: {d(1, -1, 1)}')