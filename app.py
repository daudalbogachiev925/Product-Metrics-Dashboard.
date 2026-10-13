import streamlit as st
import pandas as pd
import plotly.express as px
from metrics import generate_sample_data, calc_retention, calc_ltv_cac, calc_mau

st.set_page_config(page_title="Product Metrics Dashboard", layout="wide")
st.title("📊 Product Metrics Dashboard")

@st.cache_data
def load_data():
    df = generate_sample_data()
    df = calc_retention(df)
    df = calc_ltv_cac(df)
    return df

df = load_data()

col1, col2, col3, col4 = st.columns(4)
col1.metric("DAU (последний)", f"{df['dau'].iloc[-1]:,}")
col2.metric("MAU (30д среднее)", f"{int(calc_mau(df)):,}")
col3.metric("Retention", f"{df['retention'].iloc[-1]*100:.1f}%")
col4.metric("LTV/CAC", f"{df['ltv_cac_ratio'].iloc[-1]:.2f}")

st.subheader("Динамика DAU / New / Churned")
fig = px.line(df, x="date", y=["dau", "new_users", "churned_users"])
st.plotly_chart(fig, use_container_width=True)

st.subheader("Retention")
fig2 = px.line(df, x="date", y="retention")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Выручка")
fig3 = px.area(df, x="date", y="revenue")
st.plotly_chart(fig3, use_container_width=True)

st.subheader("Raw Data")
st.dataframe(df.tail(30))
