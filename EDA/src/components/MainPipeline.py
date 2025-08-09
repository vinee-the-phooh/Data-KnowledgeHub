import src.components.DataExploratory as eda
import src.components.DataIngestion as di
import src.core.exception as ex
import src.core.logger as logger
import pandas as pd
import sys

class MainPipeline:
    """
    Main pipeline class to handle the end-to-end data processing workflow.
    """
    def __init__(self, data_path: str) -> None:
        """
        Initializes the MainPipeline class with the given data path.
        """
        self.data_path = data_path

    def run(self) -> None:
        """
        Runs the main pipeline to load data and perform EDA.
        """
        try:
            # Load data
            logger.logger.info(f"Loading data from {self.data_path}")
            df = di.DataIngestion(self.data_path).load_data()
            # Perform EDA
            eda_instance = eda.DataExploratory(df)
            eda_instance.get_data_head()
            eda_instance.get_data_shape()
            eda_instance.get_data_info()
            eda_instance.get_data_description()
            
        except Exception as e:
            raise ex.CustomException(e, sys)
        
if __name__ == "__main__":
    data_path ="data/SuicideRatesOverview1985_2016.csv"
    main_pipeline = MainPipeline(data_path)
    main_pipeline.run()