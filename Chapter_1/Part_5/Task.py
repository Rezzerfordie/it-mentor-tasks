dict = {"Name": "Denis",
        "Age": 38,
        "Gender": "Male",
        'Height': 178,
        'Weight': 64,
        'Size Leg': 41}
print('Исходный словарь: ', dict)
print('Вывод по ключам: ',dict["Name"],
      dict["Age"],
      dict["Gender"],
      dict['Height'],
      dict['Weight'],
      dict['Size Leg'])
dict['Size Leg EU'] = 42
print('Добавил размер ноги по EU: ',dict)
dict.pop('Age')
print('Удалил возраст: ',dict)
