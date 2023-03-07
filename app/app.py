from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from functionsDB import *
from objects import Pecas
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.recycleview import RecycleView
from kivy.core.window import Window

Window.size = (1200, 800)


Builder.load_file('kv/MenuWindow.kv')
Builder.load_file('kv/MostrarWindow.kv')
Builder.load_file('kv/PesquisarWindow.kv')
Builder.load_file('kv/FaltosasWindow.kv')
Builder.load_file('kv/Classes.kv')


class AppWindow(Screen):
    pass

class PesquisarWindow(Screen):
    pass

class RV(RecycleView):
    def __init__(self, **kwargs):
        conexao = connect_db()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM telas")
        super(RV, self).__init__(**kwargs)
        self.data = [{'col1': 'ID',
        'col2': 'MARCA',
         'col3': 'MODELO',
          'col4': 'COR',
          'col5': 'QTD.',
           'col6': 'IMP.',
            'col7': 'CAIXA',}]
        self.data = self.data + [{'col1': str(Pecas.id),
         'col2': str(Pecas.marca),
          'col3': str(Pecas.modelo),
           'col4': str(Pecas.cor),
            'col5': str(Pecas.quantidade),
             'col6': str(Pecas.grau_de_importancia),
              'col7': str(Pecas.caixa)}
               for Pecas.id,
                Pecas.marca,
                 Pecas.modelo,
                  Pecas.cor,
                   Pecas.quantidade,
                    Pecas.grau_de_importancia,
                     Pecas.caixa in cursor]

class RVPesquisar(RecycleView):                 
     def pesquisar(self,pesquisa):
        print(pesquisa)   
        def __init__(self, pesquisa, **kwargs):
            pesquisa = ""
            super(RVPesquisar, self).__init__(**kwargs)
            self.data = [{'colp1': 'ID',
            'colp2': 'MARCA',
            'colp3': 'MODELO',
            'colp4': 'COR',
            'colp5': 'QTD.',
            'colp6': 'IMP.',
                'colp7': 'CAIXA',}]
            conexao = connect_db() 
            cursor = conexao.cursor()
            cursor.execute("Select * from telas where modelo='"+pesquisa+"'")
            self.data = self.data + [{'col1': str(Pecas.id),
            'col2': str(Pecas.marca),
            'col3': str(Pecas.modelo),
            'col4': str(Pecas.cor),
                'col5': str(Pecas.quantidade),
                'col6': str(Pecas.grau_de_importancia),
                'col7': str(Pecas.caixa)}
                for Pecas.id,
                    Pecas.marca,
                    Pecas.modelo,
                    Pecas.cor,
                    Pecas.quantidade,
                        Pecas.grau_de_importancia,
                        Pecas.caixa in cursor]
        

class MostrarWindow(Screen):
    pass

class FaltosasWindow(Screen):
    pass

class Screens(ScreenManager):
    def pesquisar(self,pesquisa):
        RVPesquisar.pesquisar(self,pesquisa)
        

class Screens3(App):
    def build(self):
        return Screens()

    

if __name__=='__main__':
    Screens3().run()
