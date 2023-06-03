import calendar
from datetime import datetime

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

# ---------------- DROP DOWN VALUES FOR SELECTING THE PERIOD ---------------

years = [datetime.today().year, datetime.today().year + 1]
months = list(calendar.month_name[1:])


# -------------- INPUT & SAVE PERIODS -----------------------------
st.header(f"Data Entry in {currency}")
with st.form("engry_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    col1.selectbox("Select Month:", months, key="month")
    col2.selectbox("Select Year:", years, key="year")
