# Load libraries needed
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from streamlit_lottie import st_lottie
from datetime import datetime
from sklearn.preprocessing import OrdinalEncoder

# Load the encoders from files
LE = joblib.load('Encoders/label_encoder.pkl')
BE = joblib.load('Encoders/binary_encoder.pkl')
OE = joblib.load('Encoders/ordinal_encoder.pkl')

# Load the model
model = joblib.load('Model/model.pkl')

# define app section
header = st.container()
prediction = st.container()

# Define the lottie animation URL
lottie_animation_url = "https://lottie.host/f822b8b2-5616-463a-970b-db6afcc63a9c/2Yc2T6Tm5S.json"

# Define header
with header:
    header.title(
        "Aplikasi Prediksi Penjualan Dengan Regresi Linier Di Seluruh Toko Favorit")
    
    # Display the Lottie animation using st_lottie
    st_lottie(lottie_animation_url, height=200)

    header.write("Di halaman ini, Anda dapat mempredikdi penjualan")


# Create lists
input = ["date", "holiday", "locale", "transferred", "onpromotion"]
categorical = ["holiday", "local", "transferred"]


# Set up prediction container
with st.expander("Buat Prediksi", expanded=True):

    # Define Streamlit inputs
    date = st.date_input(label="Masukkan tanggal")
    holiday = st.selectbox(label="Pilih kategori hari libur", options=[
                            'Holiday', 'Not Holiday', 'WorkDay', 'Additional', 'Event', 'Transfer', 'Bridge'])
    locale = st.radio(label="Pilih tipe hari libur", options=[
                         "National", "Regional", "local", "Not Holiday"], horizontal=True)
    transferred = st.radio(label="Pilih apakah hari libur atau tidak", options=[
        "True", "False"], horizontal=True)
    onpromotion = st.number_input(label="Silahkan masukkan jumlah total item yang diharapkan ada pada promosi")


    # Create a button
    predicted = st.button("Prediksi")

    # Flag variable to control visibility of the prediction message
    show_prediction_message = False

    # Upon predicting
    if predicted:
        # Set the flag to true when the  "predict" button is pressed
        show_prediction_message = True

        # Format for inputs
        input_dict = {
            "date": [date],
            "holiday": [holiday],
            "locale": [locale],
            "transferred": [transferred],
            "onpromotion": [onpromotion],
        }

        # Convert inputs into a Dataframe
        input_df = pd.DataFrame.from_dict(input_dict)

        # Encode categorical inputs
        input_df["transferred"] = LE.transform(input_df["transferred"])
        input_df = BE.transform(input_df)

        hier = ["National", "Regional", "Local", "Not Holiday"]
        # Initialize the OrdinalEncoder with the hierarchy

        OE = OrdinalEncoder(categories=[hier])

        input_df[["locale"]] = OE.fit_transform(input_df[["locale"]])

        # Converrt date to datetime
        input_df["date"] = pd.to_datetime(input_df["date"])

        # Extract date features and add to input_df
        input_df['year'] = input_df['date'].dt.year
        input_df['month'] = input_df['date'].dt.month
        input_df['day'] = input_df['date'.dt.day]
        input_df['day_of_week'] = input_df['date'].dt.dayofweek
        input_df['day_of_year'] = input_df['date'].dt.dayofyear
        input_df['week_of_year'] = input_df['date'].dt.isocalendar().week
        input_df['quarter'] = input_df['date'].dt.quarter
        input_df['is_weekend'] = (
            input_df['date'].dt.dayofweek // 5 == 1).astype(int)
        input_df['day_of_month'] = input_df['date'].dt.day
        
        # Drop date after extracting
        input_df.drop(columns=['date'], inplace=True)

        # Make predictions
        model_output = model.predict(input_df)

        # Round the model output to 2 significant figures
        rounded_output = np.round(model_output, 2)

        # Add rounded predictions to the input_dict
        input_dict["Total Sales($)"] = rounded_output

        # Format the rounded output with bold and dollar sign
        formatted_output = f"<b>${rounded_output[0]}</b>"

# Display prediction message inside the expander with HTMLformatting
        st.write(
            f"Total prediksi penjualan anda akan menjadi {formatted_output}", unsafe_allow_html=True)

# Displahy the Dataframe outside the expander
if show_prediction_message:
    st.write("datagrame yang berisi masukkan dan perkiraan penjualan Anda ditunjukkan di bawah ini:")
    st.dataframe(input_dict)        

    