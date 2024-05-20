import pdb
from core.database.connector import estabilish_connection


def authenticate(username: str, password: str) -> bool:
    QUERY = (
        'SELECT * FROM jogadores WHERE login = "{username}" AND senha = "{password}"'
    ).format(username=username, password=password)

    conn = estabilish_connection()
    cursor = conn.cursor()

    cursor.execute(QUERY)

    users = cursor.fetchall()

    return len(users) > 0
