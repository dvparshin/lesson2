"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""
def determine_age(age):
    if age < 0 or age >= 90:
        return "В этом возрасте еще/уже не работают"
    elif age >=0 and age <=6:
        return "Пользователь должен учиться в детском саду"
    elif age >=7 and age <= 16:
        return "Пользователь должен учиться в школе"
    elif age >=17 and age <= 23:
        return "Пользователь должен учиться в ВУЗе"
    else:
        return "Пользователь должен работать"

def main():
    user_age = int(input("Введите свой возраст: "))
    result = determine_age(user_age)
    print(result)


if __name__ == "__main__":
    main()
