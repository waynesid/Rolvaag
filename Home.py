import streamlit as st
import pandas as pd
import numpy as np
import pickle
import torch


from NeuralNet import NeuralNetworkClassificationModel



st.title("predictions")

DATA_URL = "allPdfs.csv"

pickled_model = pickle.load(open('model.pkl', 'rb'))


def make_prediction(model,features):
    prediction=model.predict(features)
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
    X_new = np.array([[1.08,1.08,1.00,1.60,1.00]])
    X_net = torch.FloatTensor(X_new)
    prediction = pickled_model(X_net)

    st.subheader(f"The estimated prediction is ${prediction}")

    return prediction


input_selection()