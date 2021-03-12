import threading
import time
import numpy as np

matrix_a = [[1, 2, 3, 4], [4, 5, 6, 3], [7, 8, 9, 6], [5, 3, 5, 8]]
matrix_b = [[9, 8, 7, 6], [6, 5, 4, 5], [3, 2, 1, 0], [1, 0, 2, 3]]
matrix_c = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


class Thread1(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        print ("Starting " + self.name + "\n")

        vector_3x1a = [matrix_a[0][0], matrix_a[1][0], matrix_a[2][0], matrix_a[3][0]]
        vector_1x3b = [matrix_b[0][0], matrix_b[0][1], matrix_b[0][2], matrix_b[0][3]]

        matrix_c[0][0] += vector_3x1a[0] * vector_1x3b[0]
        matrix_c[0][1] += vector_3x1a[0] * vector_1x3b[1]
        matrix_c[0][2] += vector_3x1a[0] * vector_1x3b[2]
        matrix_c[0][3] += vector_3x1a[0] * vector_1x3b[3]

        matrix_c[1][0] += vector_3x1a[1] * vector_1x3b[0]
        matrix_c[1][1] += vector_3x1a[1] * vector_1x3b[1]
        matrix_c[1][2] += vector_3x1a[1] * vector_1x3b[2]
        matrix_c[1][3] += vector_3x1a[1] * vector_1x3b[3]

        matrix_c[2][0] += vector_3x1a[2] * vector_1x3b[0]
        matrix_c[2][1] += vector_3x1a[2] * vector_1x3b[1]
        matrix_c[2][2] += vector_3x1a[2] * vector_1x3b[2]
        matrix_c[2][3] += vector_3x1a[2] * vector_1x3b[3]

        matrix_c[3][0] += vector_3x1a[3] * vector_1x3b[0]
        matrix_c[3][1] += vector_3x1a[3] * vector_1x3b[1]
        matrix_c[3][2] += vector_3x1a[3] * vector_1x3b[2]
        matrix_c[3][3] += vector_3x1a[3] * vector_1x3b[3]

        
        print (np.asmatrix(matrix_c))
        print ("End " + self.name + "\n")

class Thread2(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        print ("Starting " + self.name + "\n")

        vector_3x1a = [matrix_a[0][1], matrix_a[1][1], matrix_a[2][1], matrix_a[3][1]]
        vector_1x3b = [matrix_b[1][0], matrix_b[1][1], matrix_b[1][2], matrix_b[1][3]]

        matrix_c[0][0] += vector_3x1a[0] * vector_1x3b[0]
        matrix_c[0][1] += vector_3x1a[0] * vector_1x3b[1]
        matrix_c[0][2] += vector_3x1a[0] * vector_1x3b[2]
        matrix_c[0][3] += vector_3x1a[0] * vector_1x3b[3]

        matrix_c[1][0] += vector_3x1a[1] * vector_1x3b[0]
        matrix_c[1][1] += vector_3x1a[1] * vector_1x3b[1]
        matrix_c[1][2] += vector_3x1a[1] * vector_1x3b[2]
        matrix_c[1][3] += vector_3x1a[1] * vector_1x3b[3]

        matrix_c[2][0] += vector_3x1a[2] * vector_1x3b[0]
        matrix_c[2][1] += vector_3x1a[2] * vector_1x3b[1]
        matrix_c[2][2] += vector_3x1a[2] * vector_1x3b[2]
        matrix_c[2][3] += vector_3x1a[2] * vector_1x3b[3]

        matrix_c[3][0] += vector_3x1a[3] * vector_1x3b[0]
        matrix_c[3][1] += vector_3x1a[3] * vector_1x3b[1]
        matrix_c[3][2] += vector_3x1a[3] * vector_1x3b[2]
        matrix_c[3][3] += vector_3x1a[3] * vector_1x3b[3]

        
        print (np.asmatrix(matrix_c))
        print ("End " + self.name + "\n")


class Thread3(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        print ("Starting " + self.name + "\n")

        vector_3x1a = [matrix_a[0][2], matrix_a[1][2], matrix_a[2][2], matrix_a[3][2]]
        vector_1x3b = [matrix_b[2][0], matrix_b[2][1], matrix_b[2][2], matrix_b[2][3]]

        matrix_c[0][0] += vector_3x1a[0] * vector_1x3b[0]
        matrix_c[0][1] += vector_3x1a[0] * vector_1x3b[1]
        matrix_c[0][2] += vector_3x1a[0] * vector_1x3b[2]
        matrix_c[0][3] += vector_3x1a[0] * vector_1x3b[3]

        matrix_c[1][0] += vector_3x1a[1] * vector_1x3b[0]
        matrix_c[1][1] += vector_3x1a[1] * vector_1x3b[1]
        matrix_c[1][2] += vector_3x1a[1] * vector_1x3b[2]
        matrix_c[1][3] += vector_3x1a[1] * vector_1x3b[3]

        matrix_c[2][0] += vector_3x1a[2] * vector_1x3b[0]
        matrix_c[2][1] += vector_3x1a[2] * vector_1x3b[1]
        matrix_c[2][2] += vector_3x1a[2] * vector_1x3b[2]
        matrix_c[2][3] += vector_3x1a[2] * vector_1x3b[3]

        matrix_c[3][0] += vector_3x1a[3] * vector_1x3b[0]
        matrix_c[3][1] += vector_3x1a[3] * vector_1x3b[1]
        matrix_c[3][2] += vector_3x1a[3] * vector_1x3b[2]
        matrix_c[3][3] += vector_3x1a[3] * vector_1x3b[3]

        print (np.asmatrix(matrix_c))
        print ("End " + self.name + "\n")

class Thread4(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name

    def run(self):
        print ("Starting " + self.name + "\n")

        vector_3x1a = [matrix_a[0][3], matrix_a[1][3], matrix_a[2][3], matrix_a[3][3]]
        vector_1x3b = [matrix_b[3][0], matrix_b[3][1], matrix_b[3][2], matrix_b[3][3]]

        matrix_c[0][0] += vector_3x1a[0] * vector_1x3b[0]
        matrix_c[0][1] += vector_3x1a[0] * vector_1x3b[1]
        matrix_c[0][2] += vector_3x1a[0] * vector_1x3b[2]
        matrix_c[0][3] += vector_3x1a[0] * vector_1x3b[3]

        matrix_c[1][0] += vector_3x1a[1] * vector_1x3b[0]
        matrix_c[1][1] += vector_3x1a[1] * vector_1x3b[1]
        matrix_c[1][2] += vector_3x1a[1] * vector_1x3b[2]
        matrix_c[1][3] += vector_3x1a[1] * vector_1x3b[3]

        matrix_c[2][0] += vector_3x1a[2] * vector_1x3b[0]
        matrix_c[2][1] += vector_3x1a[2] * vector_1x3b[1]
        matrix_c[2][2] += vector_3x1a[2] * vector_1x3b[2]
        matrix_c[2][3] += vector_3x1a[2] * vector_1x3b[3]

        matrix_c[3][0] += vector_3x1a[3] * vector_1x3b[0]
        matrix_c[3][1] += vector_3x1a[3] * vector_1x3b[1]
        matrix_c[3][2] += vector_3x1a[3] * vector_1x3b[2]
        matrix_c[3][3] += vector_3x1a[3] * vector_1x3b[3]

        print (np.asmatrix(matrix_c))
        print ("End " + self.name + "\n")

start = int(round(time.time() * 1000))

thread1 = Thread1(1, "Thread 1")
thread2 = Thread2(2, "Thread 2")
thread3 = Thread3(3, "Thread 3")
thread4 = Thread4(4, "Thread 4")

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

print("Execution Time --->", (round(time.time() * 1000) - start))
print("Hasil Akhir dari Nilai perkalian matrixnya adalah : \n")
print(np.asmatrix(matrix_c))
