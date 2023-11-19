import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG, filename='log2.log')
a = int(input('Введите первое число (не кратно 5):'))
logging.info(f'First num = {a}')
if a%5 == 0:
    raise Exception('Число не должно быть кратно 5!!')
b = int(input('Введите второе число:'))
logging.info(f'Second num = {b}')
try:
    division = a/b
except ZeroDivisionError:
    print("На ноль делить нельзя")
    logging.error(f'На ноль делить нельзя')
else:
    print('Ответ: ', division)
    logging.info(f'Result =  {division}')
finally:
    print('Как то так')
