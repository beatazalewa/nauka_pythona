# najprostszy sposób definiowania obiektu
# pass jest to po prostu miejsce dla funkcjonalności, która będzie dodana później
# pass może być użyte w ciele (a body, które nic nie robi
# def odejmij(a, b):
#     pass

class Paletka:
    pass

# tworzymy obiekt na podstawie klasy, podajeemy nazwę obiektu (paleetka_a) i wywołujemy konstruktor klasy (Paletka())
# f-string
# val = 'Python course'
# print(f"Rezultat zwracany przez naszą zmienną to {val}")

# name = 'Beata'
# age = 23
# print(f"Hello, my name is {name} nad I am {age} years old")
def testklasy():
    paletka_a = Paletka()
    print(f"Obiekt typu {type(paletka_a)} zawiera od razu pewne właściwości i metody:")
    print(dir(paletka_a))
