import math
import copy

arr = [17.4, 15.1, 15.1, 15.4, 15.3, 15.7, 15.9, 16.0, 16.2, 16.4,
15.2, 16.5, 15.0, 15.2, 15.3, 15.5, 15.3, 15.4, 18.0, 17.6,
17.1, 15.2, 17.5, 16.6, 16.7, 16.8, 15.9, 15.7, 15.2, 15.3,
16.0, 16.8, 16.2, 15.9, 16.0, 15.0, 16.3, 16.8, 15.5, 15.0]

n = len(arr)

print(arr)

arr.sort()

discrete_statistical_series = []        #дискретний статистичний ряд

number = 0
k = 0
#створення дискретного статистичного ряду
for i in range(n):
    if i > 0:
        number += 1
    if i > 0 and arr[i] != arr[i - 1] or i == n - 1:
        if i == n - 1:
            number += 1
        discrete_statistical_series.append([arr[i - 1], number, number / n])
        number = 0
        k += 1

rezerv = copy.deepcopy(discrete_statistical_series)     #копія ряду

print("=" * 50)
print("Дискретний статистичний ряд")
print("Варіанти     Частоти     Відносні частоти")
for row in discrete_statistical_series:
    for elem in row:
        print("  ", round(elem, 3), end='         ')
    print()

print("=" * 50)
k = int(round(math.sqrt(n), 0))
print("Кількість інтервалів:", k)

h = (max(arr) - min(arr))/k
print("Крок:", h)

number = min(arr)
frequencies = 0
frequencies_list = []

print("Інтервальний статистичний ряд")
for i in range(k):
    for j in range(len(discrete_statistical_series)):
        frequencies_number = discrete_statistical_series[j][1]
        if number <= rezerv[j][0] < number + h:     #якщо число знаходиться в проміжку
            frequencies += frequencies_number
        if discrete_statistical_series[j][0] == number + h and frequencies_number%2 == 0:   #якщо число че точка з парною частотою
            if j != len(discrete_statistical_series) - 1:
                frequencies += int(frequencies_number/2)
            else:
                frequencies += frequencies_number
            discrete_statistical_series[j][1] -= frequencies_number/2
        elif discrete_statistical_series[j][0] == number + h and frequencies_number%2 == 1: #якщо число че точка з непарною частотою
            if j != len(discrete_statistical_series) - 1:
                frequencies += int(frequencies_number/2 - 0.5)
            else:
                frequencies += frequencies_number
            discrete_statistical_series[j][1] -= int(frequencies_number/2 - 0.5)

    frequencies_list.append(frequencies)
    print('Інтервал (', number, ',', number + h, ')     ', "Частота", int(frequencies), "   Відносні частоти",
          frequencies / n)
    number += h
    frequencies = 0

#====================================== Лабораторна робота №2 ======================================

print("=" * 50)
print("Мода Mo")

f1 = 0                              #частота предыдущего интервала
f2 = max(frequencies_list)          #частота модального интервала
f3 = 0                              #частота следующего интервала

border = 0                          #нижняя граница модального интервала;

for i in range(len(frequencies_list)):                      #Ищем интервал с наибольшой частотой
    if max(frequencies_list) == frequencies_list[i]:
        border = min(arr) + h * i

for i in range(len(frequencies_list)):
    if f2 == frequencies_list[i]:
        if i != 0:
            f1 = frequencies_list[i - 1]
        if i != len(frequencies_list):
            f3 = frequencies_list[i + 1]

Mo = border + h * ((f2 - f1)/((f2 - f1) + (f2 - f3)))
A = border + h/2                    #условный нуль, равный варианте с максимальной частотой (нужен будет дальше)

print("Mo =", Mo)

print("=" * 50)
print("Медиана Me")
print(arr)
if n%2 == 1:
    print("Медианным будет тот интервал, который содержит эту варианту:", arr[int((n-1)/2 + 1)])
else:
    print("Медианным будет тот интервал, который содержит эти варианты:",
          arr[int((n - 1) / 2)], ",", arr[int((n - 1) / 2 + 1)])

a = min(arr)
b = a + h
for i in range(len(frequencies_list)):
    if n%2 == 1:
        if a <= arr[int((n-1)/2 + 1)] <= b:
            border = a
    else:
        if a <= arr[int((n - 1) / 2)] <= b and a <= arr[int((n - 1) / 2 + 1)] <= b:
            border = a
    a += h
    b += h

print("Нижняя граница медианного интервала:",border)

nm = 0                                  #частота медианного интервала
nm1 = 0                                 #накопленная частота предыдущего интервала.
temp = min(arr)
for i in range(len(frequencies_list)):
    if border == temp:
        nm = frequencies_list[i]
        break
    temp += h
    nm1 += frequencies_list[i]

Me = border + h * (0.5*n - nm1)/nm

print("Me =", round(Me, 3))

print("=" * 50)
print("Коэфициент асимметрии As")

a = min(arr)
b = a + h


xn = 0              #Среднее значение изучаемого признака по способу моментов.
xi = []

a = min(arr)
b = a + h
for i in range(len(frequencies_list)):
    xi.append(((a + b)/2 - A)/h)
    xn += (xi[i] * frequencies_list[i]) / sum(frequencies_list) * h

    a += h
    b += h

xn += A
D = 0


for i in range(len(frequencies_list)):
    D += ((xi[i])**2 * frequencies_list[i])/sum(frequencies_list) * h**2
D -= (xn - A)**2

sigma = math.sqrt(D)


xb = 0              #Средняя частота

a = min(arr)
b = a + h
for i in range(len(frequencies_list)):
    xb += (a+b)/2 * frequencies_list[i]/sum(frequencies_list)

    a += h
    b += h

µ2 = µ3 = µ4 = 0

a = min(arr)
b = a + h
for i in range(len(frequencies_list)):
    µ3 += (((a + b) / 2 - xb) ** 3) * frequencies_list[i] / n
    µ4 += (((a + b) / 2 - xb) ** 4) * frequencies_list[i] / n

    a += h
    b += h

As = µ3/(sigma**3)

print("As =", round(As, 3))

print("=" * 50)
print("Эксцесс Es")

Es = µ4/(sigma**4) - 3
print("Es =", round(Es, 3))