import mysql.connector

# conncet() -funktio palauttaa tietokantayhteyden, joka sijoitetaan muuttujaan
connection = mysql.connector.connect(
         host='127.0.0.1', # localhost
         port= 3306,
         database='flight_game',
         user='mikael',
         password='6499',
         autocommit=True,
         collation = 'utf8mb4_general_ci'
         )
#print(connection)

# luodaan osoitin ja sijoitetaan muuttujaan
cursor = connection.cursor()
# ajetaan SQL-kielinen kysely osoittimen avulla
sql = ("SELECT name, iso_country, continent FROM country")
cursor.execute(sql)
# fetchone hakee rivi kerrallaan, palauttaa monikon
#result = cursor.fetchone()
#print(result)
# fetchmany palauttaa halutun määrän rivejä kerrallaan, palauttaa listan
result = cursor.fetchmany(3)
print(result)
print(f"Tulosrivejä käyty läpi (kursorin sijainti): {cursor.rowcount}")
#print(result)
#result = cursor.fetchmany(3)
#print(result)
# fetchall palauttaa kaikki (loput) rivit listana
rows = cursor.fetchall()
print(rows)
print(result)
# tuloslista käsitellään toistorakenteella
for row in rows:
    print(f"{row[1]}, Maakoodi: {row[2]}, maanosa: {row[0]}")
if cursor.rowcount > 0:
    print(f"Tulosrivejä yhteensä: {cursor.rowcount}")
else:
    print("Ei tuloksia.")
