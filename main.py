import random
import numpy as np

t = int(input("Введите количество знаков после запятой при вычислении неточности : "))

row = int(input("Введите размерность матрицы: "))
while (row < 1) or (row > 35):
    row = int(input("Неверно!\nВведите размерность матрицы:"))

x = np.random.randint(1, 10, (row, row))
rank = np.linalg.matrix_rank(x)

print(f"Матрица: \n{x}")
print(f"Ранг матрицы: {rank}")

n = 1
before_digit, result, accuracy = 0, 0, 1
fact_denominator, fact_numerator = 1, 1

while abs(accuracy) > (0.1**t):
    before_digit += result
    fact_numerator = (2 * n - 1) * (2 * n)
    fact_denominator *= (2 * n - 1) * (2 * n)
    result += np.linalg.det(x*fact_numerator) / fact_denominator
    n += 1
    accuracy = abs(before_digit - result)
    before_digit = 0

print(f"\nИтоговая сумма: {result}")
print(f"Кол-во итераций: {n-1}")

