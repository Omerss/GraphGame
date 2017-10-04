from kivy.uix.button import Button


class UniButton(Button):
    def __init__(self, text, func, **kwargs):
        super(UniButton, self).__init__(**kwargs)
        self.text = text
        self.on_press = func


class MultiButton(Button):
    funcs = None
    counter = 0
    moves = 10

    def __init__(self, img, funcs, button_num, game_layout = None, **kwargs):
        super(MultiButton, self).__init__(size_hint_x=None, width=game_layout.button_width, **kwargs)
        self.game_layout = game_layout
        self.background_normal = img
        self.funcs = funcs
        self.on_press = self.get_func
        self.num = button_num
        self.lst = self.game_layout.tablet_game.button_presses
        self.set_disabled = self.game_layout.set_button_status
        self.moves = self.game_layout.tablet_game.max_turns
        self.send_data = game_layout.tablet_game.send_info_from_screen

    def get_func(self):
        print len(self.lst)
        self.set_disabled(True)
        if len(self.lst) >= self.moves:
            self.game_layout.tablet_game.end_game()
        else:
            f = self.counter % len(self.funcs)
            self.funcs[f]()
            self.counter += 1
            self.lst.append(self.num)
            self.send_data()
            if len(self.lst) == self.moves:
                self.game_layout.end_game()
            self.set_disabled(False)
