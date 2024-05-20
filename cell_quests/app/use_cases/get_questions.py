from core.database.connector import estabilish_connection


def get_questions():
    QUERY = (
        "SELECT q.*, o.letra_opcao as resposta "
        "FROM questoes as q "
        "INNER JOIN opcoes_resposta as o on q.questao_id = o.questao_id "
        "INNER JOIN respostas_corretas as r on r.questao_id = q.questao_id AND r.opcao_id = o.opcao_id"
    )

    conn = estabilish_connection()
    cursor = conn.cursor()

    cursor.execute(QUERY)

    return cursor.fetchall()
