# funkce vrati treti prvek ze seznamu, pokud ma mene nez 3 prvky, vrati None
def vrat_treti(seznam):
    if len(seznam) < 3:
        return None
    return seznam[2]

# funkce spocita prumer z hodnot v seznamu, pouzijte sum(), len()
def udelej_prumer(seznam):
    if len(seznam) == 0:
        return None
    return sum(seznam) / len(seznam)

# funkce naformatuje retezec, aby vratila text ve formatu:
# "Jmeno: Jan, Prijmeni: Novak, Vek: 20, Prumerna znamka: 2.5"
def naformatuj_text(slovnik):
    prumerna_znamka = udelej_prumer(slovnik["znamky"])
    return f"Jmeno: {slovnik['jmeno']}, Prijmeni: {slovnik['prijmeni']}, Vek: {slovnik['vek']}, Prumerna znamka: {prumerna_znamka}"


if __name__ == "__main__":
    seznam = [9, 8, 5]
    vysledek = vrat_treti(seznam)
    print(vysledek)  # Output: 5

    obalka = [9, 8, 7, 6]
    vysledek = udelej_prumer(obalka)
    print(vysledek)  # Output: 7.5

    student = {
        "jmeno": "Matěj",
        "prijmeni": "Dvořák",
        "vek": 21,
        "znamky": [1, 2, 1, 1, 3, 2]
    }
    vysledek = naformatuj_text(student)
    print(vysledek)  # Output: "Jmeno: Matěj, Prijmeni: Dvořák, Vek: 21, Prumerna znamka: 1.6666666666666667"

    # Další příklady:
    student["vek"] # -> 21
    student["znamky"] # -> [1, 2, 1, 1, 3, 2]
    student["znamky"][2] # -> 1

    a = 1
    f"Naformatovany retezes s hodnotou {a}"  # Output: "Naformatovany retezes s hodnotou 1"
