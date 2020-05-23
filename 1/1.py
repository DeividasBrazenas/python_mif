import numpy as np
from scipy.misc import derivative
import scipy.integrate as integrate
import sympy as sym

# 1. Padalinkite intervalą nuo -1.3 iki 2.5 tolygiai į 64 dalis.
interval = np.linspace(-1.3, 2.5, 64)

print(interval)

# 2. Sugeneruokite masyvą dydžio 3n ir užpildykite jį cikliniu šablonu [1, 2, 3].
n = 5;
array = np.tile(np.array([1, 2, 3]), 3 * n)

print(array)

# 3. Sukurkite masyvą iš pirmųjų 10 nelyginių sveikųjų skaičių.
array = np.arange(1, 21, 2)

print(array)

# 4. Sukurkite masyvą dydžio 10 x 10 iš nulių ir "įrėminkite" jį vienetais.
def pad_with(vector, iaxis_pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', 1)
    vector[:iaxis_pad_width[0]] = pad_value
    vector[-iaxis_pad_width[1]:] = pad_value
    return vector

matrix = np.pad(np.zeros((8, 8)), 1, pad_with)
print(matrix)

# 5. Sukurkite masyvą dydžio 8 x 8, kur 1 ir 0 išdėlioti šachmatine tvarka (panaudokite slicing+striding metodą).
matrix = np.zeros((8, 8))
matrix[::2, ::2] = 1
matrix[1::2, 1::2] = 1

print(matrix)

# 6. Sukurkite masyvą dydžio n×n , kurio (i,j)-oji pozicija lygi i+j
n = 3
sums = np.zeros((3, 3))
for idx, xval in enumerate(sums):
    for idy, yval in enumerate(xval):
        sums[idx, idy] = idx + idy

print(sums)

# 7. Sukurkite atsitiktinį masyvą dydžio 3×5 naudodami np.random.rand(3, 5) funkciją ir suskaičiuokite: sumą, eilučių sumą, stulpelių sumą.
matrix = np.random.rand(3, 5)

print(np.sum(matrix))
print(matrix.sum(axis=0))
print(matrix.sum(axis=1))

# 8. Sukurkite atsitiktinį masyvą dydžio 5×5 naudodami np.random.rand(5, 5). Surūšiuokite eilutes pagal antrąjį stulpelį. Tam pamėginkite apjungti masyvo slicing + argsort + indexing metodus.
matrix = np.random.rand(5, 5)
print(matrix)

matrix = sorted(matrix, key=lambda col: col[1])
print("########")
print(np.reshape(matrix, (5, 5)))

# 9. Atvirkštinę matricą
matrix = np.array([1, 2, 3, 4])
matrix = np.reshape(matrix, (2, 2))
matrix = np.linalg.inv(matrix)

print(matrix)

# 10. Apskaičiuokite matricos tikrines reikšmes ir tikrinį vektorių
x = np.linspace(0, 10)
dx = x[1] - x[0]
y = x ** 2 + 1
dydx = np.gradient(y, dx)

print(dydx)


# 11. Pasirinktos funkcijos išvestinę
def f(x):
    return x ** 4 + x ** 2

print(derivative(f, 1.0, dx=1e-6))

# 12. Pasirinktos funkcijos apibrėžtinį ir neapibrėžtinį integralus
func = lambda x: x ** 4
res = integrate.quad(func, 0, 4)

print(res)

x = sym.symbols('x')
x = sym.integrate(x ** 4)

print(x)
