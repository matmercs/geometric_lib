def area(a, h):
    return a * h / 2


def perimeter(a, b, c):
    return a + b + c


def semi_perimeter(a, b, c):
    return perimeter(a, b, c) / 2


def heron_area(a, b, c):
    s = semi_perimeter(a, b, c)
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a


def circumscribed_circle_radius(a, b, c):
    return (a * b * c) / (4 * heron_area(a, b, c))


def inscribed_circle_radius(a, b, c):
    p = semi_perimeter(a, b, c)
    return heron_area(a, b, c) / p
