def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """

    tl_to_br = 0
    bl_to_tr = 0
    
    for idx in range(len(matrix)):
        tl_to_br += matrix[idx][idx]
        bl_to_tr += matrix[-idx][idx-1]
        print(tl_to_br,bl_to_tr)
    
    return tl_to_br + bl_to_tr