from kivy.app import App
from TaoNode import taonode
import sqlite3
class MainApp(App):
    connection = None
    cursor = None
    def on_start(self):
        self.connection = sqlite3.connect("Node.db")
        self.cursor=self.connection.cursor()


    pass
MainApp().run()