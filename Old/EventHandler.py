from pydispatch import dispatcher



def event_press_button(sender):
    """Performs an action when a button is pressed"""
    print 'Signal was sent by', sender

dispatcher.connect(event_press_button, signal=SIG_BUTTON_PRESS, sender=dispatcher.Any)


def send_event(signal_type, sender):
    dispatcher.send(signal=signal_type, sender=sender)
