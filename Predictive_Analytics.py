import streamlit as st
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objects as go
from datetime import date

# to run the application open the file folder, with the right button click on git bash here and type the command: streamlit run Predictive_Analytics.py
st.title("Aplicação de Análise Preditiva")

