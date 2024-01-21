from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.textfield import MDTextField

# Define as strings de identificação das telas
TelaInicial = "tela_inicial"
Tela1 = "tela1"
TelaCadastro = "tela_cadastro"
TelaLogin = "tela_login"

# Define o layout da Tela Inicial
tela_inicial_layout = f"""
Screen:
    name: "{TelaInicial}"

    MDRaisedButton:
        text: "Entrar"
        pos_hint: {{"center_x": 0.5, "center_y": 0.7}}
        on_release: app.root.current = "{TelaLogin}"

    MDRaisedButton:
        text: "Cadastrar"
        pos_hint: {{"center_x": 0.5, "center_y": 0.3}}
        on_release: app.root.current = "{TelaCadastro}"
"""

# Define o layout da Tela de Login
tela_login_layout = f"""
Screen:
    name: "{TelaLogin}"

    MDTextField:
        id: login
        hint_text: "Login"
        pos_hint: {{"center_x": 0.5, "center_y": 0.7}}
        size_hint_x: None
        width: "300dp"

    MDTextField:
        id: senha
        hint_text: "Senha"
        pos_hint: {{"center_x": 0.5, "center_y": 0.5}}
        size_hint_x: None
        width: "300dp"
        password: True

    MDRaisedButton:
        text: "Conectar"
        pos_hint: {{"center_x": 0.5, "center_y": 0.3}}
        on_release: app.print_credentials(login.text, senha.text)
"""

# Define o layout da Tela 1
tela1_layout = f"""
Screen:
    name: "{Tela1}"

    MDRaisedButton:
        text: "Ir para Tela 2"
        pos_hint: {{"center_x": 0.5, "center_y": 0.7}}
        on_release: app.root.current = "{Tela1}"

    MDRaisedButton:
        text: "Outro Botão Tela 1"
        pos_hint: {{"center_x": 0.5, "center_y": 0.3}}
        on_release: print("Botão Tela 1 pressionado")
"""

# Define o layout da Tela de Cadastro
tela_cadastro_layout = f"""
Screen:
    name: "{TelaCadastro}"

    MDRaisedButton:
        text: "Voltar para Tela Inicial"
        pos_hint: {{"center_x": 0.5, "center_y": 0.7}}
        on_release: app.root.current = "{TelaInicial}"

    MDRaisedButton:
        text: "Outro Botão Cadastro"
        pos_hint: {{"center_x": 0.5, "center_y": 0.3}}
        on_release: print("Botão Cadastro pressionado")
"""

# Cria a classe da aplicação
class MyApp(MDApp):
    def build(self):
        # Cria um gerenciador de telas
        screen_manager = ScreenManager()

        # Cria as telas e adiciona ao gerenciador de telas
        tela_inicial = Builder.load_string(tela_inicial_layout)
        tela_login = Builder.load_string(tela_login_layout)
        screen1 = Builder.load_string(tela1_layout)
        tela_cadastro = Builder.load_string(tela_cadastro_layout)

        screen_manager.add_widget(tela_inicial)
        screen_manager.add_widget(tela_login)
        screen_manager.add_widget(screen1)
        screen_manager.add_widget(tela_cadastro)

        return screen_manager

    def print_credentials(self, login, senha):
        print(f"Login: {login}, Senha: {senha}")

# Executa a aplicação
if __name__ == "__main__":
    MyApp().run()
