# Напишите функцию для транспонирования матрицы


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def transpose_matrix(matrix):
    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed


transposed = transpose_matrix(matrix)
print(transposed)
