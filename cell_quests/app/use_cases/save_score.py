from core.database.connector import estabilish_connection


def save_score(current_player_id: int, score: int):
    QUERY = (
        "INSERT INTO pontuacoes (jogador_id, pontuacao) VALUES "
        f"({current_player_id}, {score})"
    )

    conn = estabilish_connection()
    cursor = conn.cursor()

    cursor.execute(QUERY)
