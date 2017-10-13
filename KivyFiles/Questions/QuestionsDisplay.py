from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from KivyFiles.Questions.AnswerObject import AnswerObject
from KivyFiles.Questions.QuestionWidgets import MultipleAnswersObj, IntInput, BooleanQuestion
from SupplementaryFiles.Enums import QuestionTypes


class QuestionDisplay:
    """
    This object lies between the screen and the widget. It is used as a buffer between the two.
    """
    parent_screen = None

    def __init__(self, parent_screen=None):
        self.parent_screen = parent_screen
        self.the_widget = QuestionnaireWidget(parent_screen, self.parent_screen.main_app)
        self.the_end = False

    def load(self):
        self.is_playing = True


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
        self.set_questions(self.question_list)
        self.submit_button = Button(text='submit')
        self.submit_button.bind(on_press=self.submit_action)
        self.add_widget(self.submit_button)

    # DO NOT REMOVE instance
    def submit_action(self, instance):
        """
        Called when the user presses the submit button. Saves the user's answers in the main app for future screens.
        :param instance: DO NOT REMOVE instance
        """
        go_to_answers = True
        bad_answers = []
        self.main_app.user_answers = []
        for question in self.questionsArray:
            if question.get_answer() is None:
                # At least one of the questions was left unanswered.
                go_to_answers = False
                bad_answers.append(question)
            else:
                self.main_app.user_answers.append(AnswerObject(question,
                                                               user_seen_graph=self.main_app.discovered_graph,
                                                               real_graph=self.main_app.current_graph))
        if go_to_answers:
            self.parent_screen.end_questionnaire()
        else:
            self.main_app.user_answers = []
            popup = Popup(title='Inappropriate Answers',
                          content=Label(text='At least one of your answers is invalid. Please recheck you choices'),
                          auto_dismiss=True,
                          size_hint=(None, None),
                          size=(600, 150))
            popup.open()

    def set_questions(self, question_list):
        """
        Goes over the question list, creates a new widget for each question and sets in in the window.
        """
        for question in question_list:
            new_question_label = Label(text=question.question_string)
            if question.question_type_number == QuestionTypes['NUMBER']:
                new_question = IntInput(question=question)

            elif question.question_type_number == QuestionTypes['MULTIPLE_CHOICE']:
                new_question = MultipleAnswersObj(question=question)

            elif question.question_type_number == QuestionTypes['BOOLEAN']:
                new_question = BooleanQuestion(question=question)

            self.questionsArray.append(new_question)
            self.add_widget(new_question_label)
            self.add_widget(new_question)