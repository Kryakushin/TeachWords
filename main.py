from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.recycleview import RecycleView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.config import ConfigParser
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.metrics import dp

class TeachWordsApp(App):
    def __init__(self, **kvargs):
        super(TeachWordsApp, self).__init__(**kvargs)

    def build(self):
        return sm

class MenuScreen(Screen):
    def __init__(self, **kw):
        super(MenuScreen, self).__init__(**kw)

        box = BoxLayout(orientation='vertical')

        def xxx():
            
            Krya().run()

        box.add_widget(Button(text='Играть', on_press=lambda x: xxx()))
        self.add_widget(box)

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))

def set_screen(name_screen):
    sm.current = name_screen

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))

class Krya(App):
    def addoperation(self, instence):
        o

    def build(self):
        gl = GridLayout(cols=5, spacing=20, padding=30)

        gl.add_widget(Button(text=('A'), on_press=self.addoperation))
        gl.add_widget(Button(text=('Б'), on_press=self.addoperation))
        gl.add_widget(Button(text=('В'), on_press=self.addoperation))
        gl.add_widget(Button(text=('Г'), on_press=self.addoperation))
        gl.add_widget(Button(text=('Д'), on_press=self.addoperation))

        gl.add_widget(Button(text=('И'), on_press=self.addoperation))
        gl.add_widget(Button(text=('Й'), on_press=self.addoperation))
        gl.add_widget(Button(text=('К'), on_press=self.addoperation))
        gl.add_widget(Button(text=('Л'), on_press=self.addoperation))
        gl.add_widget(Button(text=('М'), on_press=self.addoperation))

        gl.add_widget(Button(text=('О'), on_press=self.addoperation))
        gl.add_widget(Button(text=('П'), on_press=self.addoperation))
        gl.add_widget(Button(text=('Р'), on_press=self.addoperation))
        gl.add_widget(Button(text=('С'), on_press=self.addoperation))
        gl.add_widget(Button(text=('Т'), on_press=self.addoperation))

        gl.add_widget(Button(text=('У'), on_press=self.addoperation))
        gl.add_widget(Button(text=('Ф'), on_press=self.addoperation))
        gl.add_widget(Button(text=('Х'), on_press=self.addoperation))
        gl.add_widget(Button(text=('Ц'), on_press=self.addoperation))
        gl.add_widget(Button(text=('Ч'), on_press=self.addoperation))

        gl.add_widget(Button(text=('Ш'), on_press=self.addoperation))
        gl.add_widget(Button(text=('Щ'), on_press=self.addoperation))
        gl.add_widget(Button(text=('Ъ'), on_press=self.addoperation))
        gl.add_widget(Button(text=('Ы'), on_press=self.addoperation))
        gl.add_widget(Button(text=('Ь'), on_press=self.addoperation))

        return gl

if __name__ == '__main__':
    TeachWordsApp().run()