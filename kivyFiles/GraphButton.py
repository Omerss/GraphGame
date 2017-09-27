from kivy.uix.button import Button


class UniButton(Button):
    def __init__(self, img, func, **kwargs):
        super(UniButton, self).__init__(**kwargs)
        self.background_normal = img
        self.on_press = func


class MultiButton(Button):
    funcs = None
    counter = 0
    moves = 10

    def __init__(self, img, funcs, button_lst, button_num, button_width, updater_func, set_disabled, max_moves,
                 end_game, **kwargs):
        super(MultiButton, self).__init__(size_hint_x=None, width=button_width, **kwargs)
        self.background_normal = img
        self.funcs = funcs
        self.on_press = self.get_func
        self.num = button_num
        self.lst = button_lst
        self.send_screen_info = updater_func
        self.set_disabled = set_disabled
        self.moves = max_moves
        self.end_game = end_game

    def get_func(self):
        self.set_disabled(True)
        if len(self.lst) >= self.moves:
            self.end_game()
        else:
            f = self.counter % len(self.funcs)
            self.funcs[f]()
            self.counter += 1
            self.lst.append(self.num)
            self.send_screen_info()
            self.set_disabled(False)

