

class server_logger ():
    ip = ""

    def __init__(self, writing_location, user_data_dir):
        self.ip = writing_location
        self.init_communication(self.ip,user_data_dir)

    def log_write (self,**kwargs):
        from KivyCommunication import *
        KL.log.insert(**kwargs)


    def init_communication(self, server_ip, user_data_dir):
        from KivyCommunication import *
        """
        Initiolize the communication protocol to the server.
        """
        KC.start(the_ip=server_ip, the_parents=[self])
        KL.start(mode=[DataMode.file], pathname=user_data_dir)
        KL.restart()

    #
    # @staticmethod
    # def on_connection():
    #     pass
