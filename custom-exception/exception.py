##Custom exceptions  allow me to describe specific error conditions clearly, separate different failure types, and handle them in a targeted way.
##If I am unsure what exceptions might occur, I use a generic except Exception block to log the error and optionally re-raise it. 
##This helps me catch unexpected issues without hiding bugs. Later, I refine the exception handling once I understand the failure modes better

"""
sys gives access to Python's runtime environment.
Here,sys is used to extract exception info (file name, line number) from traceback object during exceptions.
"""
import sys
from core.logger import logger

"""
This method extracts the traceback object using the 'sys' - type error_detail parameter.
error_detail.exc_info() returns (type, value, traceback). We ignore type and value using _, _ and extract only the traceback object for further use.
"""
def get_error_details(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error in file [{file_name}] at line [{line_number}]: {str(error)}"
    return error_message

"""
CustomException is a user-defined exception class that extends Python’s built-in Exception.
It captures both a custom error message and runtime error details using the sys module.
The sys object is used to extract detailed runtime error information via sys.exc_info().
"""
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = get_error_details(error_message, error_detail)
        logger.error(f"Exception Occurred: {self.error_message}")

    def __str__(self):
        return self.error_message