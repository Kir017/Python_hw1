length = int(input('Введите длину плитки шоколада (в дольках):'))
width =  int(input('Введите ширину плитки шоколада (в дольках):'))
count =  int(input('Введите количество отломанных долек:'))
if count < width * length and ((count % length == 0) or (count % width == 0)):
    print(f'{length} {width} {count} -> можно разделить')
else: print(f'{length} {width} {count} -> нельзя разделить')
