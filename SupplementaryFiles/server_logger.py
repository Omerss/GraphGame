
class server_logger ():
    ip = ""

    def __init__(self, writing_location):
        from KivyCommunication import *
        self.ip = writing_location

    def log_write (self,msg):
        pass