__all__ = ('CheckBox', )

from QuestionObj import QuestionObject
from QuestionObj import QuestionObject
from QuestionObj import QuestionObject
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import BooleanProperty, StringProperty, ListProperty
from kivy.uix.behaviors import ToggleButtonBehavior
from random import uniform
from kivy.base import runTouchApp
from kivy.uix.gridlayout import GridLayout

class CheckBox(ToggleButtonBehavior, Widget):
    '''CheckBox class, see module documentation for more information.
    '''
    answer = -1
    questionString = ""
    possibleAnswers= []
    funcDict= {}
    x = None
    def __init__ (self,question):
        self.questionString = question.getQuestionString()
        self.possibleAnswers = question.getListOfPossibleAnswers()
        self.x = GridLayout(cols=4)
        Label(text=self.questionString)
        self.funcDict = {'0': self.on_checkbox_active_0, '1': self.on_checkbox_active_1, '2': self.on_checkbox_active_2}
        i = 0
        for ans in self.possibleAnswers:
            checkbox = self.x.add_widget(CheckBox(group='1', color=[0, 0, 1]))
            self.x.add_widget(Label(ans))
            func = self.funcDict(str(i))
            checkbox.bind(active=func)
            i = i + 1

    def on_checkbox_active_0(self, checkbox, value):
        if value:
            self.answer = 0

    def on_checkbox_active_1(self, checkbox, value):
        if value:
            self.answer = 1

    def on_checkbox_active_2(self, checkbox, value):
        if value:
            self.answer = 2



    active = BooleanProperty(False)
    '''Indicates if the switch is active or inactive.

    :attr:`active` is a :class:`~kivy.properties.BooleanProperty` and defaults
    to False.
    '''

    background_checkbox_normal = StringProperty(
        'atlas://data/images/defaulttheme/checkbox_off')
    '''Background image of the checkbox used for the default graphical
    representation when the checkbox is not active.

    .. versionadded:: 1.9.0

    :attr:`background_checkbox_normal` is a
    :class:`~kivy.properties.StringProperty` and defaults to
    'atlas://data/images/defaulttheme/checkbox_off'.
    '''

    background_checkbox_down = StringProperty(
        'atlas://data/images/defaulttheme/checkbox_on')
    '''Background image of the checkbox used for the default graphical
    representation when the checkbox is active.

    .. versionadded:: 1.9.0

    :attr:`background_checkbox_down` is a
    :class:`~kivy.properties.StringProperty` and defaults to
    'atlas://data/images/defaulttheme/checkbox_on'.
    '''

    background_checkbox_disabled_normal = StringProperty(
        'atlas://data/images/defaulttheme/checkbox_disabled_off')
    '''Background image of the checkbox used for the default graphical
    representation when the checkbox is disabled and not active.

    .. versionadded:: 1.9.0

    :attr:`background_checkbox_disabled_normal` is a
    :class:`~kivy.properties.StringProperty` and defaults to
    'atlas://data/images/defaulttheme/checkbox_disabled_off'.
    '''

    background_checkbox_disabled_down = StringProperty(
        'atlas://data/images/defaulttheme/checkbox_disabled_on')
    '''Background image of the checkbox used for the default graphical
    representation when the checkbox is disabled and active.

    .. versionadded:: 1.9.0

    :attr:`background_checkbox_disabled_down` is a
    :class:`~kivy.properties.StringProperty` and defaults to
    'atlas://data/images/defaulttheme/checkbox_disabled_on'.
    '''

    background_radio_normal = StringProperty(
        'atlas://data/images/defaulttheme/checkbox_radio_off')
    '''Background image of the radio button used for the default graphical
    representation when the radio button is not active.

    .. versionadded:: 1.9.0

    :attr:`background_radio_normal` is a
    :class:`~kivy.properties.StringProperty` and defaults to
    'atlas://data/images/defaulttheme/checkbox_radio_off'.
    '''

    background_radio_down = StringProperty(
        'atlas://data/images/defaulttheme/checkbox_radio_on')
    '''Background image of the radio button used for the default graphical
    representation when the radio button is active.

    .. versionadded:: 1.9.0

    :attr:`background_radio_down` is a
    :class:`~kivy.properties.StringProperty` and defaults to
    'atlas://data/images/defaulttheme/checkbox_radio_on'.
    '''

    background_radio_disabled_normal = StringProperty(
        'atlas://data/images/defaulttheme/checkbox_radio_disabled_off')
    '''Background image of the radio button used for the default graphical
    representation when the radio button is disabled and not active.

    .. versionadded:: 1.9.0

    :attr:`background_radio_disabled_normal` is a
    :class:`~kivy.properties.StringProperty` and defaults to
    'atlas://data/images/defaulttheme/checkbox_radio_disabled_off'.
    '''

    background_radio_disabled_down = StringProperty(
        'atlas://data/images/defaulttheme/checkbox_radio_disabled_on')
    '''Background image of the radio button used for the default graphical
    representation when the radio button is disabled and active.

    .. versionadded:: 1.9.0

    :attr:`background_radio_disabled_down` is a
    :class:`~kivy.properties.StringProperty` and defaults to
    'atlas://data/images/defaulttheme/checkbox_radio_disabled_on'.
    '''

    color = ListProperty([1, 1, 1, 1])
    '''Color is used for tinting the default graphical representation
    of checkbox and radio button (images).

    Color is in the format (r, g, b, a). Use alpha greater than 1 for
    brighter colors. Alpha greater than 4 causes blending border and check
    mark together.

    .. versionadded:: 1.10.0

    :attr:`color` is a
    :class:`~kivy.properties.ListProperty` and defaults to
    '[1, 1, 1, 1]'.
    '''



    def on_state(self, instance, value):
        if value == 'down':
            self.active = True
        else:
            self.active = False

    def _toggle_active(self):
        self._do_press()

    def on_active(self, instance, value):
        self.state = 'down' if value else 'normal'


