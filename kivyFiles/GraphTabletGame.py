import time

from GraphLayout import GraphLayout
from kivy.app import App

class GraphTabletGame(App):

    def build(self):
        layout = GraphLayout()
        return layout

    def press_button(self,num):
        pass

    def read_data_from_window(self):
        pass




a = GraphTabletGame()
a.run()
while True:
    time.sleep(5000)