import matplotlib.pyplot as plt
import numpy as np
# import random

with open('readings.txt', 'r', encoding='utf-8') as file:
    split_data = file.readline().split(', ')
    reading_data = list(map(int, split_data))

data = np.array(reading_data)
minSize = [min(data), list(data).index(min(data))]
maxSize = [max(data), list(data).index(max(data))]

fig, axis = plt.subplots(figsize=(13, 8))
fig.suptitle('Показания датчика')

axis.plot(data, 'g')
axis.plot(minSize[1], minSize[0], 'ro', markersize=13)
axis.plot(maxSize[1], maxSize[0], 'bo', markersize=13)
axis.text(minSize[1] + 0.25, minSize[0], 'Локальный минимум')
axis.text(maxSize[1] + 0.25, maxSize[0], 'Локальный максимум')

fig.show()