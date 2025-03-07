import streamlit as st
import requests

# Title
st.title("💰 Currency Converter")

# API URL
API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

# Fetch exchange rates
@st.cache_data
def get_exchange_rates():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json().get("rates", {})
    return {}

rates = get_exchange_rates()

# User Input
amount = st.number_input("Enter Amount:", min_value=0.01, value=1.00)
from_currency = st.selectbox("From Currency:", list(rates.keys()), index=list(rates.keys()).index("USD"))
to_currency = st.selectbox("To Currency:", list(rates.keys()), index=list(rates.keys()).index("INR"))

# Convert
if st.button("Convert"):
    if from_currency in rates and to_currency in rates:
        converted_amount = (amount / rates[from_currency]) * rates[to_currency]
        st.success(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    else:
        st.error("Invalid currency selection!")

# Footer
st.caption("🔄 Rates from vamsi.api")