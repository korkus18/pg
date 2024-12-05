def dec_to_bin(cislo):
    # Ak je cislo reťazec, preveďte ho na celé číslo
    # Vrátiť binárnu reprezentáciu bez "0b"



    if isinstance(cislo, str):
        cislo = int(cislo)

    #  return bin(cislo)[2:] jednodussi zbusob na konvertovani

    if cislo == 0:
        return "0"

    vysledek = ""

    while cislo > 0:
        zbytek = cislo % 2
        vysledek = str(zbytek) + vysledek
        cislo //= 2

    return vysledek

def test_bin_to_dec():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"