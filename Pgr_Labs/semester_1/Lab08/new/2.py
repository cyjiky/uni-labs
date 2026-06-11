# Реализуйте функцию store(value)
#   которая сохранит значение в замыкании
#   возвращаемой функции, а после ее вызова
#   вернет значение из замыкания,
#   как в примере:

"""
const read = store(5);
const value = read();
console.log(value); // Output: 5
"""


def store(val: int):
    def fn():
        return val

    return fn


print(store(5)())
