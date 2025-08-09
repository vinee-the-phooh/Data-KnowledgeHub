import src.core.exception as ex
import src.core.logger as logger
import pandas as pd
import sys
import io

class DataExploratory:
    """
    Class to handle Exploratory Data Analysis (EDA) operations.
    """

    def __init__(self, df: pd.DataFrame) -> None:
        """
        Initializes the EDA class with the given DataFrame.
        """
        self.df = df

    def get_data_head(self) ->None:
   
        logger.logger.info("Getting the first 5 rows of the data")    
        try:
           data_head = self.df.head().to_string(index=False)
           """
            df.head() displays the first five rows of the dataset, including all columns.
            By looking at a single row, we can understand what one row represents—such as a specific group or time period.
            By looking at five rows, we get an initial idea of how the data behaves—its structure, consistency, and possible patterns.
           """
           logger.logger.info(f"Data Head:\n{data_head}")
            
        except Exception as e:
            raise ex.CustomException(e, sys)
        
    def get_data_shape(self) -> None:
        """
        This method retrieves the shape of the DataFrame.
        The shape is a tuple representing the number of rows and columns in the DataFrame.
        """
        logger.logger.info("Getting the shape of the data")
        try:
            data_shape = self.df.shape
            logger.logger.info(f"Data Shape: {data_shape}")
        except Exception as e:
            raise ex.CustomException(e, sys)
    
    def get_data_info(self) -> None:
        """
        We use df.info() to check the data types of all columns and see if there are any missing values.
        """
        logger.logger.info("Getting data info")
        try:
            buffer = io.StringIO()
            self.df.info(buf=buffer)
            data_info = buffer.getvalue()
            logger.logger.info(f"Data Info:\n{data_info}")
        except Exception as e:
            raise ex.CustomException(e, sys) 
        
    def get_data_description(self) -> None:
        """
        We use df.describe()—to get a statistical summary of the numeric columns. It helps us understand the central tendency, spread, and potential outliers in the data.
        """
        logger.logger.info("Getting data description")
        try:
            data_description = self.df.describe().to_string()
            logger.logger.info(f"Data Description:\n{data_description}")
        except Exception as e:
            raise ex.CustomException(e, sys)