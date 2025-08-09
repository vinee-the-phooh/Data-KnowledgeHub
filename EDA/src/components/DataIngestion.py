import pandas as pd
import src.core.exception as ex
import src.core.logger as logger
import sys

class DataIngestion:
    """
    Class to handle data ingestion operations.
    """

    def __init__(self, data_path: str)-> None:  
        """
        Python first calls __new__ to create the object.
        Then __new__ calls __init__ to initialize the object — setting up its attributes.
        The __init__ method then initializes the DataIngestion class with the given data_path parameter.
        In Python, __init__ is often referred to as the constructor, even though the actual constructor is __new__.
        The __init__ method should not return anything — it must return None.
        """
        self.data_path = data_path

 
    def load_data(self)->pd.DataFrame:
        """
        This method loads data from the specified path and returns it as a pandas DataFrame.
        """
        logger.logger.info(f"Loading data from {self.data_path}")
        try:
            data = pd.read_csv(self.data_path)
            return data
        except Exception as e:
            raise ex.CustomException(e,sys)
        

        