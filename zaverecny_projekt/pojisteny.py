class Pojisteny:
    """
       Třída reprezentuje jednu pojištěnou osobu.
       Obsahuje jméno, příjmení, věk a telefonní číslo.
    """
    def __init__(self, jmeno, prijmeni, vek, telefon):
        """
        Konstruktor třídy. Vytvoří instanci pojištěného s validací.
        """
        if not jmeno or not prijmeni:
            raise ValueError("Jméno a příjmení nesmí být prázdné.")
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        """
        Vrací hezky formátovaný řetězec pro výpis pojištěného.
        """
        return f"{self.jmeno:<10} {self.prijmeni:<10} {self.vek:<3} {self.telefon}"
