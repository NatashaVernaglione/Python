import math

class Forma:
    def area(self):
        pass

    def perimetro(self):
        pass


class Cerchio(Forma):
    def __init__(self, raggio):
        self.raggio = raggio

    def area(self):
        return math.pi * self.raggio ** 2

    def perimetro(self):
        return 2 * math.pi * self.raggio


class Rettangolo(Forma):
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza

    def area(self):
        return self.base * self.altezza

    def perimetro(self):
        return 2 * (self.base + self.altezza)


class Triangolo(Forma):
    def __init__(self, lato1, lato2, lato3):
        self.lato1 = lato1
        self.lato2 = lato2
        self.lato3 = lato3

    def perimetro(self):
        return self.lato1 + self.lato2 + self.lato3

    def area(self):
        s = self.perimetro() / 2
        return math.sqrt(s * (s - self.lato1) *
                         (s - self.lato2) *
                         (s - self.lato3))


scelta = input("Scegli una forma (cerchio, rettangolo, triangolo): ").lower()

if scelta == "cerchio":
    raggio = float(input("Inserisci il raggio: "))
    forma = Cerchio(raggio)

elif scelta == "rettangolo":
    base = float(input("Inserisci la base: "))
    altezza = float(input("Inserisci l'altezza: "))
    forma = Rettangolo(base, altezza)

elif scelta == "triangolo":
    lato1 = float(input("Inserisci il primo lato: "))
    lato2 = float(input("Inserisci il secondo lato: "))
    lato3 = float(input("Inserisci il terzo lato: "))
    forma = Triangolo(lato1, lato2, lato3)

else:
    print("Forma non valida.")
    exit()

print("Area:", forma.area())
print("Perimetro:", forma.perimetro())
