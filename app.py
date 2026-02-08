st.set_page_config(
    page_title="Time Sharing",
    page_icon="⏰"
)

st.title("⏰ Time Sharing")

import streamlit as st
import pandas as pd
import os

FILE = "activities.csv"
COLUMNS = ["name", "area", "activity", "time"]

try:
    if os.path.exists(FILE):
        df = pd.read_csv(FILE)
        if df.empty or list(df.columns) != COLUMNS:
            df = pd.DataFrame(columns=COLUMNS)
    else:
        df = pd.DataFrame(columns=COLUMNS)
except Exception:
    df = pd.DataFrame(columns=COLUMNS)

df.to_csv(FILE, index=False)

st.title("Time Sharing App")

with st.form("activity_form"):
    name = st.text_input("Your name")
    area = st.text_input("Your area")
    activity = st.text_input("Activity you want to do")
    time = st.text_input("Preferred time")

    submitted = st.form_submit_button("Find people")

if submitted:
    df = pd.concat(
        [df, pd.DataFrame([{
            "name": name,
            "area": area,
            "activity": activity,
            "time": time
        }])],
        ignore_index=True
    )
    df.to_csv(FILE, index=False)
    st.success("Saved! Checking for matches...")

    matches = df[
        (df["area"].str.lower() == area.lower()) &
        (df["activity"].str.lower() == activity.lower()) &
        (df["time"].str.lower() == time.lower()) &
        (df["name"] != name)
    ]

    if not matches.empty:
        st.subheader("People you can match with:")
        st.dataframe(matches[["name", "area", "activity", "time"]])
    else:
        st.info("No matches yet. Check back later!")


        st.info("No matches yet. Check back later!")



