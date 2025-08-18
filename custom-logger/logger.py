"""
logging is a built-in module used for tracking events during program execution.
os is used to create directories and handle file paths.
datetime helps timestamp the log file to make each one unique.
warnings is used to capture Python warnings and redirect them to logs.
"""

import logging 
import os 
from datetime import datetime 
import warnings 

"""
Log Directory Setup to store log files.
    Creates a folder named 'logs' if it does not exist.
"""

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

"""
Dynamic Log File Naming - Prevents overwriting and helps to trace logs to specific runs.
    Generates a log file name based on the current date and time.
    Each run of the program creates a unique log file.
"""

log_file = os.path.join(LOG_DIR, f"EDA_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

"""
logging.basicConfig(...) configures the logging module—where it writes, how it writes, and what each log message looks like.
    With INFO level, it captures all messages at INFO level and above (WARNING, ERROR, CRITICAL).
    format defines how each log message will write. It includes timestamp, log level, filename, and the actual message.
    filemode='w' means the log file will be overwritten each time the program runs.
"""

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - [%(levelname)s] - %(filename)s - %(message)s",
    filemode="w"
)

"""
logging.getLogger(name) returns a Logger object from Python’s logging module.
    This object has methods like info(), warning(), error(), etc., to log messages at different severity levels.
    This function creates a logger with a specific name and sets its level to INFO.
"""

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger

"""
This line creates a logger object labeled with the name of this file and sets it to log INFO-level messages.
The line logger.info("Logger initialized successfully!") acts like a welcome message printed when the module loads.
This happens because when Python imports a module, it executes the entire module from top to bottom.
"""
logger = get_logger(__name__)
logger.info("Logger initialized successfully!")

"""
By default, Python prints warnings (like DeprecationWarning or RuntimeWarning) to the console.
    But these messages are not saved to the log file.
    warnings.showwarning = log_warning tells Python to use the log_warning function whenever a warning is raised.
    This overrides the default behavior of printing warnings to the console.
    log_warning is a custom function defined with pre-set parameters to capture the warning message, category, filename, line number, and other details.
"""

def log_warning(message, category, filename, lineno, file=None, line=None):
    logger.warning(f"Warning [{category.__name__}] in {filename} at line {lineno}: {message}")

warnings.showwarning = log_warning
logger.info("Logger initialized with warning handling!")