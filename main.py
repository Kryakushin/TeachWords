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
from datetime import datetime
import os
import ast
import time
    
class MenuScreen(Screen):
    def __init__(self, **kw):
        super(MenuScreen, self).__init__(**kw)
        box = BoxLayout(orientation='vertical')
        box.add_widget(Button(text='Играть', on_press=lambda x:
                              set_screen('Krya')))
        box.add_widget(Button(text='Словарь',
                              on_press=lambda x: set_screen('add_food')))
        box.add_widget(Button(text='Контакты',
                              on_press=lambda x: set_screen('contacts')))
        self.add_widget(box)


class Krya(Screen):
    def addoperation(self, instence):
        o

    def __init__(self, **kw):
        super(Krya, self).__init__(**kw)
        #gl = GridLayout(cols=5, spacing=20, padding=30)

        self.add_widget(Button(background_normal=('img/A.png'), on_press=self.addoperation))
        self.add_widget(Button(background_normal=('img/B.png'), on_press=self.addoperation))
        self.add_widget(Button(background_normal=('img/C.png'), on_press=self.addoperation))
        self.add_widget(Button(background_normal=('img/D.png'), on_press=self.addoperation))
        self.add_widget(Button(background_normal=('img/E.png'), on_press=self.addoperation))

        self.add_widget(Button(background_normal=('img/F.png'), on_press=self.addoperation))
        self.add_widget(Button(background_normal=('img/G.png'), on_press=self.addoperation))
        self.add_widget(Button(background_normal=('img/H.png'), on_press=self.addoperation))
        self.add_widget(Button(background_normal=('img/I.png'), on_press=self.addoperation))
        self.add_widget(Button(background_normal=('img/J.png'), on_press=self.addoperation))

        self.add_widget(Button(background_normal=('img/K.png'), on_press=self.addoperation))
        self.add_widget(Button(background_normal=('img/L.png'), on_press=self.addoperation))
        self.add_widget(Button(background_normal=('img/M.png'), on_press=self.addoperation))
        self.add_widget(Button(background_normal=('img/N.png'), on_press=self.addoperation))
        self.add_widget(Button(background_normal=('img/O.png'), on_press=self.addoperation))

        self.add_widget(Button(background_normal=('img/P.png'), on_press=self.addoperation))
        self.add_widget(Button(background_normal=('img/Q.png'), on_press=self.addoperation))
        self.add_widget(Button(background_normal=('img/R.png'), on_press=self.addoperation))
        self.add_widget(Button(background_normal=('img/S.png'), on_press=self.addoperation))
        self.add_widget(Button(background_normal=('img/T.png'), on_press=self.addoperation))

        self.add_widget(Button(background_normal=('img/U.png'), on_press=self.addoperation))
        self.add_widget(Button(background_normal=('img/V.png'), on_press=self.addoperation))
        self.add_widget(Button(background_normal=('img/W.png'), on_press=self.addoperation))
        self.add_widget(Button(background_normal=('img/X.png'), on_press=self.addoperation))
        self.add_widget(Button(background_normal=('img/Y.png'), on_press=self.addoperation))

class AddFood(Screen):

    def buttonClicked(self, btn1):
        if not self.txt1.text:
            return
        self.app = App.get_running_app()
        self.app.user_data = ast.literal_eval(
            self.app.config.get('General', 'user_data'))
        self.app.user_data[self.txt1.text.encode('u8')] = int(time.time())

        self.app.config.set('General', 'user_data', self.app.user_data)
        self.app.config.write()

        text = "Последнее изученное слово:  " + self.txt1.text
        self.result.text = text
        self.txt1.text = ''

    def __init__(self, **kw):
        super(AddFood, self).__init__(**kw)
        box = BoxLayout(orientation='vertical')
        back_button = Button(text='< Назад в главное меню', on_press=lambda x:
                             set_screen('menu'), size_hint_y=None, height=dp(40))
        box.add_widget(back_button)
        self.txt1 = TextInput(text='', multiline=False, height=dp(40),
                              size_hint_y=None, hint_text="Слово")
        box.add_widget(self.txt1)
        btn1 = Button(text="Добавить изученное слово", size_hint_y=None, height=dp(40))
        btn1.bind(on_press=self.buttonClicked)
        box.add_widget(btn1)
        self.result = Label(text='')
        box.add_widget(self.result)
        self.add_widget(box)

class Contacts(Screen):
    def buttonClicked(self, btn1):
        if not self.txt1.text:
            return

    def __init__(self, **kw):
        super(Contacts, self).__init__(**kw)
        box = BoxLayout(orientation='vertical')
        back_button = Button(text='< Назад в главное меню', on_press=lambda x:
                             set_screen('menu'), size_hint_y=None, height=dp(40))
        box.add_widget(back_button)
        cont1 = Button(text="Крякушин Артем", size_hint_y=None, height=dp(40))
        cont1.bind(on_press=self.buttonClicked)
        box.add_widget(cont1)
        cont2 = Button(text="Вежеев Тимофей", size_hint_y=None, height=dp(40))
        cont2.bind(on_press=self.buttonClicked)
        box.add_widget(cont2)
        self.result = Label(text='')
        box.add_widget(self.result)
        self.add_widget(box)

def set_screen(name_screen):
    sm.current = name_screen


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(Krya(name='Krya'))
sm.add_widget(AddFood(name='add_food'))
sm.add_widget(Contacts(name='contacts'))


class TeachWordsApp(App):
    def __init__(self, **kvargs):
        super(TeachWordsApp, self).__init__(**kvargs)
        self.config = ConfigParser()

    def build_config(self, config):
        config.adddefaultsection('General')
        config.setdefault('General', 'user_data', '{}')

    def set_value_from_config(self):
        self.config.read(os.path.join(self.directory, '%(appname)s.ini'))
        self.user_data = ast.literal_eval(self.config.get(
            'General', 'user_data'))

    def get_application_config(self):
        return super(TeachWordsApp, self).get_application_config(
            '{}/%(appname)s.ini'.format(self.directory))

    def build(self):
        return sm


if __name__ == '__main__':
    TeachWordsApp().run()