import psycopg2
from config import load_config

def delete(del_data):
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                if isinstance(del_data, str):
                    cur.execute(f"DELETE FROM data WHERE name=\'{del_data}\';")
                else:
                    cur.execute(f"DELETE FROM data WHERE number={del_data};")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    del_data = input("Enter 1 if you want to delete by name\nEnter 2 if you want to delete by phone number\nWaiting: ")
    if del_data == "1":
        del_name = input("Name to delete: ")
        delete(del_name)
    if del_data == "2":
        del_phone = int(input("Phone to delete: "))
        delete(del_phone)