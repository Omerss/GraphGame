# import Kivy
import kivy
import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

# my app
class getNumber():
# layout
    answer = 0
    lbl1 = None
    txt1 = ""

    def __init__ (self, question):
        layout = BoxLayout(padding=10, orientation='vertical')
        btn1 = Button(text="OK")
        btn1.bind(on_press=self.buttonClicked)
        layout.add_widget(btn1)
        lbl2 = Label(text=question.getQuestionString)
        layout.add_widget(lbl2)
        self.lbl1 = Label(text="test")
        layout.add_widget(self.lbl1)
        self.txt1 = TextInput(text='', multiline=False)
        layout.add_widget(self.txt1)


# button click function
    def buttonClicked(self,btn):
        self.lbl1.text = "Your answer " + self.txt1.text
        try:
            self.answer= int(self.txt1)
        except ValueError:
            self.txt1 = "please enter a number value"

