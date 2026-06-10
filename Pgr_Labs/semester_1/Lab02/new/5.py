# Реализуйте телефонную книгу на массиве объектов.


# Объявите массив объектов с двумя полями:
#   name и phone для хранения телефонной книги.
#   Пример объекта: { name: 'Marcus Aurelius', phone: '+380445554433' }
#   и добавьте несколько объектов в массив, чтоб было на чем проверять.

books = [
    {
        "name": "Marcus", 
        "phone": "+380445554433"
    },
    {
        "name": "Richard", 
        "phone": "+380292837549"
    },
    {
        "name": "Uwe", 
        "phone": "+380443974523"
    },
]


# Реализуйте функцию findPhoneByName с сигнатурой findPhoneByName(name: string): string.
#   При вызове функция должна находить объект, где поле name равно аргументу name
#   и возвращать номер телефона из объекта. Для поиска воспользуйтесь циклом for.
#   Реализуйте телефонную книгу на хеш-таблицах, т.е. справочниках (объектах).


def find_phone_by_name(name: str) -> str | None:
    for i in books:
        if i["name"] == name:
            return i["phone"]


print(find_phone_by_name(name="Uwe"))


def find_phone_by_name2(name: str) -> list:
    return [x for x in books if x["name"] == name]


print(find_phone_by_name2(name="Uwe"))


# Задайте справочник (объект) с ключами равными значениям поля
#   name (из предыдущего примера) и значениями равными полю phone.

phone_book = {
    "Marcus": "+380445554433",
    "Richard": "+380292837549",
    "Uwe": "+380443974523",
}
print(f'phone_book -> {phone_book["Uwe"]}')


# Реализуйте функцию findPhoneByName с сигнатурой
#   findPhoneByName(name: string): string которая находит телефон
#   в хеше по имени и возвращает номер телефона.
#   Используйте hash[key] для поиска телефона


def find_phone_by_name_2(name: str) -> str:
    return phone_book.get(name)


print(f"find_phone_by_name_2 -> {find_phone_by_name_2('Uwe')}")
