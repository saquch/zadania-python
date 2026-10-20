print("Zadanie 2.10")
line = "Przykładowy tekst " \
"abcd " \
"ttt" #zeby byl wielowierszowy
print("line = ", line)
liczba_wyrazow = len(line.split())
print ("Liczba wyrazow = ", liczba_wyrazow)
assert(liczba_wyrazow == 4)


print("Zadanie 2.11")
line2 = "-".join(line)
print(line2)
assert "-" in line2

print("Zadanie 2.12")
words = line.split()

line3 ="".join(w[0] for w in words)
print ("pierwsze znaki = ",line3)
assert line3 == "Ptat"

line4 ="".join(w[-1] for w in words)
print ("ostatnie znaki = ",line4)
assert line4 == "ytdt"

print("Zadanie 2.13")

words2 = line.split() #wiem bylo powyzej ale dalem zeby kazde zadanie bylo osobne 
sum = 0
for w in words2:
    sum = sum+len(w)    
print(sum)
assert sum == 23


print("Zadanie 2.14")
words3 = line.split()
dlugosc_naj_slowa = 0
naj_slowo = ""
for w in words3:
    if len(w) > dlugosc_naj_slowa:
        naj_slowo = w
        dlugosc_naj_slowa = len(w)
print("najdluzsze slowo = ", naj_slowo)
print("dlugosc najdłuższego słowa = ", dlugosc_naj_slowa)
assert naj_slowo == "Przykładowy"
assert dlugosc_naj_slowa == 11

print("Zadanie 2.15")
L = [3, 7, 10, 20, 15]
line15 =""
for x in L:
    line15+= str(x)
print("line = ", line15)
assert line15 == "37102015"

print("Zadanie 2.16")


line16 = ("abcd auhd sddsGvRdsd")
print("line przed zmiana = ", line16)
line16 = line16.replace("GvR", "Guido van Rossum")
print("line po zmianie = ",line16)
assert line16 == "abcd auhd sddsGuido van Rossumdsd"



print("Zadanie 2.17")
words4 = line.split()
posortowane_alf = sorted(words)
posortowane_dlugosc = sorted(words, key =len)

print ("Posortowane alfabetycznie = ", posortowane_alf)
print("Posortowane po długosci = ", posortowane_dlugosc)
assert posortowane_alf[0] == "Przykładowy"
assert posortowane_dlugosc[0] == "ttt"

print("Zadanie 2.18")

liczba = 1287469149623400432404234021042012412454606000346023620
liczba_string = str(liczba)
liczba_zer = liczba_string.count("0")
print ("liczba = ", liczba)
print("liczba zer = ", liczba_zer)
assert liczba_zer == 12

print("Zadanie 2.19")
L = [3, 42, 128, 7, 500]

wynik = ""
for x in L:
    liczba_z_zerami = str(x).zfill(3)
    wynik = wynik + liczba_z_zerami

print ("wynik = ", wynik)
assert wynik == "003042128007500"