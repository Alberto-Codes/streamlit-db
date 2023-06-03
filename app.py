import plotly.graph_objects as go
import streamlit as st

# ---------SETTINGS--------------
income = ["Salary", "Blog", "Other Income"]
expenses = ["Rent", "Utilities", "Groceries", "Car", "Other Expenses", "Saving"]
currency = ["USD"]
page_title = "Income and Expense Tracker"
page_icon = ":money_with_wings:"
layout = "centered"
# -------------------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)
