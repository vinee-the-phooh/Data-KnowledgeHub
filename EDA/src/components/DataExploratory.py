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
        
    def get_data_columns(self) -> None:
        """
        This method retrieves the names of the columns in the DataFrame.
        It helps to understand the features available in the dataset.
        """
        logger.logger.info("Getting the columns of the data")
        try:
            data_columns = self.df.columns.tolist()
            logger.logger.info(f"Data Columns: {data_columns}")
        except Exception as e:
            raise ex.CustomException(e, sys)
        
    def get_data_types(self) -> None:
        """
        This method retrieves the data types of each column in the DataFrame.
        It helps to understand the nature of the data in each column.
        """
        logger.logger.info("Getting the data types of the columns")
        try:
            data_types = self.df.dtypes.to_dict()
            logger.logger.info(f"Data Types: {data_types}")
        except Exception as e:
            raise ex.CustomException(e, sys)
    
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
        
    def get_data_tail(self)-> None:
        """
        This method retrieves the last five rows of the DataFrame.
        It helps to understand any anomalies that differ from the initial rows.
        """
        logger.logger.info("Getting the last 5 rows of the data")
        try:
            data_tail = self.df.tail().to_string(index=False)
            logger.logger.info(f"Data Tail:\n{data_tail}")
        except Exception as e:
            raise ex.CustomException(e, sys)
    
    def get_data_info(self) -> None:
        """
        We use df.info() to check the data types of all columns and see if there are any missing values.
        """
        logger.logger.info("Getting data info")
        try:
            """
                This code is used to capture the output of self.df.head() as a string.
                io.StringIO() creates an in-memory text stream, like a fake file.
                Normally, pandas returns the first five rows of a DataFrame when calling df.head().
                But when passing buf=buffer, pandas writes the formatted output (like a table) into the buffer instead of printing it.
                buffer.getvalue() reads the entire content of the buffer as a string.
            """

            buffer = io.StringIO()
            self.df.info(buf=buffer)
            data_info = buffer.getvalue()
            logger.logger.info(f"Data Info:\n{data_info}")
        except Exception as e:
            raise ex.CustomException(e, sys) 
        
    def get_data_describe(self) -> None:
        """
        We use df.describe()—to get a statistical summary of the numeric columns. It helps us understand the central tendency, spread, and potential outliers in the data.
        """
        logger.logger.info("Getting data description")
        try:
            data_description = self.df.describe().to_string()
            logger.logger.info(f"Data Description:\n{data_description}")
        except Exception as e:
            raise ex.CustomException(e, sys)
        
    def get_data_null_count(self) -> None:
        """
        This method retrieves the count of null values in each feature of the DataFrame.
        It helps to understand missing data that need to be handled before analysis.
        """
        logger.logger.info("Getting null values in the data")
        try:
            null_values = self.df.isnull().sum()
            logger.logger.info(f"Null Values:\n{null_values}")
        except Exception as e:
            raise ex.CustomException(e, sys)

    def get_data_duplicate_count(self) -> None:
        """
        This method retrieves the count of duplicate rows in the DataFrame.
        It helps to understand any redundancy in the dataset that may need to be addressed.
        """
        logger.logger.info("Getting duplicate rows in the data")
        try:
            duplicate_count = self.df.duplicated().sum()
            logger.logger.info(f"Duplicate Rows Count: {duplicate_count}")
        except Exception as e:
            raise ex.CustomException(e, sys)

    def get_data_unique_values_count(self) -> None:
        """
        This method retrieves the count of unique values in each feature of the DataFrame.
        It helps to understand the diversity of data in each column.
        """
        logger.logger.info("Getting unique values in the data")
        try:
            unique_values = self.df.nunique()
            logger.logger.info(f"Unique Values:\n{unique_values}")
        except Exception as e:
            raise ex.CustomException(e, sys)
        
    def get_numerical_features_outliers(self) -> None:
        """
        This method retrieves the outliers in each numerical column of the DataFrame.
        It uses the Interquartile Range (IQR) method to identify outliers.
        """
        logger.logger.info("Getting outliers in numerical features")
        try:
            numerical_features = self.df.select_dtypes(include=['float64', 'int64']).columns
            outliers = {}
            for feature in numerical_features:
                Q1 = self.df[feature].quantile(0.25)
                Q3 = self.df[feature].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                outlier_count = self.df[(self.df[feature] < lower_bound) | (self.df[feature] > upper_bound)].shape[0]
                outliers[feature] = outlier_count
            logger.logger.info(f"Outliers in Numerical Features: {outliers}")
        except Exception as e:
            raise ex.CustomException(e, sys)