# SII_Lab2
# Вариант 10
Предметная область - экология. Загрязнение воздуха и уровень шума. Импликация моделируется минимумом
# Подключение необходимых библиотек
```
import numpy as np
import matplotlib.pyplot as plt
```
# Трапецевидная функция принадлежности
```
def trapmf(x, a, b, c, d):
    result = np.zeros_like(x, dtype=float)

    for i, val in enumerate(x):
        if val < a:
            result[i] = 0
        elif a <= val < b:
            result[i] = (val - a) / (b - a) if b != a else 1
        elif b <= val <= c:
            result[i] = 1
        elif c < val <= d:
            result[i] = (d - val) / (d - c) if d != c else 0
        else:
            result[i] = 0
    return result
```
Функция рассчитывает степень принадлежности каждого значения от 0 до 1.
По сути описывает нечеткую логику с плавными границами между категориями
# Функция интерполяции
```
def interp_membership(x, mf, val):
    idx = np.argmin(np.abs(x - val))
    return mf[idx]
```
Возвращает степень принадлежности значения к нечеткому множеству.
По сути ищет в массиве индекс, который ближе всего находится к значению.
# Создание нечетких множеств
```
# Загрязнение воздуха
air_clean      = trapmf(x, 0, 0, 20, 40)
air_moderate   = trapmf(x, 30, 45, 55, 70)
air_polluted   = trapmf(x, 60, 75, 85, 95)
air_heavily    = trapmf(x, 85, 95, 100, 100)

# Шум
noise_quiet      = trapmf(x, 0, 0, 20, 40)
noise_medium     = trapmf(x, 30, 45, 55, 70)
noise_loud       = trapmf(x, 60, 75, 85, 95)
noise_very_loud  = trapmf(x, 85, 95, 100, 100)
```
Определяются границы чистоты воздуха и уровня шума.
Для каждого параметра четыре категории.
Каждое из множеств - трапецевидная функция.
# Вычисление степени принадлежности
```
air_membership = max(
    interp_membership(x, air_clean, air_val),
    interp_membership(x, air_moderate, air_val),
    interp_membership(x, air_polluted, air_val),
    interp_membership(x, air_heavily, air_val),
)

noise_membership = max(
    interp_membership(x, noise_quiet, noise_val),
    interp_membership(x, noise_medium, noise_val),
    interp_membership(x, noise_loud, noise_val),
    interp_membership(x, noise_very_loud, noise_val),
)
```
Для загрязнения воздуха и уровня шума находится максимальная степень принадлежности
из четырех категорий.
# Вычисление импликации
```
mu_implication = min(1 - air_membership, noise_membership)
```
Рассчет показывает на сколько выполняется условие - Если воздух чистый, то шум минимальный.
Далее строятся графики принадлежности для загрязнения воздуха и уровня шума
