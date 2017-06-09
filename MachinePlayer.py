import os
import random
import threading

from GameHandler import GameHandler

graphs_to_run = ["Graph_1"]
game = GameHandler()
game_ready_event = threading.Event()


def game_thread():
   # game.run_single_game(graph, None, False)
    score = game.run_single_game(None, "{}\GraphsData\config.ini".format(os.getcwd()), real_user=False,
                         machine_signal=game_ready_event)
    print(score)
    game_ready_event.clear()


for graph in graphs_to_run:
    click_thread = threading.Thread(name='game_thread',
                                    target=game_thread).start()
    turns = 5
    while True:
        game_ready = game_ready_event.wait()
        print('playing turn {}'.format(game.current_turn))
        game_ready_event.clear()
        if game.stop_threads:
            break
        button_to_press = random.randint(1, 4)
        game.machine_press_button(button_to_press)
    game_ready = game_ready_event.wait()



