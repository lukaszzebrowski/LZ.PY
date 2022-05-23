import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro:')
# plt.ylabel('Liczby z wektora')
#
#
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'r:')
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'bo')
# plt.show()
# plt.axis([0, 6, 0, 20])
# plt.show()

x = np.arange(0, 5.2, 0.2)

# plt.plot(x, x, 'r-', x, x**2, 'b^', x, x**3, 'gs')
# plt.legend(labels=['Liniowa', 'Kwadratowa', 'Sześcienna'], loc='center left')
plt.plot(x, x, label='Liniowa')
plt.plot(x, x**2, label='Kwadratowa')
plt.plot(x, x**3, label='Sześcienna')
plt.legend()
# plt.savefig('plot.png')
plt.show()

image1 = Image.open('plot.png')
image1 = image1.convert('RGB')
image1.save('plot.jpg')