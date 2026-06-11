# Реализуйте функцию removeElement(array, item)
#   для удаления элемента item из массива array. 
#   Например:

"""
const array = [1, 2, 3, 4, 5, 6, 7];
removeElement(array, 5);
console.log(array);
// Результат: [1, 2, 3, 4, 6, 7]
"""

# или

"""
const array = ['Kiev', 'Beijing', 'Lima', 'Saratov'];
removeElement(array, 'Lima'); // удалит 'Lima' из массива
removeElement(array, 'Berlin'); // не удалит ничего
console.log(array);
// Результат: ['Kiev', 'Beijing', 'Saratov']
"""
from typing import List

arr1 = [1, 2, 3, 4, 5, 6, 7]
arr2 = ['Kiev', 'Beijing', 'Lima', 'Saratov']

def remove_element(arr: List, *el: int | str) -> List:
    return [elem for elem in arr if elem not in el]

print(remove_element(arr1, 2, 5))
print(remove_element(arr2, 'Kiev', 'Lima'))