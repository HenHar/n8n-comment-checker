import os
import psycopg2
from dotenv import load_dotenv


load_dotenv()
# Database configuration
DATABASE_URL = os.getenv("DB_URL")
conn = psycopg2.connect(DATABASE_URL)


def create_comments_table(table_name: str):
    try:
        cur = conn.cursor()
        # SQL command to create the table
        query = f'''
                       CREATE TABLE IF NOT EXISTS {table_name} (
                    id SERIAL PRIMARY KEY,
                    content TEXT NOT NULL,
                    date TIMESTAMPTZ NOT NULL DEFAULT NOW()
                        );
                        '''
        cur.execute(query)
        conn.commit()
        cur.close()
        print("Table created successfully.")
    except Exception as e:
        print(f"Error creating table: {e}")

def query_comments():
    cur = conn.cursor()
    cur.execute("SELECT * FROM comments;")
    rows = cur.fetchall()
    return rows
