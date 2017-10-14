
class server_logger ():
    ip = ""

    def __init__(self, writing_location):

        self.ip = writing_location

    def log_write (self,msg):
        pass

    def init_communication(self, server_ip):
        from KivyCommunication import *
        """
        Initiolize the communication protocol to the server.
        """
        KC.start(the_ip=server_ip, the_parents=[self])
        KL.start(mode=[DataMode.file], pathname=self.user_data_dir)


    @staticmethod
    def on_connection():
        pass
