col = str(input("Введите данные через пробел: ")).split()

#Вариант 1
res = []
for i in col:
    if len(i) <= 3:
        res.append(i)
print(res)

#Вариант 2
for i in col:
    if len(i) > 3:
        col.remove(i)
print(col)