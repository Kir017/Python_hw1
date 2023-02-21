number = int(input('введите количество журавликов: '))
if number % 6 == 0:
    petr = number /3 /2
    sergey = number /3 /2
    katiy = number - number / 3
    print (f'Петя сделал {int (petr)} , Сергей сделал {int (sergey)} , Катя сделала {int(katiy)}')
else: print ('Не корректное количество журавлей')