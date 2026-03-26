import numpy as np
import matplotlib.pyplot as plt


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


def interp_membership(x, mf, val):
    idx = np.argmin(np.abs(x - val))
    return mf[idx]


x = np.arange(0, 101, 1)

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

air_val = float(input("Введите уровень загрязнения воздуха (0–100): "))
noise_val = float(input("Введите уровень шума (0–100): "))

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

mu_implication = min(1 - air_membership, noise_membership)

print(f"\nСтепень принадлежности воздуха: {air_membership:.2f}")
print(f"Степень принадлежности шума: {noise_membership:.2f}")
print(f"Импликация (A -> B): {mu_implication:.3f}")

plt.figure(figsize=(17, 8))

plt.plot(x, air_clean, label="Воздух: чисто")
plt.plot(x, air_moderate, label="Воздух: умеренное загрязнение")
plt.plot(x, air_polluted, label="Воздух: загрязнено")
plt.plot(x, air_heavily, label="Воздух: сильно загрязнено")

plt.plot(x, noise_quiet, "--", label="Шум: тихо")
plt.plot(x, noise_medium, "--", label="Шум: средне")
plt.plot(x, noise_loud, "--", label="Шум: шумно")
plt.plot(x, noise_very_loud, "--", label="Шум: очень шумно")

plt.title("Импликация между нечеткими множествами")
plt.xlabel("Уровень (0–100)")
plt.ylabel("Степень принадлежности")
plt.legend()
plt.grid()
plt.show()