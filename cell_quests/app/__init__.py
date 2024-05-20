import pdb
import os
import random

from app.use_cases import authenticate, get_questions, get_alternatives
from core.window import end_window, start_window, dpg

hits = 0


def authenticate_callback():
    username = dpg.get_value("username")
    password = dpg.get_value("password")

    if authenticate(username, password):
        # ! TROCANDO DE JANELA
        dpg.hide_item("initial_window")
        dpg.set_primary_window("initial_window", False)

        dpg.set_primary_window("game_window", True)
        dpg.show_item("game_window")
    else:
        raise ValueError("Usuário ou senha inválidos")


def alternative_callback(_sender, _app_data, hit: bool):
    pdb.set_trace()
    pass


def run():
    start_window()

    # JANELA DO JOGO (USUÁRIO JÁ AUTENTICADO)
    with dpg.window(label=os.getenv("APP_NAME"), tag="game_window", show=False):
        questions = get_questions()

        # seleciona questão aleatória e exibe na tela
        random_number = random.choice(range(len(questions)))
        selected_question = questions[random_number]

        question_id, texto, _, resposta = selected_question
        alternatives = get_alternatives(question_id)  # type: ignore

        dpg.add_text(f"Questão {question_id}")
        dpg.add_text(str(texto))

        for alternative, label in alternatives.items():
            dpg.add_button(
                label=f"{alternative.upper()} - {label}",
                user_data=alternative == resposta,
                callback=alternative_callback,
            )

    # JANELA DE LOGIN
    with dpg.window(label=os.getenv("APP_NAME"), tag="initial_window"):
        dpg.set_primary_window("initial_window", True)

        dpg.add_input_text(
            label="string",
            hint="nome de usuário",
            tag="username",
        )
        dpg.add_input_text(
            label="string",
            hint="senha",
            tag="password",
            password=True,
        )
        dpg.add_button(label="Entrar", callback=authenticate_callback)

    end_window()
