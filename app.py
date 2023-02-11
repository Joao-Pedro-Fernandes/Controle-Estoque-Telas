from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from functions import *
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.recycleview import RecycleView

conexao = connect_db()
cursor = conexao.cursor()
cursor.execute("SELECT * FROM telas")
Builder.load_file('app.kv')

class AppWindow(Screen):
    pass

class PesquisarWindow(Screen):
    pass


class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'col1': str(Pecas.id),
         'col2': str(Pecas.marca),
          'col3': str(Pecas.modelo),
           'col4': str(Pecas.cor),
            'col5': str(Pecas.quantidade),
             'col6': str(Pecas.grau_de_importancia),
              'col7': str(Pecas.caixa)}
               for Pecas.id, Pecas.marca, Pecas.modelo, Pecas.cor, Pecas.quantidade, Pecas.grau_de_importancia, Pecas.caixa in cursor]


class MostrarWindow(Screen):
    pass

class FaltosasWindow(Screen):
    pass

class Screens(ScreenManager):
    pass

class Screens3(App):
    def build(self):
        return Screens()

if __name__=='__main__':
    Screens3().run()
