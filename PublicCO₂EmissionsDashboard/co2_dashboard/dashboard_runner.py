import data_cleaning as cleaning
import data_explore as explore
import data_streamlit_app as stapp
import emissions_forecast as forecast
import os
os.system("pip list")
from core.logger_config import setup_logger
from core.custom_exceptions import AppError

logger = setup_logger("main_dashboard")

def run_dashboard():
    """
        ****Run the CO₂ emissions dashboard by loading, cleaning, and exploring the data.
    """
    try:
        logger.info("....Starting CO₂ Emissions Dashboard...")
        stapp.setup_app()
        file_path = os.path.join(os.path.dirname(__file__), "data", "owid-co2-data.csv")
        raw_df = explore.load_data(file_path)
        cleaned_df = cleaning.clean_data(raw_df)

        filtered_df, comparison_df = stapp.add_sidebar(cleaned_df)
        stapp.display_charts(filtered_df)
        stapp.display_comparison_chart(comparison_df)
        stapp.display_global_top_emitters(cleaned_df)
        stapp.display_download_button(filtered_df)
        stapp.display_data_info(cleaned_df)

        forecast.run_forecast_module(cleaned_df)

        logger.info("----Dashboard executed successfully----")

    except AppError as ae:
        logger.error(f"Application error: {ae}")
    except Exception as e:
        logger.critical(f"Unexpected error in dashboard: {e}")

if __name__ == "__main__":
    run_dashboard()
