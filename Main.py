import kivy
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget

def callback1(instance):
    print('button1 is being pressed')
def callback2(instance):
    print('button2 is being pressed')
def callback3(instance):
    print('button3 is being pressed')
def callback4(instance):
    print('button4 is being pressed')

class myLayout(FloatLayout):
    def __init__(self, **kwargs):
        super(myLayout, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical',size_hint=(0.1, 1), padding=10, spacing=20)
        button1 = Button(background_normal='button1.png')
        button1.bind(on_press =callback1)
        button2 = Button(background_normal='button2.jpg')
        button2.bind(on_press=callback2)
        button3 = Button(background_normal='button3.jpg')
        button3.bind(on_press=callback3)
        button4 = Button(background_normal='button4.jpg')
        button4.bind(on_press=callback4)
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)
        layout.add_widget(button4)
        self.add_widget(layout)

class SampleApp(App):
    def build(self):
        lay = myLayout()
        return lay


if __name__ == "__main__":
    SampleApp().run()



