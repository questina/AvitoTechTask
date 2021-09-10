import asyncio
from math import sqrt

import aiohttp
from typing import List, Tuple

SOURCE_URL = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'


def read_matrix(raw_matr: str) -> Tuple[List[int], int]:
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
    iter_num: int = 1
    cur_i: int = 0
    res_matr: List[int] = list()
    res_matr.append(matrix[cur_i])
    for i in range(matr_dim-iter_num):
        cur_i += matr_dim
        res_matr.append(matrix[cur_i])
    while iter_num != matr_dim:
        for i in range(matr_dim-iter_num):
            cur_i += 1 if iter_num%2 == 1 else -1
            res_matr.append(matrix[cur_i])
        for i in range(matr_dim-iter_num):
            cur_i -= matr_dim if iter_num%2 == 1 else -matr_dim
            res_matr.append(matrix[cur_i])
        iter_num += 1
    return res_matr


async def get_matrix(url: str) -> List[int]:
    async with aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(ssl=False)  # HTTP Connection
    ) as session:
        async with session.get(url=url) as response:
            data = await response.text()
            matr, matr_dim = read_matrix(data)
    return zig_zag_change(matr, matr_dim)


loop = asyncio.get_event_loop()
loop.run_until_complete(get_matrix(SOURCE_URL))
