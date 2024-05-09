from datetime import datetime, timedelta

class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 10000)

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 15000)

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

class FoglalasKezelo:
    def __init__(self):
        self.foglalasok = []

    def foglalas(self, szoba, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba == szoba and foglalas.datum == datum:
                print("A szoba már foglalt ekkor.")
                return
        self.foglalasok.append(Foglalas(szoba, datum))
        print("Foglalás sikeres.")

    def lemondas(self, szoba, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba == szoba and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                print("Foglalás lemondva.")
                return
        print("Nincs ilyen foglalás.")

    def listaz(self):
        if self.foglalasok:
            print("Foglalások:")
            for foglalas in self.foglalasok:
                print(f"  Szoba: {foglalas.szoba.szobaszam}, Dátum: {foglalas.datum}")
        else:
            print("Nincs foglalás.")

def main():
    szalloda = Szalloda("Példa Szálloda")
    szalloda.add_szoba(EgyagyasSzoba("101"))
    szalloda.add_szoba(KetagyasSzoba("201"))
    szalloda.add_szoba(KetagyasSzoba("202"))

    foglalaskezelo = FoglalasKezelo()

    # Feltöltjük a rendszert néhány foglalással
    foglalaskezelo.foglalas(szalloda.szobak[0], datetime.now() + timedelta(days=1))
    foglalaskezelo.foglalas(szalloda.szobak[1], datetime.now() + timedelta(days=2))
    foglalaskezelo.foglalas(szalloda.szobak[2], datetime.now() + timedelta(days=3))
    foglalaskezelo.foglalas(szalloda.szobak[0], datetime.now() + timedelta(days=4))
    foglalaskezelo.foglalas(szalloda.szobak[1], datetime.now() + timedelta(days=5))

    # Felhasználói interfész
    while True:
        print("\nVálassz műveletet:")
        print("1. Szoba foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        valasztas = input("Választott művelet: ")

        if valasztas == "1":
            szobaszam = input("Add meg a szoba számát: ")
            for szoba in szalloda.szobak:
                if szoba.szobaszam == szobaszam:
                    datum_str = input("Add meg a foglalás dátumát (YYYY-MM-DD): ")
                    datum = datetime.strptime(datum_str, "%Y-%m-%d")
                    foglalaskezelo.foglalas(szoba, datum)
                    break
            else:
                print("Nincs ilyen szoba.")

        elif valasztas == "2":
            szobaszam = input("Add meg a szoba számát: ")
            for szoba in szalloda.szobak:
                if szoba.szobaszam == szobaszam:
                    datum_str = input("Add meg a foglalás dátumát (YYYY-MM-DD): ")
                    datum = datetime.strptime(datum_str, "%Y-%m-%d")
                    foglalaskezelo.lemondas(szoba, datum)
                    break
            else:
                print("Nincs ilyen szoba.")

        elif valasztas == "3":
            foglalaskezelo.listaz()

        elif valasztas == "4":
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás.")

if __name__ == "__main__":
    main()