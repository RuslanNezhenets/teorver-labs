import math
import copy
from scipy.interpolate import make_interp_spline

import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt

#arr = [17.4, 15.1, 15.1, 15.4, 15.3, 15.7, 15.9, 16.0, 16.2, 16.4,
#15.2, 16.5, 15.0, 15.2, 15.3, 15.5, 15.3, 15.4, 18.0, 17.6,
#17.1, 15.2, 17.5, 16.6, 16.7, 16.8, 15.9, 15.7, 15.2, 15.3,
#16.0, 16.8, 16.2, 15.9, 16.0, 15.0, 16.3, 16.8, 15.5, 15.0]

arr = [340, 316, 325, 329, 351, 348, 330, 345, 352, 331,
       318, 332, 341, 318, 341, 353, 356, 320, 347, 349,
       352, 342, 337, 341, 350, 348, 327, 339, 340, 339]


n = len(arr)

print(arr)

arr.sort()

print("=" * 50)
print("Відсортований список")
print(arr)

discrete_statistical_series = []        #дискретний статистичний ряд

number = 0
k = 0
#створення дискретного статистичного ряду
for i in range(n):
    if i > 0:
        number += 1
    if i > 0 and arr[i] != arr[i - 1] or i == n - 1:
        discrete_statistical_series.append([arr[i - 1], number, number / n])
        if i == n - 1:
            discrete_statistical_series.append([arr[i], number, number / n])
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
        if discrete_statistical_series[j][0] == number + h and frequencies_number%2 == 0:   #якщо число це точка з парною частотою
            if j != len(discrete_statistical_series) - 1:
                frequencies += int(frequencies_number/2)
            else:
                frequencies += frequencies_number
            discrete_statistical_series[j][1] -= frequencies_number/2
        elif discrete_statistical_series[j][0] == number + h and frequencies_number%2 == 1: #якщо число це точка з непарною частотою
            if j != len(discrete_statistical_series) - 1:
                frequencies += int(frequencies_number/2 - 0.5)
            else:
                frequencies += frequencies_number
            discrete_statistical_series[j][1] -= int(frequencies_number/2 - 0.5)

    frequencies_list.append(frequencies)
    print('Інтервал (', number, ',', number + h, ')     ', "Частота", frequencies, "   Відносні частоти", frequencies/n)
    number += h
    frequencies = 0

print("="*80)
print("Емпірична функція розподілу F*(x)")

number = min(arr)
frequencies = 0
#створення масиву частот для подального виводу
for i in range(len(frequencies_list) + 1):
    print(round(frequencies, 3), "при x =", number)
    if i != len(frequencies_list):
        frequencies += frequencies_list[i] / n
    number += h

numbers = []
number = min(arr)
#створення масивів для виводу
for i in range(k):
    numbers.append(number)
    number += h
    frequencies_list[i] /= n

#Полігон
plt.plot(numbers, frequencies_list)
plt.plot(numbers, frequencies_list, 'ro')
plt.title("Полігон")
plt.show()

plt.plot([316, 324, 332, 340, 348, 356], [0, 0.133, 0.3, 0.467, 0.733, 1])
plt.plot([316, 324, 332, 340, 348, 356], [0, 0.133, 0.3, 0.467, 0.733, 1], 'ro')
plt.title("Графік емпіричної функції за інтегральним розподілом")
plt.show()

temp_numbers = []

density = []        #Щільність
for i in range(k):
    density.append(round(frequencies_list[i]/h, 3))
    temp_numbers.append(numbers[i] + h/2)

#Гістограма
fig, ax = plt.subplots()
ax.bar(temp_numbers, density, width = h)

X_Y_Spline = make_interp_spline(temp_numbers, density)

X_ = np.linspace(min(temp_numbers), max(numbers)+h/2, 500)
Y_ = X_Y_Spline(X_)

plt.plot(X_, Y_, 'r')
plt.title("Гістограма")
plt.show()



for i in range(len(frequencies_list)):
    frequencies_list[i] = frequencies_list[i]/h

fig, ax = plt.subplots()
ax.bar(temp_numbers, frequencies_list, width = h)

X_Y_Spline = make_interp_spline(temp_numbers, frequencies_list)

X_ = np.linspace(min(temp_numbers), max(temp_numbers))
Y_ = X_Y_Spline(X_)

plt.plot(X_, Y_, 'r')
plt.title("Гістограма відносних частот")
plt.show()