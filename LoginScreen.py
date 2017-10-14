from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.textinput import TextInput


class LoginScreen(Screen):
    """
    Zero screen collects the user's id
    """
    main_app = None
    display = None

    def setup(self, main_app):
        self.main_app = main_app
        self.display = LoginDisplay(self)

    def on_enter(self, *args):
        self.display.load()

    def start_game(self):
        self.main_app.sm.current = 'game_graph_0'


class LoginDisplay:
    """
        This object lies between the screen and the widget. It is used as a buffer between the two.
    """
    parent_screen = None

    def __init__(self, parent_screen=None):
        self.parent_screen = parent_screen
        self.layout = LoginLayout(self, self.parent_screen.main_app)

    def load(self):
        self.is_playing = True


class LoginLayout(GridLayout):
    main_app = None
    parent_app = None

    def __init__(self, parent_app, main_app):
        # The result window is split to 3 parts - information, scoreboard and button
        super(LoginLayout, self).__init__(rows=1, cols=3, row_default_height=40, row_force_default=True, padding=[0, 100, 0, 0])

        self.parent_app = parent_app
        self.main_app = main_app

        self.add_widget(Label(text="Subject ID", font_size='20sp', size_hint=(10, 0.2)))
        self.user_id_text = TextInput(font_size='20sp', size_hint=(40, 0.2))
        self.add_widget(self.user_id_text)
        submit_button = Button(text='Start', size_hint_y=None, font_size='20sp', size_hint=(10, 0.2))
        submit_button.bind(on_press=self.stop_me)
        self.add_widget(submit_button)

    def stop_me(self, instance):
        self.parent_app.parent_screen.main_app.user_id = self.user_id_text.text
        self.parent_app.parent_screen.start_game()


