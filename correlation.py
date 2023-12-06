import math

def pearson(array_1, array_2):

    if len(array_1) != len(array_2):
        raise ValueError("Массивы должны быть одинаковой длины")

    n = len(array_1)

    mean_x = sum(array_1) / n
    mean_y = sum(array_2) / n

    var_x = sum([(xi - mean_x) ** 2 for xi in array_1]) / float(len(array_1))
    var_y = sum([(yi - mean_y) ** 2 for yi in array_2]) / float(len(array_2))

    covariance = sum([(xi - mean_x) * (yi - mean_y) for xi, yi in zip(array_1, array_2)]) / float(len(array_1))
    corr = covariance / (math.sqrt(var_x * var_y))

    return corr


array_1 = [11, 21, 3, 1, 15, 24, 38, 7, 54, 9]
array_2 = [18, 5, 15, 9, 3, 56, 2, 5, 47, 88]

correlation = round(pearson(array_1, array_2), 3)
print(f"Корреляция Пирсона: {correlation}")add