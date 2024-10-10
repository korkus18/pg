def cislo_text(cislo):
    # Předdefinované textové reprezentace pro čísla do 20 a násobky desítek
    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět"]
    desitky = ["", "deset", "dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
    teens = ["jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]

    # Převod čísla na integer
    try:
        cislo = int(cislo)
    except ValueError:
        return "Neplatný vstup"

    # Zpracování čísel od 0 do 100
    if cislo < 0 or cislo > 100:
        return "Číslo mimo rozsah"
    elif cislo == 100:
        return "sto"
    elif cislo < 10:
        return jednotky[cislo]
    elif cislo < 20:
        if cislo == 10:
            return "deset"
        else:
            return teens[cislo - 11]
    else:
        desitka = cislo // 10
        jednotka = cislo % 10

        if jednotka == 0:
            return desitky[desitka]
        else:
            return f"{desitky[desitka]} {jednotky[jednotka]}"

if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(cislo)
    print(text)
