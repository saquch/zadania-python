#Zadanie 3.1

x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
#                   dotąd jest poprawny




#for i in "axby": if ord(i) < 100: print(i)
#                   ta linijka jest nie poprawna
#                   poniewaz po for w tej samej linijce nie może być if


for i in "axby": print(ord(i) if ord(i) < 100 else i)
#                   Ten fragment jest poprawny



# Zadanie 3.2


#L = [3, 5, 4] ; L = L.sort() # Zwraca None wiec L jest kasowana po tym 
#x, y = 1, 2, 3 # Przypisanie 3 wartosci do 2
#X = 1, 2, 3 ; X[1] = 4 # Elementów krotki nie można podmienić po jej utworzeniu
#X = [1, 2, 3] ; X[3] = 4 # Lista ma tylko 3 elementy (0,1,2) a chcemy przypisać do 4
#X = "abc" ; X.append("d") # Stringi w pythonie nie mają metody .append()
#L = list(map(pow, range(8))) # funkcja pow potrzebuje przynajmniej 2 argumentow a tu tylko jeden przy kazdej iteracji


# Zadanie 3.3
spodziewany_wynik = "1 2 4 5 7 8 10 11 13 14 16 17 19 20 22 23 25 26 28 29"

wynik_for = ""
wynik_while = ""

for x in range (31):
    if x % 3 != 0:
        wynik_for += str(x) + " " 

wynik_for = wynik_for.strip() # bo inaczej przez bialy znak assert dawalo bląd
assert wynik_for == spodziewany_wynik

y = 0
while y <= 30:
    if y%3 != 0:
        wynik_while += str(y) + " " 

    y+= 1
wynik_while = wynik_while.strip() # bo inaczej przez bialy znak assert dawalo bląd
assert wynik_while == spodziewany_wynik


# Zadanie 3.4    

while True:
    dane = input("Podaj liczbę: ")
    
    if dane =="stop":
        break
        
    try:
        x = float(dane)
        print("x =", x)
        print("x^3 =", x**3)
    except ValueError:
        print("Błąd")



# Zadanie 3.5

x = 12
gora = "|" + "....|" * x


dol = "0"
for i in range(1, x +1):

    dol += str(i).rjust(5)


wynik = gora + "\n" + dol
print(wynik)


#Zadanie 3.6

x = 4
y = 2

poziom = "+---" * x +"+\n"
pion = "|   " * x + "|\n"


prostokat = (poziom+ pion)*y + poziom
print (prostokat)

#Zadanie 3.8

sekwencja1 = "abraaxscaca"
sekwencja2 = "piesek"

wspolne =list (set(sekwencja1) &set(sekwencja2))
wszystkie = list(set(sekwencja1) |set(sekwencja2))

spodziewane_wspolne = ['s']
spodziewane_wszystkie = ['a','b', 'c','e', 'i', 'k', 'p', 'r', 's', 'x']

wspolne.sort()
wszystkie.sort() # dodalem 2 sort zeby asset nie dawalo blad
assert wspolne ==spodziewane_wspolne
assert wszystkie == spodziewane_wszystkie

# zadanie 3.9

sekwencje = [[], [4], (1, 2), [3, 4], (5, 6, 7)]
spodziewany_wynik = [0, 4, 3, 7, 18]

wynik = [sum(s) for s in sekwencje]

assert wynik == spodziewany_wynik


#zadanie 3.10

#1 
slownik_1 = {'I':1, 'V':5, 'X': 10, 'L':50,'C':100,'D':500, 'M':1000}
#2
slownik_2  = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

def roman2int(liczba_rzymska):
    slownik = {'I':1, 'V':5, 'X': 10, 'L':50,'C':100,'D':500, 'M':1000}
    wynik = 0

    for i in range (len(liczba_rzymska)):
        wartosc_obecna = slownik[liczba_rzymska[i]]

        if (i+ 1 < len(liczba_rzymska)) and wartosc_obecna < slownik[liczba_rzymska[i+1]]:
            wynik -= wartosc_obecna
        else:
            wynik +=wartosc_obecna
    return wynik                


assert roman2int("II") == 2
assert roman2int("V") == 5
assert roman2int("IX") == 9
assert roman2int("LVIII") == 58
assert roman2int("MCMXCVI") == 1996