import sys

def error_message_detail(error: Exception) -> str:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    
    if exc_tb is not None:
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
    else:
        file_name = "Unknown File"
        line_number = "Unknown Line"

    return f"Error occurred in python script [{file_name}] at line [{line_number}] with message [{str(error)}]"

class CustomException(Exception):
    def __init__(self, error_message: Exception):
        super().__init__(str(error_message))
        self.error_message = error_message_detail(error_message)

    def __str__(self):
        return self.error_message
