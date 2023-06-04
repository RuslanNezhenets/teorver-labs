import matplotlib.pyplot as plt

#arr = [2, 2, 1, 3, 2, 3, 4, 2, 3, 2, 1, 3, 4, 2, 1]

arr = [340, 316, 325, 329, 351, 348, 330, 345, 352, 331,
       318, 332, 341, 318, 341, 353, 356, 320, 347, 349,
       352, 342, 337, 341, 350, 348, 327, 339, 340, 339]

n = len(arr)

print(arr)

arr.sort()

print("=" * 50)
print("Відсортований список")
print(arr)

discrete_statistical_series = []

number = 0
k = 0
for i in range(n):
    if i > 0:
        number += 1
    if i > 0 and arr[i] != arr[i - 1] or i == n - 1:
        discrete_statistical_series.append([arr[i - 1], number, number / n])
        if i == n - 1:
            discrete_statistical_series.append([arr[i], number, number / n])
        number = 0
        k += 1

print("=" * 50)
print("Дискретний статистичний ряд")
print("Варіанти     Частоти     Відносні частоти")
for row in discrete_statistical_series:
    for elem in row:
        print("  ", round(elem, 3), end='         ')
    print()


print("=" * 50)
print("Емпірична функція розподілу F*(x)")

number = 0
for i in range(len(discrete_statistical_series)):
    if i == 0:
        print(number, "при x <=", discrete_statistical_series[i][0])
    else:
        number += discrete_statistical_series[i - 1][2]
        print(round(number, 3), "при", discrete_statistical_series[i - 1][0] ,"< x <=", discrete_statistical_series[i][0])
    if i == len(discrete_statistical_series) - 1:
        number += discrete_statistical_series[i][2]
        print(round(number, 3), "при x >", discrete_statistical_series[i][0])

unique_numbers = list(set(arr))

relative_frequencies = []
for i in range(len(discrete_statistical_series)):
    relative_frequencies.append(discrete_statistical_series[i][2])

unique_numbers.sort()

plt.plot(unique_numbers, relative_frequencies)
plt.plot(unique_numbers, relative_frequencies, 'ro')
plt.title("Полігон")
plt.show()