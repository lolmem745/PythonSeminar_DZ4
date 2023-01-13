def numInputFloat(message):
    is_ok = True
    while is_ok:
        try:
            number = float(input(f"{message}"))
            is_ok = False
        except ValueError:
            print("Чето не то написал. Давай ещё раз.")
    return number


def numInputInt(message):
    is_ok = True
    while is_ok:
        try:
            number = int(input(f"{message}"))
            is_ok = False
        except ValueError:
            print("Чето не то написал. Давай ещё раз.")
    return number


a = numInputFloat("Введите вещественное число: ")
c = numInputInt("Введите количество знаков после запятой: ")
b = format(a, f".{c}f")
print(f"d = {10**-c}\nВаше число: {b}")
