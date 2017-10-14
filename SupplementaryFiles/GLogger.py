import logging
from SupplementaryFiles.file_logger import file_logger
class GLogger ():
    logger = None
    log_output_type = ""
    log_level = logging.INFO
    #log levels chart
    # 0 = ERROR
    # 1 = WARNING
    # 2 = INFO
    # 3 = DEBUG

    def __init__(self,output_type, writing_location,level="INFO"):
        self.log_level =logging.getLevelName(level)
        self.set_logger(output_type,writing_location)


    def set_logger(self, output_type, writing_location):
        if output_type == "file" :
            self.logger = file_logger(writing_location)

        # elif output_type== "server":
        #     self.logger =

        # elif output_type == "console":
        #     self.logger =

        else:
            raise ValueError ("invalid output type")

    def format_log_msg(self, msg, **kwargs):
        new_message = msg
        for key, value in kwargs.iteritems():
            new_message = "{0}, {1}={2}".format(new_message, key, value)
        return new_message

    def log (self, log_level, msg , **kwargs):
        if log_level < self.log_level:
            return
        else:
            logging.log_write (self.format_log_msg(msg, **kwargs))


