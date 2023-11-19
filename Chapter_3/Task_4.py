lst = []
dct = {}
for i in range(10):
    lst.append(i)
for k in range(5):
    dct.update({k : k*2})
for a in range(len(lst)):
    print(f'Чтение списка: {lst[a]}')
for k, v in dct.items():
    print(f'Чтение словаря: {k} - {v}')

