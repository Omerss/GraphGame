from random import random, randrange, randint

EPSILON = 0.1
GAMMA = 0.8
ALPHA = 0.01


class q_matrix:
    array = []
    reword = []
    action_space = 4

    def __init__(self, action_space, step_count):
        """

        :param action_space:
        """
        self.action_space = action_space
        self.reword = [step_count]
        self.array = [action_space]
        for i in range(action_space):
            self.array[i] = [action_space]

    def max_args(self):
        """
        Returns
        :return:
        """
        pass

    def choose_action_epsilon_greedy(self):
        if random() < EPSILON:
            return randint(1, self.action_space)
        else:
            return self.max_args()
