from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle

from Questions.QuestionWidgets import MultipleAnswersObj, IntInput, BooleanQuestion
from SupplementaryFiles.Enums import QuestionTypes


class QuestionDisplay:
    parent_screen = None

    def __init__(self, parent_screen=None):
        self.parent_screen = parent_screen
        self.the_widget = QuestionnaireWidget(self, self.parent_screen.main_app)

    def load(self):
        pass


class QuestionnaireWidget(GridLayout):
    question_list = None
    main_app = None
    parent_screen = None

    def __init__(self, parent_screen, main_app):
        """
        :param main_app: The main app that runs the program. We use it to pass on the question list and the user answers
        """
        super(QuestionnaireWidget, self).__init__(rows=2 * len(main_app.question_list) + 1, cols=1)
        self.parent_screen = parent_screen
        self.main_app = main_app
        self.question_list = self.main_app.question_list
        self.questionsArray = []
        self.main_app.user_answers = []
        self.set_questions(self.main_app.question_list)
        self.submit_button = Button(text='submit')
        self.submit_button.bind(on_press=self.submit_action)
        self.add_widget(self.submit_button)

    # DO NOT REMOVE instance
    def submit_action(self, instance):
        go_to_answers = True
        bad_answers = []
        for question in self.questionsArray:
            if question.get_answer() is None:
                go_to_answers = False
                bad_answers.append(question)
            else:
                self.main_app.append(question)

        if go_to_answers:
            self.parent_screen.end_questionnaire()
        else:
            self.main_app = []
            popup = Popup(title='Inappropriate Answers',
                          content=Label(text='At least one of your answers is invalid. Please recheck you choices'),
                          auto_dismiss=True,
                          size_hint=(None, None),
                          size=(600, 150))
            popup.open()

    def set_questions(self, question_list):
        for question in question_list:
            new_question_label = Label(text=question.question_string)
            if question.question_type_number == QuestionTypes.NUMBER:
                new_question = IntInput(question=question)

            elif question.question_type_number == QuestionTypes.MULTIPLE_CHOICE:
                new_question = MultipleAnswersObj(question=question)

            elif question.question_type_number == QuestionTypes.BOOLEAN:
                new_question = BooleanQuestion(question=question)

            self.questionsArray.append(new_question)
            self.add_widget(new_question_label)
            self.add_widget(new_question)

    def update_background(self, filename):
        with self.canvas.before:
            self.rect = Rectangle(source=filename, size=self.size)
            self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
        self.the_game.network.update_pos_size(instance.size)