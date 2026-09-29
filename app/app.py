import streamlit as st
import joblib
import pandas as pd

st.title("Flight Price Prediction")

st.write("Enter the flight information to predict the price.")

model = joblib.load("models/random_forest_model.joblib")


st.subheader("Flight info")

airline = st.selectbox("Airline" ,["Air India", "AirAsia", "GO_FIRST", "Indigo", "SpiceJet", "Vistara"])

flight = st.text_input("Flight number", placeholder="Example: AI-202")


departure_city = st.selectbox("Departure City" , ["Bangalore", "Chennai", "Delhi", "Hyderabad", "Kolkata", "Mumbai"])
arrival_city = st.selectbox("Arrival City" , ["Bangalore", "Chennai", "Delhi", "Hyderabad", "Kolkata", "Mumbai"])


departure_time = st.selectbox(
    "Departure Time",
    ["Early_Morning", "Morning", "Afternoon", "Evening", "Night", "Late_Night"]
)

arrival_time = st.selectbox(
    "Arrival Time",
    ["Early_Morning", "Morning", "Afternoon", "Evening", "Night", "Late_Night"]
)


stops = st.selectbox("Number of Stops",["zero", "one", "two_or_more"])

travel_class = st.selectbox("Class",["Economy", "Business"])


duration = st.number_input(
                          "Duration (hours)",
                           min_value=0.0,
                           max_value=50.0,
                           value=2.0,
                           step=0.5
                           )


days_left = st.number_input(
    "Days Left Before Departure",
    min_value=1,
    max_value=50,
    value=10,
    step=1
)

if st.button("Predict Price"):
    input_data = pd.DataFrame([{
        "airline": airline,
        "flight": flight,
        "source_city": departure_city,
        "departure_time": departure_time,
        "stops": stops,
        "arrival_time": arrival_time,
        "destination_city": arrival_city,
        "class": travel_class,
        "duration": duration,
        "days_left": days_left,
        "Unnamed: 0": 0
    }])

    prediction = model.predict(input_data)

    st.success(f"Predicted Price : {prediction[0]:,.2f}" )