import sys

try:
    a = int(input("Сколько витаминок хочешь купить?"))
    b = float(input("По какой цене?"))
    c = str(input("Есть ли у вас социальная карта?"))
    skidka = 0
    result = 0

    if a <= 0 or b <= 0:
        sys.exit(print('Количество витаминок и цена должны быть положительными числами'))
    else:
        if a < 5:
            result = a * b
        elif a < 10:
            skidka = a * b / 10
            result = a * b - skidka
        elif a > 10:
            a = a - (a // 10)
            result = a * b

            if c == 'yes' or c == 'да' or c == 'no' or c == 'нет':
                if c == 'yes' or c == 'да':
                    skidkaTwo = result / 10
                    result = result - skidkaTwo
                    skidka = skidka + skidkaTwo
            else:
                sys.exit(print('Введите только да, нет, yes, no'))

        print('             ЧЕК                 ')
        print('---------------------------------')
        print("Соц. карта:", c)
        print('Сумма покупки: ', a * b, 'р.')
        print('Скидка:', skidka, 'р.')
        print('Итого:', result, 'р.')
        print('---------------------------------')
except:
    print('Вы ввели некорректное значение')

