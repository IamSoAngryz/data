"""
Python specific data science libraries
Pandas  = librarie Python pentu data analysis (analiza volumelor 
mari de date)
        = modul de tip ETL (Extract, Transfer, Load)
Instalare:
pip install pandas
Clase specifice pandas:
Seriers - clasa pandas pentru date oraganizate similar arrays
        (un ndarray unidemensional, cu index pe prima coloana si
        datele pe a doua)
DataFrame - clasa specifica pandas pentru date organizate tabelar
            bidimensional
Jupyther - aplicatie care permite vizualizarea datelor in browser
Instalare:
    pip install jupyterlab
Executie:
    jupyter notebook
    - deschide un notebook in browser
    click New, selectam Python 3 pentru a incepe lucrul cu date
    * in notebook dolosim Shift-Enter pentru a rual o comanda
"""

import pandas as pd

s = pd.Series([10, 4, 22, 1, 7])
print(s)

office_dict = {
    'limbaje':['Python', 'Java', 'JavaScript'],
    'developeri':[4, 2, 3]
}
df = pd.DataFrame.from_dict(office_dict)
print(df)
print(df.head())
print(type(df))
print(df['developeri'])
print('Counter elemente:', df['developeri'].count())
print('Media elemente:', df['developeri'].mean())
print(df.dtypes)