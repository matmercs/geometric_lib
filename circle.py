import math


def area(r):
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r


def arc_length(r, angle):
    return (angle / 360) * perimeter(r)


def sector_area(r, angle):
    return (angle / 360) * area(r)


def segment_area(r, angle):
    angle_rad = math.radians(angle)
    return (r * r / 2) * (angle_rad - math.sin(angle_rad))
