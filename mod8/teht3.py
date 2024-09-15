import mysql.connector
from geopy.distance import geodesic

connection = mysql.connector.connect(
         host='127.0.0.1', # localhost
         port= 3306,
         database='flight_game',
         user='mikael',
         password='6499',
         autocommit=True,
         collation = 'utf8mb4_general_ci'
         )

def fetch_airport_coordinates(icao_code):
    sql = (f"SELECT latitude_deg, longitude_deg"
           f" FROM airport WHERE ident = '{icao_code}'")
    cursor = connection.cursor()
    cursor.execute(sql)
    result_row = cursor.fetchone()
    if result_row:
        return (float(result_row[0]), float(result_row[1]))
    return None

icao_code_1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ")
icao_code_2 = input("Anna toisen lentokentän ICAO-koodi: ")

coords_1 = fetch_airport_coordinates(icao_code_1)
coords_2 = fetch_airport_coordinates(icao_code_2)

if coords_1 and coords_2:
    distance_km = geodesic(coords_1, coords_2).kilometers
    print(f"Lentokenttien {icao_code_1} ja {icao_code_2} välinen etäisyys on {distance_km:.2f} kilometriä.")
else:
    if not coords_1:
        print(f"Lentokenttää ICAO-koodilla {icao_code_1} ei löytynyt.")
    if not coords_2:
        print(f"Lentokenttää ICAO-koodilla {icao_code_2} ei löytynyt.")