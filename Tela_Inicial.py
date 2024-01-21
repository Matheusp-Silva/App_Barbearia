from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivymd.uix.button import MDRaisedButton
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp

TelaInicial_kv = """
<TelaInicial>:
    orientation: "vertical"

    Image:
        source: "./images/Barber_Shop_Logo.png"
        allow_stretch: True
        keep_ratio: False

    MDRaisedButton:
        text: "Entrar"
        size_hint: (0.8, 0.1)
        on_release: app.root.current = "tela_login"

    MDRaisedButton:
        text: "Cadastrar"
        size_hint: (0.8, 0.1)
        on_release: app.root.current = "tela_cadastro"
        
"""


class TelaInicial(Screen, BoxLayout):
    def __init__(self, **kwargs):

        super(TelaInicial, self).__init__(**kwargs)
        self.orientation = "vertical"
        self.add_widget(Image(source="./images/Barber_Shop_Logo.png", allow_stretch=True, keep_ratio=False))
        self.add_widget(MDRaisedButton(text="Entrar", pos_hint={"center_x": 0.5, "center_y": 0.7}, on_release=self.go_to_login))
        self.add_widget(MDRaisedButton(text="Cadastrar", pos_hint={"center_x": 0.5, "center_y": 0.3}, on_release=self.go_to_cadastro))

    def go_to_login(self, *args):
        app = MDApp.get_running_app()
        app.root.current = "tela_login"

    def go_to_cadastro(self, *args):
        app = MDApp.get_running_app()
        app.root.current = "tela_cadastro"
