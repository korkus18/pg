import requests
from bs4 import BeautifulSoup

"""
Program stáhne URL a z ní vrátí pouze hlavní nadpisy <h1>:
<h1>Hlavní nadpis</h1>
"""


def dowload(url):
    nadpisy = []
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        for nadpis in soup.find_all('h1'):
            nadpisy.append(nadpis.text.strip())


    except requests.exceptions.RequestException as e:
        print("error")

    return nadpisy

if __name__ == "__main__":
    url = "https://www.python.org/download/releases/3.0/"
    nadpisy_h1 = dowload(url)
    print(nadpisy_h1)
