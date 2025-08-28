def prva_naloga():
    vsota = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            vsota += i
    return vsota

def druga_naloga():
    prva = 1
    druga = 2
    vsota = 2
    while prva + druga < 4000000:
        tretja = prva + druga
        prva = druga
        druga = tretja
        if druga % 2 == 0:
            vsota += druga
    return vsota

def tretja_naloga(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
        else:
            i += 1
    return n

def je_palindrom(stevilo):
    return str(stevilo) == str(stevilo)[::-1]

def cetrta_naloga():
    najvecji = 0
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            produkt = i * j
            if je_palindrom(produkt) and produkt > najvecji:
                najvecji = produkt
    return najvecji

def peta_naloga():
    return 2*3*5*7*11*13*17*19*2*2*3*2

def šesta_naloga():
    vsota_kvadratov = (100 * 101 * 201) / 6
    kvadrat_vsote = (50*101)**2
    return kvadrat_vsote - vsota_kvadratov

def je_prastevilo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def sedma_naloga():
    i = 1
    n=1
    praštevilo = 0
    while i != 10002:
        if je_prastevilo(n):
            praštevilo = n
            n += 1
            i += 1
        else:
            n += 1
    return praštevilo

def osma_naloga():
    število = str(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)
    največji = 1
    for i in range(988):
        naše = število[i:i+13]
        produkt = 1
        for števka in naše:
            produkt = produkt * int(števka)
            if produkt > največji:
                največji = produkt
    return največji

import math
def deveta_naloga():
    zmnozek = 1
    for i in range(1, 1001):
        for j in range(1, i):
            c2 = i**2 + j**2
            c = math.isqrt(c2)
            if c * c == c2 and i + j + c == 1000:
                zmnozek = i * j * c
    return zmnozek

def deseta_naloga():
    vsota = 0
    for i in range(2000001):
        if je_prastevilo(i):
            vsota += i
    return vsota