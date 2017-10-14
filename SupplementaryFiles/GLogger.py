import logging
from SupplementaryFiles.file_logger import file_logger
from SupplementaryFiles.server_logger import server_logger
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
        GLogger.log_level =logging.getLevelName(level)
        self.set_logger(output_type,writing_location)


    def set_logger(self, output_type, writing_location):
        if output_type == "file" :
            GLogger.logger = file_logger(writing_location)

        elif output_type== "server":
             GLogger.logger = server_logger (writing_location)

        # elif output_type == "console":
        #     self.logger =

        else:
            raise ValueError ("invalid output type")
    @staticmethod
    def format_log_msg(msg, **kwargs):
        new_message = msg
        for key, value in kwargs.iteritems():
            new_message = "{0}, {1}={2}".format(new_message, key, value)
        return new_message

    @staticmethod
    def log (log_level, msg , **kwargs):
        if log_level < log_level:
            return
        else:
            GLogger.logger.log_write(GLogger.format_log_msg(msg, **kwargs))


