# Выполнить следующие пункты внутри функции fn (см. заготовку: 7-objects.js)

# Создайте объект с одним полем name и присвойте его в константу.
USERS = {"name": "Viky"}
print(USERS["name"])

# Создайте объект с одним полем name и присвойте его в переменную.
users = {"name": "Viky"}
print(users["name"])

# Попробуйте поменять поле name у обоих объектов.
USERS["name"] = "Vikyy"
users["name"] = "Vikyy2"

print(USERS)
print(users)

# Попробуйте присвоить другой объект в оба идентификатора
"""
-> В питоне возможно присвоить другой объект в константу, однако 
    само понятие константы говорит о том, что её нельзя изменять
    или присваивать туда что-то другое
"""
users["city"] = "Kyiv"
print(users)


# Реализуйте функцию createUser с сигнатурой createUser(name: string, city: string): object.
#   Пример вызова: createUser('Marcus Aurelius', 'Roma')
#   функция должна вернуть объект { name: 'Marcus Aurelius', city: 'Roma' }


def createUser(name: str, city: str) -> dict:
    return {
        "name": name, 
        "city": city
    }
print(createUser("Marcus Aurelius", "Roma"))
