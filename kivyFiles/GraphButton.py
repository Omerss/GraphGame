from kivy.uix.button import Button
from time import sleep


class TextButton(Button):
    def __init__(self, text, func,**kwargs):
        super(TextButton, self).__init__(**kwargs)
        self.text = text
        self.on_press = func


class MultiButton(Button):
    funcs = None
    counter = 0
    moves = 10

    def __init__(self, img, funcs, button_num, game_layout=None, **kwargs):
        super(MultiButton, self).__init__(size_hint_x=None, width=game_layout.button_width, **kwargs)
        self.game_layout = game_layout
        self.background_normal = img
        self.funcs = funcs
        #self.on_press = self.get_func
        self.num = button_num
        self.lst = self.game_layout.tablet_game.button_presses
        self.set_disabled = self.game_layout.set_button_status
        self.moves = self.game_layout.tablet_game.max_turns
        self.send_data = game_layout.tablet_game.send_info_from_screen

    def on_press1(self):
        # self.game_layout.set_button_status(True)
        self.disabled = True
        f = self.counter % len(self.funcs)
        self.funcs[f]()
        self.counter += 1
        self.lst.append(self.num)
        self.send_data()
        if self.game_layout.move_counter == self.moves:
            self.game_layout.end_game()
        self.disabled = False

    def on_press(self):
        if self.game_layout.next_func is None:
            self.game_layout.disable_buttons()
            f = self.counter % len(self.funcs)
            self.game_layout.next_func = self.funcs[f]
            self.counter += 1
            self.lst.append(self.num)
