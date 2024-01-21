from Tela_Inicial import TelaInicial
from Tela_Login import TelaLogin
from Tela_Cadastro import TelaCadastro
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp


class MyApp(MDApp):
    def build(self):
        # Cria um gerenciador de telas
        screen_manager = ScreenManager()

        # Adiciona as telas ao gerenciador
        screen_manager.add_widget(TelaInicial(name="tela_inicial"))
        screen_manager.add_widget(TelaLogin(name="tela_login"))
        screen_manager.add_widget(TelaCadastro(name="tela_cadastro"))

        return screen_manager

    def print_credentials(self, login, senha):
        print(f"Login: {login}, Senha: {senha}")


# Executa a aplicação
if __name__ == "__main__":
    MyApp().run()