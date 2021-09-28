""""
 Author: Chris Warren
 Interview Question

 testing file for cartesian_coords_to_line
"""

import pytest
from cartesian_coords_to_line import coords_to_line


def test_1():
    """
     basic test with known int values
    """
    a, b, c = coords_to_line(1, 1, 2, 2)
    assert a == -1 and b == 1 and c == 0


def test_2():
    """
     basic test with known float values
    """
    a, b, c = coords_to_line(1.0, 1.0, 2.0, 2.0)
    assert a == -1 and b == 1 and c == 0


def test_3():
    """
     basic test with large values
    """
    a, b, c = coords_to_line(999999, 999998, 999997, 999996)
    assert a == -1 and b == 1 and c == -1


def test_4():
    """
     making sure the function simplifies
    """
    a, b, c = coords_to_line(1, 3, -1, 5)
    assert a == 1 and b == 1 and c == 4


def test_5():
    """
     generating values in a range and making sure all values work in the equation
     ignoring cases when both points are the same
    """
    for x1 in range(-10, 10):
        for y1 in range(-10, 10):
            for x2 in range(-10, 10):
                for y2 in range(-10, 10):
                    if x1 != x2 and y1 != y2:
                        a, b, c = coords_to_line(x1, y1, x2, y2)
                        assert (a * x1 + b * y1 == c) and (a * x2 + b * y2 == c)


def test_6():
    """
     calling function with wrong number of inputs
    """
    with pytest.raises(Exception):
        assert coords_to_line(1, 2, 3)
        assert coords_to_line(1, 2, 3, 4, 5)
        assert coords_to_line()


def test_7():
    """
     calling function with wrong data type
    """
    with pytest.raises(Exception):
        assert coords_to_line("test1", "test2", "test3", "test4")
        assert coords_to_line(True, True, True, True)


def test_8():
    """
     calling function with two of the same points
    """
    with pytest.raises(Exception):
        assert coords_to_line(1, 1, 1, 1)


def test_9():
    """
     calling function with leftmost point as p2
    """
    a, b, c = coords_to_line(6, 4, -1, -7)
    assert a == -11 and b == 7 and c == -38


def test_10():
    """
     vertical line
    """
    a, b, c = coords_to_line(0, 1, 0, 0)
    assert a == 1 and b == 0 and c == 0
    a, b, c = coords_to_line(0, 0, 0, 1)
    assert a == 1 and b == 0 and c == 0


def test_11():
    """
     horizontal line
    """
    a, b, c = coords_to_line(1, 1, 6, 1)
    assert a == 0 and b == 1 and c == 1
    a, b, c = coords_to_line(6, 1, 1, 1)
    assert a == 0 and b == 1 and c == 1

def test_12():
    """
     zeros test
    """
    a, b, c = coords_to_line(0, 0, 5, 6)
    assert a == -6 and b == 5 and c == 0
    a, b, c = coords_to_line(5, 6, 0, 0)
    assert a == -6 and b == 5 and c == 0
