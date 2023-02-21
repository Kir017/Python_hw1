number = int(input('Введите число'))
sum = 0
while number > 0:
    sum = sum + number % 10
    number = number // 10
print (f'Сумма цифр в числе = {sum}')
