import psycopg2
from config import load_config

def add_data(username, phone_number):
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT * FROM data WHERE number={phone_number} OR name=\'{username}\';")
                is_valid = cur.fetchone()
                if is_valid == None:
                    cur.execute(f"INSERT INTO data(name, number) VALUES(\'{username}\', {phone_number});")
                else:
                    print("Already exists!")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    username = input("Enter your name: ")
    phone_number = int(input("Enter your phone number: "))
    add_data(username, phone_number)