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







st.title('Product Price Forecast')

user_input = st.text_input('Enter The Brand Name')
user_input_1 = st.number_input('Enter Product Id', min_value=1, max_value=None, value=1, step=1)
df = pd.read_csv(r"C:\Users\demit\Downloads\Frontend_ML\data\purchases.csv")


df = df[df['category_code'] == "electronics.smartphone"]
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df = df[df['brand']==user_input]
df = df[df['product_id']==user_input_1]
df = df.drop(['event_type','category_code','category_id', 'user_id', 'user_session'], axis=1)
df = df.drop_duplicates(subset=['event_time', 'product_id'], keep="first")




# Data
st.subheader('Data from Oct-Nov')
st.dataframe(df)


# Visualization
st.subheader('PAST 7-8 WEEKS DATA')
fig = plt.figure(figsize=(12,6))
plt.plot(df.price)
st.pyplot(fig)




# Load model
if user_input_1 == 1004856:
    model = load_model("models\(1)Dense_model_1004856.h5",compile=False)
    model.compile()
if user_input_1 == 1004767:
    model = load_model("models\(2)Dense_model_1004767.h5",compile=False)
    model.compile()
if user_input_1 == 1004833:
    model = load_model("models\(3)Dense_model_1004833.h5",compile=False)
    model.compile()
if user_input_1 == 1004870:
    model = load_model("models\(4)Dense_model_1004870.h5",compile=False)
    model.compile()
if user_input_1 == 10048386:
    model = load_model("models\(5)Dense_model_10048386.h5",compile=False)
    model.compile()
if user_input_1 == 1005100:
    model = load_model("models\(6)Dense_model_1005100.h5",compile=False)
    model.compile()
if user_input_1 == 1004873:
    model = load_model("models\(7)Dense_model_1004873.h5",compile=False)
    model.compile()
if user_input_1 == 1004750:
    model = load_model("models\(8)Dense_model_1004750.h5",compile=False)
    model.compile()
if user_input_1 == 1004858:
    model = load_model("models\(9)Dense_model_1004858.h5",compile=False)
    model.compile()
if user_input_1 == 1004209:
    model = load_model("models\(10)Dense_model_1004209.h5",compile=False)
    model.compile()



# Get elastic data array
timesteps = df["event_time"].to_numpy()
prices = df['price'].to_numpy()



# Creating train and test split the right way for the series data

split_size = int(0.70 * len(prices))


# Create train data split (everything before split)

X_train, y_train = timesteps[:split_size], prices[:split_size]


# Create test data split (everything beyond the split)

X_test, y_test = timesteps[split_size:], prices[split_size:]











# Let's setup global variable for window and horizon size

HORIZON =  1      # predict next 1 day
WINDOW_SIZE = 1   # use the past week of data to make the prediction




# Create function to label window data

def get_labelled_window(x, horizon=HORIZON):

  """
  Creates labels for windowed dataset.

  E.g. if horizon=1 
  Input: [0,1,2,3,4,5,6,7] -> Output: ([0,1,2,3,4,5,6], [7]) 

  """

  return x[:, :-horizon], x[:, -horizon]





# Create function to view Numpy arrays as windows

def make_windows(x, window_size=WINDOW_SIZE, horizon=HORIZON):
  """
  Turns a 1D array into a 2D array of sequential labelled windows of window_size with horizon size labels.
  """

  # 1. Create a window of specific window_size (add the horizon on the end for labelling later)

  window_step = np.expand_dims(np.arange(window_size+horizon), axis=0)


  # 2. Create a 2D array of multiple window steps (minus 1 to account for 0 indexing)

  window_indexes = window_step + np.expand_dims(np.arange(len(x)-(window_size+horizon-1)), axis=0).T        # create 2D array of windows of size window size

  print(f"Window indexes:\n {window_indexes, window_indexes.shape}")


  # 3. Index on the target array (a time series) with 2D array of multiple window steps
  windowed_array = x[window_indexes]

  # print(windowed_array)


  # 4. Get the labelled windows
  windows, labels = get_labelled_window(windowed_array, horizon=horizon)
  return windows, labels







# WINDOWS AND LABELS

full_windows, full_labels = make_windows(prices, window_size=WINDOW_SIZE, horizon=HORIZON)









# Make the train/test split

def make_train_test_splits(windows, labels, test_split=0.2):
  """
  Splits matching pairs of windows and labels into train and test splits.
  """

  split_size = int(len(windows) * (1-test_split))                               # this will default to 80% train 20% test
  train_windows = windows[:split_size]
  train_labels = labels[:split_size]
  test_windows = windows[split_size:]
  test_labels = labels[split_size:]
  return train_windows, test_windows, train_labels, test_labels





# Create train and test windows

train_windows, test_windows, train_labels, test_labels = make_train_test_splits(full_windows, full_labels)







# Defining model_preds:

def make_preds(model, input_data):
  """
  Usese model to make predictions on input_data.
  """

  forecast = model.predict(input_data)
  return tf.squeeze(forecast)         # return 1D array of predictions







# Make predictions using model_1 on the test dataset and view results


model_1_preds = make_preds(model, test_windows)

# Cache the dataframe so it's only loaded once
def load_data():
    return pd.DataFrame(
        {
            "Event_Time": X_test[-len(test_windows):],
            "Actual_Price": test_labels[:,],
            "Predicted_Price": model_1_preds,
        }
    )

sd = load_data()
st.subheader('Prices')
st.dataframe(sd)







# Using Plotly to display graphs


trace_one = go.Scatter(
    x=X_test[-len(test_windows):],
    y=model_1_preds,
    name="Preds",
    line=dict(color='#17BECF'),
    opacity=0.8
)

trace_two = go.Scatter(
    x=X_test[-len(test_windows):],
    y=test_labels[:,],
    name="Actual Price",
    line=dict(color='red'),
    opacity=0.8
)


data = [ trace_two]

layout = dict(
    title="Actual vs Predicted Price"
)

fig_3 = dict(data=data, layout=layout)
st.plotly_chart(fig_3,theme=None, use_container_width=True)
