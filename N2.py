def dividerAdd(num):
    dividers = []
    for i in range(2, num + 1):
        divideable = True
        while divideable:
            if num % i == 0:
                dividers.append(i)
                num = int(num / i)
            else:
                divideable = False
    return dividers


def numInput(message):
    is_ok = True
    while is_ok:
        try:
            number = int(input(f"{message}"))
            is_ok = False
        except ValueError:
            print("Чето не то написал. Давай ещё раз.")
    return number


number = numInput("Введите натуральное число: ")
list = dividerAdd(number)
if len(list) == 1:
    print(f"Число {list[0]} — простое")
else:
    print(f"Список простых множителей числа {number} — {list}")
