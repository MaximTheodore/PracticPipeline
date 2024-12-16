import numpy as np
import matplotlib.pyplot as plt

# Определим функцию для построения линий
x1 = np.linspace(0, 1000, 500)  # Значения x1

# Ограничения
y1 = (2000 - 2 * x1) / 4
y2 = 1400 - 4 * x1
y3 = 800 - 2 * x1

# Устанавливаем неотрицательные области для y
y1 = np.where(y1 >= 0, y1, np.nan)
y2 = np.where(y2 >= 0, y2, np.nan)
y3 = np.where(y3 >= 0, y3, np.nan)

# Создаем график
plt.figure(figsize=(10, 8))
plt.plot(x1, y1, label=r'$2x_1 + 4x_2 \geq 2000$', color='blue')
plt.plot(x1, y2, label=r'$4x_1 + x_2 \geq 1400$', color='green')
plt.plot(x1, y3, label=r'$2x_1 + x_2 \geq 800$', color='red')

# Заштриховываем область допустимых решений
plt.fill_between(x1, 0, np.minimum(np.minimum(y1, y2), y3), where=(np.minimum(np.minimum(y1, y2), y3) >= 0),
                 color='yellow', alpha=0.3, label='Область допустимых решений')

# Настройки графика
plt.xlim(0, 1000)
plt.ylim(0, 1000)
plt.xlabel(r'$x_1$', fontsize=14)
plt.ylabel(r'$x_2$', fontsize=14)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend(fontsize=12)
plt.title('Область допустимых решений', fontsize=16)
plt.show()
