import mysql.connector
from collections import Counter

connection = mysql.connector.connect(
         host='127.0.0.1', # localhost
         port= 3306,
         database='flight_game',
         user='mikael',
         password='6499',
         autocommit=True,
         collation = 'utf8mb4_general_ci'
         )

def fetch_airport_types_by_country(country_code):
    sql = (f"SELECT type"
           f" FROM airport WHERE iso_country = '{country_code}'")
    cursor = connection.cursor()
    cursor.execute(sql)
    result_row = cursor.fetchall()
    return [row[0] for row in result_row]

user_input = input("Anna maakoodi: ")
airport_types = fetch_airport_types_by_country(user_input)

if airport_types:
    type_counter = Counter(airport_types)
    print(f"Lentokenttien lukumäärät maassa {user_input}: ")
    for airport_type, count in type_counter.items():
        print(f"{airport_type}: {count} kpl")
else:
    print("Lentokenttää ei löydetty annetulla koodilla {user_input}.")