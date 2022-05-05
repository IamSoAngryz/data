"""
NumPy (Numeric Python)
    = o librarie pentru calcul numeric si stintific in limbajul Python
    - permite stocarea de date numerice intr-un mod eficient si performant
    cu ajutorul unui tip de date specific - clasa ndarray
ndarray = n-dimensional array - un tablou omogen, multidimensional
        - elementele sunt de acelasi tip (omogen)
        - dimensiuena este fixata (spre deosebire de list)
NumPy   - ofera functii de prelucrare a tablourilor multidimensionale
            - functii de baza
            - functii statistice
            - functii matematice
Instalare:
    - modulul numpy se instaleaza cu pip
    pip instal numpy
    sau
    pup3 install numpy
Link: https://numpy.org/
"""
import numpy as np

a = np.array([4, 6, 7])     # tablou unidimensional
print(a)
b = np.arange(7)        # similar functiei range doar ca returneaza un tablou
print(b)
b2 = np.arange(6, 18, 3)
print(b2)
print(f'Tipul este: {type(a)}')
# tavlou 2-dimensional (matrice 2x3)
c = np.array(([5, 8, 21], [33, 10001, 5]))
print(c)
print(f'Dimensiune tablou c: {c.ndim}')
print(f'Marime tablou c: {c.size}')
print(f'Numar linii si coloane tablou c: {c.shape}')
d = c.reshape(3, 2)
print('Dupa redimensionare, pastrand acelasi numar de elemente \n', d)
arr = np.array([3, 5, 8], dtype='float32')
print(arr)
arr2 = np.array([2, 5.6])
print(arr2)
print(arr2.dtype)
