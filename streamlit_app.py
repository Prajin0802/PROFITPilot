import streamlit as st
import pandas as pd

# import all the defined functions from the 'main.py' file
from main import (
    read_data,
    revenue_per_month,
    revenue_per_product,
    revenue_per_customer,
    top_10_customers,
)

# Load the data
file_path = "orders.csv"
data = read_data(file_path)
data["total_price"] = data["product_price"] * data["quantity"]

# Streamlit application to show visualizations of the requires tasks
st.title("PROFITPilot - An Online Store Revenue Analyser")
st.header("- By Prajin C Makam")

# line chart would be easy to analyse the fluctuations of the revenue and compare with other months
st.header("Revenue per Month")
monthly_revenue = revenue_per_month(data)
st.line_chart(monthly_revenue)

# bar chart would be a perfect visualization to differentiate the revenue between different products
st.header("Revenue per Product")
product_revenue = revenue_per_product(data)
st.bar_chart(product_revenue)

# similarly for customers as well
st.header("Revenue per Customer")
customer_revenue = revenue_per_customer(data)
st.bar_chart(customer_revenue)

# this table will list out the top 10 customers (just for a formatting purpose so that the visualization looks clean)
st.header("Top 10 Customers by Revenue")
top_customers = top_10_customers(data)
st.table(top_customers)
