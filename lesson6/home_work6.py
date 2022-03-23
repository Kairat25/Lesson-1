print("Загадай любое число от 1 до 1 000 000 000: ")
print('Нужные команды \n*** ДА *** \n*** МЕНЬШЕ *** \n*** БОЛЬШЕ ***')
a = 0
b = 1_000_000_000
f = 0
while True:
    f += 1
    q = (b + a) // 2
    otvet = input(f"Ваше число {q}? ")
    if otvet.lower() == "да":
        print(f"Мы угадали ваше число {q} \nувас ушло {f} попыток")
        break
    elif otvet.lower() == "меньше":
        b = q
    elif otvet.lower() == "больше":
        a = q
    else:
        print("Такой команды нету!")