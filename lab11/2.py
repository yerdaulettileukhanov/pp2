import psycopg2
from config import load_config


def add_part(name, number):
    """ Add a new part """
    # read database configuration
    params = load_config()
    
    try:
        # connect to the PostgreSQL database
        with psycopg2.connect(**params) as conn:
            with conn.cursor() as cur:
                # call a stored procedure
                cur.execute(f'SELECT * FROM data WHERE name = \'{name}\'')
                result = cur.fetchone()
                if result == None:
                    cur.execute('CALL add_data(%s,%s)', (name, number))

            # commit the transaction
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    add_part('Bekzhn', 7007890)


    
"""CREATE OR REPLACE PROCEDURE add_data(
	pname varchar,
	pnumber integer
) 
AS $$
DECLARE
	name VARCHAR;
	number INT;
BEGIN
	-- insert into the parts table
	INSERT INTO data(name, number) 
	VALUES(pname, pnumber);
END;
$$
LANGUAGE PLPGSQL;"""