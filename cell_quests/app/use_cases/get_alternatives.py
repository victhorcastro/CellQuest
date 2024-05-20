from core.database.connector import estabilish_connection


def get_alternatives(id: int) -> dict:
    QUERY = (
        "SELECT opcao_id, questao_id, texto_opcao, letra_opcao "
        "FROM opcoes_resposta "
        f"WHERE questao_id = {id}"
    )

    conn = estabilish_connection()
    cursor = conn.cursor()

    cursor.execute(QUERY)

    alternatives = cursor.fetchall()
    formatted_response = {}

    for _, _, text, letter in alternatives:
        formatted_response[str(letter)] = text

    return formatted_response
