import time
import numpy as np

matrix_a = [[1, 2, 3, 5], [4, 5, 6, 1], [7, 8, 9, 2], [3, 2, 1, 0]]
matrix_b = [[9, 8, 7, 4], [6, 5, 4, 0], [3, 2, 1, 1], [3, 3, 0, 1]]
matrix_c = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

start = int(round(time.time() * 1000))
count = 1

for i in range(0, len(matrix_a)):
        for j in range(0, len(matrix_b[0])):
            for k in range(0, len(matrix_b)):
                print("Matriks ke - %d" % count,matrix_c)
                matrix_c[i][j] += matrix_a[i][k] * matrix_b[k][j]
                count +=1
print("Time --->", (round(time.time() * 1000) - start))
#print(matrix_c)
print("HASIL PERKALIAN MATRIX A dan B")

print()
print("Matrix A :")
print(np.asmatrix(matrix_a))
print()
print("Matrix B :")
print(np.asmatrix(matrix_b))
print()
print("Maka didapatkan hasil perkalian Matrix 4x4 A dan B adalah : \n")
print(np.asmatrix(matrix_c))
