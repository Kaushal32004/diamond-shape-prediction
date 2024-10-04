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

color_mapping = {"D": 1, "E": 2, "F": 3, "G": 4, "H": 5, "I": 6, "J": 7}
clarity_mapping = {"IF": 1, "VVS1": 2, "VVS2": 3, "VS1": 4, "VS2": 5, "SI1": 6, "SI2": 7, "I1": 8}
cut_quality_mapping = {"Excellent": 1, "Very Good": 2, "Good": 3, "Fair": 4}
lab_mapping = {"GIA": 1, "IGI": 2, "HRD": 3}
symmetry_mapping = {"Excellent": 1, "Very Good": 2, "Good": 3, "Fair": 4}
polish_mapping = {"Excellent": 1, "Very Good": 2, "Good": 3, "Fair": 4}
culet_condition_mapping = {"None": 1, "Small": 2, "Medium": 3, "Large": 4}
fluor_color_mapping = {"None": 1, "Faint": 2, "Medium": 3, "Strong": 4}


def main():
    st.title("Diamond Shape Prediction")
    
    html_temp = """
    <div style="background-color:aqua;padding:10px">
    <h2 style="color:white;text-align:center;">Diamond Shape Prediction using ML</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # Collect user inputs
    color = st.selectbox("Color", options=list(color_mapping.keys()))
    clarity = st.selectbox("Clarity", options=list(clarity_mapping.keys()))
    carat_weight = st.number_input("Carat Weight", min_value=0.0, format="%.2f")
    cut_quality = st.selectbox("Cut Quality", options=list(cut_quality_mapping.keys()))
    lab = st.selectbox("Lab", options=list(lab_mapping.keys()))
    symmetry = st.selectbox("Symmetry", options=list(symmetry_mapping.keys()))
    polish = st.selectbox("Polish", options=list(polish_mapping.keys()))
    culet_size = st.number_input("Culet Size", min_value=0.0, format="%.2f")
    culet_condition = st.selectbox("Culet Condition", options=list(culet_condition_mapping.keys()))
    depth_percent = st.number_input("Depth Percent", min_value=0.0, format="%.2f")
    table_percent = st.number_input("Table Percent", min_value=0.0, format="%.2f")
    meas_length = st.number_input("Measurement Length", min_value=0.0, format="%.2f")
    meas_width = st.number_input("Measurement Width", min_value=0.0, format="%.2f")
    meas_depth = st.number_input("Measurement Depth", min_value=0.0, format="%.2f")
    girdle_min = st.number_input("Girdle Min", min_value=0.0, format="%.2f")
    girdle_max = st.number_input("Girdle Max", min_value=0.0, format="%.2f")
    fluor_color = st.selectbox("Fluorescence Color", options=list(fluor_color_mapping.keys()))

    result = ""
    if st.button("Predict"):
        # Prepare the feature list for prediction by mapping categorical values to their numeric counterparts
        features = [
            color_mapping[color],
            clarity_mapping[clarity],
            float(carat_weight),
            cut_quality_mapping[cut_quality],
            lab_mapping[lab],
            symmetry_mapping[symmetry],
            polish_mapping[polish],
            float(culet_size),
            culet_condition_mapping[culet_condition],
            float(depth_percent),
            float(table_percent),
            float(meas_length),
            float(meas_width),
            float(meas_depth),
            float(girdle_min),
            float(girdle_max),
            fluor_color_mapping[fluor_color]
        ]
        
        result = prediction(features)
        
    st.success(f'The predicted shape is: {result}')


if __name__ == '__main__':
    main()
