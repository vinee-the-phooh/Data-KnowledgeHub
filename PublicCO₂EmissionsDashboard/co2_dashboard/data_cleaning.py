import pandas as pd
import core.custom_exceptions as exceptions
import core.logger_config as logger_config

logger = logger_config.setup_logger("data_cleaning")

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    try:
        logger.info("----Starting data cleaning----")

        if not isinstance(df, pd.DataFrame):
            raise exceptions.InvalidDataFrameError()

        df = df[df['co2'].notnull()]
        df = df[~df['country'].isin([
            'World', 'Asia', 'Europe', 'Africa',
            'North America', 'South America', 'Oceania'
        ])]
        df = df[df['country'].isin([
            'United States', 'Australia', 'India', 'China', 'Japan',
            'France', 'United Kingdom', 'Sri Lanka', 'Germany', 'Canada',
            'Brazil', 'Russia', 'South Korea', 'Indonesia', 'Mexico', 'Turkey'
        ])]

        logger.info("---Data cleaning completed---")
        return df

    except Exception as e:
        logger.error(f"Data cleaning failed: {e}")
        raise exceptions.DataCleaningError(str(e))
