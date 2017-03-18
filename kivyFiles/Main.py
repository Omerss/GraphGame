import kivy
kivy.require('1.9.1')

from kivy.app import App
from GraphLayout import GraphLayout


class GraphGameApp(App):
    def build(self):
        layout = GraphLayout()
        return layout

if __name__ == "__main__":
    GraphGameApp().run()