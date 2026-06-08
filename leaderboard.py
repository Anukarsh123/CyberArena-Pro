import sqlite3

conn = sqlite3.connect("game.db")

cursor = conn.cursor()

def get_top_scores():

    cursor.execute("""
    SELECT score
    FROM scores
    ORDER BY score DESC
    LIMIT 10
    """)

    return cursor.fetchall()
