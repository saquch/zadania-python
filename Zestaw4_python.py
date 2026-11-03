#Zadanie 4.2
def make_ruler(n):
    gora = "|" + "....|" * n


    dol = "0"
    for i in range(1, n +1):

        dol += str(i).rjust(5)


    wynik = gora + "\n" + dol
    return wynik

def make_grid(rows, cols):
    poziom = "+---" * cols +"+\n"
    pion = "|   " * cols + "|\n"


    prostokat = (poziom+ pion)*rows + poziom
    return prostokat
#Zadanie 4.3


def factorial(n):
    wynik = 1
    for i in range (1, n+ 1):
        wynik *= i
    
    return wynik

assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) ==120
assert factorial(6) == 720


#zadanie 4.4
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        nowa_suma = a+b
        a = b
        b = nowa_suma

    return a
assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3)== 2
assert fibonacci(4) == 3
assert fibonacci(5) == 5
assert fibonacci(10) == 55

#zadanie 4.5

def odwracanie_iteracyjne(L, left,right):
    while left <right:
        tymczasowa = L[left]
        L[left] = L[right]
        L[right] = tymczasowa

        left +=1
        right-= 1

def odwracanie_rekurencyjne (L,left, right):
    if left< right:
        tymczasowa = L[left]
        L[left] = L[right]
        L[right] = tymczasowa
        odwracanie_rekurencyjne(L, left +1, right- 1)


# Test dla wersji iteracyjnej
lista1 = [0, 1, 2, 3, 4, 5]
odwracanie_iteracyjne(lista1, 1, 4)
assert lista1 == [0,4,3,2,1,5]

# Test dla wersji rekurencyjnej
lista2 = [10, 20, 30, 40, 50, 60]
odwracanie_rekurencyjne(lista2, 2, 5)
assert lista2 == [10, 20, 60, 50, 40, 30]



#zadanie 4.6
def sum_seq(sequence):
    suma =0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            suma+=sum_seq(item )
        else:
            suma +=item

    return suma

assert sum_seq([]) == 0
assert sum_seq([1, 2, 3]) == 6
assert sum_seq([1, (2, 3), [], [4, [5, 6]]]) == 21

#zadanie 4.7

def flatten(sequence):
    plaska_lista =[]

    for item in sequence:
        if isinstance(item, (list, tuple)):
            plaska_lista.extend(flatten(item))
        else:
            plaska_lista.append(item)

    return plaska_lista


sequence = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
assert flatten(sequence) == [1, 2, 3, 4, 5, 6, 7, 8, 9]