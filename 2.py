print("тут о программе короче напишиешь")

mode = input("чем вы хотите воспользоваться: конвертер весов(напишите 1), доходность вклада(напишите 2), перевод систем счисления(напишите 3)")

if mode == 1:
    print("какой перевод вы хотите:")
    print("тонны-граммы(напишите 1)")
    print("тонны-килограммы(напишите 2)")
    print("килограммы-граммы(напишите 3)")
    print("килограммы-тонны(напишите 4)")
    print("граммы-килограммы(напишите 5)")
    print("граммы-тонны(напишите 6)")
    unitChoice = input()
    number1 = int(input())
    if unitChoice == 1:
        print(number1 * 1000000)
    elif unitChoice == 1:
        pass
    elif unitChoice == 1:
        pass
    elif unitChoice == 1:
        pass
    elif unitChoice == 1:
        pass
    elif unitChoice == 1:
        pass
    else:
        print("это просто пипяо, такого перевода нема")
elif mode == 2:
    initialAmount = float(input("Введите начальную сумму вклада: "))
    interestRate = float(input("Введите годовую процентную ставку: "))
    years = int(input("Введите количество лет вклада: "))

    finalAmount = initialAmount * (1 + interestRate / 100) ** years

    print(f"Через {years} лет при годовой процентной ставке {interestRate}% ваш вклад вырастет до {initialAmount:.2f} рублей.")
elif mode == 3:
    print("какой перевод вы хотите:")
    print("десятичная-двоичная(напишите 1)")
    print("десятичная-восьмиричная(напишите 2)")
    print("килограммы-граммы(напишите 3)")
    print("килограммы-тонны(напишите 4)")
    print("граммы-килограммы(напишите 5)")
    print("граммы-тонны(напишите 6)")
else:
    print("это просто пипяо, такого режима у нас нет")
