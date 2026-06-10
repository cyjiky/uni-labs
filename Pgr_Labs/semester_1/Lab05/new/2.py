# Реализуйте функцию array() создающую функциональный объект,
#   который содержит массив в своем замыкании
#   и обеспечивает следующий интерфейс доступа к нему:
#
# Создание нового экземпляра const a = array();
#
# Получение элемента по индексу a(i)
#
# Добавление элемента в конец a.push(value)
#
# Удаление последнего элемента и получение
#   его значения a.pop()

"""
const arr = array();

arr.push('first');
arr.push('second');
arr.push('third');

console.log(arr(0)); // Выводит: first
console.log(arr(1)); // Выводит: second
console.log(arr(2)); // Выводит: third

console.log(arr.pop()); // Выводит: third
console.log(arr.pop()); // Выводит: second
console.log(arr.pop()); // Выводит: first

console.log(arr.pop()); // Выводит: undefined
"""

from typing import List

arr = []

def add_el(arr: List) -> None:
    arr.append(input("write el: "))

def update_el(arr: List) -> List:
    el_id = int(input("write el_id: "))
    new_el = input("write el_id: ")
    arr[el_id] = new_el
    return arr

def del_el(arr: List) -> List:
    el_id = int(input("write el_id: "))
    del arr[el_id]
    return arr

while True:
    val = input("action [add | update | del | stop]: ").strip().upper()
    match val:
        case "ADD":
            add_el(arr)
            print(arr)
        case "UPDATE":
            update_el(arr)
            print(arr)
        case "DEL":
            del_el(arr)
            print(arr)
        case "STOP":
            break
        case _:
            print("Unknown value")
