import asyncio

from main import get_matrix, zig_zag_change

SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'

TRAVERSAL = [
    10, 50, 90, 130,
    140, 150, 160, 120,
    80, 40, 30, 20,
    60, 100, 110, 70,
]


def test_get_matrix():
    assert asyncio.run(get_matrix(SOURCE_URL)) == TRAVERSAL


def test_zig_zag_algorithm_5():
    matr = [i * 10 for i in range(1, 26)]
    trav_matr = [10, 60, 110, 160, 210,
                 220, 230, 240, 250, 200,
                 150, 100, 50, 40, 30,
                 20, 70, 120, 170, 180,
                 190, 140, 90, 80, 130]
    assert zig_zag_change(matr, 5) == trav_matr


def test_zig_zag_algorithm_1():
    matr = [1]
    trav_matr = [1]
    assert zig_zag_change(matr, 0) == trav_matr


def test_zig_zag_algoritm_3():
    matr = [i * 10 for i in range(1, 10)]
    trav_matr = [10, 40, 70,
                 80, 90, 60,
                 30, 20, 50]
    assert zig_zag_change(matr, 3) == trav_matr


def test_zig_zag_algorithm_2():
    matr = [i * 10 for i in range(1, 5)]
    trav_matr = [10, 30,
                 40, 20]
    assert zig_zag_change(matr, 2) == trav_matr


def run_tests():
    test_get_matrix()
    test_zig_zag_algorithm_1()
    test_zig_zag_algorithm_2()
    test_zig_zag_algoritm_3()
    test_zig_zag_algorithm_5()
