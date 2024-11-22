import math


def area(r):
    """
    Вычисляет площадь круга по заданному радиусу.

    Параметры:
    r (float): Радиус круга.

    Возвращает:
    float: Площадь круга.

    Пример:
    > area(5)
    78.53981633974483
    """
    return math.pi * r * r


def perimeter(r):
    """
    Вычисляет длину окружности по заданному радиусу.

    Параметры:
    r (float): Радиус окружности.

    Возвращает:
    float: Длина окружности.

    Пример:
    > perimeter(5)
    31.41592653589793
    """
    return 2 * math.pi * r


def arc_length(r, angle):
    """
    Вычисляет длину дуги окружности.

    Параметры:
    r (float): Радиус окружности.
    angle (float): Угол дуги в градусах.

    Возвращает:
    float: Длина дуги.

    Пример:
    > arc_length(5, 90)
    7.853981633974483
    """
    return (angle / 360) * perimeter(r)


def sector_area(r, angle):
    """
    Вычисляет площадь сектора окружности.

    Параметры:
    r (float): Радиус окружности.
    angle (float): Угол сектора в градусах.

    Возвращает:
    float: Площадь сектора.

    Пример:
    > sector_area(5, 90)
    19.634954084936208
    """
    return (angle / 360) * area(r)


def segment_area(r, angle):
    """
    Вычисляет площадь сегмента окружности.

    Параметры:
    r (float): Радиус окружности.
    angle (float): Угол сегмента в градусах.

    Возвращает:
    float: Площадь сегмента.

    Пример:
    > segment_area(5, 90)
    7.134954084936207
    """
    angle_rad = math.radians(angle)
    return (r * r / 2) * (angle_rad - math.sin(angle_rad))
