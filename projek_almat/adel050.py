def perkalian_matriks(A, B):
    """
    Mengalikan dua matriks 3x3.
    """

    hasil = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for i in range(3):
        for j in range(3):
            for k in range(3):
                hasil[i][j] += A[i][k] * B[k][j]

    return hasil

def determinan(A):
    """
    Menghitung determinan matriks 3x3 menggunakan
    ekspansi kofaktor pada baris pertama.
    """

    m00 = A[1][1] * A[2][2] - A[1][2] * A[2][1]
    m01 = A[1][0] * A[2][2] - A[1][2] * A[2][0]
    m02 = A[1][0] * A[2][1] - A[1][1] * A[2][0]

    det = A[0][0] * m00 - A[0][1] * m01 + A[0][2] * m02

    return det
