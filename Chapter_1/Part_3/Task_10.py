a = int(input('Введите число A:'))
b = int(input('Введите число B:'))
a_ch = a % 2
b_ch = b % 2
if a_ch == 1 and b_ch == 0 or a_ch == 0 and b_ch == 1:
    print('true')
else:
    print('false')