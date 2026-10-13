import streamlit as st
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
import pandas as pd
import pickle

# Importing Model 
model = tf.keras.models.load_model('models/models.h5')

# Encoder
with open('models/onehot_encoder_geo.pkl', 'rb') as file:
    onehot_encoder_geo = pickle.load(file)

# Gender
with open('models/label_encoder_gender.pkl', 'rb') as file:
    label_encoder_gender = pickle.load(file)

# Scaler
with open('models/scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

# Streamlit Part
st.title('Customer Churn Prediction using ANN')



