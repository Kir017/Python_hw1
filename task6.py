number = int(input('введите шестизначное число'))
if 99999 < number < 1000000:
    numberFirst = number //1000
    numberSecond = number % 1000
    sumFirs = numberFirst // 100 + numberFirst % 10 + numberFirst // 10 % 10
    sumSecond = numberSecond // 100 + numberSecond % 10 + numberSecond // 10 % 10
    if sumFirs == sumSecond:
        print(number, '<- счастливый билет')
    else: print(number, '<- обычный билет')
else: print ('Введено не верное число')
