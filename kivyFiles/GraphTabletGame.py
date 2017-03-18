import time

from GraphLayout import GraphLayout
from kivy.app import App

class GraphTabletGame(App):

    def build(self):
        self.layout = GraphLayout()
        return self.layout

    def press_button(self,num):
        if(num == 1):
            self.layout.button1_func
        elif (num == 2):
            self.layout.button2_func
        elif (num == 3):
            self.layout.button3_func
        elif (num == 4):
            self.layout.button4_func

    def read_data_from_window(self):
        pass
        screen_edges = self.layout.dim
        displayed_nodes = []

