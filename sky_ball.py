import numpy as np
import matplotlib.pyplot as plt

# Данные задачи
r = 0.033  # Радиус мяча, м
m = 0.15  # Масса мяча, кг
v0 = 20  # Начальная скорость, м/с
g = 9.81  # Ускорение свободного падения, м/с^2
rho = 1.225  # Плотность воздуха, кг/м^3
Cd = 0.47  # Коэффициент сопротивления
A = np.pi * r ** 2  # Площадь поперечного сечения мяча, м^2

t_max = 2 * v0 / g
dt = 0.1


# Функция для моделирования без учета сопротивления воздуха
def flight_without_resistance(v0, g, dt):
    t_values = [0]
    h_values = [0]
    v_values = [v0]

    v = v0
    h = 0
    t = 0
    while h >= 0:
        v -= g * dt
        h += v * dt
        t += dt
        t_values.append(t)
        h_values.append(h)
        v_values.append(v)

    return np.array(t_values), np.array(h_values), np.array(v_values)


def flight_with_resistance(v0, g, rho, Cd, A, m, dt):
    t_values = [0]
    h_values = [0]
    v_values = [v0]
    a_values = [-g]
    F_resistance_values = []

    v = v0
    h = 0
    t = 0
    while h >= 0:
        F_resistance = 0.5 * Cd * rho * A * v ** 2
        a = -g - (F_resistance / m)

        v += a * dt
        h += v * dt
        t += dt

        t_values.append(t)
        h_values.append(h)
        v_values.append(v)
        a_values.append(a)
        F_resistance_values.append(F_resistance)

    # Добавляем последнее значение силы сопротивления, чтобы массивы были одинаковой длины
    F_resistance_values.append(F_resistance_values[-1])

    return np.array(t_values), np.array(h_values), np.array(v_values), np.array(a_values), np.array(F_resistance_values)


# Моделирование без сопротивления
t_values_no_res, h_values_no_res, v_values_no_res = flight_without_resistance(v0, g, dt)

# Моделирование с сопротивлением
t_values_res, h_values_res, v_values_res, a_values_res, F_resistance_values = flight_with_resistance(v0, g, rho, Cd, A,
                                                                                                     m, dt)

# Построение графиков

# График траектории (высота по времени)
plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.plot(t_values_no_res, h_values_no_res, label="Без сопротивления", color='blue')
plt.plot(t_values_res, h_values_res, label="С сопротивлением", color='red')
plt.xlabel("Время (с)")
plt.ylabel("Высота (м)")
plt.title("Траектория движения мяча")
plt.legend()

# График скорости (время)
plt.subplot(2, 2, 2)
plt.plot(t_values_no_res, v_values_no_res, label="Без сопротивления", color='blue')
plt.plot(t_values_res, v_values_res, label="С сопротивлением", color='red')
plt.xlabel("Время (с)")
plt.ylabel("Скорость (м/с)")
plt.title("Скорость мяча по времени")
plt.legend()

# График ускорения (время)
plt.subplot(2, 2, 3)
plt.plot(t_values_res, a_values_res, label="С сопротивлением", color='red')
plt.axhline(-g, color='blue', linestyle='--', label="Без сопротивления")
plt.xlabel("Время (с)")
plt.ylabel("Ускорение (м/с²)")
plt.title("Ускорение мяча по времени")
plt.legend()

# График силы сопротивления (время)
plt.subplot(2, 2, 4)
plt.plot(t_values_res, F_resistance_values, label="Сила сопротивления", color='green')
plt.xlabel("Время (с)")
plt.ylabel("Сила сопротивления (Н)")
plt.title("Сила сопротивления воздуха по времени")
plt.legend()

# Показываем графики
plt.tight_layout()
plt.show()

# Сравнение результатов
print("Без сопротивления воздуха:")
print(f"Время полета: {t_values_no_res[-1]:.2f} секунд")
print(f"Максимальная высота: {h_values_no_res.max():.2f} м")
print(f"Скорость при приземлении: {v_values_no_res[-1]:.2f} м/с")

print("\nС сопротивлением воздуха:")
print(f"Время полета: {t_values_res[-1]:.2f} секунд")
print(f"Максимальная высота: {h_values_res.max():.2f} м")
print(f"Скорость при приземлении: {v_values_res[-1]:.2f} м/с")
