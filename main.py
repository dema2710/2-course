import psycopg2

PGHOST = "ep-square-hill-a23rxcu8-pooler.eu-central-1.aws.neon.tech"
PGDATABASE = "neondb"
PGUSER = "neondb_owner"
PGPASSWORD = "npg_hTqeb9Za1VLi"
PORT = 5432

with psycopg2.connect(
    dbname=PGDATABASE, user=PGUSER, password=PGPASSWORD, host=PGHOST, port=PORT
) as connection:
    with connection.cursor() as cursor:
        query = """
                    CREATE TABLE IF NOT EXISTS brand (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(50) UNIQUE NOT NULL
                    )
                """
        cursor.execute(query)

        query = """
                    CREATE TABLE IF NOT EXISTS customer (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(50) NOT NULL
                    );

                    CREATE TABLE IF NOT EXISTS car (
                        id SERIAL PRIMARY KEY,
                        model VARCHAR(50) NOT NULL,
                        cost INTEGER,
                        brand_id INTEGER REFERENCES brand(id),
                        customer_id INTEGER REFERENCES customer(id)
                    );
                """
        cursor.execute(query)
