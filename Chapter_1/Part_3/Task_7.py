a = int(input('Введите число A:'))
b = int(input('Введите число B:'))
c = int(input('Введите число C:'))
if a < b < c or c < b < a:
    print('true')
else:
    print('false')