"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
def check_string(first_string, second_string):
    if isinstance(first_string, str) == 0 or isinstance(second_string, str) == 0:
      return 0
    elif first_string == second_string:
      return 1 # Строки одинаковые
    elif first_string > second_string:
        return 2 # Первая строка длиннее
    elif first_string != second_string and second_string == 'learn':
        return 3 # Cтроки разные и вторая строка 'learn'


def main():
    result = check_string("1", 1)
    print(result)
    
if __name__ == "__main__":
    main()
