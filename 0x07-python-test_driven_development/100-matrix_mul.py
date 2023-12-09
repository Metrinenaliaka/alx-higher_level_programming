#!/usr/bin/python3


def matrix_mul(m_a, m_b):
    """
    multiplies two matrices
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    else:
        for row in m_a:
            if not isinstance(row, list):
                raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    else:
        for row in m_b:
            if not isinstance(row, list):
                raise TypeError("m_b must be a list of lists")
    if m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for el in row:
            if not isinstance(el, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for el in row:
            if not isinstance(el, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    len_m_a = len(m_a[0])
    len_m_b = len(m_b[0])
    for row in m_a:
        if len(row) != len_m_a:
            raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        if len(row) != len_m_b:
            raise TypeError("each row of m_b must be of the same size")
    column_ma = len(m_a[0])
    row_mb = len(m_b)
    if column_ma != row_mb:
        raise ValueError("m_a and m_b can't be multiplied")
    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for i in range(len(m_a)):  # finds number or rows in m_a
        for j in range(len(m_b[0])):  # finds number of cols in m_b
            for k in range(len(m_b)):  # finds number of rows in m_b
                result[i][j] += m_a[i][k] * m_b[k][j]
    return result
