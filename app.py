import streamlit as st
import pandas as pd
import pickle

# Page Configuration
st.set_page_config(
    page_title="California House Price Predictor",
    page_icon="🏠",
    layout="centered"
)


# Load Saved Model
@st.cache_resource
def load_model():
    with open("hist_gradient_boosting.pkl", "rb") as file:
        return pickle.load(file)


model = load_model()

# Header
st.title("🏠 California House Price Predictor")

st.write(
    "Enter the housing information below to predict "
    "the median house value."
)

st.divider()

# Input Section
st.subheader("🏡 House Information")


col1, col2 = st.columns(2)


with col1:

    longitude = st.number_input(
        "Longitude",
        value=-122.23,
        format="%.3f"
    )

    latitude = st.number_input(
        "Latitude",
        value=37.88,
        format="%.3f"
    )

    housing_median_age = st.number_input(
        "Housing Median Age",
        min_value=1,
        value=30
    )

    total_rooms = st.number_input(
        "Total Rooms",
        min_value=1,
        value=880
    )

    total_bedrooms = st.number_input(
        "Total Bedrooms",
        min_value=1,
        value=129
    )


with col2:

    population = st.number_input(
        "Population",
        min_value=1,
        value=322
    )

    households = st.number_input(
        "Households",
        min_value=1,
        value=126
    )

    median_income = st.number_input(
        "Median Income",
        min_value=0.0,
        value=8.3252,
        format="%.4f"
    )

    ocean_proximity = st.selectbox(
        "Ocean Proximity",
        [
            "<1H OCEAN",
            "INLAND",
            "NEAR OCEAN",
            "NEAR BAY",
            "ISLAND"
        ]
    )


st.divider()


# Prediction Button
predict_button = st.button(
    "🔮 Predict House Value",
    use_container_width=True
)


# Prediction
if predict_button:

    new_data = pd.DataFrame([{
        "longitude": longitude,
        "latitude": latitude,
        "housing_median_age": housing_median_age,
        "total_rooms": total_rooms,
        "total_bedrooms": total_bedrooms,
        "population": population,
        "households": households,
        "median_income": median_income,
        "ocean_proximity": ocean_proximity
    }])

    prediction = model.predict(new_data)

    predicted_value = prediction[0]

    st.success("Prediction completed successfully!")

    st.metric(
        label="🏠 Predicted Median House Value",
        value=f"${predicted_value:,.2f}"
    )