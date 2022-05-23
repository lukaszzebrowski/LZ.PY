import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# x = np.arange(1, 20.5, 0.5)
# y = 1/x
#
# plt.plot(x, y, 'b-')
# plt.show()

# x = np.arange(0, 10.1, 0.1)
# y = np.sin(x)
# z = np.cos(x)
# plt.plot(x, y, linestyle='dashed', marker='^', color='lightblue', linewidth=2, label='sin(x)')
# plt.plot(x, z, linestyle='dotted', marker='*', color='green', linewidth=2, label='cos(x)')
# plt.ylabel('Oś y')
# plt.xlabel('Oś x')
# plt.legend(loc='lower left')
# plt.show()


# x1 = np.arange(0, 2.02, 0.02)
# x2 = np.arange(0, 2.02, 0.02)
#
# y1 = np.sin(2*np.pi*x1)
# y2 = np.cos(2*np.pi*x2)
#
# plt.subplot(2, 1, 1)
# plt.plot(x1, y1, 'r--')
# plt.ylabel('sin(y)')
# plt.title('Wykres sin(x)')
#
# plt.subplot(2, 1, 2)
# plt.plot(x2, y2, 'go')
# plt.xlabel('x')
# plt.ylabel('cos(y)')
# plt.title('Wykres cos(x)')
# plt.subplots_adjust(hspace=0.5)
# plt.show()

# fig, axs = plt.subplots(3, 2)
#
# axs[0, 0].plot(x1, y1, 'r-')
# axs[0, 0].set_xlabel('x')
# axs[0, 0].set_ylabel('sin(x)')
# axs[0, 0].set_title('Wykres sin(x)')
#
# axs[1, 1].plot(x2, y2, 'g-')
# axs[1, 1].set_xlabel('x')
# axs[1, 1].set_ylabel('cos(x)')
# axs[1, 1].set_title('Wykres cos(x)')
#
# axs[2, 0].plot(x2, y2, 'b-')
# axs[2, 0].set_xlabel('x')
# axs[2, 0].set_ylabel('cos(x)')
# axs[2, 0].set_title('Wykres cos(x)')
# fig.delaxes(axs[0, 1])
# fig.delaxes(axs[1, 0])
# fig.delaxes(axs[2, 1])
# plt.show()

# dane = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
#
# dane['b'] = dane['a'] + 10*np.random.rand(50)
# dane['d'] = np.abs(dane['d'])*100
#
# plt.scatter(data=dane, x='a', y='b', c='c', s='d')
# plt.xlabel('Wartość a')
# plt.ylabel('Wartość b')
# plt.show()
# print(dane['c'])
#
# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
#         'Stolica': ['Bruksela', 'New Delphi', 'Brasilia'],
#         'Populacja': [11190846, 1303171035, 207847528],
#         'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa']}
#
# df = pd.DataFrame(data)
#
# grupa = df.groupby('Kontynent')
# etykiety = list(grupa.groups.keys())
# wartosc = list(grupa.agg('Populacja').sum())
#
# plt.bar(x=etykiety, height=wartosc, color=['red', 'green', 'blue'])
# plt.xlabel('Kontynenty')
# plt.ylabel('Populacja na kontynentach')
# plt.show()

x = np.random.randn(10000)
plt.hist(x, bins=15, facecolor='b', alpha=0.75, density=True, orientation=u'horizontal')
plt.xlabel('Wartości x')
plt.ylabel('Prawdopodobieństwa')
plt.show()