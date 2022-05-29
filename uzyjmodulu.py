# importujemy moduł i nadajemy mu alias
from mytoolkit import matematyczny as mat
from mytoolkit import pomocniczy as pom #j.w. tylko dla drugiego modułu
# wywołanie funkcji/metod z mytoolkit/matematyczny (alias: 'mat')
print(mat.dodaj(4, 14))
print(mat.odejmij(10, 5))
# wywołanie funkci/metody z mytoolkit/pomocniczy (alias: 'pom')
pom.czesc() 
