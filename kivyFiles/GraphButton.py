import kivy
kivy.require('1.9.1')

from kivy.uix.button import Button

class uniButton(Button):

    def __init__(self,img,func,**kwargs):
        super(uniButton,self).__init__(**kwargs)
        self.background_normal = img
        self.on_press = func

class multiButton(Button):
    funcs = []
    counter = 0

    def __init__(self,img,funcs,**kwargs):
        super(multiButton,self).__init__(**kwargs)
        self.background_normal = img
        self.funcs = funcs
        self.on_press = self.get_func

    def get_func(self):
        f = self.counter%len(self.funcs)
        self.funcs[f]()
        self.counter += 1
