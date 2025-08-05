import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import streamlit as st
from core.logger_config import setup_logger
from core.custom_exceptions import AppError

logger = setup_logger("---emissions_forecast---")

def train_model(df: pd.DataFrame, country: str):
    try:
        country_df = df[(df['country'] == country) & (df['year'] >= 2000) & (df['year'] <= 2023)][['year', 'co2']]
        country_df = country_df.dropna()

        if country_df.empty:
            raise AppError(f"No valid data available for {country} between 2000 and 2023.")

        X = country_df['year'].values.reshape(-1, 1)
        y = country_df['co2'].values

        model = LinearRegression()
        model.fit(X, y)

        logger.info(f"Model trained successfully for {country}.")
        return model, country_df

    except Exception as e:
        logger.error(f"Error training model for {country}: {e}")
        raise AppError(f"Model training failed for {country}: {e}")

def predict_emissions(model, start_year=2025, end_year=2035):
    try:
        future_years = np.arange(start_year, end_year + 1).reshape(-1, 1)
        predictions = model.predict(future_years)

        logger.info(f"Predictions generated for years {start_year}–{end_year}.")
        return pd.DataFrame({
            'year': future_years.flatten(),
            'predicted_emissions': predictions
        })

    except Exception as e:
        logger.error(f"Error generating predictions: {e}")
        raise AppError(f"Prediction error: {e}")

def plot_emissions(actual_df: pd.DataFrame, pred_df: pd.DataFrame):
    try:
        fig, ax = plt.subplots()
        ax.plot(actual_df['year'], actual_df['co2'], label='Actual Emissions (2000–2023)', marker='o')
        ax.plot(pred_df['year'], pred_df['predicted_emissions'], label='Predicted Emissions (2025–2035)', linestyle='--', marker='x')
        ax.axvline(x=2024, color='gray', linestyle='--', label='Prediction Start')
        ax.set_xlabel('Year')
        ax.set_ylabel('CO₂ Emissions (Million Tonnes)')
        ax.set_title('CO₂ Emissions Forecast')
        ax.legend()
        st.pyplot(fig)
        logger.info("Forecast plot displayed.")
    except Exception as e:
        logger.error(f"Error plotting emissions: {e}")
        st.error("Failed to render emissions forecast chart.")
        raise AppError(f"Plotting error: {e}")

def generate_summary(actual_df: pd.DataFrame, country: str) -> str:
    try:
        start_val = actual_df[actual_df['year'] == 2000]['co2'].values
        end_val = actual_df[actual_df['year'] == 2023]['co2'].values

        if len(start_val) == 0 or len(end_val) == 0:
            return f"Not enough data to summarize emissions change for {country}."

        change = ((end_val[0] - start_val[0]) / start_val[0]) * 100
        direction = "grew" if change > 0 else "declined"
        logger.info(f"Summary generated for {country}.")
        return f"{country}'s emissions {direction} {abs(change):.1f}% from 2000 to 2023."

    except Exception as e:
        logger.error(f"Error generating summary for {country}: {e}")
        return f"Could not generate summary for {country}."

def generate_story(actual_df: pd.DataFrame, country: str) -> str:
    try:
        start_val = actual_df[actual_df['year'] == 2000]['co2'].values
        end_val = actual_df[actual_df['year'] == 2023]['co2'].values

        if len(start_val) == 0 or len(end_val) == 0:
            return "Data is insufficient to generate a story."

        change = end_val[0] - start_val[0]
        logger.info(f"Story generated for {country}.")

        if change > 0:
            return (
                f"Between 2000 and 2023, {country} saw a significant rise in CO₂ emissions, "
                f"reflecting industrial growth, increased energy consumption, and urban expansion. "
                f"This upward trend highlights the importance of sustainable development and clean energy policies."
            )
        elif change < 0:
            return (
                f"{country} successfully reduced its CO₂ emissions between 2000 and 2023, "
                f"indicating progress in environmental regulations, renewable energy adoption, and public awareness. "
                f"This decline showcases the impact of targeted climate action."
            )
        else:
            return (
                f"{country}'s emissions remained relatively stable from 2000 to 2023, "
                f"suggesting a balance between economic activity and environmental efforts. "
                f"Future policies could tip the scale toward further reductions."
            )

    except Exception as e:
        logger.error(f"Error generating story for {country}: {e}")
        return "Could not generate story due to an error."

def run_forecast_module(cleaned_df: pd.DataFrame):
    try:
        st.subheader("CO₂ Emissions Forecast")

        selected_countries = [
            'United States', 'Australia', 'India', 'China', 'Japan',
            'France', 'United Kingdom', 'Sri Lanka', 'Germany', 'Canada',
            'Brazil', 'Russia', 'South Korea', 'Indonesia', 'Mexico', 'Turkey'
        ]
        selected_country = st.selectbox("Select a country for prediction", sorted(selected_countries))

        model, actual_df = train_model(cleaned_df, selected_country)
        pred_df = predict_emissions(model)

        plot_emissions(actual_df, pred_df)

        st.markdown("--- **Summary Insight** ---")
        summary_text = generate_summary(actual_df, selected_country)
        st.success(summary_text)

        st.markdown("---- **What the Data Tells Us** ----")
        story_text = generate_story(actual_df, selected_country)
        st.write(story_text)

        st.markdown(f"Forecast complete for **{selected_country}** from 2025 to 2035.")
        logger.info(f"Forecast module completed for {selected_country}.")

    except AppError as ae:
        st.error(f"Forecast error: {ae}")
    except Exception as e:
        logger.critical(f"Unexpected error in forecast module: {e}")
        st.error("A critical error occurred during forecasting.")
