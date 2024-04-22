import psycopg2
from config import load_config

def csv():
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("COPY data(name, number) FROM \'D:\pp2\lab10\phonebook\data.csv\' DELIMITER \',\' CSV HEADER;")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    csv()