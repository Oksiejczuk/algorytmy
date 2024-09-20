def zSystemNa10 (tekst,system):
    wynik = 0
    for znak in tekst:
        if znak >='0' and znak <='9':
            wynik = wynik*system+ord(znak)-48
        else:
            wynik = wynik*system+ord(znak)-55
    return wynik


def z10naSystem (liczba1, system2):
    wynik2 = ''
    while liczba>0:
        reszta = liczba%system
        liczba = liczba // system
        if reszta < 10:
            wynik = chr(reszta+48) + wynik
        else:
            wynik = chr(reszta+55) + wynik
    return wynik

+

def z10na8 (liczba2):
    wynik3 = ''
    while liczba2>0:
        reszta = liczba%8
        liczba = liczba // 8
        if reszta < 10:
            wynik = chr(reszta+48) + wynik
        else:
            wynik = chr(reszta+55) + wynik
    return wynik



def z8Na10 (tekst):
    wynik = 0
    for znak in tekst:
        if znak >='0' and znak <='9':
            wynik = wynik*system+ord(znak)-48
        return wynik


#zadanie system36

dana,system1,system2 =input().split()
system1 = int(system1)
system2 = int(system2)
wynikW10 = zSystemNa10 (dana,system1)
print(z10naSystem (wynikW10, system2))
