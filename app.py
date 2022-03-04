import streamlit as st
import requests

'''
# TaxiFareModel Prediction
'''

st.markdown('''
Please insert the required inputs
''')


#- date and time
date = st.text_input(label='Date and Time')
#pickup longitude
long1 = st.text_input(label='Pickup Longitude')
#pickup latitude
lat1 = st.text_input(label='Pickup Latitude')
#dropoff longitude
long2 = st.text_input(label='Dropoff Longitude')
#dropoff latitude
lat2 = st.text_input(label='Dropoff Latitude')
#passenger count
cont = st.text_input(label='Number of passengers')



url = 'https://taxifare.lewagon.ai/predict?\
pickup_datetime='+date+'&\
pickup_longitude='+long1+'&\
pickup_latitude='+lat1+'&\
dropoff_longitude='+long2+'&\
dropoff_latitude='+lat2+'&\
passenger_count='+cont

params = { 'pickup_datetime':date,
          'pickup_longitude':long1,
          'pickup_latitude': lat1,
          'dropoff_longitude': long2,
          'dropoff_latitude':lat2,
          'passenger_count': cont
}

response = requests.get(url).json()
response = round (response['fare'],2)
texto = 3
st.text(url)
st.markdown(f'### The Fare prediction is:\n### {response}')
