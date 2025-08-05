class AppError(Exception):
    """***Base class for all custom exceptions***"""
    pass

class InvalidDataFrameError(AppError):
    """***Raised when input is not a valid pandas DataFrame***"""
    def __init__(self, message="Input must be a pandas DataFrame."):
        super().__init__(message)

class DataCleaningError(AppError):
    """***Raised for errors during data cleaning***"""
    def __init__(self, message="Error occurred during data cleaning."):
        super().__init__(message)

class ModelTrainingError(AppError):
    """***Raised for errors during model training***"""
    def __init__(self, message="Error occurred during model training."):
        super().__init__(message)
