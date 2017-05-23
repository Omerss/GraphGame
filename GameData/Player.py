def do_move(self):
    btn_num = self.get_best_button()
    self.tablet_game.press_button(btn_num)
    print("Pressing button {0}".format(btn_num))
    graph_window = self.read_data_from_window(self.tablet_game)
    self.add_view_to_db(graph_window)
    print(self.graph)


def get_best_button(self):
    # use A* search algorithm
    return random.randint(1, 4)