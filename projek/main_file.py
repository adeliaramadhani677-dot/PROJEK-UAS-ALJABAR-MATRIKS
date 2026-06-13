import adel050

A = [
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0]
]

B = [
    [7, 8, 9],
    [1, 2, 3],
    [4, 5, 6]
]

hasil = adel050.perkalian_matriks(A, B)

print("Hasil Perkalian:")
for baris in hasil:
    print(baris)

print("\nDeterminan A =", adel050.determinan(A))
