
import streamlit as st
import pickle
import pandas as pd
from prophet import Prophet
from datetime import datetime

# --- Configuration ---
APP_TITLE = "Forecasting Nepal Economic and Social Development"

# --- Page Setup ---
st.set_page_config(page_title=APP_TITLE, layout="wide")

# -------------------------------
# Caching: Use st.cache_resource for ML models (Best Practice)
# This prevents the app from reloading models on every user interaction.
# -------------------------------
@st.cache_resource
def load_models():
    """Load all pre-trained Prophet models from pickle files."""
    try:
        models = {
            "gdp": pickle.load(open("model_gdp.pkl", "rb")),
            "life": pickle.load(open("model_life.pkl", "rb")),
            "pop": pickle.load(open("model_pop.pkl", "rb")),
            "gdp_cap": pickle.load(open("model_gdp_cap.pkl", "rb"))
        }
        return models
    except FileNotFoundError:
        st.error("❌ Model files not found. Please ensure the .pkl files are in the same directory.")
        st.stop()

MODELS = load_models()
model_gdp = MODELS["gdp"]
model_life = MODELS["life"]
model_pop = MODELS["pop"]
model_gdp_cap = MODELS["gdp_cap"]


# -------------------------------
# Helper function
# -------------------------------
@st.cache_data
def predict_for_date(date):
    """Predict all 4 metrics for a given date"""
    future_date = pd.DataFrame({'ds': [pd.to_datetime(date)]})

    forecast_gdp = model_gdp.predict(future_date)
    forecast_life = model_life.predict(future_date)
    forecast_pop = model_pop.predict(future_date)
    forecast_gdp_cap = model_gdp_cap.predict(future_date)

    return {
        "GDP (Billion US$)": round(forecast_gdp['yhat'].iloc[0], 2),
        "Life Expectancy (Years)": round(forecast_life['yhat'].iloc[0], 2),
        "Total Population (Billion)": round(forecast_pop['yhat'].iloc[0], 3),
        "GDP per capita (US$)": round(forecast_gdp_cap['yhat'].iloc[0], 2)
    }

# -------------------------------
# Streamlit UI
# -------------------------------

# --- Header Section (Custom Styling for Professional Look) ---
st.markdown(
    """
    <div style="text-align: center; padding: 10px; border-bottom: 2px solid #f0f2f6;">
        <h1 style="color:#008080;">Forecasting Nepal Economic and Social Development</h1>
    
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("---")


# --- Prediction Input Area (Using st.container for visual grouping) ---
with st.container(border=True):
    st.subheader("🗓️ Select Prediction Date")
    
    # Use columns with vertical_alignment="bottom" for perfect alignment
    col_date, col_button, col_spacer = st.columns([1.5, 1, 2.5], vertical_alignment="bottom")

    with col_date:
        # Default the date input to a year in the near future for better UX
        default_date = datetime(2030, 1, 1).date()
        date = st.date_input("Select a future year" \
        " format - Year/01/01 (Max 10 years ahead):", default_date)

    with col_button:
        # No need for st.write('') spacer now
        predict_button = st.button(
            "🧠 Generate Forecast",
            type='primary', 
            use_container_width=True
        )

# --- Results Area ---
if predict_button:
    st.markdown("## 📊 Forecast Results")
    st.info(f"Displaying predictions for **{date.strftime('%Y-%m-%d')}**")
    
    results = predict_for_date(date)

    # Use a two-row, two-column layout for the metrics (KPI cards)
    c1, c2, c3, c4 = st.columns(4)

    # Note: Use specific formatting for professional appearance (e.g., currency symbols)
    with c1:
        st.metric(
            label="Gross Domestic Product (GDP)", 
            value=f"${results['GDP (Billion US$)']:.2f} B",
        )
    with c2:
        st.metric(
            label="Life Expectancy", 
            value=f"{results['Life Expectancy (Years)']:.1f} Yrs",
        )
    with c3:
        st.metric(
            label="Total Population", 
            value=f"{results['Total Population (Billion)']:.3f} B",

        )
    with c4:
        st.metric(
            label="GDP per Capita", 
            value=f"${results['GDP per capita (US$)']:.0f}",
        )

# --- Footer/Documentation (Using st.expander for clean design) ---
st.markdown("---")
with st.expander("ℹ️ Key Terms Explanations"):
    st.write(
        """
Gross Domestic Product (GDP): The total value of all goods and services a country produces in a year. It shows the size of the country’s economy.

Life Expectancy: The average number of years a person is expected to live, based on current health and living conditions.

Total Population: The total number of people living in a country at a given time.

GDP per Capita: The average economic output (GDP) per person. It is calculated by dividing GDP by the total population and reflects the standard of living.

        """
    )


# Footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 10px;
        left: 0;
        width: 100%;
        text-align: center;
        font-size: 0.9em;
        color: gray;
    }
    </style>
    <div class="footer">
        🧑Developed by <strong>Dipen Sherpa</strong>&nbsp;|&nbsp; © 2025
    </div>
    """,
    unsafe_allow_html=True
)


