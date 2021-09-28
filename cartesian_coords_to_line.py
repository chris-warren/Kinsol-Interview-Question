""""
 Author: Chris Warren
 Interview Question

 This program converts two points into a line in standard form
"""


def coords_to_line(x1, y1, x2, y2):
    """
     Input: 4 numbers describing two points (x1, y1) (x2, y2)
     Output: 3 integers a, b, c describing the line ax + by = c
    """
    try:
        # making sure that the two points are not the same
        if x1 == x2 and y1 == y2:
            raise ValueError
        # making sure that the leftmost point is x1 / y1
        x1, y1, x2, y2 = points_in_order(x1, y1, x2, y2)
        # calculate a b c values
        a = y1 - y2
        b = x2 - x1
        c = ((x1 - x2) * y1 + (y2 - y1) * x1)*-1
        # simplify the expression
        greatest_divisor = gcd(a, b, c)
        if greatest_divisor > 1:
            a = a / greatest_divisor
            b = b / greatest_divisor
            c = c / greatest_divisor
        return int(a), int(b), int(c)
    except ValueError:
        print("point 1 is the same as point 2")


def gcd(a, b, c):
    """
     calculates the greatest common divisor of 3 values
    """
    def gcd_helper(x, y):
        while y:
            x, y = y, x % y
        return x
    gcd1 = gcd_helper(a, b)
    gcd2 = gcd_helper(c, gcd1)
    return gcd2


def points_in_order(x1, y1, x2, y2):
    """
     takes two points as input and ensures that p1 is the leftmost point
     or if x1 and x2 are the same ensures the upper point is p1
    """
    if x1 > x2:
        return x2, y2, x1, y1
    if x1 == x2 and y1 < y2:
        return x2, y2, x1, y1
    return x1, y1, x2, y2
