from core.database.connector import estabilish_connection


def get_scoreboard(id: int) -> list:
    QUERY = (
        "SELECT j.id, j.nome, MAX(p.pontuacao) "
        "FROM pontuacoes as p, jogadores as j "
        "WHERE p.jogador_id = j.id "
        "GROUP BY j.id"
    )

    conn = estabilish_connection()
    cursor = conn.cursor()

    cursor.execute(QUERY)

    scores = cursor.fetchall()

    return [{"id": id, "nome": nome, "pontuacao": score} for id, nome, score in scores]
