import kivy
kivy.require('1.9.1')

from kivy.uix.button import Button


class UniButton(Button):
    def __init__(self,img,func,**kwargs):
        super(UniButton, self).__init__(**kwargs)
        self.background_normal = img
        self.on_press = func


class MultiButton(Button):
    funcs = None
    counter = 0
    active = True

    def __init__(self, img, funcs, signal, button_lst, button_num,  **kwargs):
        super(MultiButton,self).__init__(**kwargs)
        self.background_normal = img

        self.funcs = funcs
        self.on_press = self.get_func
        self.signal = signal
        self.num = button_num
        self.lst = button_lst


    def get_func(self):
        if(self.active):
            f = self.counter % len(self.funcs)
            self.funcs[f]()
            self.counter += 1
            self.lst.append(self.num)
            self.signal.set()

