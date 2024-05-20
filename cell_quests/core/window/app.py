import dearpygui.dearpygui as dpg


def start_window():
    dpg.create_context()
    dpg.create_viewport(title="Cell Quests", width=800, height=600)
    dpg.setup_dearpygui()


def end_window():
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
