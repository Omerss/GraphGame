import kivy
kivy.require('1.9.1')

from kivy.uix.button import Button

class GraphButton(Button):

    def __init__(self,img,func,**kwargs):
        super(GraphButton,self).__init__(**kwargs)
        self.background_normal = img
        self.on_press = func

