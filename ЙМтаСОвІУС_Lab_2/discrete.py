import math

arr = [2, 2, 1, 3, 2, 3, 4, 2, 3, 2, 1, 3, 4, 2, 1]

n = len(arr)

arr.sort()

discrete_statistical_series = []

number = 0
k = 0
for i in range(n):
    if i > 0:
        number += 1
    if i > 0 and arr[i] != arr[i - 1] or i == n - 1:
        if i == n - 1:
            number += 1
        discrete_statistical_series.append([arr[i - 1], number, number / n])
        number = 0
        k += 1

print("=" * 50)
print("Дискретний статистичний ряд")
print("Варіанти     Частоти     Відносні частоти")
for row in discrete_statistical_series:
    for elem in row:
        print("  ", round(elem, 3), end='         ')
    print()

#====================================== Лабораторна робота №2 ======================================

max = 0
option = []

for elem in discrete_statistical_series:
    if elem[1] > max:
        option = []
    if elem[1] >= max:
        option.append(elem[0])
        max = elem[1]

print("=" * 50)
print("Мода Mo")
if len(option) == 1:
    print("Варианта:", option[0], "Частота:", max)
    print("Ряд одномодальный")
    print("Mo =", option[0])
else:
    print("Варианты:", option[0], "Частота:", max)
    print("Ряд двомодальный")
    print("Mo =", option)

print("=" * 50)
print("Медиана Me")
print(arr)
if n%2 == 1:
    print("Me =", arr[int((n-1)/2 + 1)])
else:
    print("Me =", arr[int((n - 1) / 2)], ",", arr[int((n - 1) / 2 + 1)])

print("=" * 50)
print("Коэфициент асимметрии As")

Mx = 0
Mx2 = 0
for elem in discrete_statistical_series:
    Mx += elem[0]*elem[2]
    Mx2 += (elem[0]**2)*elem[2]

Dx = Mx2 - Mx**2

sigma = math.sqrt(Dx)

#M3 = (x-M[x])^3*pi

µ3 = 0
for elem in discrete_statistical_series:
    µ3 += ((elem[0] - Mx)**3)*elem[2]

As = µ3/(sigma**3)

print("As =", round(As, 5))

print("=" * 50)
print("Эксцесс Es")

µ4 = 0
for elem in discrete_statistical_series:
    µ4 += ((elem[0] - Mx)**4)*elem[2]

Es = µ4/(sigma**4) - 3

print("Es =", round(Es, 5))