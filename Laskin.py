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

# Tulosten katselu-funktio
def katso_tulokset():
    with open("laskimen_tulokset.txt", "r") as f:
        rivit = f.readlines()
        for rivi in rivit[-5:]:
            print(rivi)

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
    print("6. lopeta ohjelma")
    print("-----------")

    valinta = input("valintasi (1/2/3/4/5/6): ")


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
    
    # Ohjelman lopetus
    elif valinta == '6':
        break

    else:
        print("Väärä valinta.")