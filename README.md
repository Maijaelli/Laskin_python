# Laskin
---

Tämä on osa Turun avoimen yliopiston 'Ohjelmoinnin perusteet' -kurssia. Osana kurssia oli tehdä oma 100 riivin ohjelmakoodi. 

Ohjelma on tehty Python -kielellä ja se on simppeli laskin.


Tämä readme-paketti toimii kurssin raporttina. Raportti sisältää pyydetyt ongelman kuvauksen, ongelman ja varsinaisen ratkaisun analysoinnin sekä riippuvaisuudet, kirjastot ja miten ohjelmaa ajetaan. Lopuksi lisätty lähteet.


---

## Ongelman kuvaus

Laskinsovellus on ohjelmistosovellus, jonka avulla käyttäjät voivat suorittaa matemaattisia laskelmia. Se sisältää tyypillisesti matemaattisia perustoimintoja, kuten yhteen-, vähennys-, kerto- ja jakolaskutoimintoja, ja se voi sisältää myös lisäominaisuuksia, kuten trigonometrisiä ja logaritmisia toimintoja. Laskinsovelluksia käytetään laajasti eri aloilla, kuten koulutuksessa, rahoituksessa, tekniikassa ja tieteessä. Opiskelijat, ammattilaiset ja yksityishenkilöt käyttävät niitä yleisesti yksinkertaisten ja monimutkaisten matemaattisten laskelmien suorittamiseen. Matemaattisten perustoimintojen lisäksi joissakin laskinsovelluksissa on myös kehittyneitä ominaisuuksia, kuten kyky suorittaa muunnoksia eri mittayksiköiden välillä, tuki kompleksiluvuille ja mahdollisuus luoda ja tallentaa mukautettuja toimintoja.


## Ongelman analysointi

Pythonin laskinsovellus voidaan toteuttaa useilla erilaisilla teknisillä ratkaisuilla. Yksi yleinen lähestymistapa on käyttää perusohjelmointikäsitteitä, kuten funktioita, muuttujia ja silmukoita, luomaan erilaisia matemaattisia operaatioita.

Syöttökäsittelyssä sovellus voi käyttää input()-funktiota vastaanottamaan syötteitä käyttäjältä. Tämä syöte voidaan sitten muuntaa numeeriseksi tietotyypiksi, kuten kokonaisluvuksi tai floatiksi, jatkokäsittelyä varten. Sovellus voi käyttää erillisiä toimintoja kunkin matemaattisen toiminnon suorittamiseen, kuten yhteen-, vähennys-, kerto- ja jakolaskuihin. Nämä funktiot voivat ottaa käyttäjän syötteitä muuttujina ja palauttaa toiminnon tuloksen.

Sovellus voi myös käyttää while-silmukkaa pitääkseen sovelluksen käynnissä, kunnes käyttäjä päättää poistua. Näin käyttäjä voi suorittaa useita laskutoimituksia ilman, että hänen tarvitsee käynnistää sovellusta uudelleen. Laskelmien tulosten tallentamiseen sovellus voi käyttää pythonin open()-funktiota tiedoston luomiseen ja siihen liittämiseen. Tämän avulla käyttäjä voi tarkastella 5 viimeistä tulosta myöhemmin.

Sovelluksen mahdollinen rajoitus on, että se pystyy suorittamaan vain matemaattisia perusoperaatioita eikä pysty käsittelemään monimutkaisempia matemaattisia laskelmia. Joitakin muita rajoituksia ovat virheiden käsittelyn rajoitetut toiminnot ja symbolisten laskelmien tuen puuttuminen.

Toimintalogiikan kannalta sovellus ottaa syötteen käyttäjältä, käsittelee sen ja suorittaa vastaavan matemaattisen operaation, jonka jälkeen se tallentaa tuloksen tiedostoon ja jos käyttäjä haluaa nähdä viimeiset 5 tulosta, se lukee tiedoston ja näyttää tulokset. Sovellus on käynnissä, kunnes käyttäjä poistuu.


## Varsinainen ratkaisu

Käyttäjä voi laskinsovelluksessa valita yksinkertaisesta komentovalikosta, joko:
1. Yhteenlaskun
2. Vähennyslaskun
3. Jakolaskun
4. Kertolaskun
5. Katsoa viisi (5) viimeistintä laskutoimitusta
6. Resetoida ohjelma, eli poistaa em. tallennettu laskutoimitustiedosto
7. Lopettaa ohjelma
Komentovalikko on while-silmukka ja se pitää ohjelman käynnissä, kunnes käyttäjä päättää sen lopettaa. Käyttäjän valinnan jälkeen kutsutaan if-else-lauseen avulla oikeaa funktiota. 

Käyttäjän valittua jokin laskutoimitus, pyytää ohjelma käyttäjältä kahta kokonaislukua, jotka tallennetaajn muuttujaan ja kutsutaan oikea laskutoimitusfunktio. Funktio palauttaa käyttäjälle tuloksen ja tallentaa sen tiedostoon (juureen) 'laskin-tulokset.txt'.

Käyttäjä voi myös valita katsoa viisi (5) viimeisintä tulosta, jolloin ohjelma kutsuu 'katso_tulokset()' funktiota. Funktio avaa ja lukee viisi viimeisintä riviä tiedostosta sekä tulostaa ne käyttäjälle. Tulostuksessa käytetään apuna for-loop menetelmää.

Ohjelman resetoinnissa käytetään virheidenhallintaa, jonka avulla ohjelma ei kaadu, mikäli ko. tiedostoa ei löydy. Ohjelman resetointi tapahtuu käyttäen Pythonin omaa 'os' -kirjastoa, jonka avulla poistetaan ohjelamn luoma 'laskimen_tulokset.txt' tiedosto. Mikäli tiedostoa ei ole, ohjelma palaa alkuvalikkoon.


## Riippuvaisuudet ja kirjastot

- Python
- Os

Ohjelma ajetaan käyttäen komentoa:
> python3 Laskin.py


## Lähteet

- Kurssin oppimateriaali ja luennot
- https://extr3metech.wordpress.com/2014/09/14/simple-text-menu-in-python/
- https://docs.python.org/3/tutorial/errors.html