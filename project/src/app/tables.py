import psycopg2
from psycopg2 import sql

def create_tables():
    #database_url = "postgresql+psycopg2://admin:admin@postgres:5432/testDB_Presley"
    #database_url = "postgresql+psycopg2://admin:admin@postgres:5432/testDB_Presley"

    try:
        connection = psycopg2.connect(dbname="testdb_presley",user="admin",password="admin",host="127.0.0.1")
        cursor = connection.cursor()

        # Создание таблицы пользователей
        create_users_table_query = """
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(255) NOT NULL,
                language VARCHAR(2) NOT NULL
            );
        """
        cursor.execute(create_users_table_query)

        # Создание таблицы достижений
        create_achievements_table_query = """
            CREATE TABLE IF NOT EXISTS achievements (
                id SERIAL PRIMARY KEY,
                userid INTEGER REFERENCES users(id) NOT NULL,
                achievement_name VARCHAR(255) NOT NULL,
                points INTEGER NOT NULL,
                description TEXT
            );
        """
        cursor.execute(create_achievements_table_query)

        connection.commit()
        print("Tables created successfully!")

    except psycopg2.Error as e:
        print("Error while connecting to PostgreSQL:", e)

    finally:
        if connection:
            cursor.close()
            connection.close()

create_tables()