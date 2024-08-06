import streamlit as st
import numpy as np
import pickle
import json


st.set_page_config(
    page_title="Singapore retail Sale Price",
    # page_icon="ICM.jpg",
    layout="wide"
)


st.markdown(f'### <html><body><h1 style="font-family:Neutro; font-size:40px"> Singapore resale Flat price Prediction </h1></body></html>', unsafe_allow_html=True)

with open('town.json') as File1:
    town_DICT=json.load(File1)
with open('flat_type.json') as File2:
    flat_type_DICT=json.load(File2)
with open('storey_range.json') as File3:
    storey_range_DICT=json.load(File3)
with open('flat_model.json') as File4:
    flat_model_DICT=json.load(File4)

month=[1,2,3,4,5,6,7,8,9,10,11,12]
Year=list(range(1977,2025))
year=list(range(1990,2025))

def regression():

    with st.form("Regression"):
        col1,col2,col3 = st.columns([0.4,0.4,0.4])
        with col1:
            town=st.selectbox("Select one option",town_DICT.keys(),index=None,placeholder="Towns...")
            flat_type=st.selectbox("Select one option",flat_type_DICT.keys(),index=None,placeholder="Flat Type...")
            flat_model=st.selectbox("Select one option",flat_model_DICT.keys(),index=None,placeholder="Flat Model...")
        with col2:
            floor_area_sqm=st.text_input(label="Enter the Floor Area(sqmt.):",placeholder="Please Fill Values")
            storey_range=st.selectbox("Select one option",storey_range_DICT.keys(),index=None,placeholder="Storey Range...")
            lease_commence_date=st.selectbox(label="Enter the Lease_Commence_Year(1977-2024):",options=Year,index=None,placeholder="Please Fill Values...")
            
        with col3:
            
            reg_month=st.selectbox(label="Enter the registered Month(1 to 12):",options=month,index=None,placeholder="Please Fill Values...")
            reg_year=st.selectbox(label="Select the registered Year:",options=year,index=None,placeholder="Please Fill Values...")
            remaining_lease_year=st.text_input(label="Enter the remaining Lease Year[ie. 93]:",placeholder="Please Fill Values...")
            remaining_lease_month=st.selectbox(label="Enter the remaining Lease month(1 to 12):",options=month,index=None,placeholder="Please Fill Values...")

        button = st.form_submit_button(label='Submit')


    if button:
        

        # load the regression pickle model
        with open(r'model.pkl', 'rb') as f:
            model = pickle.load(f)
    
            
        # make array for all user input values in required order for model prediction
        user_data = np.array([[town_DICT[town],flat_type_DICT[flat_type],storey_range_DICT[storey_range],floor_area_sqm,flat_model_DICT[flat_model],lease_commence_date,reg_month,reg_year,remaining_lease_year,remaining_lease_month]])
    
        # model predict the selling price based on user input
        y_pred = model.predict(user_data)

        # inverse transformation for log transformation data
        price = np.exp(y_pred[0])

        # round the value with 2 decimal point (Eg: 1.35678 to 1.36)
        price = round(price, 2)
        return price


try:
        PRICE=regression()
        if PRICE:
            st.markdown(PRICE)
except:
        st.warning('##### Please Fill Values')
            
   



