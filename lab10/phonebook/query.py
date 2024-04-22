import psycopg2
from config import load_config

def query():
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM data;")
                result = cur.fetchall()
                print("All data")
                for res in result:
                    print(res)

                cur.execute(f"SELECT * FROM data ORDER BY number;")
                result = cur.fetchall()
                print("All data by ordering phone")
                for res in result:
                    print(res)
                
                cur.execute(f"SELECT * FROM data WHERE name LIKE \'N%\';")
                result = cur.fetchall()
                print("Users name starts with letter \'N\'")
                for res in result:
                    print(res)

    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    query()