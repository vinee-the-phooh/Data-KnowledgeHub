import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import data_cleaning as cleaning
import data_explore as explore
import emissions_forecast as forecast
from core.logger_config import setup_logger
from core.custom_exceptions import AppError

logger = setup_logger("streamlit_app")

# Set up the Streamlit app
def setup_app():
    try:
        st.set_page_config(page_title="CO₂ Emissions Explorer", layout="wide")
        st.title("CO₂ Emissions Explorer (2000–2023)")
        st.write("Visualize CO₂ emissions trends across selected countries from 2000 to 2023. Use the filters to explore national-level data and uncover insights.")

        with st.expander("About This Dashboard"):
            st.write("""
            This dashboard presents CO₂ emissions data for a selected set of countries between 2000 and 2023. 
            Built by Vineetha as part of a data science learning journey, it highlights trends in total and per capita emissions, 
            enabling comparative analysis and storytelling through interactive charts.
            """)
        logger.info("App setup completed.")
    except Exception as e:
        logger.error(f"Error during app setup: {e}")
        st.error("Failed to initialize the dashboard.")
        raise AppError(f"App setup error: {e}")

# Sidebar with filters and personal info
def add_sidebar(df):
    try:
        st.sidebar.header("Filters")

        countries = df['country'].unique()
        selected_country = st.sidebar.selectbox("Select a country", countries)

        selected_countries = st.sidebar.multiselect("Compare multiple countries", countries, default=[selected_country])
        year_range = st.sidebar.slider("Select year range", 2000, 2023, (2000, 2023))

        filtered_df = df[
            (df['country'] == selected_country) &
            (df['year'] >= year_range[0]) &
            (df['year'] <= year_range[1])
        ]

        comparison_df = df[
            (df['country'].isin(selected_countries)) &
            (df['year'] >= year_range[0]) &
            (df['year'] <= year_range[1])
        ]

        st.sidebar.write("[LinkedIn](https://www.linkedin.com/in/vineetha-w-54725737/)")
        st.sidebar.write("[GitHub](https://github.com/vinee-the-phooh/Data-KnowledgeHub)")
        st.sidebar.write("Email: vins.im.ruh@gmail.com")

        with st.sidebar.expander("About Me"):
            st.write("""
            Hi, I'm Vineetha — a tech professional with over 14 years of experience, starting as a backend Java developer and later specializing in QA automation. 
            My curiosity, love for data, analytical mindset, and mathematical background naturally led me into data science and machine learning. 
            Having used Python extensively in automation, I’ve built a solid foundation in programming and analytical thinking. 
            Over time, I’ve expanded my skills in exploratory data analysis (EDA), statistics, data visualization, and machine learning modeling. 
            I enjoy working with data to uncover insights and create interactive dashboards that tell meaningful stories.
            """)

        st.subheader(f"CO₂ Emissions in {selected_country} ({year_range[0]}–{year_range[1]})")
        st.write(filtered_df.describe())

        logger.info("Sidebar filters applied successfully.")
        return filtered_df, comparison_df

    except Exception as e:
        logger.error(f"Error in sidebar setup: {e}")
        st.error("Failed to load sidebar filters.")
        raise AppError(f"Sidebar error: {e}")

# Display charts for selected country
def display_charts(filtered_df):
    try:
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("CO₂ Emissions Over Time")
            st.line_chart(filtered_df.set_index('year')['co2'])

        with col2:
            st.subheader("Per Capita Emissions")
            st.bar_chart(filtered_df.set_index('year')['co2_per_capita'])

        st.markdown("--- **Trend Insights** ---")
        peak_year = filtered_df.loc[filtered_df['co2'].idxmax(), 'year']
        peak_value = filtered_df['co2'].max()
        st.write(f"Peak CO₂ emissions occurred in **{peak_year}**, reaching **{peak_value:,.2f} million tonnes**.")

        drop_year = filtered_df.loc[filtered_df['co2'].idxmin(), 'year']
        drop_value = filtered_df['co2'].min()
        st.write(f"Lowest CO₂ emissions occurred in **{drop_year}**, with **{drop_value:,.2f} million tonnes**.")

        with st.expander("How to Use This Dashboard"):
            st.write("""
            1. Use the sidebar to select a country and year range.
            2. View CO₂ emissions trends and per capita data.
            3. Compare multiple countries side-by-side.
            4. Explore top global emitters in the latest year.
            5. Download filtered data for further analysis.
            """)
        logger.info("Charts displayed successfully.")
    except Exception as e:
        logger.error(f"Error displaying charts: {e}")
        st.error("Failed to render charts.")
        raise AppError(f"Chart display error: {e}")

# Multi-country comparison
def display_comparison_chart(comparison_df):
    try:
        st.subheader("Multi-Country CO₂ Comparison")
        pivot_df = comparison_df.pivot(index='year', columns='country', values='co2')
        st.line_chart(pivot_df)
        logger.info("Comparison chart rendered.")
    except Exception as e:
        logger.error(f"Error displaying comparison chart: {e}")
        st.error("Failed to render comparison chart.")
        raise AppError(f"Comparison chart error: {e}")

# Display top global emitters
def display_global_top_emitters(df):
    try:
        latest_year = df['year'].max()
        latest_data = df[df['year'] == latest_year]
        top_countries = latest_data.groupby('country')['co2'].sum().sort_values(ascending=False).head(5)

        st.markdown(f"--- **Top 5 Global Emitters in {latest_year}** ---")
        fig, ax = plt.subplots()
        ax.pie(top_countries, labels=top_countries.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')
        st.pyplot(fig)

        st.markdown("---")
        st.markdown("Made with Love using Streamlit | Data: Our World in Data")
        logger.info("Global top emitters chart displayed.")
    except Exception as e:
        logger.error(f"Error displaying global emitters: {e}")
        st.error("Failed to render global emitters chart.")
        raise AppError(f"Global emitters error: {e}")

# Download filtered data
def display_download_button(filtered_df):
    try:
        st.subheader("Download Filtered Data")
        csv = filtered_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name='co2_filtered_data.csv',
            mime='Vinee/csv'
        )
        logger.info("Download button rendered.")
    except Exception as e:
        logger.error(f"Error rendering download button: {e}")
        st.error("Failed to generate download.")
        raise AppError(f"Download button error: {e}")

# Display basic data info
def display_data_info(df):
    try:
        st.subheader("Data Overview")
        st.write("This dashboard visualizes CO₂ emissions data from selected countries over time.")
        st.write(f"Total records: {len(df)}")
        st.write(f"Countries: {df['country'].nunique()}")
        st.write(f"Years: {df['year'].nunique()}")
        logger.info("Data overview displayed.")
    except Exception as e:
        logger.error(f"Error displaying data overview: {e}")
        st.error("Failed to display data overview.")
        raise AppError(f"Data overview error: {e}")

# Main function to run the app
def main():
    try:
        setup_app()
        raw_df = explore.load_data("data/owid-co2-data.csv")
        cleaned_df = cleaning.clean_data(raw_df)
        filtered_df, comparison_df = add_sidebar(cleaned_df)
        display_charts(filtered_df)
        display_comparison_chart(comparison_df)
        display_global_top_emitters(cleaned_df)
        display_download_button(filtered_df)
        display_data_info(cleaned_df)
        forecast.run_forecast_module(cleaned_df)
        logger.info("Dashboard loaded successfully.")
    except AppError as ae:
        st.error(f"Application error: {ae}")
    except Exception as e:
        logger.critical(f"Unexpected error in main: {e}")
        st.error("A critical error occurred.... Please check the logs!!")

if __name__ == "__main__":
    main()
