def obvod_ctverce(delka_strany):
    # funkce vypocita obvod ctverce z delky jeho strany
    return 4 * delka_strany


def obsah_ctverce(delka_strany):
    # funkce vypocita obsah ctverce z delky jeho strany
    return delka_strany ** 2


def pocet_pismen(text, pismeno):
    # funkce vrati pocet vyskytu pismene v textu
    return text.count(pismeno)


def index_pismene(text, pismeno):
    # funkce vrati indexy daneho pismene v textu, tzn. pro text="ahoj, honzo" a pismeno="h" vrati [1, 6]
    return [index for index, char in enumerate(text) if char == pismeno]


def fibonachi(maximum):
    # funkce vrati fibonachiho posloupnost, pro maximum=5 -> [1, 1, 2, 3, 5]
    if maximum < 1:
        return []
    fib_sequence = [1, 1]
    while fib_sequence[-1] + fib_sequence[-2] <= maximum:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence


if __name__ == "__main__":
    index_pismene("ahoj, honzo", "h")