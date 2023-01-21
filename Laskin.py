"""
MG tehnyt tämän laskimen. Laskurissa mahdollista suorittaa
lisäys-, vähennys-, jako- ja kertolaskuja.
Laskuri tallentaa laskutoimitukset txt-tiedostoon, sen juureen.
Yksinkertainen terminaalikäyttöliittymä, jossa mahdollista
valita em. laskutoimitukset sekä viisi edellistä laskutoimitusta,
ohjelman resetointi ja lopettaminen.
"""

import os


"""
Kaikki laskufunktiot ottavat kaksi muuttujaa ja funktio käyttää
pythonin sisäistä laskuominaisuutta palauttaen tuloksen.
"""
# Lisäysfunktio
def lisaa(x, y):
    return x + y

# Vähennysfunktio
def vahenna(x, y):
    return x - y

# Jakofunktio
def jako(x, y):
    return x / y

# Kertofunktio
def kerto(x, y):
    return x * y


"""
Funktio hakee tulokset tiedostosta ja tulostaa ne käyttäjälle.
"""
# Tulosten katselu-funktio
def katso_tulokset():
    with open("laskimen_tulokset.txt", "r") as f:
        rivit = f.readlines()
        for rivi in rivit[-5:]:
            print(rivi)


"""
Päävalikko kokonaisuudessaan, jossa valintalogiikka, ohjelman
resetointi ja lopettaminen.
"""
while True:
    #valikon valinnat
    print("-----------")
    print("Tervetuloa Maijan laskimeen!")
    print("Valitse vaihtoehdoista")
    print("1. lisää")
    print("2. vähennä")
    print("3. jaa")
    print("4. kerro")
    print("5. katso 5 viimeisintä laskutoimitusta")
    print("6. ohjelman resetointi")
    print("7. lopeta ohjelma")
    print("-----------")

    valinta = input("valintasi (1/2/3/4/5/6/7): ")

    #riippuen käyttäjän valinnasta, mikä funktio kutsutaan käyttöön
    if valinta in ['1','2','3','4']:
        num1 = int(input("Anna ensimmäinen numero: "))
        num2 = int(input("Anna toinen numero: "))

        if valinta == '1':
            tulos = lisaa(num1, num2)
            op = "+"
        elif valinta == '2':
            tulos = vahenna(num1, num2)
            op = "-"
        elif valinta == '3':
            tulos = jako(num1, num2)
            op = "/"
        elif valinta == '4':
            tulos = kerto(num1, num2)
            op = "*"

        # Tallenna tulokset txt-tiedostoon
        with open("laskimen_tulokset.txt", "a") as f:
            f.write(f"{num1} {op} {num2} = {tulos}\n")
        print(f"{num1} {op} {num2} = {tulos}")
    
    # Kutsutaan viisi viimeisintä laskutoimitusta
    elif valinta == '5':
        katso_tulokset()

    # Ohjelman resetointi
    elif valinta == '6':
        try:
            os.remove("laskimen_tulokset.txt")
            print("Tiedosto poistettu.")

        except Exception as e:
            print("error", e)
            print("Tiedosto on jo poistettu.")
    
    # Ohjelman lopetus
    elif valinta == '7':
        break

    else:
        print("Väärä valinta.")