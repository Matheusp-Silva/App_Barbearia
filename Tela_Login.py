from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField

TelaLogin_kv = """
Screen:
    name: "tela_login"

    MDTextField:
        id: login
        hint_text: "Login"
        size_hint: (0.8, 0.1)
        pos_hint: {"center_x": 0.5, "center_y": 0.7}

    MDTextField:
        id: senha
        hint_text: "Senha"
        size_hint: (0.8, 0.1)
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        password: True

    MDRaisedButton:
        text: "Conectar"
        size_hint: (0.6, 0.1)
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
"""


class TelaLogin(Screen):
    def __init__(self, **kwargs):
        super(TelaLogin, self).__init__(**kwargs)
        self.add_widget(Builder.load_string(TelaLogin_kv))

