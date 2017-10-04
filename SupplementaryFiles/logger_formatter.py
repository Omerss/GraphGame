

def format_log_msg (msg,**kwargs):
    new_message = msg
    for key, value in kwargs.iteritems():
        new_message = "{0}, {1}={2}".format(new_message,key,value)
    return new_message