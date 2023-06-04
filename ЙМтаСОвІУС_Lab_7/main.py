import statsmodels.api as sm
import numpy as np
import pandas as pd

rounding = 5

data = {
'Y': [2.0222, 2.1899, 2.3056, 2.4253, 2.5648, 2.7515, 2.8121, 3.0125, 3.0951, 3.2202, 3.2688, 3.3606, 2.3760, 3.4423, 3.3735],
'X': [3.21, 3.39, 3.45, 3.52, 3.62, 3.79, 3.81, 3.97, 4.01, 4.12, 4.18, 4.32, 4.38, 4.45, 4.52],
'Z': [2.09, 2.13, 2.18, 2.22, 2.26, 2.31, 2.33, 2.39, 2.42, 2.39, 2.35, 2.15, 2.17, 2.08, 2.03],
't': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
}

info = pd.DataFrame(data, index=range(1, 16))
info['ln Y'] = np.log(info['Y'])
info['ln X'] = np.log(info['X'])
info['ln Z'] = np.log(info['Z'])
print(info)

X = np.array(info[['ln X', 'ln Z', 't']])
number_of_lines = np.ones(X.shape[0])       #Кількість рядків таблиці
X = np.c_[X, number_of_lines]               #Перетворення двомірного масиву в одномірний

module = sm.OLS(info['ln Y'].to_numpy(), X) #Найменші квадрати
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

correlation = round(R.rsquared**.5, rounding)
print("Коефіцієнт множинної кореляції:", correlation)