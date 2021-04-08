import matplotlib.pyplot as plt  # Подключение библиотек
import numpy as np

with open('readings.txt', 'r', encoding='utf-8') as file:  # Открываем файл на чтение и присваиваем в переменную file
    split_data = file.readline().split(', ')  # Читаем первую строчку файла и разбиваем на список по запятым
    reading_data = list(map(int, split_data))  # Преобразоваем считанные данные к числовому формату

data = np.array(reading_data)  # Для ускорения работы программы, преобразовываем данные в массив numpy
minSize = [min(data), list(data).index(min(data))]  # Минимальное значение и его позиция
maxSize = [max(data), list(data).index(max(data))]  # Максимальное значение и его позиция

fig, axis = plt.subplots(figsize=(13, 8))  # Инициализация графика и оси
fig.suptitle('Показания датчика')  # Заголовок

axis.plot(data, 'g')  # Построение графика зеленого (g) цвета по данным из файла
axis.plot(minSize[1], minSize[0], 'ro', markersize=13)  # Нахождение минимума
axis.plot(maxSize[1], maxSize[0], 'bo', markersize=13)  # Аналогично нахождение максимума
axis.text(minSize[1] + 0.25, minSize[0], 'Локальный минимум')  # Текст по позиции минимума с небольшим отступом
axis.text(maxSize[1] + 0.25, maxSize[0], 'Локальный максимум')

fig.show()  # Отображение графика
