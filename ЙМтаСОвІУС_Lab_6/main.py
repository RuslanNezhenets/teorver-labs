import statsmodels.api as sm
import numpy as np
import pandas as pd

rounding = 5

data = {
'Y': [1746, 1612, 1750, 1842, 1891, 1908, 2316, 2338, 2405, 2343, 2515, 2610, 2829, 2916, 2983],
'X': [1850, 1740, 1910, 2050, 2070, 2100, 2300, 2350, 2450, 2500, 2650, 2700, 2850, 2900, 2900],
'Z': [430, 420, 390, 300, 340, 350, 550, 530, 490, 350, 350, 410, 460, 480, 550]
}

info = pd.DataFrame(data, index=range(1, 16))
info['X^2'] = info['X']**2
info['Z^2'] = info['Z']**2
print(info)

X = np.array(info[['X', 'X^2', 'Z', 'Z^2']])
number_of_lines = np.ones(X.shape[0])       #Кількість рядків таблиці
X = np.c_[X, number_of_lines]               #Перетворення двомірного масиву в одномірний

module = sm.OLS(info['Y'].to_numpy(), X)    #Найменші квадрати
R = module.fit()                            #Обгортка результатів регресії

Beta = R.params                             #Статистичні оцінки
Beta = np.append(Beta[-1], Beta[:-1])


print("Статистичні оценки: ")
for i, a in enumerate(Beta):
    print("Beta", i, "=", round(a, rounding))
print('='*50)


gama = 0.99
interval = R.conf_int(1 - gama)     #Обчислення довірчого інтервалу вибраних параметрів

#Вивід довірчого інтервалу
temp = ["x", "x^2", "z", "z^2"]
print(round(interval[-1][0], rounding), end='')
for i in range(4):
    print(' +', round(interval[i][0], rounding), '*',temp[i], end='')
print(" <= y <= ", end='')
print(round(interval[-1][1], rounding), end='')
for i in range(4):
    print(' +', round(interval[i][1], rounding), '*',temp[i], end='')
print('\n', '='*50)

#Коефіцієнт множинної кореляції
correlation = round(R.rsquared**.5, rounding)
print("Коефіцієнт множинної кореляції:", correlation)