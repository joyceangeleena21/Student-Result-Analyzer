import streamlit as st
import pandas as pd

st.title("📊 Student Result Analyzer")

df = pd.read_csv("students.csv")

st.subheader("Student Data")
st.dataframe(df)

df["Total"] = df["Maths"] + df["Science"] + df["English"]
df["Result"] = df["Total"].apply(lambda x: "Pass" if x >= 120 else "Fail")

st.subheader("Results")
st.dataframe(df)

st.subheader("Topper")
st.write(df.loc[df["Total"].idxmax()])

st.subheader("Pass vs Fail")
st.bar_chart(df["Result"].value_counts())