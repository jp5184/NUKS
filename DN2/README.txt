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


Navodila:
1) source .venv/bin/activate                                       #Zagon virtualnega okolja
2) pip install -r requirements.txt                                 #Namestitev potrebnih python modulov
3) python3 -m uvicorn main:app --host 0.0.0.0                      #Zagon API strežnika
4) uporabnik obišče http://195.47.197.43/docs                      #Spletni vmesnik za uporabnika