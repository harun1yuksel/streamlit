import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title("This is a Car Price Prediction Application")

img = Image.open("car_image.jpg")
st.image(img, width=325)

st.markdown('###### Trained and Deployed by Harun Yüksel')
st.markdown('### The model was trained with the following cars, which are up to 3 years old. If you make predictions for these or similar cars, you will get more accurate results')

st.info("Audi A1, Audi A3, Opel Astra, Opel Corsa, Opel Insignia, Renault Clio, Renault Duster, Renault Espace")

st.markdown("## Please enter the information of your car from the left side bar and below")

import pickle
filename = 'autoScout_model.pkl'
model = pickle.load(open(filename, 'rb'))



make_model = st.selectbox(
    'Please select your car',
    ('Audi A1', 'Audi A3', 'Opel Astra', 'Opel Corsa', 'Opel Insignia', 
     'Renault Clio', 'Renault Duster', 'Renault Espace', 'Other')
    )

gearing_type = st.selectbox(
    'Please select your gearing type',
    ('Automatic', 'Manual', 'Semi-automatic')
    )

h_power = st.sidebar.slider("h_power:",min_value=80, max_value=230)

# age = st.sidebar.number_input("age:",min_value=0, max_value=3)
age = st.sidebar.slider("age:",min_value=0, max_value=3)


km = st.sidebar.slider("km:",min_value=1000, max_value=200000)
gears = st.sidebar.slider("Gears:",min_value=5, max_value=8)
    


my_dict = {
    "hp_kW": h_power,
    "age": age,
    "km": km,
    "Gears": gears,
    "make_model": make_model,
    "Gearing_Type": gearing_type
    
}

df=pd.DataFrame.from_dict([my_dict])
st.table(df)

if st.button("Predict"): 
    pred = model.predict(df)
    st.success("The estimated price of your car is €{}. ".format(int(pred[0])))




