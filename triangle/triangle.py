def validar(sides):
    a, b, c =sorted(sides)
    return c <= a +b and a > 0

def equilateral(sides):
    a, b, c = sides
    return validar(sides) and a==b and a==c


def isosceles(sides):
    a, b, c = sides
    return validar(sides) and (a==b or a==c or b==c)


def scalene(sides):
    a, b, c = sides
    return validar(sides) and a!=b and a!=c and b!=c
