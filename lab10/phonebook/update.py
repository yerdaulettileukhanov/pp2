import psycopg2
from config import load_config

def update(change_new, change_old):
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                if isinstance(change_old, str):
                    cur.execute(f"UPDATE data SET name = \'{change_new}\' WHERE name=\'{change_old}\';")
                else:
                    cur.execute(f"UPDATE data SET number = {change_new} WHERE number={change_old};")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    data_to_change = input("Enter 1 if you want to change name\nEnter 2 if you want to change phone number\nWaiting: ")
    if data_to_change == "1":
        old_name = input("Old name to change: ")
        new_name = input("Okay, enter the new name: ")
        update(new_name, old_name)
    if data_to_change == "2":
        old_phone_number = int(input("Old phone number to change: "))
        new_phone_number = int(input("Okay, enter the new phone number: "))
        update(new_phone_number, old_phone_number)