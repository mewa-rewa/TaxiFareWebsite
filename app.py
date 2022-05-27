import streamlit as st
import datetime
import numpy as np
import pandas as pd

import requests
'''
# TaxiFareModel front
'''

st.markdown('''
## This is my cool app
''')

pickup_longitude = st.number_input(label='pickup longitude')
pickup_latitude = st.number_input(label='pickup latitude')
dropoff_longitude = st.number_input(label='dropoff longitude')
dropoff_latitude = st.number_input(label='dropoff latitude')
pickup_date = st.date_input(label='Pickup date', value=datetime.datetime(2022, 5, 27, 15, 10, 00))
pickup_time = st.time_input(label='Pickup time', value=datetime.datetime(2022, 5, 27, 15, 10, 00))
pickup_date_time = f'{pickup_date} {pickup_time}'
passenger_count = st.number_input(label='Number of passenegers', step=1, min_value=1)


url ='https://coolimage-ni4mcaftla-ew.a.run.app/predict'
if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')


params = {"key":'2013-07-06 17:18:00.000000119',
        "pickup_datetime": [pickup_date_time],
        "pickup_longitude": [float(pickup_longitude)],
        "pickup_latitude": [float(pickup_latitude)],
        "dropoff_longitude": [float(dropoff_longitude)],
        "dropoff_latitude": [float(dropoff_latitude)],
        "passenger_count": [int(passenger_count)]
        }


prediction = requests.get(url, params=params).json()




st.metric(label='Fare', value=round(prediction,2))
