import streamlit as st
import joblib
import numpy as np
import pandas as pd

DATA_URL = "allPdfs.csv"

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(5)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')



st.title("predictions")

def load_model():
    with open('randomforestmodel.pkl','rb') as file:
        data=joblib.load(file)
        
    return data
data=load_model()
regressor=data

#Creating the dependent variable class
fac
tor = pd.factorize(data['FTR'])
data.FTR = factor[0]
definitions = factor[1]
print(data.FTR.head())
print(definitions)

def make_prediction(model,features):
    prediction=model.predict(features.reshape(1,-1))
    return prediction[0]
#prediction page
def prediction_page():

       
  FTHG = st.number_input('Insert FTHG')
  FTAG = st.number_input('Insert a FTAG')
  HST = st.number_input('Home Shots on Target')
  AST = st.number_input('Away Shots on Target')
  HS = st.number_input('Home Shots')
  AS = st.number_input('Away Shots')
  B365H = st.number_input('Home Odds')
  B365D = st.number_input('Draw Odds')
  B365A = st.number_input('Away Odds')
  HY = st.number_input('Home Yellows')
  AY = st.number_input('Away Yellows')
  click=st.button('Predict')
  if click:
        X=np.array([ [FTHG,FTAG,HST,AST,HS,AS,B365H,B365D,B365A,HY,AY]])
        # Predict using the model
        predicted_class = data.predict(X)

        # Reverse factorize the prediction
        reversefactor = dict(zip(range(3), definitions))
        predicted_label = reversefactor.get(predicted_class[0])
        st.subheader(f"The predicted result is ${predicted_label[0]:.2f}")


prediction_page()