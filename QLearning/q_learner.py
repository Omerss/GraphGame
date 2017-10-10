from random import random, randrange

EPSILON = 0.1


def max_args(q_matrix):
    pass


def choose_action_epsilon_greedy():
    if random() < EPSILON:
        action = randrange(1,4)
    else:
        action = max_args(Q(a_t - 1, a_t))