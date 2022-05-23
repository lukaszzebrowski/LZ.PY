import numpy as np

print("Bryła platońska - ośmiościan")

macierz_incydencji = np.array([[1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
                    [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
                    [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                    [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
                    [0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0]])


macierz_incydencji_transponowana = macierz_incydencji.transpose()
print(f"I(G)T - transponowana\n {macierz_incydencji_transponowana}")

print()


print(f"I(G)*I(G)T\n {macierz_incydencji.dot(macierz_incydencji_transponowana)}")
print()

macierz_sasiedztwa = np.array([[0, 1, 1, 1, 0, 1],
                               [1, 0, 1, 1, 1, 0],
                               [1, 1, 0, 0, 1, 1],
                               [1, 1, 0, 0, 1, 1],
                               [0, 1, 1, 1, 0, 1],
                               [1, 0, 1, 1, 1, 0]])

macierz_sasiedztwa_diag = np.eye(6, dtype='int') * 4

print(f"D(G)\n {macierz_sasiedztwa+macierz_sasiedztwa_diag}")
print()

print(f"I(G)*I(G)T = D(G)+A(G)\n {macierz_incydencji.dot(macierz_incydencji_transponowana)==(macierz_sasiedztwa+macierz_sasiedztwa_diag)}")


