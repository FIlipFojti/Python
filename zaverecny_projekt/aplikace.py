from evidence import Evidence

class Aplikace:
    """
    Třída zajišťuje ovládání aplikace a komunikaci s uživatelem.
    Obsahuje hlavní smyčku menu a metody pro zadávání/vyhledávání dat.
    """

    def __init__(self):
        # Inicializace instance Evidence (správce seznamu pojištěných)
        self.evidence = Evidence()

    def spustit(self):
        """
        Hlavní smyčka aplikace. Zobrazuje nabídku a reaguje na volby uživatele.
        """
        while True:
            print("=" * 30)
            print("Evidence pojištěných")
            print("=" * 30)
            print("Vyberte si akci:")
            print("1 - Přidat nového pojištěného")
            print("2 - Vypsat všechny pojištěné")
            print("3 - Vyhledat pojištěného")
            print("4 - Konec")

            volba = input("Zadejte volbu: ")

            if volba == "1":
                self._pridej()  # Přidání nového pojištěného
            elif volba == "2":
                self.evidence.vypis_vsechny()  # Výpis všech pojištěných
            elif volba == "3":
                self._vyhledej()  # Vyhledání konkrétního pojištěného
            elif volba == "4":
                print("Ukončuji aplikaci...")
                break  # Konec programu
            else:
                print("Neplatná volba, zkuste to znovu.")

            input("\nPokračujte libovolnou klávesou...")

    def _pridej(self):
        """
        Získá a zvaliduje údaje od uživatele pro nového pojištěného.
        Obsahuje validaci vstupů a převod jména/příjmení na správný formát.
        """

        # Zadání a validace jména
        while True:
            jmeno = input("Zadejte jméno pojištěného: ").strip()  # Odstraní mezery
            if not jmeno:
                print("Jméno nesmí být prázdné.")
            elif not jmeno.isalpha():
                print("Jméno smí obsahovat pouze písmena.")
            else:
                jmeno = jmeno.capitalize()  # První písmeno velké, ostatní malá
                break

        # Zadání a validace příjmení
        while True:
            prijmeni = input("Zadejte příjmení: ").strip()
            if not prijmeni:
                print("Příjmení nesmí být prázdné.")
            elif not prijmeni.isalpha():
                print("Příjmení smí obsahovat pouze písmena.")
            else:
                prijmeni = prijmeni.capitalize()
                break

        # Zadání a validace věku
        while True:
            vek_input = input("Zadejte věk: ").strip()
            if not vek_input.isdigit():
                print("Věk musí být číslo.")
            else:
                vek = int(vek_input)
                if 0 <= vek <= 150:
                    break  # Správný věk
                else:
                    print("Věk musí být v rozmezí 0–150.")

        # Zadání a validace telefonního čísla
        while True:
            telefon = input("Zadejte telefonní číslo: ").strip()
            if not telefon.isdigit():
                print("Telefon smí obsahovat pouze číslice.")
            elif len(telefon) < 9:
                print("Telefon musí mít alespoň 9 číslic.")
            else:
                break

        # Přidání nové osoby do evidence
        self.evidence.pridej_pojisteneho(jmeno, prijmeni, vek, telefon)
        print("Pojištěný byl úspěšně přidán.")

    def _vyhledej(self):
        """
        Získá vstup od uživatele pro vyhledání pojištěného.
        Automaticky převádí vstup na správný formát.
        """
        jmeno = input("Zadejte jméno pojištěného: ").strip().capitalize()
        prijmeni = input("Zadejte příjmení: ").strip().capitalize()
        self.evidence.vyhledej(jmeno, prijmeni)
