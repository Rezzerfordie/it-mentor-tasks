a = 1
num_cyc = []
summ = 0
aver = 0
while a == 1:
    b = int(input('Введите число:'))
    num_cyc.append(b)
    summ+=b
    if b == 0:
        num_cyc.pop()
        aver = summ/len(num_cyc)
        break
print (f"Среднее число = {aver}")