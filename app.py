from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_file('app.kv')

class AppWindow(BoxLayout):
    def __init__(self):
        super().__init__()

class AppPrincipal(App):
    def build(self):
        return AppWindow()

if __name__=='__main__':
    AppPrincipal().run()