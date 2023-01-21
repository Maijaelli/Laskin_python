# Lisäysfunktio
def lisaa(x, y):
    return x + y

while True:
    #valikon valinnat
    print("-----------")
    print("Tervetuloa Maijan laskimeen!")
    print("Valitse vaihtoehdoista")
    print("1. lisää")
    print("2. poistu")
    print("-----------")

    valinta = input("valintasi (1/2): ")


    #riippuen käyttäjän valinnasta, mikä funktio kutsutaan käyttöön

    if valinta in ['1','2']:
        num1 = int(input("Anna ensimmäinen numero: "))
        num2 = int(input("Anna toinen numero: "))

        if valinta == '1':
            tulos = lisaa(num1, num2)
            print(tulos)
        elif valinta == '2':
            print("Tämä on valinta kaksi.")
        else:
            print("Väärä valinta.")