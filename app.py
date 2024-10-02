import numpy as np
import pickle
import pandas as pd
import streamlit as st

# Load the classifier model
pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def prediction(features):
    # Perform prediction using the loaded model
    prediction = classifier.predict([features])
    return prediction[0]  # Return the first element of the prediction

def main():
    st.title("Diamond Shape Prediction")
    
    html_temp = """
    <div style="background-color:aqua;padding:10px">
    <h2 style="color:white;text-align:center;">Diamond Shape Prediction using ML</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # Collect user inputs
    color = st.text_input("Color", "Type Here")
    clarity = st.text_input("Clarity", "Type Here")
    carat_weight = st.number_input("Carat Weight", min_value=0.0, format="%.2f")
    cut_quality = st.text_input("Cut Quality", "Type Here")
    lab = st.text_input("Lab", "Type Here")
    symmetry = st.text_input("Symmetry", "Type Here")
    polish = st.text_input("Polish", "Type Here")
    culet_size = st.number_input("Culet Size", min_value=0.0, format="%.2f")
    culet_condition = st.text_input("Culet Condition", "Type Here")
    depth_percent = st.number_input("Depth Percent", min_value=0.0, format="%.2f")
    table_percent = st.number_input("Table Percent", min_value=0.0, format="%.2f")
    meas_length = st.number_input("Measurement Length", min_value=0.0, format="%.2f")
    meas_width = st.number_input("Measurement Width", min_value=0.0, format="%.2f")
    meas_depth = st.number_input("Measurement Depth", min_value=0.0, format="%.2f")
    girdle_min = st.number_input("Girdle Min", min_value=0.0, format="%.2f")
    girdle_max = st.number_input("Girdle Max", min_value=0.0, format="%.2f")
    fluor_color = st.text_input("Fluorescence Color", "Type Here")

    result = ""
    if st.button("Predict"):
        # Prepare the feature list for prediction
        features = [
            color,
            clarity,
            float(carat_weight),
            cut_quality,
            lab,
            symmetry,
            polish,
            float(culet_size),
            culet_condition,
            float(depth_percent),
            float(table_percent),
            float(meas_length),
            float(meas_width),
            float(meas_depth),
            float(girdle_min),
            float(girdle_max),
            fluor_color
        ]
        
        result = prediction(features)
        
    st.success(f'The predicted shape is: {result}')

if __name__ == '__main__':
    main()
