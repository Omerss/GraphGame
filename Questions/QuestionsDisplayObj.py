from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from Questions.QuestionWidgets import MultipleAnswersObj, IntInput, BooleanQuestion
from SupplementaryFiles.Enums import QuestionTypes


class QuestionDisplay(App):
    questions = None
    usersAnswers = None
    questionsArray = None

    def __init__(self, questions, queue, **kwargs):
        super(QuestionDisplay, self).__init__(**kwargs)

        num_of_rows = 2 * len(questions) + 1
        self.layout = GridLayout(rows=num_of_rows, cols=1)
        self.questions = questions
        self.questionsArray = []
        self.user_answers = []
        self.set_questions(questions)
        self.submit_button = Button(text='submit')
        self.submit_button.bind(on_press=self.submit_action)
        self.layout.add_widget(self.submit_button)
        self.queue = queue

    # DO NOT REMOVE instance
    def submit_action(self, instance):
        go_to_answers = True
        bad_answers = []
        for question in self.questionsArray:
            if question.get_answer() is None:
                go_to_answers = False
                bad_answers.append(question)
            else:
                self.user_answers.append(question)

        if go_to_answers:
            self.queue.put(self.user_answers)
            self.stop()
        else:
            self.user_answers = []
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
            self.layout.add_widget(new_question_label)
            self.layout.add_widget(new_question)

    def build(self):
        return self.layout
