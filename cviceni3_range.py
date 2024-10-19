def my_zip(*iterables):

    length = len(iterables[0])

    results = [tuple(iterable[i] for iterable in iterables)for i in range(length)]
    return results


if __name__ == "__main__":

    jmena = ["Alice", "Bob"]
    vek = ["18let", "19let"]
    vaha = ["45KG", "63KG"]

    vysledek = my_zip(jmena, vek, vaha)
    print(vysledek)


