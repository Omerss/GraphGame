import logging

class GLogger ():
    logger = None
    log_output_type = ""
    log_level = logging.INFO
    #log levels chart
    # 0 = ERROR
    # 1 = WARNING
    # 2 = INFO
    # 3 = DEBUG

    def __init__(self,output_type, writing_location,level = "INFO" ):
        pass



    def set_logger(self, output_type):
        if output_type == "file" :
            self.logger =

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


