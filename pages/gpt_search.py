import openai
import streamlit as st
import pandas as pd
import spacy
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


# Load the OpenAI API key
openai.api_key = "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"

# Load the Spacy model
nlp = spacy.load("en_core_web_sm")

# Load the dataset
df = pd.read_csv("purchase_updated.csv")
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df = df.drop_duplicates(subset=['event_time', 'product_id'], keep="first")


# Create the search bar
search_query = st.text_input("Search Query",)

# Extract search terms and price range using GPT-3
prompt = f"Extract search terms and price range from: {search_query}\nSearch terms:\nPrice range:"
response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=50, n=1,stop=None,temperature=0.5)
result = response.choices[0].text.strip().split("\n")
search_terms = []
price_range = []

if result:
    search_terms = result[0].split(":")[1].strip().split(",")
    price_range = [s for s in search_terms if "$" in s]
    if price_range:
        min_price = float(price_range[0].strip().replace("$", ""))
        max_price = float(price_range[1].strip().replace("$", ""))

# Tokenize and lemmatize search terms using Spacy
doc = nlp(search_query)
search_terms = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]

# Filter the dataset based on search terms and price range
filtered_data = df[df["category_code"].str.lower().str.contains("|".join(search_terms)) & df["brand"].str.lower().isin(search_terms) ]
if price_range:
    filtered_data = filtered_data[(filtered_data["price"] >= min_price) & (filtered_data["price"] <= max_price)]

# Round prices to two decimal places and display the filtered data
filtered_data["price"] = filtered_data["price"].round(2)
st.write(filtered_data[["brand", "category_code","product_name","price"]])
