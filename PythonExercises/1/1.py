import numpy as np
import sympy as sp


# 1. Padalinkite intervalą nuo -1.3 iki 2.5 tolygiai į 64 dalis.
def n1_interval():
    return np.linspace(-1.3, 2.5, 64)


print(n1_interval())


# 2. Sugeneruokite masyvą dydžio 3n ir užpildykite jį cikliniu šablonu [1, 2, 3].
def n2_array(n):
    return np.tile([1, 2, 3], 3 * n)


print(n2_array(5))


# 3. Sukurkite masyvą iš pirmųjų 10 nelyginių sveikųjų skaičių.
def n3_numbers():
    return np.fromfunction(lambda n: (n * 2) + 1, (10,), dtype=int)


print(n3_numbers())


# 4. Sukurkite masyvą dydžio 10 x 10 iš nulių ir "įrėminkite" jį vienetais.
def n4_padded_array():
    arr = np.zeros((10, 10), dtype=int)
    arr = np.pad(arr, 1, mode="constant", constant_values=(1,))
    return arr


print(n4_padded_array())


# 5. Sukurkite masyvą dydžio 8 x 8, kur 1 ir 0 išdėlioti šachmatine tvarka (panaudokite slicing+striding metodą).
def n5_chess_matrix():
    matrix = np.zeros((8, 8))
    matrix[::2, ::2] = 1
    matrix[1::2, 1::2] = 1
    return matrix;


print(n5_chess_matrix())


# 6. Sukurkite masyvą dydžio n×n , kurio (i,j)-oji pozicija lygi i+j
def n6_matrix_sum(n):
    matrix = np.zeros((3, 3))
    for idx, xval in enumerate(matrix):
        for idy, yval in enumerate(xval):
            matrix[idx, idy] = idx + idy


print(n6_matrix_sum(3))


# 7. Sukurkite atsitiktinį masyvą dydžio 3×5 naudodami np.random.rand(3, 5) funkciją ir suskaičiuokite: sumą, eilučių sumą, stulpelių sumą.
def n7_random():
    matrix = np.random.rand(3, 5)
    return {"sum": np.sum(matrix), "row sum": matrix.sum(axis=1), "col sum": matrix.sum(axis=0)}


print(n7_random())


# 8. Sukurkite atsitiktinį masyvą dydžio 5×5 naudodami np.random.rand(5, 5). Surūšiuokite eilutes pagal antrąjį stulpelį. Tam pamėginkite apjungti masyvo slicing + argsort + indexing metodus.
def n8_matrix_sorted():
    matrix = np.random.rand(5, 5)
    indices = np.argsort(matrix[:, 1])
    return matrix, matrix[indices]


print(n8_matrix_sorted())


# 9. Atvirkštinę matricą
def n9_inverted_matrix():
    matrix = np.array([[1, 2, 3], [-3, -2, -1], [4, 2, 3]])
    return np.linalg.inv(matrix)


print(n9_inverted_matrix())


# 10. Apskaičiuokite matricos tikrines reikšmes ir tikrinį vektorių
def n10_matrix_eigenvector():
    matrix = np.array([[1, 2, 3], [-3, -2, -1], [4, 2, 3]])
    return np.linalg.eig(matrix)


print(n10_matrix_eigenvector())


# 11. Pasirinktos funkcijos išvestinę
def n11_diff():
    x = sp.Symbol('x')
    y = x ** 4 + x ** 2
    return y.diff(x)


print(n11_diff())


# 12. Pasirinktos funkcijos apibrėžtinį ir neapibrėžtinį integralus
def n12_integral():
    x = sp.Symbol('x')
    a = sp.Symbol('y')
    b = sp.Symbol('z')
    y = 6 * x + 42
    return sp.integrate(y, (x,)), sp.integrate(y, (x, a, b))
