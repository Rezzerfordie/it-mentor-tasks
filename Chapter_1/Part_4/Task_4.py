a = ['a', 's', '1', 'a', '32', '23']
a.sort()
a_ch = a[:3]
a_bu = a[3:]
print("Список с числами: ", a_ch)
print("Список с буквами: ", a_bu)
a_bu.pop()
a_bu.reverse()
print("Полученный список: ", a_bu)
