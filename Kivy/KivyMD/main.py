from kivymd.app import MDApp
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDRaisedButton
from kivy.lang import Builder

KV = '''
FloatLayout:
    MDRaisedButton:
        text: 'Clica em mim!'
'''

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MyApp().run()