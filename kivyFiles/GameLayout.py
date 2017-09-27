import kivy
kivy.require('1.9.1')

from SupplementaryFiles import Utils
from kivy.uix.gridlayout import GridLayout
from GraphButton import MultiButton
from GraphLayout import GraphLayout
from kivy.uix.floatlayout import FloatLayout


class GameLayout(FloatLayout):

    def __init__(self, graph, button_lst, button_width, send_screen_info, max_steps, end_game,
                 zoom_rate=0.7, edge_size=2, **kwargs):
        super(GameLayout, self).__init__(rows=1, cols=2, **kwargs)

        self.dim = {"min_x": 0, "min_y": 0, "max_x": kivy.core.window.Window.size[0],
                    "max_y": kivy.core.window.Window.size[1]}
        self.button_width = self.dim["max_x"] * button_width
        self.buttons = []
        self.original_graph = graph
        self.dim["max_x"] -= self.button_width
        self.kivy_graph_in = GraphLayout(self.original_graph, self.dim, 1, edge_size)
        self.kivy_graph_out = GraphLayout(self.original_graph, self.dim, zoom_rate, edge_size)
        self.kivy_graph_in.pos = (self.button_width, 0)
        self.kivy_graph_out.pos = (self.button_width, 0)
        self.add_widget(self.kivy_graph_in)
        self.is_zoomed_out = False
        self.set_button_functions()
        self.button_layout = self.get_buttons(button_lst, send_screen_info, max_steps, end_game)
        self.add_widget(self.button_layout)
        self.button_layout.pos=(0,0)

    def set_button_functions(self):
        self.button1_func = [self.zoom_out, self.zoom_in]
        self.button2_func = [self.centralize_most_connected]
        self.button3_func = [self.centralize_closest_same_color]
        self.button4_func = [self.centralize_closest_neighbor_diff_color]

    def get_buttons(self, button_lst, send_screen_info, max_steps, end_game):
        """
        creates a GridLayout that would hold the buttons (GraphButtons) needed for the game. each button should be
        initialized using a string representing an image to be displayed on the button and a function that will be
        responsible for the button's functionality
        """
        layout = GridLayout(cols=1, col_default_width=self.button_width, col_force_default=True)
        button1 = MultiButton('{}\\button1.jpg'.format(Utils.image_folder), self.button1_func, button_lst, 1,
                              self.button_width, send_screen_info, self.set_button_status, max_steps, end_game)
        button2 = MultiButton('{}\\button2.jpg'.format(Utils.image_folder), self.button2_func, button_lst, 2,
                              self.button_width, send_screen_info, self.set_button_status, max_steps, end_game)
        button3 = MultiButton('{}\\button3.jpg'.format(Utils.image_folder), self.button3_func, button_lst, 3,
                              self.button_width, send_screen_info, self.set_button_status, max_steps, end_game)
        button4 = MultiButton('{}\\button4.jpg'.format(Utils.image_folder), self.button4_func, button_lst, 4,
                              self.button_width, send_screen_info, self.set_button_status, max_steps, end_game)
        layout.add_widget(button1)
        layout.add_widget(button2)
        layout.add_widget(button3)
        layout.add_widget(button4)
        self.buttons.append(button1)
        self.buttons.append(button2)
        self.buttons.append(button3)
        self.buttons.append(button4)
        return layout

    def zoom_out(self):
        center_node = self.kivy_graph_out.kivy_graph.get_by_serial(self.kivy_graph_in.kivy_graph.center_node.serial)
        self.kivy_graph_out.kivy_graph.move_node_to_center(center_node, False)
        self.remove_widget(self.kivy_graph_in)
        self.add_widget(self.kivy_graph_out)
        self.is_zoomed_out = True
        self.remove_widget(self.button_layout)
        self.add_widget(self.button_layout)

    def zoom_in(self):
        center_node = self.kivy_graph_in.kivy_graph.get_by_serial(self.kivy_graph_out.kivy_graph.center_node.serial)
        self.kivy_graph_in.kivy_graph.move_node_to_center(center_node, False)
        self.remove_widget(self.kivy_graph_out)
        self.add_widget(self.kivy_graph_in)
        self.is_zoomed_out = False
        self.remove_widget(self.button_layout)
        self.add_widget(self.button_layout)

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

    def set_button_status(self, status):
        for item in self.buttons:
            item.disabled = status

