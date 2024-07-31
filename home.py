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
from PIL import Image



#homepage
im = Image.open("MAJOR_PROJECT.ico")
st.set_page_config(
    page_title="Product Forecasting",
    page_icon=im,
    layout="wide",
)

def main_page():
    st.markdown("# Main page ")
    st.sidebar.markdown("# Main page 🎈")

def page2():
    st.markdown("# Products 📲")
    st.sidebar.markdown("# Products 📲 ")

def page3():
    st.markdown("# Forecasting 📊")
    st.sidebar.markdown("# Prediction 📊")

page_names_to_funcs = {
    "Main Page": main_page,
    "Product": page2,
    "Prediction": page3,
}

# Sidebar
st.sidebar.title("Product Forecast")
file_selection = st.sidebar.selectbox("", ("Products 📲", "Forecast 📊"))

# Execute selected file
if file_selection == "Products 📲":
    exec(open("page2.py").read())
elif file_selection == "Forecast 📊":
    exec(open("page3.py").read())