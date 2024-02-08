import pickle
import base64
import pandas as pd
import numpy as np
import streamlit as st
from sklearn.preprocessing import LabelEncoder

# Setting page congiuration and Background

st.set_page_config(page_title = 'Cars_price_Prediction',layout='wide') 

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(png_file):
    bin_str = get_base64_of_bin_file(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    
    st.markdown(page_bg_img, unsafe_allow_html=True)
    return

set_png_as_page_bg('img1.png')

st.markdown("""
<style>
    [data-testid=stSidebar] {
        background-color: #9899AA;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color:brown;'>CarsDekho - Cars Price Prediction</h1>", unsafe_allow_html=True)

# Encoder instantiation
le = LabelEncoder()

# Reading the datasets
data = pd.read_csv('final_data.csv')
df1 = pd.read_csv('cars_dekho.csv')

# Decode Label Encoded columns

def encoder(col):
    encoded_col = list(data[col].unique())
    original_col = list(df1[col].unique())
    col_dic = {}
    for key in original_col:
        for value in encoded_col:
            col_dic[key] = value
            encoded_col.remove(value)
            break
    return col_dic

fuel = encoder('Fuel Type')
body = encoder('body_type')
tranmission = encoder('transmission_type')
manfac = encoder('manufacturer')
mod = encoder('model')
insv = encoder('Insurance Validity')

c1,c2 = st.columns(2)
with c1:
            name = st.selectbox('Car Name',options= list(mod.keys()))
            name1 = mod[name]

            man = st.selectbox('Car Manufacturer',options= list(manfac.keys()))
            man1 = manfac[man]

            fuel_type = st.selectbox('Fuel Type',options= list(fuel.keys()))
            fuel1 = fuel[fuel_type]

            body_type = st.selectbox('Body Type',options= list(body.keys()))
            body1 = body[body_type]

            transm = st.selectbox('Transmission Type',options= list(tranmission.keys()))
            trans1 = tranmission[transm]

            seat = st.selectbox('Seats',options=[5, 7, 6, 4, 8, 9, 2, 10])

            owner = st.selectbox('Owner Number',options=[0,1,2,3,4,5])

            
with c2:
            
            insval = st.selectbox('Insurance Validity',options= list(insv.keys()))
            insval1= insv[insval]
            
            kms = st.slider('Kilometers Driven', 0, 5500000, 10)
            kms1 = round(np.cbrt(kms),2)
            
            mile = st.slider('Mileage(kmpl)',7.0, 140.0, 7.0)
            mile1 = round(np.cbrt(mile),2)

            pow = st.slider('Max Power(bhp)',15.0, 510.0, 15.0)
            pow1 = round(np.cbrt(pow),2)

            eng = st.slider('Engine Displacement(cc)',72, 50000, 72)
            eng1 = round(np.cbrt(eng),2)

            age = st.slider('Car Age',1, 40, 5)

button = st.button('Predict Car Price')
if button:
    ip = [[fuel1,body1,kms1,trans1,owner,man1,name1,mile1,pow1,seat,insval1,eng1,age]]

    # Random Forest Model pickle file
    with open('rf_model.pkl','rb') as file:
            model = pickle.load(file)

    pr = model.predict(np.array(ip))[0]
    price = round(pr,2)
    st.markdown(f'<h2 style="text-align: center;color:brown;">Predicted Car Price : ₹ {price} </h2>', unsafe_allow_html=True)





