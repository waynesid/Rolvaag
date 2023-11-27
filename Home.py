import streamlit as st
import pandas as pd
import numpy as np
import pickle
import torch


st.title("predictions")

DATA_URL = "allPdfs.csv"

def load_model():
    with open('neuralnet.pickle','rb') as file:
        model=pickle.load(file)
        
    return model


def make_prediction(model,features):
    prediction=model.predict(features.reshape(1,-1))
    return prediction[0]

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(20)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

# INSPECT RAW DATA
st.subheader('Raw data')
st.write(data)

def input_selection():
    
  FTHG = st.number_input('Insert FTHG')
  FTAG = st.number_input('Insert a FTAG')
  HTHG = st.number_input('Insert a HTHG')
  HTAG = st.number_input('Insert a HTAG')

  predict_button= st.button("predict", type="primary")
  if predict_button:
    X_new = np.array([[FTHG,FTAG, HTHG,HTAG]])

    

input_selection()