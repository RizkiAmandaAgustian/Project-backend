import psycopg2

koneksidatabase = psycopg2.connect(
    host = 'localhost',
    port = 5432,
    database = 'PROJECT_DLMT',
    user = 'postgres',
    password = 'postgres'
)