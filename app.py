from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from functions import *
from kivy.uix.screenmanager import ScreenManager, Screen


Builder.load_file('app.kv')

class AppWindow(Screen):
    pass

class PesquisarWindow(Screen):
    pass

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
