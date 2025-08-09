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
        
    
    
    