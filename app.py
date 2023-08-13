import streamlit as st
import pandas as pd
import numpy  as np
import joblib
import pickle
from sklearn.cluster import KMeans
# import streamlit_extras
# from streamlit_extras.colored_header import colored_header

st.image('lendingkart_owler_20190913_181413_original.jpg')
st.title('Lendingkart')
st.subheader('Think Cash, Think Lendingkart!')
# colored_header(
#     label="Lendingkart",
#     description='Think Cash, Think Lendingkart!',
#     color_name="orange-70",
# )
@st.cache_data
def fetch_data():
    df = pd.read_csv('loan_approval_dataset.csv')
    return df

df = fetch_data()
df.columns = df.columns.str.replace(' ', '')

classification, clustering = st.tabs(['Loan Approval', 'Customers Cluster'])
with classification :

    st.write('Predicting customers loan approval based criterias below:')

    cibil_score =st.number_input('cibil_score', value=0)
    loan_term = st.select_slider('loan_term', [2,4,6,8,10,12,14,16,18,20])

    data = {
        'cibil_score': cibil_score,
        'loan_term': loan_term,
    }
    input = pd.DataFrame(data, index=[0])
    st.subheader('Summary :')
    st.write(input)

    # load files
    classification = joblib.load("classification.pkl")

    if st.button('Loan Approval'):
        prediction = classification.predict(input)

        if prediction == 0:
            prediction = 'Approved'
            st.write('Approved')
            st.success('This Customer is Approved! Please input the proposal documents below.')
            st.balloons()
            st.file_uploader('Upload Here')
        else:
            prediction = 'Rejected'
            st.write('Rejected')
            st.warning('Sorry the customer is rejected. Offer them with another program.')

# Create a unique key for each widget
widget_keys = {
    'income_annum': 'widget_income_annum',
    'loan_amount': 'widget_loan_amount',
    'cibil_score': 'widget_cibil_score',
    'residential_assets_value': 'widget_residential_assets_value',
    'commercial_assets_value': 'widget_commercial_assets_value',
    'luxury_assets_value': 'widget_luxury_assets_value',
    'bank_asset_value': 'widget_bank_asset_value'
}

with clustering:    
    st.write('Predicting customers class based criterias below:')

    income_annum = st.number_input('income_annum', value=0, key=widget_keys['income_annum'])
    loan_amount = st.number_input('loan_amount', value=0, key=widget_keys['loan_amount'])
    cibil_score = st.number_input('cibil_score', value=0, key=widget_keys['cibil_score'])
    residential_assets_value = st.number_input('residential_assets_value', value=0, key=widget_keys['residential_assets_value'])
    commercial_assets_value = st.number_input('commercial_assets_value', value=0, key=widget_keys['commercial_assets_value'])
    luxury_assets_value = st.number_input('luxury_assets_value', value=0, key=widget_keys['luxury_assets_value'])
    bank_asset_value = st.number_input('bank_asset_value', value=0, key=widget_keys['bank_asset_value'])

    data = {
        'income_annum': income_annum,
        'loan_amount': loan_amount,
        'cibil_score': cibil_score,
        'residential_assets_value': residential_assets_value,
        'commercial_assets_value': commercial_assets_value,
        'luxury_assets_value': luxury_assets_value,
        'bank_asset_value': bank_asset_value
    }
    input1 = pd.DataFrame(data, index=[0])

    load_model1 = joblib.load("clustering.pkl")
    if st.button('Cluster'):
        prediction1 = load_model1.predict(input1)

        if prediction1 == 0:
            prediction = 'Class B'
        else:
            prediction = 'Class B'

        st.write('This customer is from:')
        st.write(prediction)
