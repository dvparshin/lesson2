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
    if isinstance(first_string, str) and isinstance(second_string, str) and first_string == second_string:
      print("1") # Строки одинаковые
    else:
        print("0") # Строки одинаковые 
    if first_string > second_string:
        print("2") # Первая строка длиннее
    if first_string != second_string or second_string == 'learn':
        return ("3") # Cтроки разные и вторая строка 'learn'

def main():
    result = check_string("1", "learn")
    print(result)
    
if __name__ == "__main__":
    main()
