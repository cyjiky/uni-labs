# 👾 Lab06: Композиция функций

1. Напишите функцию `pipe`, композирующую передаваемые в нее аргументы слева
направо. `const pipe = (...fns) => x => ...` А если хоть один из аргументов
окажется не функционального типа, то `pipe` должен выбросить ошибку.
Например, если у нас есть три функции:
```js
const inc = x => ++x;
const twice = x => x * 2;
const cube = x => x ** 3;
```
И нам нужно скомпозировать их так `const f = pipe(inc, twice, cube);`
то при вызове `const x = f(5);` нужно ожидать, что `x` примет значение `1728`.
А если мы скомпозируем `const f = pipe(inc, inc);` то при вызове
`const x = f(7);` значение `x` будет `9`. Но если мы передадим не функцию в
`pipe`, например: `const f = pipe(inc, 7, cube);` то, не дожидаясь вызова `f`,
сразу получим ошибку.

```python
def pipe(*fns):
    for fn in fns:
        if not callable(fn):
            raise TypeError(f"'{fn}'")

    def composed(x):
        res = x
        for fn in fns:
            res = fn(res)
        return res
    return composed

def inc(x):
    return x + 1

def twice(x):
    return x * 2

def cube(x):
    return x ** 3

try:
    f = pipe(inc, twice, cube)
    x = f(5)
    print(f"F(5): {x}")  # 1728
except Exception as e: print(e)

try:
    f2 = pipe(inc, inc)
    x2 = f2(7)
    print(f"F2(7): {x2}") # 9
except Exception as e: print(e)

try:
    error = pipe(inc, 7, cube)
except TypeError as e: print(f"Fehler: {e}")
```
2. Реализуйте композицию функций справа налево (без использования рекурсии),
которая будет подавлять ошибки, если композируемые функции будут их бросать,
то, исполнение функции завершается с `undefined`, а на ошибки можно будет
подписаться через `f.on('error', e => { ... });`.

```python
def compose(*fns):
    for fn in fns:
        if not callable(fn):
            raise TypeError(f"'{fn}' keine Funktion")

    arr = []

    def composed(x):
        res = x
        for fn in reversed(fns):
            try: res = fn(res)
            except Exception as e:
                for undefined in arr:
                    undefined(e)
                return None
        return res

    def on(new, undefined):
        if new == 'error': arr.append(undefined)
    composed.on = on
    return composed

def inc(x): return x + 1
def square(x): return x * x
def n_arb(x): raise ValueError("Error")

f = compose(inc, square)
print(f"Antwort: {f(5)}")  # 26

error = compose(inc, n_arb, square)
error.on('error', lambda e: print(f"Fehler: {e}"))

res = error(5)
print(f"Antwort: {res}")
```
