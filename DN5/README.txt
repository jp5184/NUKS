Namen aplikacije: Uporabnik lahko pridobi seznam restavracij z njihovimi ocenami, ter dodaja nove ocene in restavracije.

Delovanje: API strežnik deluje s pomočjo datoteke main.py, baza podatkov prek datoteke database.py in sheme podatkov v datoteki schemas.py,
sama baza podatkov se nahaja v datoteki restaurantDatabase.db. Vsi zahtevani python moduli so zabeleženi v datoteki requirements.txt.

Vsebovane funkcionalnosti:
-> dodaj restavracijo                   POST        /addRestaurant                      (v tabelo restavracij doda novo restavracijo)
-> dodaj oceno                          POST        /addRestaurantRating                (v tabelo ocen restavracij doda novo oceno restavracije)
-> pridobi seznam imen restavracij      GET         /getRestaurantNameList              (pridobi seznam imen restavracij)
-> pridobi seznam ocen restavracij      GET         /getRestaurantRatingList            (pridobi seznam ocen restavracij)


V podatkovni bazi so podatki strukturirani na sledeči način:
        Tabela imen restavracij
+------+------------------------+
|  id  |    restaurant_name     |
+------+------------------------+
|  1   |       FE cafeteria     |
+------+------------------------+
|  2   |           ...          |
+------+------------------------+
|  3   |           ...          |
+------+------------------------+

        Tabela ocen restavracij
+------+----------------+--------+
|  id  |  restaurant_id | rating |
+------+----------------+--------+
|  1   |       1        |   4    |
+------+----------------+--------+
|  2   |       1        |   5    |
+------+----------------+--------+
|  3   |       3        |   2    |
+------+----------------+--------+

Docker storitev http://212.101.137.114:8080/function/restaurant-sort združi tabeli imen in ocen, izračuna
povprečno oceno za posamezno restavracijo in vrne urejen seznam restavracij (padajoče glede na povprečno oceno)

Podatkovna baza od DN5 naprej deluje preko MySQL dockerja, na katero se poveže fastAPI

Vsi docker imagi so na voljo: https://hub.docker.com/u/jp5184


Navodila:
1) source .venv/bin/activate                                                    #Zagon virtualnega okolja
2) pip install -r requirements.txt                                              #Namestitev potrebnih python modulov
3) sudo apt install nodejs npm
4) npm install -g @vue/cli                                                      #Potrebena je verzija Nodejs vsaj 12.0.0
5) npm install axios
6) npm install -g @vue/cli-service-global
7) npm install vuex
8) sudo docker start mysql-docker                                               #Zagon MySQL dockerja s podatkovno bazo
9) python3 -m uvicorn main:app --host 0.0.0.0                                   #Zagon API strežnika
9) sudo docker run --network=host -p 8000:8000 jp5184/fast-api-docker           #Zagon fastAPI strežnik (kot docker), če ne deluje zaženi zgornjo vrstico in ponovno build-aj docker
10) npm run serve -- --port "8085"                                              #zagon vue (iz direktorija -> vue_spa)
10) sudo docker run -p 8085:8085 jp5184/vue-spa-docker                          #Zagon vue frontend (kot docker)           
11) uporabnik obišče http://212.101.137.114:8085/                               #Spletni vmesnik za uporabnika