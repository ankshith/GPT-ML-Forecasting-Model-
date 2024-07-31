import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly as plot
import tensorflow as tf
from keras.models import load_model
import streamlit as st
from datetime import date
import plotly as px
import plotly.express as ps
import plotly.graph_objs as go
import models

# Set options for pandas dataframe
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

st.title('Product viewer')

user_input = st.text_input('Enter The Brand Name')
user_input_2 = st.text_input('Enter the Type Of Product')
#user_input1 = st.number_input('Enter your budget', min_value=1, max_value=None, value=1, step=1)
budget = st.slider('Enter your budget', 0, 5000, 0)
df = pd.read_csv(r"C:\Users\demit\Downloads\Frontend_ML\data\purchases.csv")
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]


# Dropping the unwanted columns
df = df.drop(['event_time', 'event_type', 'category_id', 'user_id', 'user_session'], axis=1)

#Samsung data
df = df[df['brand']==user_input]
df = df[df['category_code']==user_input_2]
df = df.drop_duplicates(subset=['price', 'product_id'], keep="first")

#st.dataframe(df)

# Define the range of values
min_range = budget - 5
max_range = budget + 5

# Print the range of values of samsung products 
sf = df[(df['price'] >= min_range) & (df['price'] <= max_range)]
st.subheader("Products Within Your Range")
st.dataframe(sf)



# Second dataframe
cf = pd.read_csv(r"C:\Users\demit\Downloads\Frontend_ML\data\purchases.csv")
cf = cf.loc[:, ~cf.columns.str.contains('^Unnamed')]
cf = cf.drop(['event_time', 'event_type', 'category_id', 'user_id', 'user_session'], axis=1)
cf = cf[cf['brand'] != user_input]
cf = cf[cf['category_code']==user_input_2]
cf = cf.drop_duplicates(subset=['price', 'product_id'], keep="first")
bf = cf[(cf['price'] >= min_range) & (cf['price'] <= max_range)]
st.subheader("Products Of Other Brands In Your Budget")
#bf.drop(columns=['event_time', 'event_type', 'category_id', 'category_code', 'user_id', 'user_session'], axis=1)
st.dataframe(bf)