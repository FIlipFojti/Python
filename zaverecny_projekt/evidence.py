from pojisteny import Pojisteny

class Evidence:
    """
    Třída slouží pro správu kolekce (seznamu) pojištěných osob.
    """
    def __init__(self):
        """
        Konstruktor. Vytvoří prázdný seznam pro ukládání pojištěných.
        """
        self.pojisteni = []

    def pridej_pojisteneho(self, jmeno, prijmeni, vek, telefon):
        """
        Přidá nového pojištěného do seznamu.
        """
        novy = Pojisteny(jmeno, prijmeni, vek, telefon)
        self.pojisteni.append(novy)

    def vypis_vsechny(self):
        """
        Vypíše všechny pojištěné osoby ze seznamu.
        """
        if not self.pojisteni:
            print("Seznam pojištěných je prázdný.")
        else:
            for osoba in self.pojisteni:
                print(osoba)

    def vyhledej(self, jmeno, prijmeni):
        """
        Vyhledá pojištěného podle jména a příjmení (není case-sensitive).
        """
        nalezeni = [osoba for osoba in self.pojisteni if osoba.jmeno.lower() == jmeno.lower() and osoba.prijmeni.lower() == prijmeni.lower()]
        if nalezeni:
            for osoba in nalezeni:
                print(osoba)
        else:
            print("Pojištěný nenalezen.")
