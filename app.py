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
with open('Flat_type.json') as File2:
    flat_type_DICT=json.load(File2)
with open('Flat_model.json') as File3:
    flat_model_DICT=json.load(File3)


# Lease_year=list(range(1977,2025))
# sale_year=list(range(1990,2025))
sale_month=list(range( 0,13))
def regression():

    with st.form("Regression"):
        col1,col2= st.columns([0.5,0.5])
        with col1:
            Town=st.selectbox("Select one option",town_DICT.keys(),index=None,placeholder="Towns...")
            Flat_type=st.selectbox("Select one option",flat_type_DICT.keys(),index=None,placeholder="Flat Type...")
            Flat_model=st.selectbox("Select one option",flat_model_DICT.keys(),index=None,placeholder="Flat Model...")
            block=st.text_input(label="Enter the block:",placeholder="Please Fill Values")
            
        with col2:
            Storey_range=st.text_input(label="Enter the Storey_range(i.e.15):",placeholder="Please Fill Values")
            Lease_Commence_date=st.text_input(label="Enter the Lease Commence year:",placeholder="Please Fill Values")
            Sale_year=st.text_input(label="Enter the Year oF Sale:",placeholder="Please Fill Values")
            Sale_month=st.selectbox(label="Enter the Month oF Sale :",options=sale_month,index=None,placeholder="Please Fill Values...")
            Floor_area=st.text_input(label="Enter the Floor area(per Sqm):",placeholder="Please Fill Values")
        button = st.form_submit_button(label='Submit')


    if button:
        # load the regression pickle model
        with open(r'model.pkl', 'rb') as f:
            model = pickle.load(f)
    
        # if int(Storey_range)>50:    
        # make array for all user input values in required order for model prediction
        user_data = np.array([[int(block),float(Floor_area),int(Lease_Commence_date),int(Sale_year),int(Sale_month),float(Storey_range),town_DICT[Town],flat_model_DICT[Flat_model],flat_type_DICT[Flat_type]]])
    
        # model predict the selling price based on user input
        price = model.predict(user_data)
        return round(price[0],2)


try:
        Final_Price=regression()
        if Final_Price:
            st.balloons()
            st.markdown(f'### <html><body><h3 style="font-family:Neutro; font-size:40px"> Resale Price: {Final_Price} </h3></body></html>', unsafe_allow_html=True)
except:
        st.warning('##### Please Enter/Fill the Correct Value')


#4.About My Project...................
hide_streamlit_style = """ <html> <body>
<h1 style="font-family:Neutro; color:blue;font-size:40px"> About this Project </h1>
<p style="font-family:Neutro; font-size:20px">
<b>Project_Title</b>: Singapore Flat resale Price Predicton <br>
<b>Problem Statement</b>:<br>The objective of this project is to develop a machine learning model and deploy it as a user-friendly web application that predicts the resale prices of flats in Singapore. <br>This predictive model will be based on historical data of resale flat transactions, and it aims to assist both potential buyers and sellers in estimating the resale value of a flat.<br>
<b>Technologies_Used</b> :Data Wrangling, EDA, Model Building, Model Deployment,Streamlit<br>
<b>Data Source: </b>https://beta.data.gov.sg/collections/189/view <br>
<b>Domain </b> : Real Estate<br>
<b>Author</b> : M.KOBALAN <br>
<b>Linkedin</b> :https://www.linkedin.com/in/kobalan-m-106267227/
</p>
</body>  </html>  """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)