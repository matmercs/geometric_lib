def area(a, b):
    """
    Вычисляет площадь прямоугольника.

    Параметры:
    a (float): Длина прямоугольника.
    b (float): Ширина прямоугольника.

    Возвращает:
    float: Площадь прямоугольника.

    Пример:
    > area(5, 3)
    15
    """
    return a * b


def perimeter(a, b):
    """
    Вычисляет периметр прямоугольника.

    Параметры:
    a (float): Длина прямоугольника.
    b (float): Ширина прямоугольника.

    Возвращает:
    float: Периметр прямоугольника.

    Пример:
    > perimeter(5, 3)
    16
    """
    return 2 * (a + b)


def diagonal(a, b):
    """
    Вычисляет длину диагонали прямоугольника.

    Параметры:
    a (float): Длина прямоугольника.
    b (float): Ширина прямоугольника.

    Возвращает:
    float: Длина диагонали.

    Пример:
    > diagonal(5, 3)
    5.830951894845301
    """
    return (a ** 2 + b ** 2) ** 0.5


def is_square(a, b):
    """
    Проверяет, является ли прямоугольник квадратом.

    Параметры:
    a (float): Длина прямоугольника.
    b (float): Ширина прямоугольника.

    Возвращает:
    bool: True, если прямоугольник является квадратом, иначе False.

    Пример:
    > is_square(5, 5)
    True

    > is_square(5, 3)
    False
    """
    return a == b
