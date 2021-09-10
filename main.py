import aiohttp
from typing import List, Tuple


def read_matrix(raw_matr: str) -> Tuple[List[int], int]:
    """
    Функция возвращает массив из целых неотрицательных чисел, полученный из входной строки.

    Совместно с матрицей, эта функция находит одно из измерений матрицы. Последнее значение можно было найти
    с помощью функции sqrt из библиотеки math, но в задании не было указана возможность использования
    дополнительных библиотек, поэтому автор решила обойтись без нее.
    """
    matr: List[int] = list()
    matr_dim: int = 0

    raw_matr = raw_matr.replace('+', '').replace('-', '').replace(' ', '')
    for row in raw_matr.split('\n'):
        if row == '':
            continue
        matr += [int(str_num) for str_num in row.split('|')[1:-1]]
        matr_dim += 1
    return matr, matr_dim


def zig_zag_change(matrix: List[int], matr_dim: int) -> List[int]:
    """
    Функция возвращает список, содержащий результат обхода матрицы по спирали:
    против часовой стрелки, начиная с левого верхнего угла.
    """
    if matr_dim < 2:
        return matrix

    iter_num: int = 1  # номер начальной итерации. За итерацию считается сдвиг влево или вправо + сдвиг вниз или вверх
    cur_i: int = 0  # индекс текущего элемента
    res_matr: List[int] = list()

    # Спускаемся вниз до последней строки
    res_matr.append(matrix[cur_i])
    for i in range(matr_dim - iter_num):
        cur_i += matr_dim
        res_matr.append(matrix[cur_i])

    # Основной цикл
    while iter_num != matr_dim:
        for i in range(matr_dim - iter_num):
            cur_i += 1 if iter_num % 2 == 1 else -1
            res_matr.append(matrix[cur_i])
        for i in range(matr_dim - iter_num):
            cur_i -= matr_dim if iter_num % 2 == 1 else -matr_dim
            res_matr.append(matrix[cur_i])
        iter_num += 1

    return res_matr


async def get_matrix(url: str) -> List[int]:
    async with aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(ssl=False)
    ) as session:
        async with session.get(url=url) as response:
            data = await response.text()
            matr, matr_dim = read_matrix(data)
    return zig_zag_change(matr, matr_dim)
