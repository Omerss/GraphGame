from kivy.uix.button import Button


class EndButton(Button):
    def __init__(self, func, **kwargs):
        super(EndButton, self).__init__(**kwargs)
        self.text = 'End Game.'
        self.on_press = func


class MultiButton(Button):
    funcs = None
    counter = 0

    def __init__(self, img, funcs, button_num, game_layout=None, **kwargs):
        super(MultiButton, self).__init__(size_hint_x=None, width=game_layout.button_width, **kwargs)
        self.game_layout = game_layout
        self.background_normal = img
        self.funcs = funcs
        self.num = button_num
        self.lst = self.game_layout.tablet_game.button_presses

    def on_press(self):
        if self.game_layout.next_func is None:
            self.game_layout.disable_buttons()
            f = self.counter % len(self.funcs)
            self.game_layout.next_func = self.funcs[f]
            self.counter += 1
            self.lst.append(self.num)
