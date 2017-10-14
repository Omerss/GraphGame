
class file_logger ():
    path = ""

    def __init__(self, writing_location):
        self.path = writing_location
        open(self.path, 'w').close()

    def log_write (self,msg):
        log_file = open(self.path, 'a')
        log_file.write("{}\n".format(msg))
        log_file.close()