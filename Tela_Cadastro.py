from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton

TelaCadastro_kv = """
Screen:
    name: "tela_cadastro"

    MDRaisedButton:
        text: "Voltar para Tela Inicial"
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        on_release: app.root.current = "tela_inicial"

    MDRaisedButton:
        text: "Outro Botão Cadastro"
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        on_release: print("Botão Cadastro pressionado")
"""

class TelaCadastro(Screen):
    def __init__(self, **kwargs):
        super(TelaCadastro, self).__init__(**kwargs)
        self.add_widget(Builder.load_string(TelaCadastro_kv))