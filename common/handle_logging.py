import os
import time

from nb_log import LogManager

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_DIR = os.path.join(BASE_DIR,'logs')
file_name = "D:\\PlaywrightProject\\logs"

log_path = os.path.join(LOG_DIR,file_name)
#log_path = os.path.join(os.path.dirname(__file__),'logs')

def output_log():
    logging = LogManager(__file__).get_logger_and_add_handlers(log_level_int=1,is_add_stream_handler=True,log_path=log_path,log_filename='%s.log'%time.strftime("%Y%m%d",time.localtime()))
    return logging

test_log = output_log()

if __name__=="__main__":
    test_log = output_log()
