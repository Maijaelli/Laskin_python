while True:
    #valikon valinnat
    print("-----------")
    print("Tervetuloa Maijan laskimeen!")
    print("Valitse vaihtoehdoista")
    print("1. jotain")
    print("2. poistu")
    print("-----------")

    valinta = input("valintasi (1/2): ")


    #riippuen käyttäjän valinnasta, mikä funktio kutsutaan käyttöön

    if valinta in ['1','2']:
        if valinta == '1':
            print("Tämä on vaihtoehto yksi.")
        elif valinta == '2':
            print("Tämä on valinta kaksi.")
        else:
            print("Väärä valinta.")