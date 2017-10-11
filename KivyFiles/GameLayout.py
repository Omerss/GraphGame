import kivy
kivy.require('1.9.1')

from SupplementaryFiles import Utils
from kivy.uix.gridlayout import GridLayout
from GraphButton import MultiButton, TextButton
from GraphLayout import GraphLayout
from kivy.uix.floatlayout import FloatLayout
from time import sleep
from SupplementaryFiles.RepeatedTimer import RepeatedTimer
from kivy.uix.image import Image


class GameLayout(FloatLayout):
    next_func = None
    rt = None

    def __init__(self, tablet_game=None, zoom_rate=0.7, edge_size=2, **kwargs):
        super(GameLayout, self).__init__(rows=1, cols=2, **kwargs)
        self.tablet_game = tablet_game
        self.move_counter = 0
        self.dim = {"min_x": 0, "min_y": 0, "max_x": kivy.core.window.Window.size[0],
                    "max_y": kivy.core.window.Window.size[1]}
        self.button_width = self.dim["max_x"] * self.tablet_game.game_screen.button_ratio
        self.buttons = []
        self.original_graph = self.tablet_game.original_graph
        self.dim["max_x"] -= self.button_width
        self.kivy_graph_in = GraphLayout(self.original_graph, self.dim, 1, edge_size)
        self.kivy_graph_out = GraphLayout(self.original_graph, self.dim, zoom_rate, edge_size)
        self.kivy_graph_in.pos = (self.button_width, 0)
        self.kivy_graph_out.pos = (self.button_width, 0)
        self.add_widget(self.kivy_graph_in)
        self.is_zoomed_out = False
        self.set_button_functions()
        self.button_layout = self.get_buttons()
        self.add_widget(self.button_layout)
        self.button_layout.pos=(0,0)
        if self.tablet_game.game_screen.real_user:
            self.rt = RepeatedTimer(1, self.call_function)
        self.button_hider = self.get_button_hider()
        self.button_hider.pos=(0,0)

    def set_button_functions(self):
        self.button1_func = [self.zoom_out, self.zoom_in]
        self.button2_func = [self.centralize_most_connected]
        self.button3_func = [self.centralize_closest_same_color]
        self.button4_func = [self.centralize_closest_neighbor_diff_color]

    def get_buttons(self):
        """
        creates a GridLayout that would hold the buttons (GraphButtons) needed for the game. each button should be
        initialized using a string representing an image to be displayed on the button and a function that will be
        responsible for the button's functionality
        """
        layout = GridLayout(cols=1, col_default_width=self.button_width, col_force_default=True)
        button1 = MultiButton('{}\\button1.jpg'.format(Utils.image_folder), self.button1_func, 1, self)
        button2 = MultiButton('{}\\button2.jpg'.format(Utils.image_folder), self.button2_func, 2, self)
        button3 = MultiButton('{}\\button3.jpg'.format(Utils.image_folder), self.button3_func, 3, self)
        button4 = MultiButton('{}\\button4.jpg'.format(Utils.image_folder), self.button4_func, 4, self)
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)
        layout.add_widget(button4)
        self.buttons.append(button1)
        self.buttons.append(button2)
        self.buttons.append(button3)
        self.buttons.append(button4)
        return layout

    def get_button_hider(self):
        layout = GridLayout(cols=1, col_default_width=self.button_width, col_force_default=True)
        im1 = Image(source='{}\\button1.jpg'.format(Utils.image_folder), allow_stretch=True, keep_ratio=False,
                    color=[0.8, 0.8, 0.8, 1])
        im2 = Image(source='{}\\button2.jpg'.format(Utils.image_folder), allow_stretch=True, keep_ratio=False,
                    color=[0.8, 0.8, 0.8, 1])
        im3 = Image(source='{}\\button3.jpg'.format(Utils.image_folder), allow_stretch=True, keep_ratio=False,
                    color=[0.8, 0.8, 0.8, 1])
        im4 = Image(source='{}\\button4.jpg'.format(Utils.image_folder), allow_stretch=True, keep_ratio=False,
                    color=[0.8, 0.8, 0.8, 1])
        layout.add_widget(im1)
        layout.add_widget(im2)
        layout.add_widget(im3)
        layout.add_widget(im4)
        return layout

    def zoom_out(self):
        center_node = self.kivy_graph_out.kivy_graph.get_by_serial(self.kivy_graph_in.kivy_graph.center_node.serial)
        self.kivy_graph_out.kivy_graph.move_node_to_center(center_node, False)
        self.remove_widget(self.kivy_graph_in)
        self.add_widget(self.kivy_graph_out)
        self.is_zoomed_out = True
        self.remove_widget(self.button_layout)
        self.add_widget(self.button_layout)
        self.remove_widget(self.button_hider)
        self.add_widget(self.button_hider)

    def zoom_in(self):
        center_node = self.kivy_graph_in.kivy_graph.get_by_serial(self.kivy_graph_out.kivy_graph.center_node.serial)
        self.kivy_graph_in.kivy_graph.move_node_to_center(center_node, False)
        self.remove_widget(self.kivy_graph_out)
        self.add_widget(self.kivy_graph_in)
        self.is_zoomed_out = False
        self.remove_widget(self.button_layout)
        self.add_widget(self.button_layout)
        self.remove_widget(self.button_hider)
        self.add_widget(self.button_hider)

    def centralize_most_connected(self):
        if self.is_zoomed_out:
            self.kivy_graph_out.kivy_graph.centralize_most_connected()
        else:
            self.kivy_graph_in.kivy_graph.centralize_most_connected()

    def centralize_closest_same_color(self):
        if self.is_zoomed_out:
            self.kivy_graph_out.kivy_graph.centralize_closest_same_color()
        else:
            self.kivy_graph_in.kivy_graph.centralize_closest_same_color()

    def centralize_closest_neighbor_diff_color(self):
        if self.is_zoomed_out:
            self.kivy_graph_out.kivy_graph.centralize_closest_neighbor_diff_color()
        else:
            self.kivy_graph_in.kivy_graph.centralize_closest_neighbor_diff_color()

    def call_function(self):
        if self.next_func is not None:
            self.next_func()
            self.tablet_game.send_info_from_screen()
            self.move_counter += 1
            self.next_func = None
            if self.move_counter == self.tablet_game.max_turns:
                self.remove_widget(self.button_layout)
                self.remove_widget(self.button_hider)
                end_layout = GridLayout(cols=1, col_default_width=self.button_width, col_force_default=True)
                end_button = TextButton('end game', self.end_game)
                end_layout.add_widget(end_button)
                self.add_widget(end_layout)
                end_layout.pos = (0, 0)
        else:
            self.enable_buttons()

    def disable_buttons(self):
        self.add_widget(self.button_hider)
        for button in self.buttons:
                button.disabled = True

    def enable_buttons(self):
        for button in self.buttons:
            button.disabled = False
        self.remove_widget(self.button_hider)

    def set_button_status(self, status):
        for item in self.buttons:
            item.disabled = status

    def end_game(self):
        self.rt.stop()
        self.tablet_game.end_game()

