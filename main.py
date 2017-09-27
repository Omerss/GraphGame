import os
import argparse
import threading

NUM_OF_GAMES = 10

user_id = 111
user_score = []
log_file_path = "./{}".format(user_id)

game_ready_event = threading.Event()


def main():
    from GameHandler import GameHandler
    game = GameHandler()
    for i in range(NUM_OF_GAMES):
        new_score = game.run_single_game(None, "{}\GraphsData\config.ini".format(os.getcwd()))
        user_score.append(new_score)

    try:
        with open(log_file_path, 'w') as user_log:
            user_log.write(user_score)

    except Exception as e:
        print(user_score)

if __name__ == "__main__":
    main()
