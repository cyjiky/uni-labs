#  👾 Lab02: Identifiers, Loops, Functions, Objects & Collections
## ✔️ Identifiers
1. Объявите переменную и запишите в нее свое имя как литерал строки.
2. Объявите константу и запишите в нее год своего рождения как литерал числа.
3. Создайте функцию, которая печатает приветствие и имеет один аргумент: `name`.

```java
public class Lab1 {

    public static final int birthyear = 2008;

    public static void main(String[] args) {

        String myName = "Viktoriia";
        String[] names = { "Maria", "Dascha", "Dami", myName };

        // передвигаемся по масиву и выводим все значения по очереди
        for (int i = 0; i < names.length; i++) {
            System.out.println("Hi, " + names[i]);
        }
    }

```

## ✔️ Loops
4. Реализуйте функцию `range(start: number, end: number): array` которая отдает
массив чисел из диапазона [15, 30] включая крайние числа.
5. Реализуйте функцию `rangeOdd(start: number, end: number): array` которая
отдает массив нечетных чисел из диапазона [15, 30] включая крайние числа.

```java
    public class Lab1 {

        int num = 30; 

        for (int n = 15; n <= num; n++) {
            System.out.println(n);
        }
    }

```

## ✔️ Functions
Вложенные вызовы функций в цикле
- Реализуйте функцию `average` с сигнатурой
`average(a: number, b: number): number` вычисляющую среднее арифметическое своих
аргументов.
- Реализуйте функцию `square` с сигнатурой `square(x: number): number`
вычисляющую квадрат своего аргумента.
- Реализуйте функцию `cube` с сигнатурой `cube(x: number): number`
вычисляющую куб своего аргумента.
- Вызовите функции `square` и `cube` в цикле от 0 до 9, вычисляя, соответственно
квадрат и куб от переменной цикла. Передайте квадрат и куб на каждой итерации в
функцию `average`. Результаты сложите в массив и возвратите из функции
`calculate`.

```java
    import java.util.Scanner; 

    public class Main {

        Scanner scan = new Scanner(System.in);
        System.out.println("Введите первое число... "); 
        int numX = scan.nextInt(); 

        int squareValue = Taschenrechner.square(numX); 
        int cubeValue = Taschenrechner.cube(numX);
        double averageValue = Taschenrechner.average(squareValue, cubeValue);

        System.out.println("Среднее арифметическое между квадратом и кубом: " + averageValue);

        scan.close(); 
    }
```
```java
    // детский класс 
    public class Taschenrechner {

        // создаем функции, для родительского класса

        public static int square(int numX) {
            int result = numX * numX; 
            System.out.println("Ваше число в квадрате: " + result); 
            return result; 
        }

        public static int cube(int numX) {
            int result = numX * numX * numX;
            System.out.println("Ваше число в кубе: " + result);
            return result;
        }

        public static double average(int numA, int numB) {
            return (numA + numB) / 2.0;
        }
    }
}
```
## ✔️ Objects
7. Выполнить следующие пункты внутри функции `fn` (см. заготовку: `7-objects.js`)
- Создайте объект с одним полем `name` и присвойте его в константу.
- Создайте объект с одним полем `name` и присвойте его в переменную.
- Попробуйте поменять поле `name` у обоих объектов.
- Попробуйте присвоить другой объект в оба идентификатора.
- Объясните поведение кода и оставьте только рабочий код.
8. Реализуйте функцию `createUser` с сигнатурой
`createUser(name: string, city: string): object`. Пример вызова:
`createUser('Marcus Aurelius', 'Roma')` функция должна вернуть объект
`{ name: 'Marcus Aurelius', city: 'Roma' }`

```java
public class Main {
 
    // метод, который увеличивает переданное число на 1
    public static int inc(int n) {
        return n + 1;
    }
 
    public static void main(String[] args) {
 
        int a = 5; 
        int b = inc(a); 
 
        // выводим все значения
        System.out.println("Решение 1: ");
        System.out.println("A: " + a);
        System.out.println("B: " + b);
 
    }
}
```
## ✔️ Collections
9. Реализуйте телефонную книгу на массиве объектов.
- Объявите массив объектов с двумя полями: `name` и `phone` для хранения
телефонной книги. Пример объекта:
`{ name: 'Marcus Aurelius', phone: '+380445554433' }` и добавьте несколько
объектов в массив, чтоб было на чем проверять.
- Реализуйте функцию `findPhoneByName` с сигнатурой
`findPhoneByName(name: string): string`. При вызове функция должна находить
объект, где поле `name` равно аргументу `name` и возвращать номер телефона из
объекта. Для поиска воспользуйтесь циклом `for`.
A. Реализуйте телефонную книгу на хеш-таблицах, т.е. справочниках (объектах).
- Задайте справочник (объект) с ключами равными значениям поля `name` (из
предыдущего примера) и значениями равными полю `phone`.
- Реализуйте функцию `findPhoneByName` с сигнатурой
`findPhoneByName(name: string): string` которая находит телефон в хеше по имени
и возвращает номер телефона. Используйте `hash[key]` для поиска телефона.
```java
import java.util.HashMap; // библиотека java

public class Book {

    public static void main(String[] args) {
        User[] array = new User[] { new User("Viky", "+38(067) *** **52"), new User("Daria", "+38(067) *** **48"),
                new User("Mariia", "+38(067) *** **99"), };

        // поиск по имени в массиве
        String phone = findPhoneInArray(array, "Viky");
        System.out.println("Phone: " + phone);

        // создаие в хеш-таблицы
        HashMap<String, String> bookHash = new HashMap<>();
        bookHash.put("Viky", "+38(067) *** **52");
        bookHash.put("Daria", "+38(067) *** **48");
        bookHash.put("Mariia", "+38(067) *** **99");

        // поис по имени в хеш-таблице
        phone = findPhoneInHashMap(bookHash, "Viky");
        System.out.println("Phone: " + phone);
    }

    // поиск телефона по имени в массиве
    public static String findPhoneInArray(User[] phoneBook, String name) {
        // проходимся по массиву
        for (int i = 0; i < phoneBook.length; i++) {
            if (phoneBook[i].name.equals(name)) { // усдлвие если-то
                return phoneBook[i].phone; // возвразаем значение
            }
        }
        return "not found";
    }

    // поис по имени в хеш-таблице
    public static String findPhoneInHashMap(HashMap<String, String> phoneBook, String name) {
        // возращаем "не найдено"
        return phoneBook.getOrDefault(name, "not found");
    }
}

class User { // класс User для записей в телефонной книге
    String name;
    String phone;

    // конструктор для создания объектов
    public User(String name, String phone) {
        this.name = name;
        this.phone = phone;
    }
}
```






