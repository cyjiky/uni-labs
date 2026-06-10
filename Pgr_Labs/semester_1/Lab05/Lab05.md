# 👾 Lab05: Function closures and storing data in function scope

1. Реализуйте функцию `seq(...args)` с использованием замыканий и чеининга,
которая может быть вызвана по цепочке с произвольным количеством функций, а
первый вызов со значением типа `Number` приведет к исполнению переданных ранее
функций и возвращаемый результат должен быть.

```py
def seq(*args):
    funcs = list(args)

    def main(arg):

        if isinstance(arg, int):

            val = arg

            for func in reversed(funcs):
                val = func(val)
            return val

        elif callable(arg):
            funcs.append(arg)
            return main

    return main

res = seq(1,2,3,4,5)
print("#1")
res1 = seq(lambda x: x + 7)(lambda x: x * 2)(5)
print(f"seq = {res1}")

print("---")

print("#2")
res2 = seq(lambda x: x * 2)(lambda x: x + 7)(5)
print(f"seq = {res2}")

print("---")

print("#3")
res3 = seq(lambda x: x + 1)(lambda x: x * 2)(lambda x: x / 3)(lambda x: x - 4)(7)
print(f"seq = {res3}")
```

2. Реализуйте функцию `array()` создающую функциональный объект, который
содержит массив в своем замыкании и обеспечивает следующий интерфейс доступа
к нему:
- Создание нового экземпляра `const a = array();`
- Получение элемента по индексу `a(i)`
- Добавление элемента в конец `a.push(value)`
- Удаление последнего элемента и получение его значения `a.pop()`

```py
class Main:
    def __init__(self):
        self.data = []

    def __call__(self, index):
        try:
            return self.data[index]
        except IndexError:
            return None

    def push(self, val):
        self.data.append(val)
        return len(self.data)

    def pop(self):
        try:
            return self.data.pop()
        except IndexError:
            return None

def PyArr():
    return Main()

arr_py = PyArr()

arr_py.push('first')
arr_py.push('second')
arr_py.push('third')

arr_py.push(arr_py(0))
arr_py.push(arr_py(1))
arr_py.push(arr_py(2))

print(arr_py.pop())
print(arr_py.pop())
print(arr_py.pop())
```
